from imports import *
from fechData import DataUrl
import threading

url = DataUrl()
if url is None:
    sys.exit()
else:
    def get_current_url(window):
        global current_url
        while window:
            try:
                url_change = window.get_current_url()
                if 'exit' in url_change:
                    window.destroy()
            except Exception as e :
                    continue     

    if __name__ == '__main__':
        window = webview.create_window('SOP', url,fullscreen=True,on_top=True)
        
        url_thread = threading.Thread(target=get_current_url,  args=(window,))
        url_thread.daemon = True
        url_thread.start()
        
        webview.start()
