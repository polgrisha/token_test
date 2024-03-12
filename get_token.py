import requests
import time 
import json

url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

payload='scope=GIGACHAT_API_PERS'
headers = {
'Content-Type': 'application/x-www-form-urlencoded',
'Accept': 'application/json',
'RqUID': '6f0b1291-c7f3-43c6-bb2e-9f3efb2dc98e',
'Authorization': 'Basic MDI2ODVhZjMtYWNmYi00NDE2LWFiOWMtYjNlNjY5OTVlOWRlOmRiYjQwZTM1LWMzMDQtNDI4Yi1iNGQyLTUyMTUwNjYwNThmZQ=='
}
response = requests.request("POST", url, headers=headers, data=payload, verify=False)
print(response)
json.dump(json.loads(response.text), open('token.txt', 'w'))
    
    

    