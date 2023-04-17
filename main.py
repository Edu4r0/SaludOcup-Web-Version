from imports import *
from url import open_pause

try:
    curr_date = str(date.today())
    path = 'C:\Temp\SaludOcup-Web-Version\main\LogData.txt'
    urllib.request.urlretrieve(
        'https://drive.google.com/uc?id=1YztxY4lGbtPKDz0KPrQp11HrXhg4jXKA&export=download', path)
    # Se lee el archivo LogData == 2 lineas
    leer = open('c:\Temp\SaludOcup-Web-Version\main\LogData.txt', 'r')
    line1 = leer.readline(-1)
    # Se remplaza el salto de linea (\n)E
    url = line1.replace("\n", "")[34:90]
    line2 = leer.readline(-2)

    # If line2 == fecha de dia actual instacia la clase
    if line2 == curr_date:
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

                    self.exit_button.setGeometry(366, 380, 0, 0)
                    self.exit_button.clicked.connect(
                        QApplication.instance().quit)
                    self.exit_button.show()

        if __name__ == '__main__':
            app = QApplication(sys.argv)
            window = MainWindow()
            app.exec_()
            sys.exit()
except HTTPError:
    pass

# Llamado a la funcion open_pause -file main_.py
if __name__ == '__main__':
    app = QApplication([])
    window = QMainWindow()
    open_pause(window)
    window.showFullScreen()
    app.exec_()
