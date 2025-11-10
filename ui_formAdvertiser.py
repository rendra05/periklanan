# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formAdvertiser.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(798, 715)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 70, 111, 20))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 110, 63, 20))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 150, 111, 20))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 190, 63, 20))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 230, 63, 20))
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 270, 63, 20))
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 310, 63, 20))
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 350, 63, 20))
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 390, 63, 20))
        self.kd_advertizerEdit = QLineEdit(Form)
        self.kd_advertizerEdit.setObjectName(u"kd_advertizerEdit")
        self.kd_advertizerEdit.setGeometry(QRect(230, 70, 351, 28))
        self.namaEdit = QLineEdit(Form)
        self.namaEdit.setObjectName(u"namaEdit")
        self.namaEdit.setGeometry(QRect(230, 110, 351, 28))
        self.orderEdit = QLineEdit(Form)
        self.orderEdit.setObjectName(u"orderEdit")
        self.orderEdit.setGeometry(QRect(230, 150, 351, 28))
        self.alamatEdit = QLineEdit(Form)
        self.alamatEdit.setObjectName(u"alamatEdit")
        self.alamatEdit.setGeometry(QRect(230, 190, 351, 28))
        self.kotaEdit = QLineEdit(Form)
        self.kotaEdit.setObjectName(u"kotaEdit")
        self.kotaEdit.setGeometry(QRect(230, 230, 351, 28))
        self.kodeposEdit = QLineEdit(Form)
        self.kodeposEdit.setObjectName(u"kodeposEdit")
        self.kodeposEdit.setGeometry(QRect(230, 270, 351, 28))
        self.tlpEdit = QLineEdit(Form)
        self.tlpEdit.setObjectName(u"tlpEdit")
        self.tlpEdit.setGeometry(QRect(230, 310, 351, 28))
        self.faxEdit = QLineEdit(Form)
        self.faxEdit.setObjectName(u"faxEdit")
        self.faxEdit.setGeometry(QRect(230, 350, 351, 28))
        self.emailEdit = QLineEdit(Form)
        self.emailEdit.setObjectName(u"emailEdit")
        self.emailEdit.setGeometry(QRect(230, 390, 351, 28))
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(350, 20, 101, 20))
        self.simpanButton = QPushButton(Form)
        self.simpanButton.setObjectName(u"simpanButton")
        self.simpanButton.setGeometry(QRect(230, 440, 90, 29))
        self.ubahButton = QPushButton(Form)
        self.ubahButton.setObjectName(u"ubahButton")
        self.ubahButton.setGeometry(QRect(360, 440, 90, 29))
        self.hapusButton = QPushButton(Form)
        self.hapusButton.setObjectName(u"hapusButton")
        self.hapusButton.setGeometry(QRect(490, 440, 90, 29))
        self.tableAdvertiser = QTableWidget(Form)
        if (self.tableAdvertiser.columnCount() < 9):
            self.tableAdvertiser.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableAdvertiser.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableAdvertiser.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableAdvertiser.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableAdvertiser.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableAdvertiser.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableAdvertiser.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableAdvertiser.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableAdvertiser.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableAdvertiser.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableAdvertiser.setObjectName(u"tableAdvertiser")
        self.tableAdvertiser.setGeometry(QRect(20, 480, 751, 221))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Kode Advertiser", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Nama", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Pemberi Order", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Alamat", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Kota", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Kode pos", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"No. Telp", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"No fax", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Email", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"ADVERTISER", None))
        self.simpanButton.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.ubahButton.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.hapusButton.setText(QCoreApplication.translate("Form", u"Hapus", None))
        ___qtablewidgetitem = self.tableAdvertiser.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Kode Advertiser", None));
        ___qtablewidgetitem1 = self.tableAdvertiser.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama", None));
        ___qtablewidgetitem2 = self.tableAdvertiser.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Pemberi Order", None));
        ___qtablewidgetitem3 = self.tableAdvertiser.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Alamat", None));
        ___qtablewidgetitem4 = self.tableAdvertiser.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Kota", None));
        ___qtablewidgetitem5 = self.tableAdvertiser.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Kode pos", None));
        ___qtablewidgetitem6 = self.tableAdvertiser.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"No. Telp", None));
        ___qtablewidgetitem7 = self.tableAdvertiser.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"No fax", None));
        ___qtablewidgetitem8 = self.tableAdvertiser.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Email", None));
    # retranslateUi

