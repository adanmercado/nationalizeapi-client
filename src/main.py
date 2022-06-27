import sys

from PySide6.QtWidgets import QApplication

from window import Window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName('nationalizeapi client')
    app.setApplicationDisplayName('nationalizeapi client')
    app.setApplicationVersion('1.0')
    app.setOrganizationName('adanmercado')

    window = Window()
    window.show()

    sys.exit(app.exec())