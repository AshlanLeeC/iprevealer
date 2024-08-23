#!/usr/bin/env python3

import socket

def get_local_ip():

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:

s.connect(("8.8.8.8", 80))

ip_address = s.getsockname()[0]

except Exception as e:

ip_address = "No IP Address :( "

finally:

s.close()

return ip_address

if __name__ == "__main__":

ip_address = get_local_ip()

print(ip_address)
