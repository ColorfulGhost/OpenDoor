import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(19, GPIO.OUT)
GPIO.setup(19, GPIO.HIGH)
print("CLOSED")