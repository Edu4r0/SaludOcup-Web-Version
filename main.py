from imports import *


class MainWindow(QMainWindow):

            def __init__(self, *args, **kwargs):
                super(MainWindow, self).__init__(*args, **kwargs)

                self.browser = QWebEngineView()
                self.browser.setUrl(
                    QUrl(f'https://www.google.com'))

                response = requests.get('http://localhost:5000/UsersList')
                x = response.json()
                print(x)
                self.setCentralWidget(self.browser)

                #self.setWindowFlags(
                #    Qt.Tool | Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
                #self.showFullScreen()

                self.show()

          
                    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()
    sys.exit()


#### Creado por Eduardo Barboza ####
# v.2.0.0