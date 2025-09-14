from http.client import responses

import requests
import csv
def get_info(poke):
    base = "https://pokeapi.co//api//v2//"
    poke=poke.lower()
    url=f"{base}//pokemon//{poke}"
    info=requests.get(url)
    if info.status_code==200:
        data=info.json()
        return data
    else:
        print("error code")
        print(info)
name=input("Give pokemon name")
path="C:\\Users\\My Pc\\Desktop\\prog\\poke\\poke.csv"
data=get_info((name))
if data:
    print(data["id"])
    print(data["name"])
    for k in data["moves"]:
        print(k)