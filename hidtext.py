#!/usr/bin/env python3
# -*- coding utf-8 -*-

import os
import sys
import socket
import threading
import requests

def main():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((os.getenv("HOST"), int(os.getenv("PORT"))))
	server.listen(5)
	print(f'Server listen on {os.getenv("HOST")}:{os.getenv("PORT")}')
	while True:
		client, addr = server.accept()
		client_handler = threading.Thread(target=client_hand, args=(client,))
		client_handler.start()

def client_hand(client_socket):
	with client_socket as sock:
		res = sock.recv(1024)
		html = requests.get(os.getenv("URL")).text + "<style>a,p,bid,h1,h2,h3,h4,h5,span,li,strong{color:whitesmoke;background-color:whitesmoke;border-radius:10px;padding:0}</style>"
		print(f'Received: {res.decode("utf-8")}')
		sock.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
		sock.sendall(html.encode())
		

if __name__ == "__main__": main()

