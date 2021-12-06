#!/usr/bin/env python3
from server.udp_server import udp_server
import requests

if __name__ == "__main__":
    server = udp_server("192.168.0.200", 3333)
    server.upload_data("localhost:8000/addData")
