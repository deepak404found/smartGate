import cv2
import imutils
import numpy as np
import pytesseract
from picamera.array import PiRGBArray
from picamera import PiCamera
import RPi.GPIO as GPIO
import time

valid = "HR26DK8337"

redLed = 24
greenLed = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN) # set up GPIO pin 17 as an input pin

GPIO.setup(redLed, GPIO.OUT) # set up GPIO pin redLed as an output pin
GPIO.setup(greenLed, GPIO.OUT) # set up GPIO pin greenLed as an output pin

GPIO.output(redLed, GPIO.LOW)
GPIO.output(greenLed, GPIO.LOW)

camera = PiCamera()
camera.resolution = (740, 580)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(740, 580))

# function to blink led
def blinkLed(led, count) :
    for i in range(count):
        GPIO.output(led, GPIO.HIGH)
        time.sleep(0.8)
        GPIO.output(led, GPIO.LOW)
        time.sleep(0.1)

# function to recoginise the text of license plate
def AlprFunc() :
    text = ''
    # only 5 try or return ''
    tryCount = 5
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        cv2.imshow("Frame", image)
        rawCapture.truncate(0)
        try:
            # convert to grey scale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray = cv2.bilateralFilter(
                gray, 11, 17, 17)  # Blur to reduce noise
            edged = cv2.Canny(gray, 30, 200)  # Perform Edge detection
            cnts = cv2.findContours(
                edged.copy(), cv2.RETR_TREE,              cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
            screenCnt = None
            for c in cnts:
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.018 * peri, True)
                if len(approx) == 4:
                    screenCnt = approx
                    break
            if screenCnt is None:
                detected = 0
                print("No contour detected")
            else:
                detected = 1
            if detected == 1:
                cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
            mask = np.zeros(gray.shape, np.uint8)
            new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1,)
            new_image = cv2.bitwise_and(image, image, mask=mask)
            (x, y) = np.where(mask == 255)
            (topx, topy) = (np.min(x), np.min(y))
            (bottomx, bottomy) = (np.max(x), np.max(y))
            Cropped = gray[topx:bottomx+1, topy:bottomy+1]
            text = pytesseract.image_to_string(Cropped, config='--psm 11')
            print("Detected Number is:", text)
            cv2.imshow("Frame", image)

            time.sleep(0.8)
            break
        except Exception as e:
            tryCount=tryCount-1
            print('error', e)
            if (tryCount == 0) :
                return
            else:
                continue
    cv2.destroyAllWindows()
    return text

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    if GPIO.input(17):
        print("Motion detected")
        blinkLed(redLed, 1)
        licenseNum = AlprFunc()
        print("number is :", licenseNum)
        # if licenseNum include valid
        if licenseNum and valid in licenseNum:
            blinkLed(greenLed, 1)
        else:
            blinkLed(redLed, 3)
        time.sleep(2)
    else:
        print("No motion detected")

    time.sleep(0.8)

GPIO.cleanup()
