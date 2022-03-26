from wsgiref.validate import ErrorWrapper
import serial 
import numpy as np
import time
from playsound import playsound
import KNN
from sklearn.neighbors import KNeighborsClassifier
import _constants as my
"""
columns are: [gyro_x, gyro_y, gyro_z, accel_x, accel_y, accel_z, button_pressed]
"""

PORT = my.PORT

# pretrained model
X = KNN.trainX
Y = KNN.trainY
knn_clf = KNeighborsClassifier(n_neighbors=5)
model =  knn_clf.fit(X, Y) 

testD = None # length 300 data ????

TRAINING = 'Sound/training_effect.wav'
FINISHED_TRAINING = 'Sound/finished_training.wav'

 # 1 is not pressed, 0 is pressed
PRESSED = 0
RELEASED = 1

# new class
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
# def gather_training_data(device):
#     entry_np = None
#     # entry_np = [0 for _ in range(300)]

#     while button_status == PRESSED:
#     while entry_np is  None or len(entry_np) < 300:
#         data = device.readline()
#         if (data is not None and len(data) > 0):
#             (array, button_status) = read_data_from_serial(data)
#             if entry_np is None:
#                 entry_np = np.expand_dims(array,0)
#             else:
#                 entry_np = np.append(entry_np, np.expand_dims(array,0), axis=0)
#         time.sleep(0.01)
#     # TODO: Do we want to verbally remind the users?
#     # entry_np = np.reshape(entry_np,(-1,6))
#     return entry_np

def gather_testing_data(array, entry_np):
    if entry_np is None:
        entry_np = np.expand_dims(array,0)
    else:
        entry_np = np.append(entry_np,np.expand_dims(array,0),axis=0)
        time.sleep(0.01)
    return entry_np

# Train New Model
def train_model(newClass):
    # Train KNN model 
    newXs = KNN.feature_engineering(newClass)
    newY = np.array(NEWCLASS, newXs.length())
    model = knn_clf.fit(X + newXs, Y + newY)

    # sound effects
    playsound(TRAINING) 
    playsound(FINISHED_TRAINING)

    # TODO: light effects 
    return model

# Predict New Class
def predict_class(testD):
    testX = KNN.feature_engineering_Test(testD)
    return model.predict(testX) 



arduino_samp_freq_Hz = 100
timeout = 1/arduino_samp_freq_Hz


# def pop(d):
#     return d[1:, :]

def train_loop(args):
    return 

def test_loop(args):
    return
    
# Main
if __name__ == "__main__":
    button_pressed = PRESSED # 1
    prev_button_pressed = PRESSED # 1

    print("hello world")
    arduino = serial.Serial(port=PORT, baudrate=115200, timeout=timeout)
    while True:
        serial_data = arduino.readline()
        if (serial_data is not None and len(serial_data) > 0):
            (array, _) = read_data_from_serial(serial_data)

            # if True:
                # newClass = []
            testD = gather_testing_data(array, testD) 
            if len(testD) == 300:
                r = KNN.predict_class(model, testD)
                print(r)
                testD = testD[1:, :] # pop
                    # (array, button_status) = read_data_from_serial(serial_data)

                # if button_status == PRESSED:
                #     newClass = new_class() # gather new_class


                # # if button_status == RELEASED:
                # model = train_model(newClass);
                        
    

    
    

