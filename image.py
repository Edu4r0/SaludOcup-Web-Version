from imports import *

def donload_image():
    try:
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        path = 'C:\\Temp\\SaludOcup-Web-Version\\image\\image.png'
        urllib.request.urlretrieve(
            'https://drive.google.com/uc?id=160swttBUh5qnlsCxcjAG71QT-1mkmvVm&export=download', path)
        
    except HTTPError as e:
        pass
    