import os
PATH = os.path.abspath("")
EASTER = PATH + '//easter_egg.txt'

def get_easter_egg(txtfile):
	with open(txtfile,'r') as infile:
	    text = infile.read()
	    return text



# if __name__ == '__main__':
#   x = get_easter_egg(EASTER)
#   print(x)