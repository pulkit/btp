from rapidsms.apps.base import AppBase
from views import *


class App(AppBase):
    def handle(self, msg):
        if msg.text[0:3] == "dss":
            index = []
            for i,c in enumerate(msg.text):
                if " " == c :
                    index.append(i)
            make = msg.text[index[0]+1:index[1]]
            model = msg.text[index[1]+1:index[2]]
            implement = msg.text[index[2]+1:index[3]]
            depth = int(msg.text[index[3]+1:index[4]])
            speed = int(msg.text[index[4]+1:index[5]])
            texture = msg.text[index[5]+1:index[6]]
            strength = msg.text[index[6]+1:len(msg.text)]
            reply = sms_reply(self,make,model,implement,depth,speed,texture,strength)
            s_out =str(reply[0]+", "+reply[1]+" and "+reply[2])
            print s_out
            msg.respond(str(s_out))

            return True
        return False
