from network import Handler, poll
import sys
from threading import Thread
from time import sleep



class Client(Handler):
    
    def on_close(self):
        print("Client now exiting!")

    # upon receiving message
    def on_msg(self, msg):
        sys.stdout.write("AGENT: ")
        print(msg)


        
def prompt():
    while (True):
        prompt = input('(1) Question \n(2) Complaint \n(3) Other\n Input: ')
        if(int(prompt) <= 3 and int(prompt) >= 1):
            break
        return int(prompt)

def periodic_poll():
    while 1:
        poll()
        sleep(0.05)  # seconds
                            




if __name__ == '__main__':
    myname = raw_input('What is your name? ')
    prompt()
    topic = raw_input('Topic: ')

    host, port = 'localhost', 8888
    client = Client(host, port)
    client.do_send({'join': myname})

    thread = Thread(target=periodic_poll)
    thread.daemon = True  # die when the main thread dies 
    thread.start()

    done = False; 
    while not done:
        mytxt = sys.stdin.readline().rstrip()
        client.do_send({'speak': myname, 'txt': mytxt})

    client.do_close() 