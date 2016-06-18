import tornado.web
import tornado.websocket
from tornado.ioloop import PeriodicCallback
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

class MainPage(tornado.web.RequestHandler):

    def get(self):
        self.render('readkey.html')

class SendWebSocket(tornado.websocket.WebSocketHandler):

    def on_message(self, message):
        print(chr(int(message)),message,int(message)==ord('A'))

app = tornado.web.Application([
    (r'/',MainPage),
    (r'/socket',SendWebSocket)
    ])

if __name__ == '__main__':
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
