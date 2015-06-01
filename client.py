from network import Handler, poll, get_my_ip
import sys
from threading import Thread
from time import sleep



class Client(Handler):
		
	def on_close(self):
		print("Client now exiting!")
		

	# upon receiving message
	def on_msg(self, msg):
		print("Agent: " + msg)


 
def prompt():
	while (True):
		prompt = input('(1) Question \n(2) Complaint \n(3) Other\n Input: ')
		if int(prompt) == 1:
			return 'Question'
		elif int(prompt) == 2:
			return 'Complaint'
		elif int(prompt) == 3:
			return 'Other'
		else:
			print("Please enter a number from 1-3!")
		

def periodic_poll():
	while 1:
		poll()
		sleep(0.05)  # seconds
							




if __name__ == '__main__':

	host, port = '128.195.6.149', 8888
	
	myname = raw_input('What is your name? ')
	p = prompt()
	topic = raw_input('Topic: ')
	client = Client(host, port)

	client.do_send({'name': myname, 'prompt': p, 'topic': topic})

	thread = Thread(target=periodic_poll)
	thread.daemon = True  # die when the main thread dies 
	thread.start()

	done = False
	while not done:
		mytxt = sys.stdin.readline().rstrip()
		if mytxt == ":q":
			break
		client.do_send({'txt': mytxt})

	client.do_close()