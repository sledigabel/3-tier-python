from os import environ
from redis import Redis, RedisError
from flask import Flask

app = Flask(__name__)

DEFAULT_REDIS_SERVER = 'localhost'
DEFAULT_REDIS_PORT = '6379'
global redis


@app.route("/")
def hello():
    try:
        count = int(redis.get('global_connections_count'))
        if count is None:
            count = 0
        redis.incr("global_connections_count")
    except RedisError as e:
        return 'Redis error: {}'.format(e), 500

    return "# of servers: {}\n\nPage visited: {} times".format(
        len(redis.client_list()), count)


@app.route("/healthcheck")
def healthcheck():
    pass


if __name__ == '__main__':

    REDIS_SERVER = environ.get('REDIS_SERVER', DEFAULT_REDIS_SERVER)
    REDIS_PORT = environ.get('REDIS_PORT', DEFAULT_REDIS_PORT)

    PORT = environ.get('PORT', 5000)
    redis = Redis(host=REDIS_SERVER, port=REDIS_PORT)

    # (re)setting redis values
    # redis.set('global_connections_count', 0)

    if not redis.ping():
        print("Could not connect to REDIS @ {}:{}".format(
            REDIS_SERVER, REDIS_PORT))
    app.run(port=PORT)
