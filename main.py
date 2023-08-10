from imports import *
from url import open_pause


class MainWindow(QMainWindow):

            def __init__(self, *args, **kwargs):
                super(MainWindow, self).__init__(*args, **kwargs)

                self.browser = QWebEngineView()
                self.browser.setUrl(
                    QUrl(f'www.google.com'))

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
                    self.exit_button.show()
                    self.exit_button.clicked.connect(
                    QApplication.instance().quit)
                    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()
    sys.exit()


#### Creado por Eduardo Barboza ####
# v.2.0.0