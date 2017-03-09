import os
from subprocess import call

__isOpened = False

def s_init(port, baudRate):
	try:
		call(["serial_init.exe", str(port), str(baudRate)])
	except WindowsError:
		print("Error: can't open \"serial_init.exe\"")

def s_open(port):
	global __serial, __isOpened
	if not __isOpened:
		try:
			__serial = os.open(port, os.O_RDWR)
		except:
			print("Can't open port %s" % (port))
			__isOpened = False
		else:
			print("Port %s opened" % (port))
			__isOpened = True
	elif __isOpened:
		print("Port already opened")

def s_close():
	global __isOpened
	if __isOpened:
		print("Port closed")
		os.close(__serial)
		__isOpened = False

def s_ports(lim = 10):
	ports = []
	for i in range(1, lim + 1):
		try:
			__port = os.open("COM%s" % (i), os.O_RDWR)
			os.close(__port)
		except OSError as e:
			if e.errno == 13: # PermissionError
				ports.append({"COM%s" % (i): "busy"})
		except:
			continue
		else:
			ports.append({"COM%s" % (i): "available"})
	return ports

def s_read(lastSymbol = '\n'):
	buffer = ""
	if __isOpened:
		while True:
			received = os.read(__serial, 1024).decode()
			buffer += received
			if lastSymbol in buffer:
				break
		return buffer

def s_send(text):
	if __isOpened:
		os.write(__serial, text)

def s_isOpened():
	return __isOpened
