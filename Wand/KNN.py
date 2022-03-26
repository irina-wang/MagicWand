import numpy as np
import pandas as pd

# from sklearn.datasets import make_blobs, make_circles
from sklearn.neighbors import KNeighborsClassifier
# from sklearn import preprocessing

# import matplotlib.pyplot as plt
# from mpl_toolkits import mplot3d 
# %matplotlib inline
# import seaborn as sns; sns.set()

# --------------------------------------------------------------
# Importing Training Data
SAMPLE_SIZE = 20

def import_data(label,n):
    data = np.zeros((20,300,6))
    for i in range(n):
        f = './' + str(label) + '/data_' + str(i+1) + '_np.csv'
        data[i] = np.loadtxt(f, delimiter=',')
    return data

wave_Xs = import_data('wave', SAMPLE_SIZE)
swipe_Xs = import_data('swipe', SAMPLE_SIZE)
spin_Xs = import_data('spin', SAMPLE_SIZE)
new_Xs = import_data('new', SAMPLE_SIZE)

wave_y =  np.full(SAMPLE_SIZE, 0)
swipe_y = np.full(SAMPLE_SIZE, 1)
spin_y = np.full(SAMPLE_SIZE, 2)
new_y = np.full(SAMPLE_SIZE, 3)

trainY = np.concatenate((wave_y,swipe_y,spin_y))

# --------------------------------------------------------------
# Importing Testing Data
def import_category_data(label, sample_size, index):
    data = []
    f = './' + str(label) + '/data_' + str(index) + '_np.csv'
    data.append(pd.read_csv(f))
    return data

# import test data 
wave_testX = import_category_data('test', 1, 1)
swipe_testX  = import_category_data('test', 1, 5)
spin_testX  = import_category_data('test', 1, 8)


# --------------------------------------------------------------
## Feature Engineering 
#     Take sd of gyro y, gyro z, accel x
def feature_engineering(d):
    d_prime = np.array(d).std(axis=1)
    d_prime[:, 3] = d_prime[:, 3] * 100 # scale accel x
    return d_prime[:,[1,2,3]] # select gyro y, gyro z, accel x

# n = feature_engineering(new_Xs) 

w = feature_engineering(wave_Xs)
sw = feature_engineering(swipe_Xs)
sp = feature_engineering(spin_Xs) 

# Concat Xs, y
trainX = np.concatenate((w,sw,sp))

# --------------------------------------------------------------
## Feature Engineering 
# Take sd of one feature

w_ = feature_engineering(wave_testX, 1)
sw_ = feature_engineering(swipe_testX, 1)
sp_ = feature_engineering(spin_testX, 1)

w_3 = w_[:,[1,2,3]]
sw_3 = sw_[:,[1,2,3]]
sp_3 = sp_[:,[1,2,3]]

w_3[:, 2] = w_3[:, 2] * 100
sw_3[:, 2] = sw_3[:, 2] * 100
sp_3[:, 2] = sp_3[:, 2] * 100

# --------------------------------------------------------------
## Predict
# Take sd of one feature
if __name__ == '__main__': 
    knn_clf = KNeighborsClassifier(n_neighbors=5)
    knn_clf.fit(Xs_, y)
    ypred=knn_clf.predict(w_3)
    print(ypred)
