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
serial data: [gyro_x, gyro_y, gyro_z, accel_x, accel_y, accel_z, button_pressed]
"""

# Model
X = KNN.trainX
Y = KNN.trainY
knn_clf = KNeighborsClassifier(n_neighbors=5)
model =  knn_clf.fit(X, Y) 

# New Data
testD = None 
trainD = None

# Constants 
NEWCLASS = 4
MIN_ENTRY = 50 # group size 
PRESSED = 0
RELEASED = 1

PORT = my.PORT
PORT2 = my.PORTOUT
TRAINING = my.TRAINING
FINISHED_TRAINING = my.FINISHED_TRAINING

#   Read data and return gyro data and button status tuple.
def read_data_from_serial(bytes_string):  
    data = bytes_string.decode('UTF-8')
    array = np.fromstring(data, sep=',')
    return (array[:-1], array[-1])


#  Append new data to existing array
def gather_data(curr_arr, entry_np):
    if entry_np is None:
        entry_np = np.expand_dims(curr_arr,0)
    else:
        entry_np = np.append(entry_np,np.expand_dims(curr_arr,0),axis=0)
    return entry_np


#  Reshape the currenty data based on group size.
def slice_new_data():
    n = int(len(trainD)/MIN_ENTRY)
    print(len(trainD))
    print(n)
    return (trainD[:n*MIN_ENTRY,:], n)


#  Train model based on the data gathered 
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


# Main function 
if __name__ == "__main__":
    button_pressed = RELEASED # 1
    prev_button_status = RELEASED # 1
    i = 0

    print("\/\/\ Hi, Welcome to the Magic World. /\/\/")
    
    # set baud rate and port, send data faster from input arduino than for output one
    arduino = serial.Serial(port=PORT, baudrate=115200, timeout=timeout)
    arduinoOUT = serial.Serial(port=PORT2, baudrate=9600, timeout=timeout)  

    while True:
        # clear buffer and read data 
        arduinoOUT.reset_input_buffer()
        serial_data = arduino.readline()
        
        if (serial_data is not None and len(serial_data) > 0): 
            (array, button_status) = read_data_from_serial(serial_data)

            # Case 1: button realeased  - play mode with existing model
            if button_status == RELEASED and prev_button_status == RELEASED:
                testD = gather_data(array, testD) 
                
                # predict class if enough samples are collected 
                if len(testD) == MIN_ENTRY:
                    # predict class and probability with current model
                    r = KNN.predict_class(model, testD)
                    r_prob = KNN.show_proba(model, testD)
                    print('predict prob:' + str(r_prob[0]))
                    
                    arduinoOUT.write(str(r[0]).encode()) 
                    
                    # pop the first elem out 
                    testD = testD[1:, :] 
                    
                prev_button_status = RELEASED

            # Case 2: button just released - train new model
            elif button_status == RELEASED and prev_button_status == PRESSED: 
                
                # train if enough samples were collected
                # 2 was used to allow some buffer time, could be substitute by any number greater than 1
                if (len(trainD) >= 2*MIN_ENTRY): 
                    model = train_model()
                    
                    # clear training data and arduino buffer data jammed while training
                    trainD = None 
                    arduinoOUT.reset_input_buffer() 
                else:
                    print("Oops!  Too short.  Try press longer...")
                 
                prev_button_status = RELEASED 

            # Case 3: button is pressed - gather new datas
            else: 
                trainD = gather_data(array, trainD) 
                prev_button_status = PRESSED
        i += 1

