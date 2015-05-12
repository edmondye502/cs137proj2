from network import Listener, Handler, poll

class MyHandler(Handler):
    def on_open(self):
        print("Server has opened")
        self.do_send("Connecting you with an agent...")
             
    def on_close(self):
        print("Connection has been closed...")
        print("Server now exiting")

    # when receive message
    def on_msg(self, msg):
        
        for key in msg:
        	k = key
        	# if(k == 'join'):
        	# 	return
        	str_msg = msg[key]
        	break

        # quit
        if(str_msg == ":q"):
            self.handle_close()

        # save log
        elif(str_msg == ":s"):
            infile = open("log.txt", "w")
            strlist_to_str(self._buffer)
            infile.write()

        # easter egg
        elif(str_msg == ":e"):
            self.do_send("Happy Easter!")


        else:
        	if(k != 'join'):
        		print("CLIENT: " + str_msg)
        	reply = raw_input("Reply: ")
        	self.do_send(reply)





def strlist_to_str(l):
    text = ""
    for s in l:
        text += s + "\n"
    return text

        
 

if __name__ == '__main__':
    handlers = {}  # map client handler to user name
    port = 8888

    server = Listener(port, MyHandler)
    while True:
        poll(timeout=0.05) # in seconds
    server.stop()
