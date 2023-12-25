# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chart.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QWidget)
import icons_rc

class Ui_ChartWindow(object):
    def setupUi(self, ChartWindow):
        if not ChartWindow.objectName():
            ChartWindow.setObjectName(u"ChartWindow")
        ChartWindow.resize(436, 348)
        icon = QIcon()
        icon.addFile(u":/main/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        ChartWindow.setWindowIcon(icon)
        self.gridLayout_2 = QGridLayout(ChartWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.ListsView = QTableView(ChartWindow)
        self.ListsView.setObjectName(u"ListsView")

        self.gridLayout.addWidget(self.ListsView, 0, 0, 1, 3)

        self.quit_btn = QPushButton(ChartWindow)
        self.quit_btn.setObjectName(u"quit_btn")
        icon1 = QIcon()
        icon1.addFile(u":/buttons/media/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.quit_btn.setIcon(icon1)

        self.gridLayout.addWidget(self.quit_btn, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.label = QLabel(ChartWindow)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(ChartWindow)

        QMetaObject.connectSlotsByName(ChartWindow)
    # setupUi

    def retranslateUi(self, ChartWindow):
        ChartWindow.setWindowTitle(QCoreApplication.translate("ChartWindow", u"Chart viewer | Randomize Me", None))
        self.quit_btn.setText(QCoreApplication.translate("ChartWindow", u" close", None))
        self.label.setText(QCoreApplication.translate("ChartWindow", u"<html><head/><body><p>these values can be edited in settings</p></body></html>", None))
    # retranslateUi

