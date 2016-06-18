import tornado.web
import tornado.websocket
from tornado.ioloop import PeriodicCallback

class MainPage(tornado.web.RequestHandler):

    def get(self):
        self.render('keyread.html')

class SendWebSocket(tornado.websocket.WebSocketHandler):

    def on_message(self, message):
        print(chr(int(message)))

app = tornado.web.Application([
    (r'/',MainPage),
    (r'/socket',SendWebSocket)
    ])

if __name__ == '__main__':
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
