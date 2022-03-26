import serial 
import numpy as np
import csv
import time
"""
columns are: [gyro_x, gyro_y, gyro_z, accel_x, accel_y, accel_z, button_pressed]
"""
def read_data_from_serial(bytes_string):
    data = bytes_string.decode('UTF-8')
    # print(data)
    array = np.fromstring(data, sep=',')
    return (array[:-1], array[-1])

def button_released(button_pressed, prev_button_pressed):
    return button_pressed == 1 and prev_button_pressed == 0

def train_new_model():
    pass

arduino_samp_freq_Hz = 100
timeout = 1/arduino_samp_freq_Hz

if __name__ == "__main__":
    # 1 is not pressed, 0 is pressed
    button_pressed = 1
    prev_button_pressed = 1
    print("hello world")
    arduino = serial.Serial(port='/dev/cu.usbmodem1444301', baudrate=115200, timeout=timeout)
    if True:
        k = 0
        while k < 20:
            print('Collecting the ' + str(k) + 'th Data -------------')
            time.sleep(1)

            entry_np = None
            # collect motion data for 3s
            while (entry_np is None or len(entry_np) < 300):
                data = arduino.readline()
                if (data is not None and len(data) > 0):
                    # print("here")
                    prev_button_pressed = button_pressed
                    (array, button_pressed) = read_data_from_serial(data)
                    if entry_np is None:
                        entry_np = np.expand_dims(array,0)
                    else:
                        entry_np = np.append(entry_np,np.expand_dims(array,0),axis=0)
                time.sleep(0.01)
            print('im out, adding ---------')
           

            k += 1
            entry_np = np.reshape(entry_np,(-1,6))
            print(entry_np.shape)

            np.savetxt('./new/data_'+str(k)+'_np.csv', entry_np, delimiter=',')
        
            # print("button pressed = " + str(button_pressed))
        # if button_released(button_pressed, prev_button_pressed):
        #     train_new_model()
        #     pass 
