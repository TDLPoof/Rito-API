# champSuggest.py
# A Python program that reads in a summoner name, and prints out a champion similar to the highest rated champion the summoner has.
# Rando Comment

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
apiKey = "RGAPI-8c5e4dd9-36e8-43e6-9d12-cf1ff4e698a3"

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
champsMast = json.loads(mastData)
ids = list()

for champMast in champsMast:
    ids.append(champMast["championId"])

cnvUrl = "https://na1.api.riotgames.com/lol/static-data/v3/champions/" + str(ids[0]) + "?api_key=" + apiKey
cnvCt = urllib.request.urlopen(cnvUrl, context=ctx)
time.sleep(0.25)
    
cnvData = cnvCt.read().decode()
cnvJs = json.loads(cnvData)

ddrg = "http://ddragon.leagueoflegends.com/cdn/8.13.1/data/en_US/champion/" + cnvJs["name"] + ".json"
champCt = urllib.request.urlopen(ddrg, context=ctx)
time.sleep(0.25)

champData = champCt.read().decode()
champInfo = json.loads(champData)
champRoles = champInfo["data"][cnvJs["key"]]["tags"]

role = champRoles[0]

cmpsUrl = "http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json"
cmpsCt = urllib.request.urlopen(ddrg, context=ctx)
time.sleep(0.25)
