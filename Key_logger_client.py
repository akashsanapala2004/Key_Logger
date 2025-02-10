import socket as skt
import pickle as pkle
client = skt.socket(skt.AF_INET,skt.SOCK_STREAM)
while True:
	try:
		client.connect(('127.0.0.1',9999))
		break
	except  ConnectionError :
		continue

while True:
	unpacked = client.recv(1024)
	if (unpacked):
		data = pkle.loads(unpacked)
		st,time,key,app = data
		if(st):
			state = " Pressed"
		else:
			state = "Released"
		print(f"{time}  {state} : {key}  {app}")
		unpacked = ''
	else : 
		break

