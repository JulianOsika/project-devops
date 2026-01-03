from flask import Flask
from redis import Redis

app = Flask(__name__)
# Timeout 1 sekunda - klucz do sukcesu
redis = Redis(host='127.0.0.1', port=6379, socket_timeout=1, socket_connect_timeout=1)

@app.route('/')
def hello():
    try:
        count = redis.incr('hits')
    except Exception:
        count = "brak polaczenia z Redis"
    return 'Witaj! To jest projekt DevOps. Tę stronę odwiedzono {} razy.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
