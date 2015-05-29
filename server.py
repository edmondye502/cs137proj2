from network import Listener, Handler, poll

class MyHandler(Handler):

	def on_open(self):
		print("Server has opened")
		self.do_send("Connecting you with any Agent. Please wait...")

			 
	def on_close(self):
		print("Client has disconnected...")

	# when receive message
	def on_msg(self, msg):

		if len(msg) == 3:

			print("You are speaking with " + msg.get('name'))
			print(msg.get('name') + ' chose ' + msg.get('prompt'))
			print("The topic is: " + msg.get('topic'))
		
		elif len(msg) == 1:

			# save log
			if(msg.get('txt') == ":s"):
				infile = open("log.txt", "w")
				strlist_to_str(self._buffer)
				infile.write()

			# easter egg
			elif(msg.get('txt') == ":e"):
				self.do_send("Happy Easter!")

			else:
				print("Client: " + msg.get('txt'))

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
