import requests

cep = input("Digite seu CEP:\n")

resposta = requests.get(url=f"http://viacep.com.br/ws/{cep}/json/").json()

filtro = resposta["localidade"]
print(filtro)