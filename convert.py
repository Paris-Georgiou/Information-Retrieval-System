import xmltodict
import pprint
import json
import os 

def make_json(filename):
    with open('./Parsed files/' + filename, encoding='utf-8') as fd:
        doc = xmltodict.parse(fd.read(), encoding='utf-8', process_namespaces=True, namespaces={"http://cordis.europa.eu":''})
    if(not(os.path.exists('./Collection/'))):
        os.makedirs('./Collection/')
    out_file_name = filename[0:len(filename)-4] +".json"
    with open('./Collection/' + out_file_name, 'w') as outfile:
        outfile.write(json.dumps(doc, indent=4))
        outfile.close()
    print(out_file_name + ' OK')
    
path = './Parsed files/'

for filename in os.listdir(path):
    make_json(filename)
print('Finished converting the Parsed xml files to json files!')    