# TODO: an additional class for no movement
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# --------------------------------------------------------------
# Importing Training Data
SAMPLE_SIZE = 20
K = 10


def import_data(label,n):
    data = np.zeros((n,300,6)) # pretrained dimension
    for i in range(n):
        f = './new/' + str(label) + '/data_' + str(i+1) + '_np.csv'
        data[i] = np.loadtxt(f, delimiter=',')
    return reshape_X(data)

def reshape_X(x):
    X = x.reshape(-1,50,6)
    n = X.shape[0]
    return (X, n)

def make_Y(n, CLASS):
    return np.full(n, CLASS)

wave_Xs, wave_n = import_data('wave', SAMPLE_SIZE)
swipe_Xs, swipe_n = import_data('swipe', SAMPLE_SIZE)
spin_Xs, spin_n = import_data('spin', SAMPLE_SIZE)
empty_Xs, empty_n = import_data('empty', SAMPLE_SIZE)

wave_y = make_Y(wave_n, 0)
swipe_y = make_Y(swipe_n, 1)
spin_y = make_Y(spin_n, 2)
empty_y = make_Y(spin_n, 3)

trainY = np.concatenate((wave_y,swipe_y,spin_y,empty_y))
# trainY = np.concatenate((wave_y,swipe_y,spin_y,new_y))

# --------------------------------------------------------------
## Feature Engineering 
#     Take sd of gyro y, gyro z, accel x
            # train: axis = 1
            # test:  axis = 0 
def feature_engineering(d,a):
    d_prime = np.array(d).std(axis=a)
    d_prime[:, 3] = d_prime[:, 3] * 100 # scale accel x
    return d_prime[:,[1,2,3]] # select gyro y, gyro z, accel x

wa = feature_engineering(wave_Xs,1)
sw = feature_engineering(swipe_Xs,1)
sp = feature_engineering(spin_Xs,1) 
em = feature_engineering(empty_Xs,1) 
# nw = feature_engineering(new_Xs) 

# Concat Xs, y
trainX = np.concatenate((wa,sw,sp,em))
# trainX = np.concatenate((wa,sw,sp,nw))

# --------------------------------------------------------------
# Importing Testing Data
# test = np.loadtxt('./new/wave/data_' + str(i+1) + '_np.csv', delimiter=',')

# --------------------------------------------------------------
## Predict

def feature_engineering_Test(d):
    d_prime = np.array(d).std(axis=0)
    d_prime[3] = d_prime[3] * 100 # scale accel x
    return d_prime[[1,2,3]] # select gyro y, gyro z, accel x

def predict_class(model, x):
    d = feature_engineering_Test(x)
    return model.predict([d]) # expected 2d array

def show_proba(model, x):
    d = feature_engineering_Test(x)
    return model.predict_proba([d]) # expected 2d array

if __name__ == '__main__': 
    knn_clf = KNeighborsClassifier(n_neighbors=K)
    knn_clf.fit(trainX, trainY)
    print('done')

    for i in range(20):
        test = np.loadtxt('./new/spin/data_' + str(i+1) + '_np.csv', delimiter=',')
        print(predict_class(knn_clf, test))
    # for i in range(60):
    #     ypred = knn_clf.predict([trainX[i]])
    #     print(ypred)
