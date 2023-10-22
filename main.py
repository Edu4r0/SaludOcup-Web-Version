from imports import *
from fechData import DataUrl
url = DataUrl()
webview.create_window('SOP', url,fullscreen=True, on_top=True)
webview.start(ssl=False)