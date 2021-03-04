import requests

res = requests.post('https://reqres.in/api/users')

print(res)
print(res.content)
