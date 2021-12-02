import requests

ip = '192.168.212.40'

if (ip == ''):
    print('Setup ip-address of Tekronix oscilloscope')
    quit()

url = 'http://' + ip + '/image.png'
r = requests.get(url, allow_redirects=True)

with open('tektronix3.png', 'wb') as file:
    file.write(r.content)