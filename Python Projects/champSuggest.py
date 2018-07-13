# champSuggest.py
# A Python program that reads in a summoner name, and prints out a champion similar to the highest rated champion the summoner has.

import urllib.request
import json
import ssl
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# sumName = input("Enter summoner name: ")
# apiKey = input("Enter your API key: ")

sumName = "tdlpoof"
apiKey = "RGAPI-44ebfac1-76d0-44b7-9b5b-d41d1fe13301"

lolUrl = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + sumName + "?api_key=" + apiKey
connection = urllib.request.urlopen(lolUrl, context=ctx)
time.sleep(0.25)

data = connection.read().decode()
js = json.loads(data)
sumId = js["id"]

cMastUrl = "https://na1.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/" + str(sumId) + "?api_key=" + apiKey
mastCt = urllib.request.urlopen(cMastUrl, context=ctx)
time.sleep(0.25)

mastData = mastCt.read().decode()
champs = json.loads(mastData)
ids = list()

for champ in champs:
    ids.append(champ["championId"])

cnvUrl = "https://na1.api.riotgames.com/lol/static-data/v3/champions/" + str(ids[0]) + "?api_key=" + apiKey
cnvCt = urllib.request.urlopen(cnvUrl, context=ctx)
time.sleep(0.25)
    
cnvData = cnvCt.read().decode()
cnvJs = json.loads(cnvData)
    
print(cnvJs["name"] + ",", cnvJs["title"])

ddrg = "http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion/" + cnvJs["name"] + ".json"
champCt = urllib.request.urlopen(ddrg, context=ctx)
time.sleep(0.25)

champData = champCt.read().decode()
champInfo = json.loads(champData)
print(json.dumps(champInfo,indent=2))
