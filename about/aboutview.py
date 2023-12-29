import sys
from PySide6 import QtWidgets as qtw

from about.UI.about import Ui_AboutWindow

class AboutView(qtw.QWidget, Ui_AboutWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.quit_btn.clicked.connect(self.close)

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = AboutView()
    w.show()
    sys.exit(app.exec())
