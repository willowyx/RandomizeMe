import sys
import os
import data
import importlib.resources
from PySide6 import QtWidgets as qtw

import prefs.prefsview
from main.UI.main import Ui_MainWindow
from genedit import generator


def load_resource(package, resource_name):
    return importlib.resources.read_text(package, resource_name)


queuePrefData = []
queueWindowData = []

def setqpd(value):
    queuePrefData.append(value)
    if value is None:
        return queuePrefData

def setqwd(value):
    queueWindowData.append(value)
    if value is None:
        return queueWindowData

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

        self.actionAbout.triggered.connect(self.showabout)

        self.actionPreferences.triggered.connect(self.showprefs)
        self.prefs_btn.clicked.connect(self.showprefs)

    def prefscan(self):
        import re
        import prefs.prefsview
        open(data.getModulePath('prefs'), 'a').close()
        # check uwu
        with open(data.getModulePath('prefs'), 'r') as file:
            contents = file.read()
            match = re.search(r'PREFS_UWU=(\d+)', contents)
            if match:
                uwu_value = match.group(1)
                print('uwu toggle state loaded as ' + uwu_value)
                if uwu_value == '1':
                    import prefs.prefsview
                    print('queuing data for instantiated windows...')  # debug
                    self.uwuify_main()
                    print('queuing data for other windows...')  # debug
                    setqpd('PREFS_UWU')  # queues prefdata for when prefs is launched
                    setqwd('PREFS_UWU')  # queues window data for when prefs is launched
                    setqwd('CHART_UWU')  # chart window
                    setqwd('ABOUT_UWU')  # about window

    def getoutput(self, nogensval):
        self.text_output.setText(generator.returnstr(nogensval))

    def uwuify_main(self):
        self.randomize_btn.setText('wandomize m-me!')
        self.quit_btn.setText('q-quit')
        self.open_chart_btn.setText('open chawt')
        self.prefs_btn.setText('pwefs')
        self.enter_sval_btn.setText('e-enter')
        self.text_output.setText('p-pwess \"wandomize me!\" to genewate wandom text, ow enter a genewation seed and'
                                 ' pwess \"entew\"')
        self.setWindowTitle('wandomize me!')

    def getsval(self):
        with open(data.getModulePath('sval'), 'r') as f:
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
        from chart.chartview import ChartView
        self.chart = ChartView()
        if 'CHART_UWU' in setqwd(None):
            self.chart.uwuify_chart()
            print('loaded window data for chart viewer: uwu')
        self.chart.popChart()
        self.chart.show()

    def showabout(self):
        from about.aboutview import AboutView
        self.about = AboutView()
        if 'ABOUT_UWU' in setqwd(None):
            self.about.uwuify_about()
            print('loaded limited window data for prefs: uwu (expected)')
        self.about.show()

    def showprefs(self):
        from prefs.prefsview import PrefsView
        self.prefs = PrefsView()
        if 'PREFS_UWU' in setqpd(None):
            self.prefs.setuwucheck()
        if 'PREFS_UWU' in setqwd(None):
            self.prefs.uwuify_prefs()
            print('loaded window data for prefs: uwu')
        self.prefs.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    app.setStyle('Fusion')
    w = Randomize()
    w.prefscan()
    w.show()
    sys.exit(app.exec())
