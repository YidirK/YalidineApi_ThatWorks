
# YalidineApi_ThatWorks (Self-Hosted)

The original Yalidine API is blocked by CORS origin when accessed from a browser. This self-hosted API bypasses that issue, saving you from CORS headaches. xD

## Use the API

Creat config.json and replace the placeholder values with your API **Id** and **Token**  (You can find them [here](https://yalidine.app/app/dev/index.php)):

```bash
YALIDINE_API_ID = "Your API Id"
YALIDINE_API_ID_TOKEN = "Your API Token"
YALIDINE_API_ID_URL = "https://api.yalidine.app/v1/"
```

Install the required packages:

```bash
pip install fastapi
pip install requests
pip install "uvicorn[standard]"
pip install cachetools

```

Run the Api

```bash
Python Main.py
```

## Enabling SSL
For enhanced security, you can enable SSL to secure the communication between your API server and clients.

### How to Enable SSL
#### 1- Obtain an SSL Certificate: 
Use Certbot or any other SSL certificate provider to obtain your SSL certificate files. Certbot is a popular choice for free SSL certificates.

#### 2- Configure SSL in Main.py: 
Uncomment the following lines in the Main.py file to enable SSL. Make sure to replace ./key.pem and ./cert.pem with the paths to your actual SSL certificate files:
### Example Configuration :
```bash
if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=__config["server_port"],
        ssl_keyfile="./key.pem",
        ssl_certfile="./cert.pem"
    )
```

## API Reference

#### Get all wilaya

```http
  GET /api/wilaya
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `No parameters` | `-`| `Fetches all wilayas` |

#### Get fees

```http
  GET /api/fees
```

| Parameter | Type  | Description                      |
| :-------- |:------|:---------------------------------|
| `from_wilaya_id`      | `int` | `ID of the starting wilaya`      |
| `to_wilaya_id`      | `int` | `ID of the destination wilaya`      |

#### Get communes

```http
  GET /api/communes
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `No parameters`      | `-` | `Fetches all communes` |

#### Get Centers

```http
  GET /api/centers
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `No parameters`      | `-` | `Fetches all centers` |

#### Create Parcel

```http
  POST /api/parcel
```

| Parameter | Type       | Description                                  |
| :-------- |:-----------|:---------------------------------------------|
| `order_id`      | `string`   | `Unique identifier for the order`            |
| `from_wilaya_name`      | `string`   | `Name of the origin wilaya`                  |
| `firstname`      | `string`   | `Destination firstname`                      |
| `familyname`      | `string`   | `Destination familyname`                     |
| `contact_phone`      | `string`   | `Destination contact_phone`                  |
| `address`      | `string`   | `Destination addressr`                       |
| `to_commune_name`      | `string`   | `Destination commune`                        |
| `to_wilaya_name`      | `string`   | `Destination wilaya`                         |
| `product_list`      | `string`   | `List of products being shipped`             |
| `price`      | `	float`   | `Price of the parcel`                        |
| `do_insurance`      | `	boolean` | `Whether the parcel is insured`              |
| `declared_value`      | `float`    | `Declared value of the parcel for insurance` |
| `height`      | `float`    | `Height of the parcel in cm`                 |
| `width`      | `float`    | `Width of the parcel in cm`                  |
| `length`      | `float`    | `	Length of the parcel`                      |
| `weight`      | `float`    | `Weight of the parcel in kg`                 |
| `freeshipping`      | `boolean`  | `Whether shipping is free`                   |
| `is_stopdesk`      | `boolean`  | `Whether the parcel is a stop desk parcel`   |
| `stopdesk_id`      | `int`      | `ID of the stop desk`   |
| `has_exchange`      | `boolean`  | `Whether an exchange is possible`   |
| `product_to_collect`      | `string`   | `Product to be collected (if has_exchange)`   |


## Roadmap

- **Add more API references**
-  **Improve caching** 



## Tech Stack

**Python** 


**FastApi** 


## Authors

- [@YidirK](https://github.com/YidirK)

## License
This project is licensed under the MIT License - see the LICENSE file for details.




