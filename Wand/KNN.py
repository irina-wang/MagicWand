import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# --------------------------------------------------------------
# Importing Training Data
SAMPLE_SIZE = 20

def import_data(label,n):
    data = np.zeros((n,300,6)) # pretrained dimension
    for i in range(n):
        f = './' + str(label) + '/data_' + str(i+1) + '_np.csv'
        data[i] = np.loadtxt(f, delimiter=',')
    return data

wave_Xs = import_data('wave', SAMPLE_SIZE)
swipe_Xs = import_data('swipe', SAMPLE_SIZE)
spin_Xs = import_data('spin', SAMPLE_SIZE)
# new_Xs = import_data('new', SAMPLE_SIZE)

wave_y =  np.full(SAMPLE_SIZE, 0)
swipe_y = np.full(SAMPLE_SIZE, 1)
spin_y = np.full(SAMPLE_SIZE, 2)
# new_y = np.full(SAMPLE_SIZE, 3)

trainY = np.concatenate((wave_y,swipe_y,spin_y))
# trainY = np.concatenate((wave_y,swipe_y,spin_y,new_y))

# --------------------------------------------------------------
## Feature Engineering 
#     Take sd of gyro y, gyro z, accel x
def feature_engineering(d):
    d_prime = np.array(d).std(axis=1)
    d_prime[:, 3] = d_prime[:, 3] * 100 # scale accel x
    return d_prime[:,[1,2,3]] # select gyro y, gyro z, accel x

wa = feature_engineering(wave_Xs)
sw = feature_engineering(swipe_Xs)
sp = feature_engineering(spin_Xs) 
# nw = feature_engineering(new_Xs) 

# Concat Xs, y
trainX = np.concatenate((wa,sw,sp))
# trainX = np.concatenate((wa,sw,sp,nw))

# --------------------------------------------------------------
# Importing Testing Data
def import_test_data(label, index):
    data = []
    f = './' + str(label) + '/data_' + str(index) + '_np.csv'
    data.append(pd.read_csv(f))
    return data

# import test data 
wave_testX = import_test_data('test', 1, 1)
swipe_testX  = import_test_data('test', 1, 5)
spin_testX  = import_test_data('test', 1, 8)

test1 = feature_engineering(wave_testX)
test2 = feature_engineering(wave_testX)
test3 = feature_engineering(wave_testX)

# --------------------------------------------------------------
## Predict
def predict_class(model, testX):
    return model.predict(testX)

if __name__ == '__main__': 
    knn_clf = KNeighborsClassifier(n_neighbors=5)
    knn_clf.fit(trainX, trainY)
    ypred = knn_clf.predict(test1)
    print(ypred)
