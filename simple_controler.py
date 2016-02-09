import joystick
import RPi.GPIO as GPIO

right_driver_forward = 27
right_driver_backward = 17
left_driver_forward = 15
left_driver_backward = 14
threshold = 30

gpios = [right_driver_forward,
        right_driver_backward,
        left_driver_forward,
        left_driver_backward]

print(gpios)
GPIO.setmode(GPIO.BCM)
for pin in gpios:
    print(pin)
    GPIO.setup(pin, GPIO.OUT)

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

    print(ly, ry ,ry > threshold, ry < -threshold, ly > threshold, ly < -threshold)

    GPIO.output(right_driver_forward, ry > threshold)
    GPIO.output(right_driver_backward, ry < -threshold)
    GPIO.output(left_driver_forward, ly > threshold)
    GPIO.output(left_driver_backward, ly < -threshold)
