import json
import random 

class MakeFakeData:
  
    def __init__(self):
      self.faketime = 0

    def fakedata(self):
      self.faketime = self.faketime + 1

      fakedatadict = {
        'time': self.faketime,
        'vboost_1': random.randint(0, 10),
        'vboost_2': random.randint(0, 10),
        'vboost_3': random.randint(0, 10),
        'vbatt': random.randint(0, 10),
        'curin_1': random.randint(0, 10),
        'curin_2': random.randint(0, 10),
        'curin_3': random.randint(0, 10),
        'suncurrent': random.randint(0, 10),
        'cursys': random.randint(0, 10),
      }

      json_dict = json.dumps(fakedatadict).encode('utf-8')

      return json_dict

