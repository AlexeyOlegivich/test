import requests

url = 'https://wttr.in/'
city = ['London', 'SVO', 'череповец']
for i in range(3):
    response = requests.get(url+city[i])
    response.raise_for_status()
    print(response.text)
    #print(response.url)
    i += 1