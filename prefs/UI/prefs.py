# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prefs.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)
import icons_rc

class Ui_PrefsWindow(object):
    def setupUi(self, PrefsWindow):
        if not PrefsWindow.objectName():
            PrefsWindow.setObjectName(u"PrefsWindow")
        PrefsWindow.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PrefsWindow.sizePolicy().hasHeightForWidth())
        PrefsWindow.setSizePolicy(sizePolicy)
        PrefsWindow.setMinimumSize(QSize(400, 300))
        PrefsWindow.setMaximumSize(QSize(400, 300))
        icon = QIcon()
        icon.addFile(u":/main/media/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        PrefsWindow.setWindowIcon(icon)
        self.gridLayout_2 = QGridLayout(PrefsWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(PrefsWindow)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Yu Gothic UI"])
        font.setPointSize(12)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.unins_btn = QPushButton(PrefsWindow)
        self.unins_btn.setObjectName(u"unins_btn")

        self.gridLayout.addWidget(self.unins_btn, 8, 1, 1, 1)

        self.label_5 = QLabel(PrefsWindow)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic UI"])
        font1.setPointSize(10)
        self.label_5.setFont(font1)

        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)

        self.update_btn = QPushButton(PrefsWindow)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setToolTipDuration(0)
        icon1 = QIcon()
        icon1.addFile(u":/buttons/media/external.png", QSize(), QIcon.Normal, QIcon.Off)
        self.update_btn.setIcon(icon1)

        self.gridLayout.addWidget(self.update_btn, 7, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 3, 11, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 10, 1, 1, 1)

        self.label_3 = QLabel(PrefsWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)

        self.open_lists_btn = QPushButton(PrefsWindow)
        self.open_lists_btn.setObjectName(u"open_lists_btn")

        self.gridLayout.addWidget(self.open_lists_btn, 4, 1, 1, 1)

        self.label_2 = QLabel(PrefsWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.quit_btn = QPushButton(PrefsWindow)
        self.quit_btn.setObjectName(u"quit_btn")
        icon2 = QIcon()
        icon2.addFile(u":/buttons/media/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.quit_btn.setIcon(icon2)

        self.gridLayout.addWidget(self.quit_btn, 12, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.label_4 = QLabel(PrefsWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout.addWidget(self.label_4, 8, 0, 1, 1)

        self.repo_btn = QPushButton(PrefsWindow)
        self.repo_btn.setObjectName(u"repo_btn")
        self.repo_btn.setIcon(icon1)

        self.gridLayout.addWidget(self.repo_btn, 12, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 0, 1, 2, 1)

        self.about_btn = QPushButton(PrefsWindow)
        self.about_btn.setObjectName(u"about_btn")

        self.gridLayout.addWidget(self.about_btn, 12, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 10, 0, 1, 1)

        self.open_genlog_btn = QPushButton(PrefsWindow)
        self.open_genlog_btn.setObjectName(u"open_genlog_btn")

        self.gridLayout.addWidget(self.open_genlog_btn, 6, 1, 1, 1)

        self.label_6 = QLabel(PrefsWindow)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setFamilies([u"Yu Gothic UI"])
        font2.setPointSize(9)
        self.label_6.setFont(font2)

        self.gridLayout.addWidget(self.label_6, 11, 0, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)


        self.retranslateUi(PrefsWindow)

        QMetaObject.connectSlotsByName(PrefsWindow)
    # setupUi

    def retranslateUi(self, PrefsWindow):
        PrefsWindow.setWindowTitle(QCoreApplication.translate("PrefsWindow", u"Preferences | Randomize Me", None))
        self.label.setText(QCoreApplication.translate("PrefsWindow", u"preferences", None))
#if QT_CONFIG(tooltip)
        self.unins_btn.setToolTip(QCoreApplication.translate("PrefsWindow", u"<html><head/><body><p>this will show the uninstaller executable in your file explorer</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.unins_btn.setText(QCoreApplication.translate("PrefsWindow", u"locate uninstaller", None))
        self.label_5.setText(QCoreApplication.translate("PrefsWindow", u"<html><head/><body><p align=\"center\">generation log</p></body></html>", None))
        self.update_btn.setText(QCoreApplication.translate("PrefsWindow", u" view releases", None))
        self.label_3.setText(QCoreApplication.translate("PrefsWindow", u"<html><head/><body><p align=\"center\">updates</p></body></html>", None))
        self.open_lists_btn.setText(QCoreApplication.translate("PrefsWindow", u"lists.py", None))
        self.label_2.setText(QCoreApplication.translate("PrefsWindow", u"<html><head/><body><p align=\"center\">edit lists</p></body></html>", None))
        self.quit_btn.setText(QCoreApplication.translate("PrefsWindow", u" close", None))
        self.label_4.setText(QCoreApplication.translate("PrefsWindow", u"<html><head/><body><p align=\"center\">uninstall</p></body></html>", None))
        self.repo_btn.setText(QCoreApplication.translate("PrefsWindow", u" open repository", None))
        self.about_btn.setText(QCoreApplication.translate("PrefsWindow", u"About this project", None))
        self.open_genlog_btn.setText(QCoreApplication.translate("PrefsWindow", u"sval.txt", None))
        self.label_6.setText(QCoreApplication.translate("PrefsWindow", u"<html><head/><body><p align=\"center\">you'll need to restart for edits to take effect</p></body></html>", None))
    # retranslateUi

