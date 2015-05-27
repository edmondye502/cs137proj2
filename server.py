from network import Listener, Handler, poll

class MyHandler(Handler):

	count = 0

	def on_open(self):
		print("Server has opened")
		self.do_send("Connecting you with an agent...")
		self.do_send(count)
		count += 1

			 
	def on_close(self):
		print("Client has disconnected...")
		count -= 1

	# when receive message
	def on_msg(self, msg):
		
		for key in msg:
			k = key
			# if(k == 'join'):
			#   return
			str_msg = msg[key]
			break

		# save log
		if(str_msg == ":s"):
			infile = open("log.txt", "w")
			strlist_to_str(self._buffer)
			infile.write()

		# easter egg
		elif(str_msg == ":e"):
			self.do_send("Happy Easter!")


		else:
			if(k != 'join'):
				print("Client: " + str_msg)
			else:
				print("You are speaking with " + str_msg)
				print("There topic is: " + msg['topic'])
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
