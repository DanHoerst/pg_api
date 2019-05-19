PG API 

Python3 and Flask


**Requirements**

```bash
pip3 install -r requirements.txt
```

All steps assume a working directory of `pg_api/`

**Starting the application**

```bash
python3 -m flask run
```

**Starting the application w/ debug logging**

```bash
FLASK_DEBUG=1 python3 -m flask run
```

Debug logging adds an additional debug log line per request like so:

```bash
[2019-05-19 11:06:54,607] DEBUG in app: 2019-05-19 15:06:54.606053: GET http://localhost:5000/ */*
127.0.0.1 - - [19/May/2019 11:06:54] "GET / HTTP/1.1" 200 -
[2019-05-19 11:06:59,997] DEBUG in app: 2019-05-19 15:06:59.997115: POST http://localhost:5000/ */*
127.0.0.1 - - [19/May/2019 11:06:59] "POST / HTTP/1.1" 200 -
[2019-05-19 11:07:18,820] DEBUG in app: 2019-05-19 15:07:18.820209: GET http://localhost:5000/ text/html
127.0.0.1 - - [19/May/2019 11:07:18] "GET / HTTP/1.1" 200 -
[2019-05-19 11:07:25,421] DEBUG in app: 2019-05-19 15:07:25.420940: POST http://localhost:5000/ text/html
127.0.0.1 - - [19/May/2019 11:07:25] "POST / HTTP/1.1" 200 -
[2019-05-19 11:07:40,410] DEBUG in app: 2019-05-19 15:07:40.409870: GET http://localhost:5000/ application/json
127.0.0.1 - - [19/May/2019 11:07:40] "GET / HTTP/1.1" 200 -
[2019-05-19 11:07:46,304] DEBUG in app: 2019-05-19 15:07:46.304336: POST http://localhost:5000/ application/json
127.0.0.1 - - [19/May/2019 11:07:46] "POST / HTTP/1.1" 200 -

```

**Unit testing the application**

```bash
python3 -m unittest tests/app_test.py
```

**Manual testing of the application**

Open Accept Header:
```bash
[11:06:40] dan ➜  ~ » curl -XGET localhost:5000
<p>Hello World!</p>%

[11:06:54] dan ➜  ~ » curl -XPOST localhost:5000
<p>Hello World!</p>%
```

`text/html` Accept Header:
```bash
[11:07:00] dan ➜  ~ » curl -XGET -Haccept:text/html http://localhost:5000/
<p>Hello World!</p>%

[11:07:18] dan ➜  ~ » curl -XPOST -Haccept:text/html http://localhost:5000/
<p>Hello World!</p>%
```

`application/json` Accept Header:
```bash
[11:07:25] dan ➜  ~ » curl -XGET -Haccept:application/json http://localhost:5000/
{
  "message": "Good morning"
}

[11:07:40] dan ➜  ~ » curl -XPOST -Haccept:application/json http://localhost:5000/
{
  "message": "Good morning"
}
```
