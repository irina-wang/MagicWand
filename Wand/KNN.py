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

def import_category_data(label, sample_size):
    data = []
    for i in range(sample_size):
        f = './' + str(label) + '/data_' + str(i+1) + '_np.csv'
        data.append(pd.read_csv(f))
    return data

wave_Xs = import_category_data('wave', SAMPLE_SIZE)
swipe_Xs = import_category_data('swipe', SAMPLE_SIZE)
spin_Xs = import_category_data('spin', SAMPLE_SIZE)
# new_Xs = import_category_data('spin', SAMPLE_SIZE)

wave_y =  np.full(SAMPLE_SIZE, 0)
swipe_y = np.full(SAMPLE_SIZE, 1)
spin_y = np.full(SAMPLE_SIZE, 2)

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
# Take sd of one feature
def feature_engineering(d, sample_size):

    d_prime = np.full((sample_size,3), 0, float)
    for i in range(sample_size):
         d_prime[i] = np.std(d[i]).to_numpy()
    return d_prime

w = feature_engineering(wave_Xs, SAMPLE_SIZE)
sw = feature_engineering(swipe_Xs, SAMPLE_SIZE)
sp = feature_engineering(spin_Xs, SAMPLE_SIZE) 


# Concat Xs, y
t = np.append(w, sw)
Xs = np.append(t, sp).reshape(60, 6)

t = np.append(wave_y, swipe_y)
y = np.append(t, spin_y)

# select gyro y, gyro z, accel x
Xs_ = Xs[:,[1,2,3]]
Xs_[:, 2] = Xs_[:, 2] * 100 # scale accel x

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
