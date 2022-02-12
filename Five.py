import json
import requests

chave = "ce3f52e8644149471bb9f041f93de570"

cidade = input("Escolha uma cidade: ")
url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(cidade, chave)

res = requests.get(url)
data = res.json()

if data["cod"] != "404":

   temp = data["main"]["temp"]
   min_temp = data["main"]["temp_min"]
   max_temp = data["main"]["temp_max"]
   sens_temp = data["main"]["feels_like"]
   desc = data["weather"][0]["description"]
   cli = data["weather"][0]["main"]

   print("Temperatura em C: {}".format(temp))
   print("Temperatura mínima: {}".format(min_temp))
   print("Temperatura máxima: {}".format(max_temp))
   print("Sensação térmica: {}".format(sens_temp))
   print("Descrição do tempo: {}".format(desc))
   if cli == "rain":
      print("Leve um guarda-chuva")

else:
    print("Cidade não encontrada")
