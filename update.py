import urllib.request 

urls = [
    "https://raw.githubusercontent.com/Edu4r0/SaludOcup-Web-Version/main/url.py",
    "https://raw.githubusercontent.com/Edu4r0/SaludOcup-Web-Version/main/imports.py",
    "https://raw.githubusercontent.com/Edu4r0/SaludOcup-Web-Version/main/js/index.js",
    "https://raw.githubusercontent.com/Edu4r0/SaludOcup-Web-Version/main/html/index.html",
    "https://raw.githubusercontent.com/Edu4r0/SaludOcup-Web-Version/main/html/poppu.html",
    "https://raw.githubusercontent.com/Edu4r0/SaludOcup-Web-Version/main/css/button.css",
    "https://raw.githubusercontent.com/Edu4r0/SaludOcup-Web-Version/main/css/poppu.css",
    "https://raw.githubusercontent.com/Edu4r0/SaludOcup-Web-Version/main/css/style.css"
]

file_paths = [
    "C:/Temp/SaludOcup-Web-Version/url.py",
    "C:/Temp/SaludOcup-Web-Version/imports.py",
    "C:/Temp/SaludOcup-Web-Version/js/index.js",
    "C:/Temp/SaludOcup-Web-Version/html/index.html",
    "C:/Temp/SaludOcup-Web-Version/html/poppu.html",
    "C:/Temp/SaludOcup-Web-Version/css/button.css",
    "C:/Temp/SaludOcup-Web-Version/css/poppu.css",
    "C:/Temp/SaludOcup-Web-Version/css/style.css"
]

def actualizar():
    for i, url in enumerate(urls):
        urllib.request.urlretrieve(url, file_paths[i])
#
