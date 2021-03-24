import requests

res = requests.get('https://reqres.in/api/unknown')

print(res)
print(res.content)
