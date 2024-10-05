import requests
import xml.etree.ElementTree as ET
import base64

PORT = 31782
ENDPOINT = "bucket"
URL = f"http://challenge.ctf.games:{PORT}/{ENDPOINT}"

r = requests.get(URL)

raw_response = r.text
tree = ET.fromstring(raw_response)
# print(tree)
# print(tree.tag, tree.attrib)
for key in tree.findall("{http://s3.amazonaws.com/doc/2006-03-01/}Contents"):
    key_path = key.find("{http://s3.amazonaws.com/doc/2006-03-01/}Key").text

    # r = requests.get(f"{URL}/{key_path}")
    # obj_contents = r.text
    print(f"processing key [{key_path}]")
    # print(obj_contents)
    try:
        contents = base64.b64decode(key_path)
        print(contents.decode("utf-8"))
    except:
        pass

    # with open(f"output/{key_path.replace('/', '__')}", "w") as f:
    #     f.write(obj_contents)
