import csv, serial, time
import numpy as np
import random as rand
"""
columns are: [gyro_x, gyro_y, gyro_z, accel_x, accel_y, accel_z, button]
"""

if __name__ == "__main__":
    # 1 is not pressed, 0 is pressed
    button = 1
    prev_button = 1
    print("hello world")

    # arduino_in = serial.Serial(port='COM5', baudrate=115200, timeout=1)
    arduino_out = serial.Serial(port='/dev/cu.usbmodem1434101', baudrate =9600, timeout=1)

    # arduino_in.reset_input_buffer()
    # arduino_in.reset_output_buffer()
    arduino_out.reset_input_buffer()
    arduino_out.reset_output_buffer()


    i = 0
    while True:
        i += 1
        # arduino_out.write

        # data = arduino_in.readline()
        arduino_out.write(str(i%5).encode())  # send class int to arduino
        time.sleep(0.100)
