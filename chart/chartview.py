import os
import sys
import importlib.util
from itertools import zip_longest
from PySide6.QtWidgets import QApplication, QTableView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6 import QtWidgets as qtw

from chart.UI.chart import Ui_ChartWindow

def import_module(mname, rpath):
    dir_path = os.path.join(os.path.dirname(__file__), rpath)
    module_file = os.path.join(dir_path, f'{mname}.py')
    spec = importlib.util.spec_from_file_location(mname, module_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


lists = import_module('lists', '../data/')

class ChartView(qtw.QWidget, Ui_ChartWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.quit_btn.clicked.connect(self.close)

        # self.popChart()

        # app = QApplication([])
        # app.exec()

    def popChart(self):
        ListsView = QTableView()
        model = QStandardItemModel()
        for a, b, c, d, e in zip_longest(lists.ListA, lists.ListB, lists.ListC, lists.ListD, lists.ListE):
            items = [QStandardItem(item) if item is not None else QStandardItem('') for item in (a, b, c, d, e)]
            model.appendRow(items)
        self.ListsView.setModel(model)
        self.ListsView.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = ChartView()
    w.popChart()
    w.show()
    sys.exit(app.exec())
