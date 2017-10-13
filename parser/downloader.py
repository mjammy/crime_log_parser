import requests

resp = requests.get('https://police.lehigh.edu/')

print(resp.content)