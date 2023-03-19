import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN) # set up GPIO pin 17 as an input pin

while True:
    if GPIO.input(17):
        print("Motion detected")
    else:
        print("No motion detected")

    time.sleep(0.1)

GPIO.cleanup()

