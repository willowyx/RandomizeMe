import os
import importlib.util
import sys
import webbrowser
from PySide6 import QtWidgets as qtw

from prefs.UI.prefs import Ui_PrefsWindow

class PrefsView(qtw.QWidget, Ui_PrefsWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.quit_btn.clicked.connect(self.close)

        self.open_lists_btn.clicked.connect(self.openlists)

        self.open_genlog_btn.clicked.connect(self.opengenlog)

        self.open_repo_btn.clicked.connect(self.openrepo)
        self.about_btn.clicked.connect(self.openrepo_info)

    def getabspath(self, rpath, rname):
        dirname = os.path.dirname(__file__)
        parent_dir = os.path.abspath(os.path.join(dirname, os.pardir))
        textout = os.path.join(parent_dir, rpath, rname)
        return textout
    def openlists(self):
        listfile = self.getabspath('data', 'lists.py')
        os.startfile(listfile)

    def opengenlog(self):
        logfile = self.getabspath('data', 'sval.txt')
        os.startfile(logfile)

    def openrepo(self):
        repo = "https://github.com/willowyx/RandomizeMe/releases"
        webbrowser.open(repo, new=0, autoraise=True)

    def openrepo_info(self):
        repo = "https://github.com/willowyx/RandomizeMe#randomize-me"
        webbrowser.open(repo, new=0, autoraise=True)

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = PrefsView()
    w.show()
    sys.exit(app.exec())
