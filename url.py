from imports import *

def open_pause(main_window):
    main_window.setWindowFlags(Qt.Tool | Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
    view = QWebEngineView(main_window)
    main_window.setCentralWidget(view)
    page = view.page()  # Obtenemos la página cargada
    page.load(QUrl.fromLocalFile('C:\Temp\SaludOcup-Web-Version\html\index.html'))

    def on_url_changed(url):
        # Verificar si la URL es la URL especial para cerrar la ventana
        if url == QUrl('file:///C:/Temp/SaludOcup-Web-Version/html/index.html?exit'):
            QApplication.instance().exit()
        if url == QUrl('file:///C:/Temp/SaludOcup-Web-Version/html/poppu.html?exit'):
            QApplication.instance().exit()

    page.urlChanged.connect(on_url_changed)