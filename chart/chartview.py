import os
import sys
import data
import importlib.util
from itertools import zip_longest
from PySide6.QtWidgets import QApplication, QTableView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6 import QtWidgets as qtw
from chart.UI.chart import Ui_ChartWindow

module_path = ''
if data.getsysname() == 'Windows':
    module_path = os.path.join(os.getenv('appdata'), 'RandomizeMe/lists.py')
elif data.getsysname() == 'Darwin':
    module_path = os.path.join(os.path.expanduser('~/Library/Application Support'), 'RandomizeMe/lists.py')

spec = importlib.util.spec_from_file_location('lists', module_path)
lists = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lists)


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
