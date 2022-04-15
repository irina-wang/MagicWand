from random import randint
# from types import NoneType
from wsgiref.validate import ErrorWrapper
import serial 
import numpy as np
import rgb


"""
columns are: [gyro_x, gyro_y, gyro_z, accel_x, accel_y, accel_z, button_pressed]
"""

# PORT = my.PORT
PORT2 = '/dev/cu.usbmodem1424201'

# pretrained model
# X = KNN.trainX
# Y = KNN.trainY

# knn_clf = KNeighborsClassifier(n_neighbors=5)
# model =  knn_clf.fit(X, Y) 

# testD = None # [50,6]
# new_class = None

# TRAINING = my.TRAINING
# FINISHED_TRAINING = my.FINISHED_TRAINING

 # 1 is not pressed, 0 is pressed
# PRESSED = 0
# RELEASED = 1

# # new class
# # NEWCLASS = 3
# NEWCLASS = 4

def read_data_from_serial(bytes_string):
    data = bytes_string.decode('UTF-8')
    # print(data)
    array = np.fromstring(data, sep=',')
    if len(array) == 3:
        return (array[0], array[1], array[2])
    else: 
        return (0,0,0)
    # return array 
    

    # return data

# def gather_data(array, entry_np):
#     if entry_np is None:
#         entry_np = np.expand_dims(array,0)
#     else:
#         entry_np = np.append(entry_np,np.expand_dims(array,0),axis=0)
#         # time.sleep(0.01)
#     return entry_np


# # check new data 
# # process new data 
# def slice_new_data():
#     n = int(len(new_class)/50)
#     print(len(new_class))
#     print(n)
#     return (new_class[:n*50,:], n)

# Train New Model
# def train_model():
#     # Train KNN model 
#     print('Training /\/\/\/\/\/\/\/\/\/\/\/\/')
#     playsound(TRAINING) # signal start
#     d,n = slice_new_data()
# # process new data
#     x, n = KNN.reshape_X(d)
#     newX = KNN.feature_engineering(x,1)
#     newY = KNN.make_Y(n, NEWCLASS)

#     trainX = np.append(X,newX).reshape(-1,3)
#     trainY = np.append(Y,newY)
#     newModel = knn_clf.fit(trainX, trainY)

#     # sound effects
#     playsound(FINISHED_TRAINING) 
#     time.sleep(1) # simulating training process
#     return newModel

arduino_samp_freq_Hz = 200
timeout = 1/arduino_samp_freq_Hz

# Main
if __name__ == "__main__":
    arduinoOUT = serial.Serial(port=PORT2, baudrate=9600, timeout=timeout)  
    

    while True:
        serial_data = arduinoOUT.readline()

    
        if (serial_data is not None and len(serial_data) > 0):
            (r,g,b) = read_data_from_serial(serial_data)

            rgb.r = r
            rgb.g = g
            rgb.b = b
            print('done')
            rgb.show()
           
            
