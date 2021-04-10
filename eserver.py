import socket
import sys
import time
import argparse
import base64
def listen(lhost, lport):
	try:
		s = socket.socket()
		s.bind((lhost, lport))
	except Exception as f:
		print(f"[-] Couldn't bind {lhost}:{str(lport)} Reason: {f}")
		sys.exit(5)
	traffic_utf = open("traffic.u", 'w')
	traffic = open("traffic.ass", 'a')
	print(f"[*] Listening as {lhost}:{str(lport)} . . . Type: server")
	s.listen(5)
	client, client_addr = s.accept()
	print(f"[*] Client {client_addr[0]} connected on port {client_addr[1]} . . .")
	client.send("infome".encode())
	info = client.recv(15813).decode()
	print(f"[*] Info about {client_addr[0]}")
	print(info)
	print(f"[*] Starting sniffer . . .")
	while True:
		data = client.recv(14813).decode()
		ds = data.encode()
		print("DATA: " + data + "\x0A")
		bs = base64.b64encode(ds)
		primary = bs.decode()
		traffic.write(primary + "\n")
		traffic_utf.write(data + "\x0A")
def __main__():
	parsie = argparse.ArgumentParser()
	parsie.add_argument("-l", "--localhost", help=f"Specify a LocalIP Default - {socket.gethostbyname(socket.gethostname())}", default=socket.gethostbyname(socket.gethostname()), required=False)
	parsie.add_argument("-p", "--localport", help=f"Specify a ForwardedPort Default: 5731", default=5731, required=False)
	args = parsie.parse_args()
	lhost = args.localhost 
	lport = int(args.localport)
	listen(lhost, lport)
__main__()