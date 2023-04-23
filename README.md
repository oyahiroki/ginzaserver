# ginzaserver

HTTP Server for GiNZA - Japanese NLP Library

# How to Run

```
python ginzaserver.py
```

# How to install as PIP

```
pip install git+https://github.com/oyahiroki/ginzaserver
```

curl -X POST -H "Content-Type: application/json" -d "{'text':'今日はいい天気です'}" http://localhost:8888/

# How to uninstall

```
pip uninstall ginzaserver
```


## Curl command from Windows command prompt

curl -X POST -H "Content-Type: application/json" -d "{\"text\":\"%E4%BB%8A%E6%97%A5%E3%81%AF%E3%81%84%E3%81%84%E5%A4%A9%E6%B0%97%E3%81%A7%E3%81%99\"}" http://localhost:8888/

