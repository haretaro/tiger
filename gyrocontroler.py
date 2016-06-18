import tornado.ioloop
import tornado.web
import tornado.websocket
from gpio import Control

control = Control()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("gyro.html")

class WebSocket(tornado.websocket.WebSocketHandler):

    def open(self):
        print("websocket opened")

    def on_message(self, message):
        value = float(message)
        if value <= 0:
            value = 0
        if value >= 40:
            value = 40
        v = value/40 * 100
        print(message, v)
        control.pwm(v)

    def on_close(self):
        print("websocket closed")

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/websocket", WebSocket)
])

if __name__ == "__main__":
    application.listen(8889)
    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        pass
    control.terminate()
    print("terminated")
