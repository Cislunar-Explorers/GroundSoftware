from server.udp_server import udp_server

if __name__ == "__main__":

    server = udp_server("192.168.0.101", 3333)
    server.upload_data("localhost:8000/addData")