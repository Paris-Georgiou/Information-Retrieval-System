import requests
import os
import re
import json

question = input("Which question do you want to Query? Question = ")
results = int(input("How many results do you want? Results = "))
#results = 20

query = ""
if(int(question) <10):
    question = '0'+question

with open('testingQueries.txt', encoding="utf-8") as readfile:
    for textline in readfile:
        if 'Q'+str(question) in textline:
            query = textline[4:].strip()
            query = re.sub('[^a-zA-Z.\d\s]', '', query)

with open('Elasticsearch_Query.json', 'w') as outfile:
    data = { "from": 1, "size": results, "query" : { "query_string":{ "query": query}}}
    json.dump(data, outfile, indent=4)

url = 'Http://localhost:9200/project/files/_search'
headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
r = requests.get(url, data=open('Elasticsearch_Query.json', 'rb'), headers=headers)

with open('Results.txt', 'w') as outfile:  
    outfile.write(json.dumps(r.json(), indent=4))
    outfile.close()