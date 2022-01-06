import requests

resp = requests.get('https://dn8mlk7hdujby.cloudfront.net/interview/insurance/58')

print(resp)

if resp:
    print('Responde correctamente')
else:
    print('Respuesta fallida, favor revisar')

json = resp.json()
print(json)
