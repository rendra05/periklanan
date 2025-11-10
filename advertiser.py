import mysql.connector
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class form_advertiser(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Load file UI
        ui_file = QFile("formAdvertiser.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.form = loader.load(ui_file, self)
        ui_file.close()

        self.setLayout(self.form.layout())
        self.setWindowTitle("Form Advertiser")

        # Koneksi ke database MySQL
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # ubah jika MySQL kamu pakai password
            database="periklanan"
        )
        self.cursor = self.db.cursor()

        # Hubungkan tombol
        self.form.simpanButton.clicked.connect(self.simpan_data)
        self.form.ubahButton.clicked.connect(self.ubah_data)
        self.form.hapusButton.clicked.connect(self.hapus_data)

        # Tampilkan data awal
        self.tampilkan_data()

    def tampilkan_data(self):
        self.cursor.execute("SELECT * FROM advertiser")
        hasil = self.cursor.fetchall()
        self.form.tableAdvertiser.setRowCount(0)
        for row_number, row_data in enumerate(hasil):
            self.form.tableAdvertiser.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.form.tableAdvertiser.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def simpan_data(self):
        try:
            sql = ("INSERT INTO advertiser "
                   "(nama_advertiser, pemberi_order, alamat, kota, kodepos, no_telp, no_fax, email) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
            val = (
                self.form.namaEdit.text(),
                self.form.orderEdit.text(),
                self.form.alamatEdit.text(),
                self.form.kotaEdit.text(),
                self.form.kodeposEdit.text(),
                self.form.tlpEdit.text(),
                self.form.faxEdit.text(),
                self.form.emailEdit.text()
            )
            self.cursor.execute(sql, val)
            self.db.commit()
            QMessageBox.information(self, "Sukses", "Data berhasil disimpan")
            self.tampilkan_data()
            self.kosongkan_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def ubah_data(self):
        row = self.form.tableAdvertiser.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin diubah")
            return

        kd = self.form.tableAdvertiser.item(row, 0).text()
        sql = ("UPDATE advertiser SET nama_advertiser=%s, pemberi_order=%s, alamat=%s, kota=%s, "
               "kodepos=%s, no_telp=%s, no_fax=%s, email=%s WHERE kd_advertiser=%s")
        val = (
            self.form.namaEdit.text(),
            self.form.orderEdit.text(),
            self.form.alamatEdit.text(),
            self.form.kotaEdit.text(),
            self.form.kodeposEdit.text(),
            self.form.tlpEdit.text(),
            self.form.faxEdit.text(),
            self.form.emailEdit.text(),
            kd
        )
        self.cursor.execute(sql, val)
        self.db.commit()
        QMessageBox.information(self, "Sukses", "Data berhasil diubah")
        self.tampilkan_data()
        self.kosongkan_form()

    def hapus_data(self):
        row = self.form.tableAdvertiser.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin dihapus")
            return

        kd = self.form.tableAdvertiser.item(row, 0).text()
        self.cursor.execute("DELETE FROM advertiser WHERE kd_advertiser=%s", (kd,))
        self.db.commit()
        QMessageBox.information(self, "Sukses", "Data berhasil dihapus")
        self.tampilkan_data()

    def kosongkan_form(self):
        self.form.namaEdit.clear()
        self.form.orderEdit.clear()
        self.form.alamatEdit.clear()
        self.form.kotaEdit.clear()
        self.form.kodeposEdit.clear()
        self.form.tlpEdit.clear()
        self.form.faxEdit.clear()
        self.form.emailEdit.clear()
