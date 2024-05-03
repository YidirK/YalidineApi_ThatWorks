
# YalidineApi_ThatWorks (self-hosted)

The original yalidine API is blocked by Cors origin when you try to use it on a browser, with this API (self-hosted) you no longer have this problem and no more headache problems xD. 



## Use the Api 
Replace with your api **Id** and your api **Token** (You can find them [here](https://yalidine.app/app/dev/index.php) )

```bash
YALIDINE_API_ID = "Your Api Id "
YALIDINE_API_ID_TOKEN = "Your Api Token"
YALIDINE_API_ID_URL = "https://api.yalidine.app/v1/"

```

Install FastApi

```bash
pip install fastapi
```

Install uvicorn

```bash
pip install "uvicorn[standard]"
```


Run the Api

```bash
Python Main.py
```
    
## API Reference

#### Get all wilaya

```http
  GET /api/wilaya
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `No parameters` | `****`| `****` |

#### Get fees

```http
  GET /api/fees
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `No parameters`      | `****` | `****` |

#### Get communes

```http
  GET /api/communes
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `No parameters`      | `****` | `****` |




## Roadmap

- **Add all API Reference**
-  **~~Add Cach~~e** 



## Tech Stack

**Python** 


**FastApi** 


## Authors

- [@YidirK](https://github.com/YidirK)




