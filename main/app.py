import sys
import importlib.util
import os
from PySide6 import QtWidgets as qtw
from PySide6.QtWidgets import QApplication

from chart.chartview import ChartView
from about.aboutview import AboutView
from prefs.prefsview import PrefsView
from main.UI.main import Ui_MainWindow

def import_module(mname, rpath):
    dir_path = os.path.join(os.path.dirname(__file__), rpath)
    module_file = os.path.join(dir_path, f'{mname}.py')
    spec = importlib.util.spec_from_file_location(mname, module_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


generator = import_module('generator', '../genedit/')
cview = import_module('chartview', '../chart/')

class Randomize(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.quit_btn.clicked.connect(self.close)
        self.actionQuit.triggered.connect(self.close)

        self.randomize_btn.clicked.connect(self.getoutput)
        self.randomize_btn.clicked.connect(self.getsval)

        self.enter_sval_btn.clicked.connect(self.usesval)

        self.open_chart_btn.clicked.connect(self.showchart)
        self.actionShow_chart.triggered.connect(self.showchart)

        self.chart = None

        self.actionAbout.triggered.connect(self.showabout)
        self.about_btn.clicked.connect(self.showabout)

        self.actionPreferences.triggered.connect(self.showprefs)
        self.prefs_btn.clicked.connect(self.showprefs)

    def getabspath(self, rpath, rname):
        dirname = os.path.dirname(__file__)
        parent_dir = os.path.abspath(os.path.join(dirname, os.pardir))
        textout = os.path.join(parent_dir, rpath, rname)
        return textout

    def getoutput(self, nogensval):
        self.text_output.setText(generator.returnstr(nogensval))

    def getsval(self):
        with open(self.getabspath('data', 'sval.txt'), 'r') as f:
            f.seek(0, os.SEEK_END)
            pos = f.tell() - 2
            while pos > 0 and f.read(1) != '\n':
                pos -= 1
                f.seek(pos, os.SEEK_SET)
            last_line = f.readline()
        # return last_line
        self.sdata.setText(last_line)

    def usesval(self):
        seval = self.sdata.text()
        self.getoutput(seval)

    def showchart(self):
        self.chart = ChartView()
        self.chart.popChart()
        self.chart.show()

    def showabout(self):
        self.about = AboutView()
        self.about.show()

    def showprefs(self):
        self.prefs = PrefsView()
        self.prefs.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = Randomize()
    w.show()
    sys.exit(app.exec())
