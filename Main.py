#!/usr/bin/python3
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
import uvicorn
from cachetools import TTLCache
import json
from pydantic import BaseModel


__config = dict()
try:
    with open("config.json", "r", encoding="utf-8") as _f:
        __config = json.loads(_f.read())
except:
    exit(1)


# the cache have 24 hours (86400 seconds)
Cache_Time = 86400
Cache_Max_Size = 1

Wilaya_Data = []
Fees_Data = []
Communes_Data = []
Centers_Data = []

# add 24h cache
wilaya_cache = TTLCache(maxsize=Cache_Max_Size, ttl=Cache_Time)
fees_cache = TTLCache(maxsize=Cache_Max_Size, ttl=Cache_Time)
communes_cache = TTLCache(maxsize=Cache_Max_Size, ttl=Cache_Time)
centers_cache = TTLCache(maxsize=Cache_Max_Size, ttl=Cache_Time)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# fetch Wilaya Data from yalidine:
def fetch_wilaya_Data():
    global Wilaya_Data
    headers = {
        'X-API-ID': __config["YALIDINE_API_ID"],
        'X-API-TOKEN': __config["YALIDINE_API_ID_TOKEN"],
    }
    try:
        response = requests.get(__config["YALIDINE_API_ID_URL"] + "wilayas/", headers=headers)
        response.raise_for_status()
        data = response.json()["data"]
        Wilaya_Data = data

    except requests.exceptions.RequestException as e:
        print('Error fetching data:', e)

# fetch fees data from yalidine :
def fetch_fees_Data():
    global Fees_Data
    headers = {
        'X-API-ID': __config["YALIDINE_API_ID"],
        'X-API-TOKEN': __config["YALIDINE_API_ID_TOKEN"],
    }
    try:
        response = requests.get(__config["YALIDINE_API_ID_URL"] + "deliveryfees/", headers=headers)
        response.raise_for_status()
        data = response.json()["data"]
        Fees_Data = data

    except requests.exceptions.RequestException as e:
        print('Error fetching data', e)

# fetch communes data from yalidine
def fetch_communes_data():
    global  Communes_Data
    headers = {
        'X-API-ID': __config["YALIDINE_API_ID"],
        'X-API-TOKEN': __config["YALIDINE_API_ID_TOKEN"],
    }
    try:
        response_page1 = requests.get(__config["YALIDINE_API_ID_URL"]+"communes/?page=1&page_size=1900&is_deliverable=true", headers=headers)
        response_page1.raise_for_status()
        data_page1 = response_page1.json()["data"]

        response_page2 = requests.get(__config["YALIDINE_API_ID_URL"]+"communes/?page=2&page_size=1900&is_deliverable=true", headers=headers)
        response_page2.raise_for_status()
        data_page2 = response_page2.json()["data"]

        Communes_Data = data_page1 + data_page2

    except requests.exceptions.RequestException as e:
        print('Error fetching data', e)

def fetch_centers_data():
    global Centers_Data
    headers={
        'X-API-ID':__config["YALIDINE_API_ID"],
        'X-API-TOKEN':__config["YALIDINE_API_ID_TOKEN"],
    }
    try:
        response = requests.get(__config["YALIDINE_API_ID_URL"]+"centers", headers=headers)
        response.raise_for_status()
        data = response.json()["data"]
        Centers_Data = data
    except requests.exceptions.RequestException as e:
        print('Error fetching data', e)

# Push parcel data  to Yalidine
def create_parcels(data):
    headers = {
        'X-API-ID': __config["YALIDINE_API_ID"],
        'X-API-TOKEN': __config["YALIDINE_API_ID_TOKEN"],
    }
    try:
        response = requests.post(__config["YALIDINE_API_ID_URL"] + "parcels", data=json.dumps(data), headers=headers)
        if response.status_code != 200:
            print("Eror" + response.text)
        else :
            return response.json()
    except Exception as e:
        print("Erreur lors de la création des colis :", e)


class Parcel(BaseModel):
    order_id: str
    from_wilaya_name: str
    firstname: str
    familyname: str
    contact_phone: str
    address: str
    to_commune_name: str
    to_wilaya_name: str
    product_list: str
    price: float
    do_insurance: bool
    declared_value: float
    height: float
    width: float
    length: float
    weight: float
    freeshipping: bool
    is_stopdesk: bool
    stopdesk_id: int
    has_exchange: bool
    product_to_collect: str = None
@app.get("/api/wilaya")
def wilaya():
    if not Wilaya_Data:
        fetch_wilaya_Data()
    return Wilaya_Data

@app.get("/api/fees")
def fees():
    if not Fees_Data:
        fetch_fees_Data()
    return Fees_Data

@app.get("/api/communes")
def communes():
    if not Communes_Data:
        fetch_communes_data()
    return Communes_Data
@app.get("/api/centers")
def centers():
    if not Centers_Data:
        fetch_centers_data()
    return  Centers_Data

@app.post("/api/parcel")
def parcel(parcel: Parcel):
    try:
        data = parcel.dict()
        create_parcels([data])
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=443,
        ssl_keyfile="./key.pem",
        ssl_certfile="./cert.pem"
    )

