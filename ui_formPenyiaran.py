# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formPenyiaran.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(672, 629)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(150, 70, 401, 251))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDSiaranLabel = QLabel(self.formLayoutWidget)
        self.iDSiaranLabel.setObjectName(u"iDSiaranLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDSiaranLabel)

        self.iDSiarLineEdit = QLineEdit(self.formLayoutWidget)
        self.iDSiarLineEdit.setObjectName(u"iDSiarLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.iDSiarLineEdit)

        self.kodeIklanLabel = QLabel(self.formLayoutWidget)
        self.kodeIklanLabel.setObjectName(u"kodeIklanLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.kodeIklanLabel)

        self.kodeIklanLineEdit = QLineEdit(self.formLayoutWidget)
        self.kodeIklanLineEdit.setObjectName(u"kodeIklanLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.kodeIklanLineEdit)

        self.produkLabel = QLabel(self.formLayoutWidget)
        self.produkLabel.setObjectName(u"produkLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.produkLabel)

        self.produkLineEdit = QLineEdit(self.formLayoutWidget)
        self.produkLineEdit.setObjectName(u"produkLineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.produkLineEdit)

        self.periodeLabel = QLabel(self.formLayoutWidget)
        self.periodeLabel.setObjectName(u"periodeLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.periodeLabel)

        self.airTimeLabel = QLabel(self.formLayoutWidget)
        self.airTimeLabel.setObjectName(u"airTimeLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.airTimeLabel)

        self.airTimeLineEdit = QLineEdit(self.formLayoutWidget)
        self.airTimeLineEdit.setObjectName(u"airTimeLineEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.airTimeLineEdit)

        self.tglMulaiLabel = QLabel(self.formLayoutWidget)
        self.tglMulaiLabel.setObjectName(u"tglMulaiLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.tglMulaiLabel)

        self.tglMulaiLineEdit = QLineEdit(self.formLayoutWidget)
        self.tglMulaiLineEdit.setObjectName(u"tglMulaiLineEdit")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.tglMulaiLineEdit)

        self.tglSelesaiLabel = QLabel(self.formLayoutWidget)
        self.tglSelesaiLabel.setObjectName(u"tglSelesaiLabel")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.tglSelesaiLabel)

        self.tglSelesaiLineEdit = QLineEdit(self.formLayoutWidget)
        self.tglSelesaiLineEdit.setObjectName(u"tglSelesaiLineEdit")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.tglSelesaiLineEdit)

        self.periodeLineEdit = QLineEdit(self.formLayoutWidget)
        self.periodeLineEdit.setObjectName(u"periodeLineEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.periodeLineEdit)

        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 400, 631, 192))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(302, 30, 71, 20))
        self.simpanButton = QPushButton(Form)
        self.simpanButton.setObjectName(u"simpanButton")
        self.simpanButton.setGeometry(QRect(230, 340, 90, 29))
        self.ubahButton = QPushButton(Form)
        self.ubahButton.setObjectName(u"ubahButton")
        self.ubahButton.setGeometry(QRect(340, 340, 90, 29))
        self.hapusButton = QPushButton(Form)
        self.hapusButton.setObjectName(u"hapusButton")
        self.hapusButton.setGeometry(QRect(450, 340, 90, 29))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDSiaranLabel.setText(QCoreApplication.translate("Form", u"ID Siaran", None))
        self.kodeIklanLabel.setText(QCoreApplication.translate("Form", u"Kode Iklan", None))
        self.produkLabel.setText(QCoreApplication.translate("Form", u"Produk", None))
        self.periodeLabel.setText(QCoreApplication.translate("Form", u"Periode", None))
        self.airTimeLabel.setText(QCoreApplication.translate("Form", u"Air Time", None))
        self.tglMulaiLabel.setText(QCoreApplication.translate("Form", u"Tgl Mulai", None))
        self.tglSelesaiLabel.setText(QCoreApplication.translate("Form", u"Tgl Selesai", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Siaran", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Kode Iklan", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Produk", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Periode", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Air Time", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Tgl Mulai", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Tgl Selesai", None));
        self.label.setText(QCoreApplication.translate("Form", u"Penyiaran", None))
        self.simpanButton.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.ubahButton.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.hapusButton.setText(QCoreApplication.translate("Form", u"Hapus", None))
    # retranslateUi

