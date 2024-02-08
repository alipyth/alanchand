import requests
from requests.structures import CaseInsensitiveDict

url = "https://admin.alanchand.com/api/arz"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

data = '{"lang":"fa"}'


resp = requests.post(url, headers=headers, data=data)
#print(resp.json()) #for see all currencys
print(f"{resp.json()['arz'][0]['price'][0]['price']} ----------- {resp.json()['arz'][0]['price'][0]['updated_at']}") #this is dollar price export
