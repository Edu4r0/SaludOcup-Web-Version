from urllib.request import urlretrieve

urls = [
    "https://github.com/Edu4r0/SaludOcup-Web-Version/blob/4bcd7a65bbd8a1a045e238b774ee6259bde0719c/url.py",
    "https://github.com/Edu4r0/SaludOcup-Web-Version/blob/4bcd7a65bbd8a1a045e238b774ee6259bde0719c/imports.py",
    "https://github.com/Edu4r0/SaludOcup-Web-Version/blob/4bcd7a65bbd8a1a045e238b774ee6259bde0719c/js/index.js",
    "https://github.com/Edu4r0/SaludOcup-Web-Version/blob/4bcd7a65bbd8a1a045e238b774ee6259bde0719c/html/index.html",
    "https://github.com/Edu4r0/SaludOcup-Web-Version/blob/4bcd7a65bbd8a1a045e238b774ee6259bde0719c/html/poppu.html",
    "https://github.com/Edu4r0/SaludOcup-Web-Version/blob/4bcd7a65bbd8a1a045e238b774ee6259bde0719c/css/button.css",
    "https://github.com/Edu4r0/SaludOcup-Web-Version/blob/4bcd7a65bbd8a1a045e238b774ee6259bde0719c/css/poppu.css",
    "https://github.com/Edu4r0/SaludOcup-Web-Version/blob/4bcd7a65bbd8a1a045e238b774ee6259bde0719c/css/style.css"
]

file_paths = [
    "C:\Temp\SaludOcup-Web-Version\url.py",
    "C:\Temp\SaludOcup-Web-Version\imports.py",
    "C:\Temp\SaludOcup-Web-Version\js\index.js",
    "C:\Temp\SaludOcup-Web-Version\html\index.html",
    "C:\Temp\SaludOcup-Web-Version\html\poppu.html",
    "C:\Temp\SaludOcup-Web-Version\css\button.css",
    "C:\Temp\SaludOcup-Web-Version\css\poppu.css",
    "C:\Temp\SaludOcup-Web-Version\css\style.csss"
]

def actualizar():
    for i, url in enumerate(urls):
        urlretrieve(url, file_paths[i])