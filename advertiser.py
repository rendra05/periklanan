import mysql.connector
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class form_advertiser(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("formAdvertiser.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.form = loader.load(ui_file, self)
        ui_file.close()

        self.setLayout(self.form.layout())
        self.setWindowTitle("Form Advertiser")

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

        self.form.tableAdvertiser.cellClicked.connect(self.isi_form_dari_tabel)

        self.tampilkan_data()

    def validasi_input(self):
        nama = self.form.namaEdit.text().strip()
        order = self.form.orderEdit.text().strip()
        email = self.form.emailEdit.text().strip()

        if not nama or not order or not email:
            QMessageBox.warning(self, "Peringatan", "Nama, pemberi order, dan email wajib diisi")
            return False

        if "@" not in email or "." not in email:
            QMessageBox.warning(self, "Peringatan", "Format email tidak valid")
            return False

        return True

    def tampilkan_data(self):
        self.cursor.execute("SELECT * FROM advertiser")
        hasil = self.cursor.fetchall()
        self.form.tableAdvertiser.setRowCount(0)

        for row_number, row_data in enumerate(hasil):
            self.form.tableAdvertiser.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.form.tableAdvertiser.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(str(data))
                )

    def isi_form_dari_tabel(self, row, column):
        self.form.kd_advertizerEdit.setText(
            self.form.tableAdvertiser.item(row, 0).text()
        )
        self.form.namaEdit.setText(self.form.tableAdvertiser.item(row, 1).text())
        self.form.orderEdit.setText(self.form.tableAdvertiser.item(row, 2).text())
        self.form.alamatEdit.setText(self.form.tableAdvertiser.item(row, 3).text())
        self.form.kotaEdit.setText(self.form.tableAdvertiser.item(row, 4).text())
        self.form.kodeposEdit.setText(self.form.tableAdvertiser.item(row, 5).text())
        self.form.tlpEdit.setText(self.form.tableAdvertiser.item(row, 6).text())
        self.form.faxEdit.setText(self.form.tableAdvertiser.item(row, 7).text())
        self.form.emailEdit.setText(self.form.tableAdvertiser.item(row, 8).text())

    def simpan_data(self):
        if not self.validasi_input():
            return

        try:
            sql = (
                "INSERT INTO advertiser "
                "(nama_advertiser, pemberi_order, alamat, kota, kodepos, no_telp, no_fax, email) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            )

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
        if not self.validasi_input():
            return

        kd = self.form.kd_advertizerEdit.text()

        if not kd:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin diubah")
            return

        sql = (
            "UPDATE advertiser SET "
            "nama_advertiser=%s, pemberi_order=%s, alamat=%s, kota=%s, "
            "kodepos=%s, no_telp=%s, no_fax=%s, email=%s "
            "WHERE kd_advertiser=%s"
        )

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
        kd = self.form.kd_advertizerEdit.text()

        if not kd:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin dihapus")
            return

        self.cursor.execute(
            "DELETE FROM advertiser WHERE kd_advertiser=%s",
            (kd,)
        )
        self.db.commit()

        QMessageBox.information(self, "Sukses", "Data berhasil dihapus")
        self.tampilkan_data()
        self.kosongkan_form()

    def kosongkan_form(self):
        self.form.kd_advertizerEdit.clear()
        self.form.namaEdit.clear()
        self.form.orderEdit.clear()
        self.form.alamatEdit.clear()
        self.form.kotaEdit.clear()
        self.form.kodeposEdit.clear()
        self.form.tlpEdit.clear()
        self.form.faxEdit.clear()
        self.form.emailEdit.clear()
