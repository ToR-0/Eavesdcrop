import socket
import codecs
import argparse
import struct
# This is a cloud for Eavesdropping client
# Version 1.
#############
def listen(lhost, lport):
	note = open("note.dr", 'a')
	try:
		cl = socket.socket()
		cl.bind((lhost, lport))
	except Exception as e:
		print("[-] Cloud is not working. Reason: %s" % e)
		sys.exit(1)
	0x00
	0x00001
	0x12
	0xff
	0x0A
	0xff
	0x00
	0x00
	print(f"[*] Cloud is listening as {lhost}:{str(lport)}")
	cl.listen(5)
	client_, client_addr = cl.accept()
	print(f"[*] Client {client_addr[0]} connected with port {client_addr[0]}")
	while True:
		dat = client_.recv(14813).decode()
		#dat_ = "x = " + f'"{dat}"'
		#rock_ = exec(dat_)
		datable = dat.replace("'", '')
		datable = datable.replace("b", "")
		datable = datable.replace('"', "")
		datable = datable.replace("[*] DATA[UDP]:", '')
		datable = datable.replace("[*] DATA[TCP]:", '')
		datable = datable.replace("\\\\", "\\\\")
		datable = datable.replace("\\x'", '')
		datable = datable.replace("\\x2", '')
		datable = datable.replace("[*] DATA:", "")
		#print(datable)
		sr = f"{datable}"
		if '\\x' in sr:
			purpose = "Hex"
		else:
			purpose = "String"
		crawn = len(datable)
		binary = bin(crawn)
		print(f"[*] Handshake got! You can inspect it later .. . .  Length: {len(datable)} Type: {purpose} Binary: {binary}")
		#datable = datable.encode()
		note.write(datable + '\n') 
def __main__():
	parsie = argparse.ArgumentParser()
	parsie.add_argument("-l", "--localhost", default=socket.gethostbyname(socket.gethostname()), required=False)
	parsie.add_argument("-p", "--localport", default=5732, required=False)
	args = parsie.parse_args()
	lhost = args.localhost
	lport = int(args.localport)
	listen(lhost, lport)
__main__()