#!/usr/bin/python3
# This code runs continually in the background to apply
# the stored PWM slider value to the GPIO output
import RPi.GPIO as GPIO
import time

ledPin1 = 17 #RED
ledPin2 = 27  #BLUE
ledPin3 = 22  #GREEN

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin1, GPIO.OUT)
GPIO.setup(ledPin2, GPIO.OUT)
GPIO.setup(ledPin3, GPIO.OUT)

pwm1 = GPIO.PWM(ledPin1, 100) # PWM object on our pin at 100 Hz
pwm2 = GPIO.PWM(ledPin2, 100) # PWM object on our pin at 100 Hz
pwm3 = GPIO.PWM(ledPin3, 100) # PWM object on our pin at 100 Hz

pwm1.start(0) # start with LED off
pwm2.start(0) # start with LED off
pwm3.start(0) # start with LED off

while True:
  with open("red_pwm.txt", 'r') as f:
    dutyCycle = float(f.read()) # read duty cycle value from red LED file
  pwm1.ChangeDutyCycle(dutyCycle)
  time.sleep(0.1)
  with open("blue_pwm.txt", 'r') as f:
    dutyCycle = float(f.read()) # read duty cycle value from blue LED file
  pwm2.ChangeDutyCycle(dutyCycle)
  time.sleep(0.1)
  with open("green_pwm.txt", 'r') as f:
    dutyCycle = float(f.read()) # read duty cycle value from green LED file
  pwm3.ChangeDutyCycle(dutyCycle)
  time.sleep(0.1)