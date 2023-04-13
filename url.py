from imports import *

def open_pause(main_window):
    view = QWebEngineView(main_window)
    main_window.setCentralWidget(view)

    page = view.page()  # Obtenemos la página cargada
    page.load(QUrl.fromLocalFile('/html/index.html'))

    def on_url_changed(url):
        # Verificar si la URL es la URL especial para cerrar la ventana
        if url == QUrl('file:///html/index.html?exit'):
            QApplication.instance().exit()
        if url == QUrl('file:///html/poppu.html?exit'):
            QApplication.instance().exit()

    page.urlChanged.connect(on_url_changed)