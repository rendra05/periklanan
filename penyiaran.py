import mysql.connector
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


class FormPenyiaran(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("formPenyiaran.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.form = loader.load(ui_file, self)
        ui_file.close()

        self.setLayout(self.form.layout())
        self.setWindowTitle("Form Penyiaran")

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
        if not self.form.iDSiarLineEdit.text().strip():
            QMessageBox.warning(self, "Peringatan", "ID Siar wajib diisi")
            return False


    def tampilkan_data(self):
        self.cursor.execute("SELECT * FROM penyiaran")
        hasil = self.cursor.fetchall()
        self.form.tableWidget.setRowCount(0)

        for row_index, row_data in enumerate(hasil):
            self.form.tableWidget.insertRow(row_index)
            for col_index, data in enumerate(row_data):
                self.form.tableWidget.setItem(
                    row_index,
                    col_index,
                    QTableWidgetItem(str(data))
                )

    def isi_form_dari_tabel(self, row, column):
        self.form.iDSiarLineEdit.setText(self.form.tableWidget.item(row, 0).text())
        self.form.kodeIklanLineEdit.setText(self.form.tableWidget.item(row, 1).text())
        self.form.produkLineEdit.setText(self.form.tableWidget.item(row, 2).text())
        self.form.periodeLineEdit.setText(self.form.tableWidget.item(row, 3).text())
        self.form.airTimeLineEdit.setText(self.form.tableWidget.item(row, 4).text())
        self.form.tglMulaiLineEdit.setText(self.form.tableWidget.item(row, 5).text())
        self.form.tglSelesaiLineEdit.setText(self.form.tableWidget.item(row, 6).text())


    def simpan_data(self):
        if not self.validasi_input():
            return

        try:
            sql = (
                "INSERT INTO penyiaran "
                "(id_siar, kd_iklan, produk, periode, air_time, tgl_mulai, tgl_selesai) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s)"
            )

            val = (
                self.form.idSiarLineEdit.text(),
                self.form.kodeIklanLineEdit.text(),
                self.form.produkLineEdit.text(),
                self.form.periodeLineEdit.text(),
                self.form.airTimeLineEdit.text(),
                self.form.tglMulaiLineEdit.text(),
                self.form.tglSelesaiLineEdit.text()
            )

            self.cursor.execute(sql, val)
            self.db.commit()

            QMessageBox.information(self, "Sukses", "Data berhasil disimpan")
            self.tampilkan_data()
            self.kosongkan_form()

        except mysql.connector.IntegrityError:
            QMessageBox.critical(self, "Error", "ID Siar sudah digunakan")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def ubah_data(self):
        id_siar = self.form.idSiarLineEdit.text().strip()

        if not id_siar:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin diubah")
            return

        sql = (
            "UPDATE penyiaran SET kd_iklan=%s, produk=%s, periode=%s, air_time=%s, "
            "tgl_mulai=%s, tgl_selesai=%s WHERE id_siar=%s"
        )

        val = (
            self.form.kodeIklanLineEdit.text(),
            self.form.produkLineEdit.text(),
            self.form.periodeLineEdit.text(),
            self.form.airTimeLineEdit.text(),
            self.form.tglMulaiLineEdit.text(),
            self.form.tglSelesaiLineEdit.text(),
            id_siar
        )

        self.cursor.execute(sql, val)
        self.db.commit()

        QMessageBox.information(self, "Sukses", "Data berhasil diubah")
        self.tampilkan_data()
        self.kosongkan_form()

    def hapus_data(self):
        id_siar = self.form.idSiarLineEdit.text().strip()

        if not id_siar:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin dihapus")
            return

        self.cursor.execute(
            "DELETE FROM penyiaran WHERE id_siar=%s",
            (id_siar,)
        )
        self.db.commit()

        QMessageBox.information(self, "Sukses", "Data berhasil dihapus")
        self.tampilkan_data()
        self.kosongkan_form()

    def kosongkan_form(self):
        self.form.idSiarLineEdit.clear()
        self.form.kodeIklanLineEdit.clear()
        self.form.produkLineEdit.clear()
        self.form.periodeLineEdit.clear()
        self.form.airTimeLineEdit.clear()
        self.form.tglMulaiLineEdit.clear()
        self.form.tglSelesaiLineEdit.clear()
