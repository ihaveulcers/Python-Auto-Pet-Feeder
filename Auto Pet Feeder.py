#https://tutorials-raspberrypi.com/raspberry-pi-servo-motor-control/

import RPi.GPIO as GPIO
import time

servo = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo,GPIO.OUT)

# GPIO 03 for PWM with 50Hz
p = GPIO.PWM(servo,50)

# Initialisation
p.start(2.5)

try:
    while True:
        p.ChangeDutyCycle(5)
        time.sleep(0.5)
        p.ChangeDutyCycle(7.5)
        time.sleep(0.5)
        p.ChangeDutyCycle(10)
        time.sleep(0.5)
        p.ChangeDutyCycle(12.5)
        time.sleep(0.5)
        p.ChangeDutyCycle(10)
        time.sleep(0.5)
        p.ChangeDutyCycle(7.5)
        time.sleep(0.5)
        p.ChangeDutyCycle(5)
        time.sleep(0.5)
        p.ChangeDutyCycle(2.5)
        time.sleep(0.5)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
