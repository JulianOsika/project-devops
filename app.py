from flask import Flask
from redis import Redis
import os

app = Flask(__name__)

# W Dockerze nazwa hosta to nazwa serwisu z docker-compose, czyli 'redis'
redis = Redis(host='redis', port=6379, socket_timeout=1, socket_connect_timeout=1)

@app.route('/')
def hello():
    try:
        count = redis.incr('hits')
    except Exception as e:
        count = "brak polaczenia z Redis: {}".format(str(e))
    return 'Witaj! To jest projekt w Docker Compose. Te strone odwiedzono {} razy.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
