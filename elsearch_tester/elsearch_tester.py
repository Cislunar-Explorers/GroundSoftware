import ast
import socket
import requests

class ServerTester:
  
    def __init__(self, addr: str, port: int):
        """
        create a UDP socket server side

        @param: addr: the IP address of the server
        @param: port: the port that the server is running in
        """
        self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverSock.bind((addr, port))
        print("UDP server up and listening")

    def binary_to_dict(self, the_data):
        """
        decode binary dict data to python string dict
        """
        dict_str = the_data.decode("UTF-8")
        data_dict = ast.literal_eval(dict_str)
        return data_dict

    def listen_for_data(self):
        """
        listen for data from client and print out data
        """
        while True:
            data, addr = self.serverSock.recvfrom(2048)
            print(f"data received from addr:{addr}")
            response = requests.put('http://localhost:9200', data = data)
            print(response.headers)