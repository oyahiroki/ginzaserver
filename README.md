# ginzaserver

HTTP Server for GiNZA - Japanese NLP Library

# Install

```
pip install -U ginza ja_ginza
pip install -U ginza ja_ginza_electra
pip install git+https://github.com/oyahiroki/ginzaserver
```


# How to Run

ginzaserver port option

```
gunzaserver 8888 0
```

# Try ginzaserver

POST

```
curl -X POST -H "Content-Type: application/json" -d "{'text':'今日はいい天気です'}" http://localhost:8888/
```

GET

```
curl http://127.0.0.1:8080/?text=%E3%81%93%E3%82%8C%E3%81%AF%E3%83%86%E3%82%B9%E3%83%88%E3%81%A7%E3%81%99%E3%80%82
```

# How to uninstall

```
pip uninstall ginzaserver
```

# How to Run as Python code

```
python ginzaserver.py 8888 0
```

.


