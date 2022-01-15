import requests
import json

req = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/inr.json")
print(req.status_code)

if(req.status_code != 200):
    print("Could not get conv rate")
    exit()

convJson =  json.loads(req.text)


 

print(convJson)

convRate = convJson["inr"]

print(f"Today's conv rate is {convRate}")

inUSD = 12000

outINR = inUSD * convRate
print(f"USD {inUSD} ==> INR {outINR}")