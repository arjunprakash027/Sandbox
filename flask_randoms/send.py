import requests

url = "http://127.0.0.1:5000/get_file"
files = {'file': open('ex.txt','rb')}
name = {'name': 'ex.txt'}

r = requests.post(url, files=files,data=name)