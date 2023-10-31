import json

def urljson():
    with open('url.json') as f:
        jsonfile = json.load(f)
    return jsonfile['URLAPI']

URL_API = urljson()

