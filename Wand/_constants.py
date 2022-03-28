from KNN import SAMPLE_SIZE

# PORT! change here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
PORT = '/dev/cu.usbmodem1434301'

TRAINING = 'Sound/training_effect.wav'
FINISHED_TRAINING = 'Sound/finished_training.wav'

dim = 50 # how many data are we taking std of
BUTTON = [0 for i in range(30)] +  [1 for i in range(10)] + [0 for i in range(500)] + [1 for i in range(100)] 
# [0 for i in range(10)] + [1 for i in range(1000)] + 