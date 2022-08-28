## 1. Registration API

method: POST
URL: /student/register

Request Parameters

| parameters     | type       |
| -------------- | -----------|
| username       | str        |
| password       | str        |
| password_2     | str        |
| email          | str        |

Response:

status code: 200

```json
{
    "message": "tanjiro1 Successfully registerd !",
    "token": "4e68307ab59399f96f659203659d8b88ce42557a",
    "username": "tanjiro1",
    "email": "tanjiro@demonslayer1.com"
}
```

status code: 400

```json
{
    "username": [
        "This field is required."
    ],
    "email": [
        "This field is required."
    ],
    "password": [
        "This field is required."
    ],
    "password_2": [
        "This field is required."
    ]
}
```



