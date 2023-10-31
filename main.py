from imports import *
from fechData import DataUrl
import threading
import time

def geturl():
    url = window.get_current_url()
    return url

url = DataUrl()
if url is None:
    sys.exit()
else:
    def get_current_url(window):
        while True:
            try:
                time.sleep(1)
                url_change = geturl()
                if 'exit' in url_change:
                    window.destroy()
            except Exception as e:
                continue

    if __name__ == '__main__':
        window = webview.create_window('SOP', url, on_top=True)

        url_thread = threading.Thread(target=get_current_url, args=(window,))
        url_thread.daemon = True
        url_thread.start()

        webview.start()