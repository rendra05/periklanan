# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formIklan.ui'
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
        Form.resize(690, 639)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(60, 80, 551, 271))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.kodeiklanLabel = QLabel(self.formLayoutWidget)
        self.kodeiklanLabel.setObjectName(u"kodeiklanLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.kodeiklanLabel)

        self.kodeiklanLineEdit = QLineEdit(self.formLayoutWidget)
        self.kodeiklanLineEdit.setObjectName(u"kodeiklanLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.kodeiklanLineEdit)

        self.produkLabel = QLabel(self.formLayoutWidget)
        self.produkLabel.setObjectName(u"produkLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.produkLabel)

        self.produkLineEdit = QLineEdit(self.formLayoutWidget)
        self.produkLineEdit.setObjectName(u"produkLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.produkLineEdit)

        self.brandLabel = QLabel(self.formLayoutWidget)
        self.brandLabel.setObjectName(u"brandLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.brandLabel)

        self.brandLineEdit = QLineEdit(self.formLayoutWidget)
        self.brandLineEdit.setObjectName(u"brandLineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.brandLineEdit)

        self.versiLabel = QLabel(self.formLayoutWidget)
        self.versiLabel.setObjectName(u"versiLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.versiLabel)

        self.versiLineEdit = QLineEdit(self.formLayoutWidget)
        self.versiLineEdit.setObjectName(u"versiLineEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.versiLineEdit)

        self.durasiLabel = QLabel(self.formLayoutWidget)
        self.durasiLabel.setObjectName(u"durasiLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.durasiLabel)

        self.durasiLineEdit = QLineEdit(self.formLayoutWidget)
        self.durasiLineEdit.setObjectName(u"durasiLineEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.durasiLineEdit)

        self.jenisLabel = QLabel(self.formLayoutWidget)
        self.jenisLabel.setObjectName(u"jenisLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.jenisLabel)

        self.jenisLineEdit = QLineEdit(self.formLayoutWidget)
        self.jenisLineEdit.setObjectName(u"jenisLineEdit")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.jenisLineEdit)

        self.hargaLabel = QLabel(self.formLayoutWidget)
        self.hargaLabel.setObjectName(u"hargaLabel")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.hargaLabel)

        self.hargaLineEdit = QLineEdit(self.formLayoutWidget)
        self.hargaLineEdit.setObjectName(u"hargaLineEdit")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.hargaLineEdit)

        self.hapusButton = QPushButton(Form)
        self.hapusButton.setObjectName(u"hapusButton")
        self.hapusButton.setGeometry(QRect(520, 360, 90, 29))
        self.simpanButton = QPushButton(Form)
        self.simpanButton.setObjectName(u"simpanButton")
        self.simpanButton.setGeometry(QRect(310, 360, 90, 29))
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
        self.tableWidget.setGeometry(QRect(65, 410, 551, 192))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 30, 63, 20))
        self.ubahButton = QPushButton(Form)
        self.ubahButton.setObjectName(u"ubahButton")
        self.ubahButton.setGeometry(QRect(410, 360, 90, 29))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.kodeiklanLabel.setText(QCoreApplication.translate("Form", u"kode iklan", None))
        self.produkLabel.setText(QCoreApplication.translate("Form", u"Produk", None))
        self.brandLabel.setText(QCoreApplication.translate("Form", u"Brand", None))
        self.versiLabel.setText(QCoreApplication.translate("Form", u"Versi", None))
        self.durasiLabel.setText(QCoreApplication.translate("Form", u" Durasi (menit)", None))
        self.jenisLabel.setText(QCoreApplication.translate("Form", u"Jenis", None))
        self.hargaLabel.setText(QCoreApplication.translate("Form", u"Harga", None))
        self.hapusButton.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.simpanButton.setText(QCoreApplication.translate("Form", u"Simpan", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Kode Iklan", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Produk", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Brand", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Versi", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Durasi", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Jenis", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Harga", None));
        self.label.setText(QCoreApplication.translate("Form", u"Iklan", None))
        self.ubahButton.setText(QCoreApplication.translate("Form", u"Ubah", None))
    # retranslateUi

