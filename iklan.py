import mysql.connector
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


class form_iklan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("formIklan.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.form = loader.load(ui_file, self)
        ui_file.close()

        self.setLayout(self.form.layout())
        self.setWindowTitle("Form Iklan")

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="periklanan"
        )
        self.cursor = self.db.cursor()

        self.form.simpanButton.clicked.connect(self.simpan_data)
        self.form.ubahButton.clicked.connect(self.ubah_data)
        self.form.hapusButton.clicked.connect(self.hapus_data)

        self.form.tableWidget.cellClicked.connect(self.isi_form_dari_tabel)

        self.tampilkan_data()

    def validasi_input(self):
        produk = self.form.produkLineEdit.text().strip()
        brand = self.form.brandLineEdit.text().strip()
        durasi = self.form.durasiLineEdit.text().strip()
        harga = self.form.hargaLineEdit.text().strip()

        if not produk or not brand or not durasi or not harga:
            QMessageBox.warning(self, "Peringatan", "Produk, brand, durasi, dan harga wajib diisi")
            return False

        if not durasi.isdigit():
            QMessageBox.warning(self, "Peringatan", "Durasi harus berupa angka")
            return False

        if not harga.isdigit():
            QMessageBox.warning(self, "Peringatan", "Harga harus berupa angka")
            return False

        return True

    def tampilkan_data(self):
        self.cursor.execute("SELECT * FROM iklan")
        hasil = self.cursor.fetchall()
        self.form.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(hasil):
            self.form.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.form.tableWidget.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(str(data))
                )

    def isi_form_dari_tabel(self, row, column):
        self.form.kodeiklanLineEdit.setText(self.form.tableWidget.item(row, 0).text())
        self.form.produkLineEdit.setText(self.form.tableWidget.item(row, 1).text())
        self.form.brandLineEdit.setText(self.form.tableWidget.item(row, 2).text())
        self.form.versiLineEdit.setText(self.form.tableWidget.item(row, 3).text())
        self.form.durasiLineEdit.setText(self.form.tableWidget.item(row, 4).text())
        self.form.jenisLineEdit.setText(self.form.tableWidget.item(row, 5).text())
        self.form.hargaLineEdit.setText(self.form.tableWidget.item(row, 6).text())

    def simpan_data(self):
        if not self.validasi_input():
            return

        try:
            sql = (
                "INSERT INTO iklan (produk, brand, versi, durasi, jenis, harga) "
                "VALUES (%s, %s, %s, %s, %s, %s)"
            )

            val = (
                self.form.produkLineEdit.text(),
                self.form.brandLineEdit.text(),
                self.form.versiLineEdit.text(),
                self.form.durasiLineEdit.text(),
                self.form.jenisLineEdit.text(),
                self.form.hargaLineEdit.text()
            )

            self.cursor.execute(sql, val)
            self.db.commit()

            QMessageBox.information(self, "Sukses", "Data berhasil disimpan")
            self.tampilkan_data()
            self.kosongkan_form()

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def ubah_data(self):
        if not self.validasi_input():
            return

        kd = self.form.kodeiklanLineEdit.text()

        if not kd:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin diubah")
            return

        sql = (
            "UPDATE iklan SET produk=%s, brand=%s, versi=%s, durasi=%s, jenis=%s, harga=%s "
            "WHERE kd_iklan=%s"
        )

        val = (
            self.form.produkLineEdit.text(),
            self.form.brandLineEdit.text(),
            self.form.versiLineEdit.text(),
            self.form.durasiLineEdit.text(),
            self.form.jenisLineEdit.text(),
            self.form.hargaLineEdit.text(),
            kd
        )

        self.cursor.execute(sql, val)
        self.db.commit()

        QMessageBox.information(self, "Sukses", "Data berhasil diubah")
        self.tampilkan_data()
        self.kosongkan_form()

    def hapus_data(self):
        kd = self.form.kodeiklanLineEdit.text()

        if not kd:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin dihapus")
            return

        self.cursor.execute(
            "DELETE FROM iklan WHERE kd_iklan=%s",
            (kd,)
        )
        self.db.commit()

        QMessageBox.information(self, "Sukses", "Data berhasil dihapus")
        self.tampilkan_data()
        self.kosongkan_form()

    def kosongkan_form(self):
        self.form.kodeiklanLineEdit.clear()
        self.form.produkLineEdit.clear()
        self.form.brandLineEdit.clear()
        self.form.versiLineEdit.clear()
        self.form.durasiLineEdit.clear()
        self.form.jenisLineEdit.clear()
        self.form.hargaLineEdit.clear()
