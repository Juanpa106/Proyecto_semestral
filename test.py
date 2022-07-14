import requests

response2 = requests.get('https://api.waifu.im/random/?selected_tags=ecchi').json()
print(response2['images'])