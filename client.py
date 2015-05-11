from network import Handler, poll
import sys
from threading import Thread
from time import sleep


myname = raw_input('What is your name? ')

while (True):
	prompt = input('1. Q \n2. C \n3. O\n Input: ')
	if(int(prompt) <= 3 and int(prompt) >= 1):
		break


topic = raw_input('Topic: ')

class Client(Handler):
    
    def on_close(self):
        pass
    
    def on_msg(self, msg):
        print msg
        
host, port = 'localhost', 8888
client = Client(host, port)
client.do_send({'join': myname})

def periodic_poll():
    while 1:
        poll()
        sleep(0.05)  # seconds
                            
thread = Thread(target=periodic_poll)
thread.daemon = True  # die when the main thread dies 
thread.start()


print('Connecting you with an agent')

while 1:
    mytxt = sys.stdin.readline().rstrip()
    client.do_send({'speak': myname, 'txt': mytxt})