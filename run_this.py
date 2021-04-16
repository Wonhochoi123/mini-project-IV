import requests
import json

with open('data.txt') as json_file:
    data_d = json.load(json_file)
data=data_d['0']
import json
URL='http://ec2-18-190-160-196.us-east-2.compute.amazonaws.com:5555/scoring'
r = requests.post(url = URL, json = data) 
if r.json()==[1]:
    print('Approved!')
if r.json()==[0]:
    print('Nope')