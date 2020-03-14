import xml.etree.ElementTree as ET
import os

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def fix_xml(filename):
    ET.register_namespace('', "http://cordis.europa.eu")
    tree = ET.parse(filename)
    root = tree.getroot()

    new_elem_string = root[3].text + ' ' + root[2].text
    root.remove(root[2])
    root.remove(root[2])
    new_elem = ET.SubElement(root, 'text')
    new_elem.text = new_elem_string
    temp_elem = root[2]
    root.remove(root[2])
    new_elem2 = ET.SubElement(root, 'identifier')
    new_elem2.text = temp_elem.text
    indent(root)
    tree.write(filename,encoding = "UTF-8", xml_declaration = True)
    print(filename + ' OK')

path = './Parsed files/'

for filename in os.listdir(path):
    fix_xml(path + filename)
print('Finished fixing the Parsed xml files!')