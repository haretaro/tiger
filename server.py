import tornado.ioloop
import tornado.web
import tornado.websocket

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("gyro.html")

class WebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("websocket opened")

    def on_message(self, message):
        print(message)

    def on_close(self):
        print("websocket closed")

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/websocket", WebSocket)
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
