from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import uvicorn

YALIDINE_API_ID = "Your Api Id "
YALIDINE_API_ID_TOKEN = "Your Api Token"
YALIDINE_API_ID_URL = "https://api.yalidine.app/v1/"

Wilaya_Data = []
Fees_Data = []
Communes_Data = []

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
        'X-API-ID': YALIDINE_API_ID,
        'X-API-TOKEN': YALIDINE_API_ID_TOKEN,
    }
    try:
        response = requests.get(YALIDINE_API_ID_URL + "wilayas/", headers=headers)
        response.raise_for_status()
        data = response.json()["data"]
        Wilaya_Data = data

    except requests.exceptions.RequestException as e:
        print('Error fetching data:', e)

# fetch fees data from yalidine :
def fetch_fees_Data():
    global Fees_Data
    headers = {
        'X-API-ID': YALIDINE_API_ID,
        'X-API-TOKEN': YALIDINE_API_ID_TOKEN,
    }
    try:
        response = requests.get(YALIDINE_API_ID_URL + "deliveryfees/", headers=headers)
        response.raise_for_status()
        data = response.json()["data"]
        Fees_Data = data

    except requests.exceptions.RequestException as e:
        print('Error fetching data', e)

# fetch communes data from yalidine
def fetch_communes_data():
    global  Communes_Data
    headers = {
        'X-API-ID': YALIDINE_API_ID,
        'X-API-TOKEN': YALIDINE_API_ID_TOKEN,
    }
    try:
        response_page1 = requests.get(YALIDINE_API_ID_URL+"communes/?page=1&page_size=1900&is_deliverable=true",headers=headers)
        response_page1.raise_for_status()
        data_page1 = response_page1.json()["data"]

        response_page2 = requests.get(YALIDINE_API_ID_URL+"communes/?page=2&page_size=1900&is_deliverable=true",headers=headers)
        response_page2.raise_for_status()
        data_page2 = response_page2.json()["data"]

        Communes_Data = data_page1 + data_page2

    except requests.exceptions.RequestException as e:
        print('Error fetching data', e)


@app.get("/api/wilaya")
def wilaya():
    fetch_wilaya_Data()
    return Wilaya_Data

@app.get("/api/fees")
def fees():
    fetch_fees_Data()
    return Fees_Data
@app.get("/api/communes")
def communes():
    fetch_communes_data()
    return Communes_Data

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)