#!/usr/bin/env python3
from server.udp_server import udp_server
import sys
import socket

if __name__ == "__main__":
    if (len(sys.args) == 2):
        udp_addr = "192.168.0." + str(sys.args[1])
        try:
            server = udp_server(udp_addr, 3333)
            server.upload_data("localhost:8000/addData")
        except socket.error as msg:
            print ("wrong ip address. Check with ifconfig command on ground station pi")
    
    else:
        print ("call this script with the last 3 digits of the udp server ip address as arg 1")

