import requests, json
import os

url = 'Http://localhost:9200/project'
headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
r = requests.get(url)
if(r.status_code == 404):
    r = requests.put(url, data=open('Elasticsearch_Analyzer.json', 'rb'), headers=headers)
    print('Index analyzer OK with status: ' + str(r.status_code))

    url = 'Http://localhost:9200/project/files/'
    path = './Collection/'
    for filename in os.listdir(path):    
       r = requests.post(url, data=open(path + filename, 'rb'), headers=headers)
       print(filename + ' Ok')
    print('Finished uploading the whole collection!')
else:
    print('Index analyzer is already running')