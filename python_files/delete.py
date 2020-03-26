import requests

url = 'http://127.0.0.1:5000'
myfiles = {'file': open('download.pdf' ,'rb')}
myjson = {'somekey': 'somevalue'}
x = requests.post(url, files = myfiles, json = myjson)

print(x.text)
