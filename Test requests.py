import requests
url = 'a'
r = requests.get(url)
data = r.json()
print(data['name'],data['temperature'])