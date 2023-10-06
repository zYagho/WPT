from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
import sys
from primeira_janela import FirstWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    firstWindow = FirstWindow()
    app.setWindowIcon(QIcon("files/icon_wpt.png"))
    firstWindow.setWindowIcon(QIcon("files/icon_wpt.png"))
    firstWindow.show()
    sys.exit(app.exec())