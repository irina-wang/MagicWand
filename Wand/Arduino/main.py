# Untitled - By: micha - Tue Mar 8 2022
import gc, time, array, rp2
from lsm6dsox import LSM6DSOX
from machine import Pin, I2C, PWM, UART
from ulab import numpy as np
import random as rand

def get_prediction():
    return rand.randint(0,3)

"""
below is some code for singe rgb led
"""
def red_light(pin_r, pin_g, pin_b):
    r_led = Pin(pin_r,Pin.OUT)
    g_led = Pin(pin_g, Pin.OUT)
    b_led = Pin(pin_b,Pin.OUT)
    r_led.on()
    g_led.off()
    b_led.off()

def yellow_light(pin_r, pin_g, pin_b):
    r_led = Pin(pin_r,Pin.OUT)
    g_led = Pin(pin_g, Pin.OUT)
    b_led = Pin(pin_b,Pin.OUT)
    r_led.on()
    g_led.on()
    b_led.off()

def green_light(pin_r, pin_g, pin_b):
    r_led = Pin(pin_r,Pin.OUT)
    g_led = Pin(pin_g, Pin.OUT)
    b_led = Pin(pin_b,Pin.OUT)
    r_led.off()
    g_led.on()
    b_led.off()

def cyan_light(pin_r, pin_g, pin_b):
    r_led = Pin(pin_r,Pin.OUT)
    g_led = Pin(pin_g, Pin.OUT)
    b_led = Pin(pin_b,Pin.OUT)
    r_led.off()
    g_led.on()
    b_led.on()

def blue_light(pin_r, pin_g, pin_b):
    r_led = Pin(pin_r,Pin.OUT)
    g_led = Pin(pin_g, Pin.OUT)
    b_led = Pin(pin_b,Pin.OUT)
    r_led.off()
    g_led.off()
    b_led.on()

def magenta_light(pin_r, pin_g, pin_b):
    r_led = Pin(pin_r,Pin.OUT)
    g_led = Pin(pin_g, Pin.OUT)
    b_led = Pin(pin_b,Pin.OUT)
    r_led.on()
    g_led.off()
    b_led.on()

def white_light(pin_r, pin_g, pin_b):
    r_led = Pin(pin_r,Pin.OUT)
    g_led = Pin(pin_g, Pin.OUT)
    b_led = Pin(pin_b,Pin.OUT)
    r_led.on()
    g_led.on()
    b_led.on()

def light_off(pin_r, pin_g, pin_b):
    r_led = Pin(pin_r,Pin.OUT)
    g_led = Pin(pin_g, Pin.OUT)
    b_led = Pin(pin_b,Pin.OUT)
    r_led.off()
    g_led.off()
    b_led.off()

lsm = LSM6DSOX(I2C(0, scl=Pin(13), sda=Pin(12)))
led = Pin(6, Pin.OUT)
led.off()


"""
below is some code for single led
"""
red_pin_n = 16     # D4
green_pin_n = 17   # D5
blue_pin_n = 18    # D6

red_led   = Pin(red_pin_n,   Pin.OUT)
green_led = Pin(green_pin_n, Pin.OUT)
blue_led  = Pin(blue_pin_n,  Pin.OUT)

"""
below is some code for multi led
"""
NUM_LEDS = 13
PIN_NUM = 22
brightness = 0.2

"""
below is some code for button
"""
button_pin_n = 15
button = Pin(button_pin_n, Pin.IN, Pin.PULL_UP)


while(True):
    gc.collect()
    # category = get_prediction()
    # time.sleep_ms(500)
    """if button.value() == 0:
     
        if category == 0:
            red_light(red_pin_n, green_pin_n, blue_pin_n)
        elif category == 1:
            yellow_light(red_pin_n, green_pin_n, blue_pin_n)
        elif category == 2:
            green_light(red_pin_n, green_pin_n, blue_pin_n)
        elif category == 3:
            cyan_light(red_pin_n, green_pin_n, blue_pin_n)
        elif category == 4:
            blue_light(red_pin_n, green_pin_n, blue_pin_n)
        elif category == 5:
            magenta_light(red_pin_n, green_pin_n, blue_pin_n)
        elif category == 6:
            white_light(red_pin_n, green_pin_n, blue_pin_n)

        light_off(red_pin_n, green_pin_n, blue_pin_n)
    """
    gyro = lsm.read_gyro()
    accel = lsm.read_accel()
    print(str(gyro[0])  + ',' + str(gyro[1])  + ',' + str(gyro[2])  + ',' +
          str(accel[0]) + ',' + str(accel[1]) + ',' + str(accel[2]) + ',' + str(button.value()))
    time.sleep_ms(10)













