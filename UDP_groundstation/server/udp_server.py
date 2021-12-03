import ast
import socket
import requests


class udp_server:

    def __init__(self, addr: str, port: int):
        """
        create a UDP socket server side

        @param addr: the IP address of the server
        @param port: the port that the server is running in
        """
        self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverSock.bind((addr, port))
        print("UDP server up and listening")


    def binary_to_dict(self, the_data: bytes):
        """
        decode binary dict data to python string dict

        @param the_data: UTF-encoded data sent from udp client
        @return decoded string
        """
        dict_str = the_data.decode("UTF-8")
        data_dict = ast.literal_eval(dict_str)
        return data_dict


    def upload_data(self, api_url: str):
        """
        listen for data from client and send to django API

        @param api_url: API endpoint url
        """
        while True:

            data, addr = self.serverSock.recvfrom(2048)
            print(f"data received from addr:{addr}")

            # # uncomment for debugging
            # print(f"data = {self.binary_to_dict(data)}")

            headers = {'content-type': 'application/json'}
            response = requests.post(api_url, data=data, headers=headers)
            print(response.headers)
