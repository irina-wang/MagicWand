from random import randint
from wsgiref.validate import ErrorWrapper
import serial 
import numpy as np
import time
from playsound import playsound
import KNN
from sklearn.neighbors import KNeighborsClassifier
import _constants as my

import govee
from random import randrange


"""
columns are: [gyro_x, gyro_y, gyro_z, accel_x, accel_y, accel_z, button_pressed]
"""


PORT = my.PORT
PORT2 = my.PORTOUT


# pretrained model
X = KNN.trainX
Y = KNN.trainY


count = 0

knn_clf = KNeighborsClassifier(n_neighbors=5)
model =  knn_clf.fit(X, Y) 

testD = None # [50,6]
new_class = None

TRAINING = my.TRAINING
FINISHED_TRAINING = my.FINISHED_TRAINING
HUH = my.HUH
BEGIN = my.BEGIN
playsound(BEGIN)




# (DEVICE_1,DEVICE_2) = govee.GET_info();
# print(DEVICE_2)
# govee.POST_Switch(DEVICE_2, 'on');

 # 1 is not pressed, 0 is pressed
PRESSED = 0
RELEASED = 1

# new class
NEWCLASS = 4

def read_data_from_serial(bytes_string):
    data = bytes_string.decode('UTF-8')
    # print(data)
    array = np.fromstring(data, sep=',')
    return (array[:-1], array[-1])

def gather_data(array, entry_np):
    if entry_np is None:
        entry_np = np.expand_dims(array,0)
    else:
        entry_np = np.append(entry_np,np.expand_dims(array,0),axis=0)
        # time.sleep(0.01)
    return entry_np


# check new data 
# process new data 
def slice_new_data():
    n = int(len(new_class)/50)
    print(len(new_class))
    print(n)
    return (new_class[:n*50,:], n)

# Train New Model
def train_model():
    # Train KNN model 
    print('Training /\/\/\/\/\/\/\/\/\/\/\/\/')
    playsound(TRAINING) # signal start
    d,n = slice_new_data()
# process new data
    x, n = KNN.reshape_X(d)
    newX = KNN.feature_engineering(x,1)
    newY = KNN.make_Y(n, NEWCLASS)

    trainX = np.append(X,newX).reshape(-1,6)
    trainY = np.append(Y,newY)
    newModel = knn_clf.fit(trainX, trainY)

    # sound effects
    playsound(FINISHED_TRAINING) 
    time.sleep(1) # simulating training process
    return newModel

arduino_samp_freq_Hz = 100
timeout = 1/arduino_samp_freq_Hz

# Main
if __name__ == "__main__":
    button_pressed = RELEASED # 1
    prev_button_status = RELEASED # 1
    i = 0

    print("hello world")
    arduino = serial.Serial(port=PORT, baudrate=115200, timeout=timeout)
    arduinoOUT = serial.Serial(port=PORT2, baudrate=9600, timeout=timeout)  
    
    # arduinoOUT = serial.Serial(port=PORT2, baudrate=9600, timeout=timeout) # write the prediction
    while True:
        # arduinoOUT.reset_input_buffer()
        serial_data = arduino.readline()
        trained = False
        
        if (serial_data is not None and len(serial_data) > 0):
            (array, button_status) = read_data_from_serial(serial_data)
        # for testing purpose 
            # button_status = randrange(2) # generate 0,1
            # button_status = my.BUTTON[i] # testing code
            print('button' + str(button_status))
            if button_status == RELEASED and prev_button_status == RELEASED:
                if (len(array) == 6):
                    testD = gather_data(array, testD) 
                # count = count + 1
               
                    if len(testD) == 50:
                        r = KNN.predict_class(model, testD)
                        print('predict:' + str(r[0]))
                        r_prob = KNN.show_proba(model, testD)
                        print('predict prob:' + str(r_prob[0]))
                        govee_brightness = r_prob[0][r[0]]
                        

                        print('govee_brightness' + str(govee_brightness))
                        # confused states
                        if govee_brightness < 1: 
                            r = [5]
                            print("I'm confused")
                        
                        arduinoOUT.write(str(r[0]).encode()) # test this
                        #  govee

                        # print(count)
                        if trained: 
                            print('trained')
                            print(r_prob[0][4])
                        # if count == 100:
                        #     print(count)
                        #     govee.POST_Brightness(DEVICE_2,0.5*100);
                        #     count = 0

                        testD = testD[1:, :] # pop
                prev_button_status = RELEASED

            elif button_status == RELEASED and prev_button_status == PRESSED: # just released
                if (len(new_class) >= 100): # try this out
                    arduinoOUT.write(str([0]).encode())
                    model = train_model()
                    arduinoOUT.reset_input_buffer()
                    arduino.reset_output_buffer()
                    trained = True
                    # arduino.reset_output_buffer()
                    # arduino.reset_input_buffer()
                    # arduinoOUT.reset_input_buffer() # something like this 
                    new_class = None
                else:
                    new_class = None
                    print("Oops!  Too short.  Try press longer...")
                # Train 
                

                # print('Now empty the list')
                # print('0' if new_class is None else len(new_class))
                prev_button_status = RELEASED

            else: # button_status == PRESSED
                arduinoOUT.write(str([0]).encode())
                if (len(array) == 6):
                    new_class = gather_data(array, new_class) 
                prev_button_status = PRESSED


                arduinoOUT.reset_input_buffer()
                arduino.reset_output_buffer()

                # prev_button_status = PRESSED
                
                # print('Gathering Data ---------------------------------')
                print('0' if new_class is None else len(new_class))
        i += 1

