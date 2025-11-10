# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(800, 600)
        self.actionAdvertiser = QAction(Main)
        self.actionAdvertiser.setObjectName(u"actionAdvertiser")
        self.actionBiaya_Iklan = QAction(Main)
        self.actionBiaya_Iklan.setObjectName(u"actionBiaya_Iklan")
        self.actionIklan = QAction(Main)
        self.actionIklan.setObjectName(u"actionIklan")
        self.actionPenyiaran = QAction(Main)
        self.actionPenyiaran.setObjectName(u"actionPenyiaran")
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.menuMenu_Utama = QMenu(self.menubar)
        self.menuMenu_Utama.setObjectName(u"menuMenu_Utama")
        Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main)
        self.statusbar.setObjectName(u"statusbar")
        Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu_Utama.menuAction())
        self.menuMenu_Utama.addAction(self.actionAdvertiser)
        self.menuMenu_Utama.addAction(self.actionIklan)
        self.menuMenu_Utama.addAction(self.actionPenyiaran)
        self.menuMenu_Utama.addAction(self.actionBiaya_Iklan)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Main", None))
        self.actionAdvertiser.setText(QCoreApplication.translate("Main", u"Advertiser", None))
        self.actionBiaya_Iklan.setText(QCoreApplication.translate("Main", u"Biaya Iklan", None))
        self.actionIklan.setText(QCoreApplication.translate("Main", u"Iklan", None))
        self.actionPenyiaran.setText(QCoreApplication.translate("Main", u"Penyiaran", None))
        self.menuMenu_Utama.setTitle(QCoreApplication.translate("Main", u"Menu Utama", None))
    # retranslateUi

