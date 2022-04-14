# ------
#
# Documentation: 
#    0 - red - no movement
#    1 - green - wave < > 
#    2 - blue - swipe ^ v
#    3 - purple - spin o O
#    4 - no color - trained class

PORT = '/dev/cu.usbmodem1424101'
PORTOUT = '/dev/cu.usbmodem1424201'

TRAINING = 'Sound/training_effect.wav'
FINISHED_TRAINING = 'Sound/finished_training.wav'

dim = 50 # how many data are we taking std of
BUTTON = [1 for i in range(30000)] 
# BUTTON = [0 for i in range(30)] +  [1 for i in range(10)] + [0 for i in range(500)] + [1 for i in range(100)] 
# [0 for i in range(10)] + [1 for i in range(1000)] + 