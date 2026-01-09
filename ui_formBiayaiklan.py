# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formBiayaiklan.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(627, 682)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(80, 80, 491, 311))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.noInvoiceLabel = QLabel(self.formLayoutWidget)
        self.noInvoiceLabel.setObjectName(u"noInvoiceLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.noInvoiceLabel)

        self.noInvoiceLineEdit = QLineEdit(self.formLayoutWidget)
        self.noInvoiceLineEdit.setObjectName(u"noInvoiceLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.noInvoiceLineEdit)

        self.tanggalLabel = QLabel(self.formLayoutWidget)
        self.tanggalLabel.setObjectName(u"tanggalLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.tanggalLabel)

        self.tanggalLineEdit = QLineEdit(self.formLayoutWidget)
        self.tanggalLineEdit.setObjectName(u"tanggalLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.tanggalLineEdit)

        self.kodeAdvertiserLabel = QLabel(self.formLayoutWidget)
        self.kodeAdvertiserLabel.setObjectName(u"kodeAdvertiserLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.kodeAdvertiserLabel)

        self.kodeAdvertiserComboBox = QComboBox(self.formLayoutWidget)
        self.kodeAdvertiserComboBox.setObjectName(u"kodeAdvertiserComboBox")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.kodeAdvertiserComboBox)

        self.kodeIklanLabel = QLabel(self.formLayoutWidget)
        self.kodeIklanLabel.setObjectName(u"kodeIklanLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.kodeIklanLabel)

        self.kodeIklanComboBox = QComboBox(self.formLayoutWidget)
        self.kodeIklanComboBox.setObjectName(u"kodeIklanComboBox")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.kodeIklanComboBox)

        self.frekwensiLabel = QLabel(self.formLayoutWidget)
        self.frekwensiLabel.setObjectName(u"frekwensiLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.frekwensiLabel)

        self.frekwensiLineEdit = QLineEdit(self.formLayoutWidget)
        self.frekwensiLineEdit.setObjectName(u"frekwensiLineEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.frekwensiLineEdit)

        self.jumlahBayarLabel = QLabel(self.formLayoutWidget)
        self.jumlahBayarLabel.setObjectName(u"jumlahBayarLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.jumlahBayarLabel)

        self.jumlahBayarLineEdit = QLineEdit(self.formLayoutWidget)
        self.jumlahBayarLineEdit.setObjectName(u"jumlahBayarLineEdit")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.jumlahBayarLineEdit)

        self.pPHLabel = QLabel(self.formLayoutWidget)
        self.pPHLabel.setObjectName(u"pPHLabel")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.pPHLabel)

        self.pPHLineEdit = QLineEdit(self.formLayoutWidget)
        self.pPHLineEdit.setObjectName(u"pPHLineEdit")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.pPHLineEdit)

        self.totalBayarLabel = QLabel(self.formLayoutWidget)
        self.totalBayarLabel.setObjectName(u"totalBayarLabel")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.totalBayarLabel)

        self.totalBayarLineEdit = QLineEdit(self.formLayoutWidget)
        self.totalBayarLineEdit.setObjectName(u"totalBayarLineEdit")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.totalBayarLineEdit)

        self.terbilangLabel = QLabel(self.formLayoutWidget)
        self.terbilangLabel.setObjectName(u"terbilangLabel")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.terbilangLabel)

        self.terbilangLineEdit = QLineEdit(self.formLayoutWidget)
        self.terbilangLineEdit.setObjectName(u"terbilangLineEdit")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.terbilangLineEdit)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 40, 91, 20))
        self.hapusButton = QPushButton(Form)
        self.hapusButton.setObjectName(u"hapusButton")
        self.hapusButton.setGeometry(QRect(480, 410, 90, 29))
        self.ubahButton = QPushButton(Form)
        self.ubahButton.setObjectName(u"ubahButton")
        self.ubahButton.setGeometry(QRect(370, 410, 90, 29))
        self.simpanButton = QPushButton(Form)
        self.simpanButton.setObjectName(u"simpanButton")
        self.simpanButton.setGeometry(QRect(260, 410, 90, 29))
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
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
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 470, 601, 192))
        self.cetakButton = QPushButton(Form)
        self.cetakButton.setObjectName(u"cetakButton")
        self.cetakButton.setGeometry(QRect(150, 410, 90, 29))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.noInvoiceLabel.setText(QCoreApplication.translate("Form", u"No Invoice", None))
        self.tanggalLabel.setText(QCoreApplication.translate("Form", u"Tanggal", None))
        self.kodeAdvertiserLabel.setText(QCoreApplication.translate("Form", u"Kode Advertiser", None))
        self.kodeIklanLabel.setText(QCoreApplication.translate("Form", u"Kode Iklan", None))
        self.frekwensiLabel.setText(QCoreApplication.translate("Form", u"Frekwensi", None))
        self.jumlahBayarLabel.setText(QCoreApplication.translate("Form", u"Jumlah Bayar", None))
        self.pPHLabel.setText(QCoreApplication.translate("Form", u"PPH", None))
        self.totalBayarLabel.setText(QCoreApplication.translate("Form", u"Total Bayar", None))
        self.terbilangLabel.setText(QCoreApplication.translate("Form", u"Terbilang", None))
        self.label.setText(QCoreApplication.translate("Form", u"Biaya Bayar", None))
        self.hapusButton.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.ubahButton.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.simpanButton.setText(QCoreApplication.translate("Form", u"Simpan", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"No Invoice", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Tanggal", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Kode Advertiser", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Kode Iklan", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Frekwensi", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Jumlah Bayar", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"PPH", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Total bayar", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Terbilang", None));
        self.cetakButton.setText(QCoreApplication.translate("Form", u"Cetak", None))
    # retranslateUi

