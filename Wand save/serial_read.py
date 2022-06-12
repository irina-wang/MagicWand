from random import randint, randrange
from wsgiref.validate import ErrorWrapper
from sklearn.neighbors import KNeighborsClassifier
from playsound import playsound

import time
import serial
import numpy as np
import KNN
import _constants as my


"""
columns are: [gyro_x, gyro_y, gyro_z, accel_x, accel_y, accel_z, button_pressed]
"""

PORT = my.PORT
PORT2 = my.PORTOUT

TRAINING = my.TRAINING
FINISHED_TRAINING = my.FINISHED_TRAINING

# pretrained model
X = KNN.trainX
Y = KNN.trainY

knn_clf = KNeighborsClassifier(n_neighbors=5)
model =  knn_clf.fit(X, Y) 

testD = None # [50,6]
new_class = None

# new class
NEWCLASS = 4

# button values
PRESSED = 0
RELEASED = 1

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
    return entry_np

def slice_new_data():
    n = int(len(new_class)/50)
    print(len(new_class))
    print(n)
    return (new_class[:n*50,:], n)

def train_model():
    print('/\/\/\/\/\/\/\/\/\/\/\/\/ Training /\/\/\/\/\/\/\/\/\/\/\/\/')
    playsound(TRAINING) # signal start
    d,n = slice_new_data()

    # process new data
    x, n = KNN.reshape_X(d)
    newX = KNN.feature_engineering(x,1)
    newY = KNN.make_Y(n, NEWCLASS)

    trainX = np.append(X,newX).reshape(-1,3)
    trainY = np.append(Y,newY)
    newModel = knn_clf.fit(trainX, trainY)

    # sound effects
    playsound(FINISHED_TRAINING) 
    time.sleep(1) # simulating training process
    return newModel

arduino_samp_freq_Hz = 100
timeout = 1/arduino_samp_freq_Hz

# ---- Main ----
if __name__ == "__main__":
    button_pressed = RELEASED # 1
    prev_button_status = RELEASED # 1
    i = 0

    print("hello world")
    arduino = serial.Serial(port=PORT, baudrate=115200, timeout=timeout)
    arduinoOUT = serial.Serial(port=PORT2, baudrate=9600, timeout=timeout)  

    while True:
        arduinoOUT.reset_input_buffer()
        serial_data = arduino.readline()
        
        if (serial_data is not None and len(serial_data) > 0): 
            (array, button_status) = read_data_from_serial(serial_data)

            # Case 1: button realeased  - play mode with existing model
            if button_status == RELEASED and prev_button_status == RELEASED:
                testD = gather_data(array, testD) 
                if len(testD) == 50:
                    r = KNN.predict_class(model, testD)
                    print('predict:' + str(r[0]))
                    r_prob = KNN.show_proba(model, testD)
                    print('predict prob:' + str(r_prob[0]))
                    
                    if r_prob[0][r[0]] < 1: 
                        print('turn off')
       
                    arduinoOUT.write(str(r[0]).encode())
                    testD = testD[1:, :] # pop
                prev_button_status = RELEASED

            # Case 2: button just released - train new model
            elif button_status == RELEASED and prev_button_status == PRESSED: # just released
                if (len(new_class) >= 100): # try this out
                    model = train_model()
                    arduinoOUT.reset_input_buffer()
                    new_class = None
                else:
                    print("Oops!  Too short.  Try press longer...")
                 
                prev_button_status = RELEASED # Training

            # Case 3: button is pressed - gather new datas
            else: 
                new_class = gather_data(array, new_class) 
                prev_button_status = PRESSED
                
                print('0' if new_class is None else len(new_class))
        i += 1

