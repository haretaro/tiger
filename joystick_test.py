import joystick

js, queue = joystick.queue('/dev/input/js0')
js.daemon = True
js.start()

while True:
    print(queue.get())
