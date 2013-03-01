from rapidsms.app.base import AppBase

class PingPong(AppBase):
    
    def handle(self,msg):
        """Handles incoming message"""
        if msg.text=='ping':
            msg.respond('pong')
            return True
        return False

