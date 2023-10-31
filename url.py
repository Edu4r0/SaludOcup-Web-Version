from imports import *

ROOT_DIR = os.path.abspath(os.curdir)

def urljson():
    with open(ROOT_DIR + '\\url.json') as f:
        jsonfile = json.load(f)
    return jsonfile['URLAPI']

URL_API = urljson()

