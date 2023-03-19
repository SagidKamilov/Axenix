from PyQt5.QtWidgets import QApplication, QSplashScreen
from PyQt5.QtGui import QIcon

from module import MainWindow
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

if __name__ == "__main__":
    app = QApplication([])
    splash = QSplashScreen(QPixmap("images/Group_8.png"), Qt.WindowStaysOnTopHint)
    splash.show()
    main_window = MainWindow()
    splash.close()
    main_window.setWindowIcon(QIcon('images/Group_7-transformed.png'))
    main_window.show()
    app.exec_()
