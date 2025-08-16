#! /bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2 :
	target = socket.gethostbyname(sys.argv[1])
else:
	print("ivalid amount of args")
	
print("-" * 50)
print("Scanning target "+ target)
print("Time started "+str(datetime.now()))
print("-" * 50)

try: 
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target , port)) #ex - error indicator if 0 - port is open , if 1 then closed
		if result == 0 :
			print(f"port {port} is open")
		s.close()


except KeyboardInterrupt:
	print("\n EXiting program ")
	sys.exit()
	
except socket.gaierror:
	print("hostname could not be resolved")
	sys.exit()
	
except socket.error:
	print("could not connect to server")
	sys.exit()
