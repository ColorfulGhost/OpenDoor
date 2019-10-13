# -*- coding: utf-8 -*-
import time
from .RotationDir import RotationDir
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class A4988:
    def __init__(self, STEP=20, DIR=21):
        self.STEP = STEP
        self.DIR = DIR
        GPIO.setup(self.STEP, GPIO.OUT)
        GPIO.setup(self.DIR, GPIO.OUT)

    def RotationDirection(self, dir):
        if dir == RotationDir.clockwise:
            GPIO.output(self.DIR, GPIO.LOW)
        else:
            GPIO.output(self.DIR, GPIO.HIGH)

    ##step_num 1 = 1.8°
    def RotationStep(self, step_num=130, rotation_dir=1, speed=0.010):
        if rotation_dir == 1:
            self.RotationDirection(RotationDir.clockwise)
        if rotation_dir == 0:
            self.RotationDirection(RotationDir.anticlockwise)

        while step_num > 0:
            GPIO.output(self.STEP, GPIO.HIGH)
            time.sleep(speed)
            GPIO.output(self.STEP, GPIO.LOW)
            time.sleep(speed)
            step_num -= 1
