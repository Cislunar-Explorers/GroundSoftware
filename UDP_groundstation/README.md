# Data Pipeline Overview
<p align="center">
  <img src="/UDP_groundstation/media/schematic.png" width="500" title="hover text" alt="data pipeline schematic here">
</p>

This repository concerns the UDP server step of the data pipeline. The UDP server on the HITL Pi listens for and receives data from the UDP client on the FlatSat Pi. It is required that the FlatSat and HITL Pi are connected to the same network and that the Django server is running in the same localhost at port 8000.

For information on the UDP client step, view: https://github.com/Cislunar-Explorers/FlightSoftware/tree/master/udp_client

For information on the Django step, view: https://github.com/Cislunar-Explorers/API_database

For information on the Grafana step, view: (doc coming soon)


# Set up instructions
<i>Note</i>: Before running the UDP server, make sure the Django server is running. If unsure, follow the url localhost:8000 on the HITL Pi's browser. If the page does not return a Django REST Framework page titled "Test Connection", you need to start the Django server - follow the instructions in the Django step link above. 

Install requests if not installed on system.
```
pip install requests
```

From this directory, run the server.
```
python3 main.py
```
