import ast
import socket
import requests
import logging

class udp_server:

    def __init__(self, addr: str, port: int):
        """
        create a UDP socket server side

        @param addr: the IP address of the server
        @param port: the port that the server is running in
        """
        self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverSock.bind((addr, port))
        logging.info("UDP server up and listening\n")
        
        self.time_check = 0;


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
            # receive data from UDP client
            data, addr = self.serverSock.recvfrom(2048)
            logging.info(f"data received from addr:{addr}\n")

            # send to API if data packet arrived in correct order
            data_dict = self.binary_to_dict(data)
            if (data_dict["time"] > self.time_check):
                headers = {'content-type': 'application/json'}
                response = requests.post(api_url, data=data, headers=headers)
                logging.info(response.headers)
                self.time_check = data_dict["time"]
