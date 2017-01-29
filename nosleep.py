import os, requests, time

url_to_get = "https://" + os.environ["APP_HEROKU_NAME"] + ".herokuapp.com"

while True:
    time.sleep(120)
    requests.get(url_to_get)