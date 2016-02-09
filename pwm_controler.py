import joystick
import RPi.GPIO as GPIO

right_driver_forward = 27
right_driver_backward = 17
pwm_right = 12

left_driver_forward = 15
left_driver_backward = 14
pwm_left = 18

threshold = 30

gpios = [right_driver_forward,
        right_driver_backward,
        left_driver_forward,
        left_driver_backward,
        pwm_left,
        pwm_right]

print(gpios)
GPIO.setmode(GPIO.BCM)
for pin in gpios:
    print(pin)
    GPIO.setup(pin, GPIO.OUT)

pwm_l = GPIO.PWM(pwm_left, 60)
pwm_r = GPIO.PWM(pwm_right, 60)
pwm_l.start(0)
pwm_r.start(0)

ly = 0
ry = 0

js, queue = joystick.queue('/dev/input/js0')
js.daemon = True
js.start()

while True:
    while not queue.empty():
        value, key_type = queue.get()
        if key_type == joystick.l_y:
            ly = value
        if key_type == joystick.r_y:
            ry = value

    l_duty = abs(ly)/128.0 * 100
    r_duty = abs(ry)/128.0 * 100
    print(ly, ry, ry > threshold, ry < -threshold, ly > threshold, ly < -threshold)

    GPIO.output(right_driver_forward, ry > threshold)
    GPIO.output(right_driver_backward, ry < -threshold)
    GPIO.output(left_driver_forward, ly > threshold)
    GPIO.output(left_driver_backward, ly < -threshold)

    pwm_l.ChangeDutyCycle(l_duty)
    pwm_r.ChangeDutyCycle(r_duty)
