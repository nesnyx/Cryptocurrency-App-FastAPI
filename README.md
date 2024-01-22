
# Cryptocurrency Webapp use FastAPI

This is simple project build use FastAPI and data from CoinMarketCap API.






## Features

- Listing Latest
- About
- SOON!



## Documentation
If you want to check out CMC API Documentation can go to through this link.
[CMC API Documentation](https://coinmarketcap.com/api/documentation)



## Installation

You need do install some packages from venv and i provide <b>requirement.txt</b> for install packages what needed

```bash
  pip install -r requirement.txt
```
    
## API Reference

#### Get all Listing

```http
  GET /listing
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `X-CMC_PRO_API_KEY` | `string` | **Required**. Your API key |

#### Get Listing by Id

```http
  GET /listing/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |


#### About

```http
  GET /about
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `none`      | `none` | |




## Support

For support, email whycreation34@gmail.com.

