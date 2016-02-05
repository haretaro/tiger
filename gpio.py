import RPi.GPIO as GPIO

class Control:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        self.pin1 = 18

        GPIO.setup(self.pin1, GPIO.OUT)

        self.pwmpin = GPIO.PWM(self.pin1, 60)
        self.pwmpin.start(0)

    def pwm(self, value):
        self.pwmpin.ChangeDutyCycle(value)

    def terminate(self):
        self.pwmpin.stop()
        GPIO.cleanup()

