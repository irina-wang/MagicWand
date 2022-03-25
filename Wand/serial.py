from wsgiref.validate import ErrorWrapper
import serial 
import numpy as np
import csv
import time
from playsound import playsound
import KNN

from sklearn.neighbors import KNeighborsClassifier


# pretrained model
Xs_ = KNN.Xs_
y = KNN.y
knn_clf = KNeighborsClassifier(n_neighbors=5)
model =  knn_clf.fit(Xs_, y) 


testD = np.zeros(300) # length 300 data ????

TRAINING = 'Sound/training_effect.wav'
FINISHED_TRAINING = 'Sound/finished_training.wav'

PRESSED = 1
RELEASED = 0
NEWCLASS = 3


"""
columns are: [gyro_x, gyro_y, gyro_z, accel_x, accel_y, accel_z, button_pressed]
"""
def read_data_from_serial(bytes_string):
    data = bytes_string.decode('UTF-8')
    # print(data)
    array = np.fromstring(data, sep=',')
    return (array[:-1], array[-1])

# get training data for new class
def new_class(data):
    try:
        return gather_training_data(data)
    except ValueError:
        print("Oops!  Too short.  Try press longer...")

# TODO check data length
def gather_training_data(device):
    entry_np = []
    # entry_np = [0 for _ in range(300)]
    while len(entry_np) < 300:
        data = device.readline()
        if (data is not None and len(data) > 0):
            (array, _) = read_data_from_serial(data)
            if entry_np is None:
                entry_np = np.expand_dims(array,0)
            else:
                entry_np = np.append(entry_np, np.expand_dims(array,0), axis=0)
        time.sleep(0.01)
    # TODO: Do we want to verbally remind the users?
    # entry_np = np.reshape(entry_np,(-1,6))
    return entry_np


def gather_testing_data(data):
    entry_np = []
    while i < 300:
        data = arduino.readline()
        if (data is not None and len(data) > 0):
            if entry_np is None:
                entry_np = np.expand_dims(array,0)
            else:
                entry_np = np.append(entry_np,np.expand_dims(array,0),axis=0)
        i += 1
        time.sleep(0.01)
    # entry_np = np.reshape(entry_np,(-1,6))
    return entry_np

# Train New Model
def train_model(newClass):
    # Train KNN model 
    newXs = KNN.feature_engineering(newClass)
    newY = np.array(NEWCLASS, newXs.length())
    model = knn_clf.fit(Xs_ + newXs, y + newY)

    # sound effects
    playsound(TRAINING) 
    playsound(FINISHED_TRAINING)

    # TODO: light effects 
    return model

# Predict New Class
def predict_class(testD):
    testX = KNN.feature_engineering(testD)
    return knn_clf.predict(testX) 



arduino_samp_freq_Hz = 100
timeout = 1/arduino_samp_freq_Hz


# Main
if __name__ == "__main__":
    button_pressed = PRESSED # 1
    prev_button_pressed = PRESSED # 1

    print("hello world")
    arduino = serial.Serial(port='/dev/tty.usbmodem142101', baudrate=115200, timeout=timeout)
    if True:
        serial_data = arduino.readline()
        if (serial_data is not None and len(serial_data) > 0):
            (array, button_status) = read_data_from_serial(serial_data)

            if True:
                newClass = []
                testD = gather_testing_data(arduino) # ???how to keep writing to the array?
                predict_class(testD) # keep testing

                while button_status == PRESSED:
                    newClass = new_class() # gather new_class
                    if button_status == RELEASED:
                        model = train_model(newClass);
                        break
    

    
    

