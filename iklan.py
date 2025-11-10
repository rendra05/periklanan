import mysql.connector
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


class form_iklan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Load UI
        ui_file = QFile("formIklan.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.form = loader.load(ui_file, self)
        ui_file.close()

        self.setLayout(self.form.layout())
        self.setWindowTitle("Form Iklan")

        # Koneksi ke database MySQL
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # ubah jika ada password
            database="periklanan"
        )
        self.cursor = self.db.cursor()

        # Hubungkan tombol ke fungsi
        self.form.simpanButton.clicked.connect(self.simpan_data)
        self.form.ubahButton.clicked.connect(self.ubah_data)
        self.form.hapusButton.clicked.connect(self.hapus_data)

        # Klik tabel untuk isi form otomatis
        self.form.tableWidget.cellClicked.connect(self.isi_form_dari_tabel)

        # Tampilkan data awal
        self.tampilkan_data()

    def tampilkan_data(self):
        self.cursor.execute("SELECT * FROM iklan")
        hasil = self.cursor.fetchall()
        self.form.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(hasil):
            self.form.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.form.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def simpan_data(self):
        try:
            sql = ("INSERT INTO iklan (produk, brand, versi, durasi, jenis, harga) "
                   "VALUES (%s, %s, %s, %s, %s, %s)")
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
        row = self.form.tableWidget.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin diubah")
            return

        kd = self.form.tableWidget.item(row, 0).text()
        sql = ("UPDATE iklan SET produk=%s, brand=%s, versi=%s, durasi=%s, jenis=%s, harga=%s "
               "WHERE kd_iklan=%s")
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
        row = self.form.tableWidget.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin dihapus")
            return

        kd = self.form.tableWidget.item(row, 0).text()
        self.cursor.execute("DELETE FROM iklan WHERE kd_iklan=%s", (kd,))
        self.db.commit()
        QMessageBox.information(self, "Sukses", "Data berhasil dihapus")
        self.tampilkan_data()
        self.kosongkan_form()

    def isi_form_dari_tabel(self, row, column):
        self.form.kodeiklanLineEdit.setText(self.form.tableWidget.item(row, 0).text())
        self.form.produkLineEdit.setText(self.form.tableWidget.item(row, 1).text())
        self.form.brandLineEdit.setText(self.form.tableWidget.item(row, 2).text())
        self.form.versiLineEdit.setText(self.form.tableWidget.item(row, 3).text())
        self.form.durasiLineEdit.setText(self.form.tableWidget.item(row, 4).text())
        self.form.jenisLineEdit.setText(self.form.tableWidget.item(row, 5).text())
        self.form.hargaLineEdit.setText(self.form.tableWidget.item(row, 6).text())

    def kosongkan_form(self):
        self.form.kodeiklanLineEdit.clear()
        self.form.produkLineEdit.clear()
        self.form.brandLineEdit.clear()
        self.form.versiLineEdit.clear()
        self.form.durasiLineEdit.clear()
        self.form.jenisLineEdit.clear()
        self.form.hargaLineEdit.clear()
