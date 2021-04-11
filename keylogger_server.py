import socket
import sys
import time
import argparse
def listen(lhost, lport):
	try:
		k = socket.socket()
		k.bind((lhost, lport))
	except Exception as e:
		print(f"[-] Couldn't bind {lhost}:{str(lport)} Reason: {e}")
		sys.exit(1)
	print(f"[*] Listening as {lhost}:{str(lport)}")
	k.listen(5)
	client, client_addr = k.accept()
	print(f"[*] Client {client_addr[0]} connected on port {client_addr[1]}")
	while True:
		_ = client.recv(16813).decode()
		print("[*] Characters: " + _)

def __main__():
	parsie = argparse.ArgumentParser()
	parsie.add_argument("-l", "--localhost", help=f"Specify LocalIP | Default: {socket.gethostbyname(socket.gethostname())}", default=socket.gethostbyname(socket.gethostname()),required=False)
	parsie.add_argument("-p", '--localport', help=f"Specify a port | Default: 5733", default=5733, required=False)
	args = parsie.parse_args()
	lhost = args.localhost
	lport = int(args.localport)
	listen(lhost, lport)
__main__()