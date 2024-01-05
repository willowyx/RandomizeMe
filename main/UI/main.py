# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTextBrowser, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(543, 398)
        font = QFont()
        font.setFamilies([u"Yu Gothic UI"])
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/main/media/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.actionShow_chart = QAction(MainWindow)
        self.actionShow_chart.setObjectName(u"actionShow_chart")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 6, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 2, 1, 1)

        self.prefs_btn = QPushButton(self.centralwidget)
        self.prefs_btn.setObjectName(u"prefs_btn")
        icon1 = QIcon()
        icon1.addFile(u":/buttons/media/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prefs_btn.setIcon(icon1)

        self.gridLayout.addWidget(self.prefs_btn, 9, 1, 1, 1)

        self.sdata = QLineEdit(self.centralwidget)
        self.sdata.setObjectName(u"sdata")
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic UI"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.sdata.setFont(font1)

        self.gridLayout.addWidget(self.sdata, 0, 0, 1, 4)

        self.quit_btn = QPushButton(self.centralwidget)
        self.quit_btn.setObjectName(u"quit_btn")
        font2 = QFont()
        font2.setFamilies([u"Yu Gothic UI"])
        font2.setPointSize(10)
        self.quit_btn.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(u":/buttons/media/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.quit_btn.setIcon(icon2)

        self.gridLayout.addWidget(self.quit_btn, 9, 0, 1, 1)

        self.enter_sval_btn = QPushButton(self.centralwidget)
        self.enter_sval_btn.setObjectName(u"enter_sval_btn")
        icon3 = QIcon()
        icon3.addFile(u":/buttons/arrow-return.png", QSize(), QIcon.Normal, QIcon.Off)
        self.enter_sval_btn.setIcon(icon3)

        self.gridLayout.addWidget(self.enter_sval_btn, 0, 4, 1, 1)

        self.randomize_btn = QPushButton(self.centralwidget)
        self.randomize_btn.setObjectName(u"randomize_btn")
        font3 = QFont()
        font3.setFamilies([u"Yu Gothic UI"])
        font3.setPointSize(11)
        self.randomize_btn.setFont(font3)
        self.randomize_btn.setContextMenuPolicy(Qt.PreventContextMenu)

        self.gridLayout.addWidget(self.randomize_btn, 9, 3, 1, 2)

        self.text_output = QTextBrowser(self.centralwidget)
        self.text_output.setObjectName(u"text_output")
        font4 = QFont()
        font4.setFamilies([u"Yu Gothic Light"])
        font4.setPointSize(16)
        self.text_output.setFont(font4)
        self.text_output.setAcceptDrops(False)
        self.text_output.setAcceptRichText(False)
        self.text_output.setOpenLinks(False)

        self.gridLayout.addWidget(self.text_output, 4, 0, 1, 5)

        self.open_chart_btn = QPushButton(self.centralwidget)
        self.open_chart_btn.setObjectName(u"open_chart_btn")
        icon4 = QIcon()
        icon4.addFile(u":/buttons/media/table.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_chart_btn.setIcon(icon4)

        self.gridLayout.addWidget(self.open_chart_btn, 9, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 543, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.randomize_btn, self.sdata)
        QWidget.setTabOrder(self.sdata, self.enter_sval_btn)
        QWidget.setTabOrder(self.enter_sval_btn, self.text_output)
        QWidget.setTabOrder(self.text_output, self.quit_btn)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionPreferences)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuView.addAction(self.actionShow_chart)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Randomize Me!", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.actionShow_chart.setText(QCoreApplication.translate("MainWindow", u"Show chart", None))
        self.prefs_btn.setText(QCoreApplication.translate("MainWindow", u"prefs", None))
#if QT_CONFIG(tooltip)
        self.sdata.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enter a numerical value for &quot;seeded&quot; text generation</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sdata.setText(QCoreApplication.translate("MainWindow", u"0000000000", None))
        self.quit_btn.setText(QCoreApplication.translate("MainWindow", u" quit", None))
        self.enter_sval_btn.setText(QCoreApplication.translate("MainWindow", u"enter", None))
#if QT_CONFIG(tooltip)
        self.randomize_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Generate new text</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.randomize_btn.setText(QCoreApplication.translate("MainWindow", u"randomize me!", None))
        self.text_output.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Yu Gothic Light'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">press &quot;randomize me!&quot; to generate random text, or enter a generation seed and press &quot;enter&quot;</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.open_chart_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>open generation chart</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.open_chart_btn.setText(QCoreApplication.translate("MainWindow", u" open chart", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi

