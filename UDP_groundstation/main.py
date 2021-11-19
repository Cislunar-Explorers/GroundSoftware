from udp_server_tester.servertester import ServerTester

if __name__ == "__main__":

    # SEE IF RASPBERRY PI TRACKS GIT DJSKDLASJDKLSA:JDKSLA:DJKAS test
    server = ServerTester("192.168.0.101", 3333)
    server.listen_for_data()