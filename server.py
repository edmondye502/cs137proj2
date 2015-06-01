from network import Listener, Handler, poll
from easter_egg import*
handlers = []  # map client handler to user name

class MyHandler(Handler):

	def on_open(self):
		print("Connection with a client has been established")
		handlers.append(self.sock)
		for i in range(len(handlers)):
			if self.sock == handlers[i]:
				position_num = i - 0
				break

		self.do_send("Connecting you with any Agent. Please wait... You are number " + str(position_num) + " in the queue.")

	def on_close(self):
		print("Client has disconnected...")
		handlers.remove(self.sock)

	# when receive message
	def on_msg(self, msg):

		if self.sock == handlers[0]:
			if len(msg) == 3:
				print("You are speaking with " + msg.get('name'))
				print(msg.get('name') + ' chose ' + msg.get('prompt'))
				print("The topic is: " + msg.get('topic'))

				reply = raw_input("Reply: ")
				self._log.append("Agent: " + reply)
				self.do_send(reply)
			
			elif len(msg) == 1:

				self._log.append("Client: " + msg.get('txt'))

				# save log
				if(msg.get('txt') == ":s"):
					infile = open("log.txt", "w")
					log_str = strlist_to_str(self._log)
					infile.write(log_str)
					self.do_send("Conversation saved.")

				# easter egg
				elif(msg.get('txt') == ":e"):
					egg = '\n' + get_easter_egg(EASTER)
					self.do_send(egg)

				else:
					print("Client: " + msg.get('txt'))
					reply = raw_input("Reply: ")
					self._log.append("Agent: " + reply)
					self.do_send(reply)
				

		else:
			self.do_send("Agent is busy")

def strlist_to_str(l):
	text = ""
	for s in l:
		text += s + "\n"
	return text

if __name__ == '__main__':
	port = 8888

	server = Listener(port, MyHandler)
	while True:
		poll(timeout=0.05) # in seconds
	server.stop()
