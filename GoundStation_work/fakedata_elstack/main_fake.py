from makeFakeData import MakeFakeData
import time, requests

datagenerator = MakeFakeData()

while True:
  json_dict = datagenerator.fakedata()
  headers = {'content-type': 'application/json'}
  url = "http://localhost:9200/tester/name"
  response = requests.post(url, data = json_dict, headers=headers)
  print(response.headers)

  time.sleep(10)