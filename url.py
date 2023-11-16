from imports import *


def urljson():
    with open('C:\Temp\SaludOcup-Web-Version' + '\\url.json') as f:
        jsonfile = json.load(f)
    return jsonfile['URLAPI']

URL_API = urljson()

