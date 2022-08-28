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

## 2. Login Api

method: POST
URL: /student/login/

Request Parameters

| parameters     | type       |
| -------------- | -----------|
| username       | str        |
| password       | str        |

Response:

status code 200:

```json
{
"token": "107ac919be1e2c0152c667b9db98ecfc5d200a13"
}
```

ststus code 400:

```json
{
    "non_field_errors": [
        "Unable to log in with provided credentials."
    ]
}
```


## 3. Logout Api

method: POST
URL: /student/logout/

header:
Authorization: Token 'access token'

response:

```json
"mohan logged out Successfully !"
```

## 4. create Student detail

method: POST
URL: /student/detail/

header:
Authorization: Token 'access token'


| parameters     | type       |
| -------------- | -----------|
| user           | id         |
| active         | bool       |


response:
status code 201

```json
{
    "id": 1,
    "student_name": "sagar",
    "subject": [],
    "roll_number": "2022sagZZS",
    "total_score": 0.0,
    "division": "NA",
    "uploaded_all_subjects": false,
    "active": true,
    "created_at": "2022-08-28T16:24:11.725744Z",
    "updated_at": "2022-08-28T16:24:11.725785Z",
    "user": 2
}
```

status codde 400:

```json
{
    "user": [
        "Invalid pk \"3\" - object does not exist."
    ]
}
```

## get student details

method: GET
URL: /student/detail/

header:
Authorization: Token 'access token'

Response:

status code 200:

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "student_name": "sagar",
            "subject": [],
            "roll_number": "2022sagZZS",
            "total_score": 0.0,
            "division": "NA",
            "uploaded_all_subjects": false,
            "active": true,
            "created_at": "2022-08-28T16:24:11.725744Z",
            "updated_at": "2022-08-28T16:24:11.725785Z",
            "user": 2
        }
    ]
}
```
## get student details by id

method: GET
URL: /student/detail/{id}

header:
Authorization: Token 'access token'

Response:

status code 200:

```json
{
    "id": 1,
    "student_name": "sagar",
    "subject": [],
    "roll_number": "2022sagZZS",
    "total_score": 0.0,
    "division": "NA",
    "uploaded_all_subjects": false,
    "active": true,
    "created_at": "2022-08-28T16:24:11.725744Z",
    "updated_at": "2022-08-28T16:24:11.725785Z",
    "user": 2
}
```

## 5 add scores api

method: POST
URL: /score_card/detail/

header:
Authorization: Token 'access token'

response:

status code 200
```json
{
    "id": 1,
    "student": {
        "id": 1,
        "student_name": "sagar",
        "subject": [
            "name: physics"
        ],
        "roll_number": "2022sagZZS",
        "total_score": 192.0,
        "division": "NA",
        "uploaded_all_subjects": false,
        "active": true,
        "created_at": "2022-08-28T16:24:11.725744Z",
        "updated_at": "2022-08-28T16:50:09.933898Z",
        "user": 2
    },
    "subject": {
        "id": 1,
        "name": "physics"
    },
    "score": 96.0,
    "created_at": "2022-08-28T16:50:09.937290Z",
    "updated_at": "2022-08-28T16:50:09.937316Z"
}
```

status code 400:

```json
{
    "subject": {
        "name": [
            "\"Sugar\" is not a valid choice."
        ]
    }
}
```

## 6 overall performance api

method: GET
URL: /score_card/overall-performance/
headers:
Authorization: Token 'access token'

response:

status code 200:

```json
{
    "total_score": 669.0,
    "division": "distinction",
    "overral_top_score": 669.0,
    "overral_top_performer": "sagar"
}
```

## 7 individual performance api

method: GET
URL: /score_card/performance/<str:subject-name>/

headers:
Authorization: Token 'access token'

response:

status code 200:

```json
{
    "subject": "physics",
    "individual_score": 96.0,
    "top_score": 96.0,
    "top_scorer": "sagar"
}
```


