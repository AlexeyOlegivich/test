import requests

url = 'https://wttr.in/'
params = '?n&lang=ru&M&m&T'
city = ['London', 'SVO', 'череповец']
for i in range(3):
    response = requests.get(url+city[i]+params)
    response.raise_for_status()
    print(response.text)
    i += 1
