import os
import sys
import webbrowser
from PySide6 import QtWidgets as qtw
from PySide6.QtWidgets import QMessageBox

from about.aboutview import AboutView
from prefs.UI.prefs import Ui_PrefsWindow
import about
import data


def openlists():
    listfile = data.getlists()
    # print(listfile)
    try:
        os.startfile(listfile)
    except:
        QMessageBox.critical(None,"Critical program error", "Could not locate lists.py\n"
                                                            "Program function may be affected")


def opengenlog():
    logfile = data.getsval()
    # print(logfile)
    try:
        os.startfile(logfile)
    except:
        QMessageBox.critical(None,"Critical program error", "Could not locate sval.txt\n"
                                                            "Program function may be affected")


def openrepo():
    repo = "https://github.com/willowyx/RandomizeMe/releases"
    webbrowser.open(repo, new=0, autoraise=True)


def openrepo_info():
    repo = "https://github.com/willowyx/RandomizeMe#randomize-me"
    webbrowser.open(repo, new=0, autoraise=True)


def locunins():
    ufile_path = os.environ["ProgramW6432"]
    ufile_path += '\\RandomizeMe'
    try:
        os.startfile(ufile_path)
    except:
        QMessageBox.critical(None,"Program error", "Could not locate uninstaller\n"
                                                   "Try locating it manually in Program Files")

class PrefsView(qtw.QWidget, Ui_PrefsWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.quit_btn.clicked.connect(self.close)

        self.open_lists_btn.clicked.connect(openlists)

        self.open_genlog_btn.clicked.connect(opengenlog)

        self.unins_btn.clicked.connect(locunins)

        self.about_btn.clicked.connect(self.showabout)

        self.update_btn.clicked.connect(openrepo)
        self.repo_btn.clicked.connect(openrepo_info)

    def showabout(self):
        self.about = AboutView()
        self.about.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = PrefsView()
    w.show()
    sys.exit(app.exec())
