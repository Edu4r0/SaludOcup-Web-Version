from imports import *

def donload_image():
    try:
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        path = 'C:\\Temp\\SaludOcup-Web-Version\\image\\image.png'
        urllib.request.urlretrieve(
            'https://raw.githubusercontent.com/Edu4r0/SaludOcup-Web-Version/main/image/font.png', path)
        
    except HTTPError as e:
        pass
    # creado por : Euardo Barboza Acosta
