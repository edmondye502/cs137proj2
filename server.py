from network import Listener, Handler, poll

class MyHandler(Handler):
     
    def on_open(self):
        print("OPENING")
         
    def on_close(self):
        print("CLOSING")

     
    def on_msg(self, msg):
    	reply = input("")
    	# do_send(reply)
   
        
 

if __name__ == '__main__':
	handlers = {}  # map client handler to user name
	port = 8888
	server = Listener(port, MyHandler)
	while 1:
	    poll(timeout=0.05) # in seconds