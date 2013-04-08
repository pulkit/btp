from rapidsms.apps.base import AppBase

class App(AppBase):
    def handle(self, msg):
        if msg.text=='pings':
            msg.respond("hello world")
            return True
        return False
