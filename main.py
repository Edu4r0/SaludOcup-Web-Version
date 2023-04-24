from imports import *
from url import open_pause

try:
    # Descargar el archivo de LogData
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
    path = 'C:\\Temp\\SaludOcup-Web-Version\\LogData.txt'
    urllib.request.urlretrieve(
        'https://raw.githubusercontent.com/Edu4r0/SaludOcup-Web-Version/main/LogData/LogData.txt', path)
    # Leer el archivo LogData
    with open('C:\\Temp\\SaludOcup-Web-Version\\LogData.txt', 'r') as f:
        line1 = f.readline()
        url = line1[34:90].strip()
        line2 = f.readline()

    curr_date = str(date.today())

    # Si la segunda línea del archivo LogData coincide con la fecha actual, instanciar la clase MainWindow
    if line2.strip() == curr_date:
        class MainWindow(QMainWindow):

            def __init__(self, *args, **kwargs):
                super(MainWindow, self).__init__(*args, **kwargs)
                url2 = (
                    f"https://docs.google.com/forms/u/0/d/e/{url}/formResponse")

                self.browser = QWebEngineView()
                self.browser.setUrl(
                    QUrl(f'https://docs.google.com/forms/d/e/{url}/viewform'))

                self.browser.urlChanged.connect(self.url_changed)

                self.setCentralWidget(self.browser)

                self.setWindowFlags(
                    Qt.Tool | Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
                self.showFullScreen()

            # Funcion Cambio de URL if = formResponse

            def url_changed(self, url2):
                if self.browser.url() == url2:

                    self.exit_button = QPushButton('Cerrar', self.browser)
                    self.exit_button.setFixedSize(640, 68)

                    with open("css/button.css") as f:
                        self.setStyleSheet(f.read())

                    self.exit_button.setGeometry(366, 335, 0, 0)
                    self.exit_button.clicked.connect(
                        QApplication.instance().quit)
                    self.exit_button.show()

        if __name__ == '__main__':
            app = QApplication(sys.argv)
            window = MainWindow()
            app.exec_()
            sys.exit()

except HTTPError as e:
    pass

# Llamado a la funcion open_pause -file main_.py
if __name__ == '__main__':
    app = QApplication([])
    window = QMainWindow()
    open_pause(window)
    window.showFullScreen()
    app.exec_()
#### Creado por Eduardo Barboza ####
# v.2.0.0