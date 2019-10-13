import time

import RPi.GPIO as GPIO
from A4988.A4988 import A4988

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# 继电器电源控制
GPIO.setup(19, GPIO.OUT)
# 避免驱动烧坏  开始关闭19 GPIO
GPIO.setup(19, GPIO.LOW)
stepper = A4988()
# 参数 ： 开门 100步  速度0.01
stepper.RotationStep()
print("OPEN")
# time.sleep(5)
# # 关闭电机
# PowerSwitch.get(0)