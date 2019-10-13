import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(19, GPIO.IN)
# 19继电器状态
if GPIO.input(19):
    print("CLOSED")
else:
    print("OPEN")