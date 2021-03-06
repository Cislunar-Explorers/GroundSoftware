# Data Pipeline Overview
<p align="center">
  <img src="/UDP_groundstation/media/frame.png" width="750" title="hover text" alt="data pipeline schematic here">
</p>

This repository concerns the UDP server step of the data pipeline. The UDP server on the HITL Pi listens for and receives data from the UDP client on the FlatSat Pi. Upon receiving data, the UDP server sends the data with a request to the specified API endpoint. It is required that the FlatSat and HITL Pi are connected to the same network. 

Note that since UDP is a connectionless protocol, the client cannot confirm that the server has received a message, and the server cannot confirm if messages were lost along the way.

For information on the UDP client step, view: https://github.com/Cislunar-Explorers/FlightSoftware/tree/master/udp_client

For information on the Django step, view: https://github.com/Cislunar-Explorers/API_database

For information on the Grafana step, view: (doc coming soon)


# Set up instructions
<i>Note</i>: Before running the UDP server, make sure the Django server is running. If unsure, follow the url https://cislunar-data.herokuapp.com/.

Install requests if not installed on system.     
```
pip install requests
```

From this directory, run the server.
```
python3 main.py
```
