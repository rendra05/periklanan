import sys
import mysql.connector
from PySide6.QtWidgets import QWidget, QApplication, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QDate

class Form_BiayaIklan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        ui_file = QFile("formBiayaiklan.ui")  # sesuai nama file di project kamu
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.form = loader.load(ui_file, self)
        ui_file.close()

        self.setLayout(self.form.layout())
        self.setWindowTitle("Form Biaya Iklan")

        # Koneksi database
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="periklanan"
        )
        self.cursor = self.db.cursor()

        # Set tanggal hari ini
        self.form.tanggalLineEdit.setText(QDate.currentDate().toString("yyyy-MM-dd"))

        # Connect tombol
        self.form.simpanButton.clicked.connect(self.simpan_data)
        self.form.ubahButton.clicked.connect(self.ubah_data)
        self.form.hapusButton.clicked.connect(self.hapus_data)

        # Hitung otomatis
        self.form.jumlahBayarLineEdit.textChanged.connect(self.hitung_total)
        self.form.pPHLineEdit.textChanged.connect(self.hitung_total)

        # Load data awal
        self.load_combo_advertiser()
        self.load_combo_iklan()
        self.load_data()

        # Klik tabel
        self.form.tableWidget.cellClicked.connect(self.pilih_data)

    def load_combo_advertiser(self):
        try:
            self.cursor.execute("SELECT kd_advertiser, nama_advertiser FROM advertiser")
            data = self.cursor.fetchall()
            self.form.kodeAdvertiserComboBox.clear()
            for row in data:
                self.form.kodeAdvertiserComboBox.addItem(f"{row[0]} - {row[1]}", row[0])
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal load advertiser: {str(e)}")

    def load_combo_iklan(self):
        try:
            self.cursor.execute("SELECT kd_iklan, produk FROM iklan")
            data = self.cursor.fetchall()
            self.form.kodeIklanComboBox.clear()
            for row in data:
                self.form.kodeIklanComboBox.addItem(f"{row[0]} - {row[1]}", row[0])
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal load iklan: {str(e)}")

    def hitung_total(self):
        try:
            jumlah = float(self.form.jumlahBayarLineEdit.text() or 0)
            pph = float(self.form.pPHLineEdit.text() or 0)
            total = jumlah - pph
            self.form.totalBayarLineEdit.setText(str(total))
            self.form.terbilangLineEdit.setText(self.angka_ke_terbilang(int(total)))
        except ValueError:
            self.form.totalBayarLineEdit.setText("0")
            self.form.terbilangLineEdit.clear()

    def angka_ke_terbilang(self, angka):
        angka_str = ["", "Satu", "Dua", "Tiga", "Empat", "Lima", "Enam", "Tujuh", "Delapan", "Sembilan"]
        if angka == 0:
            return "Nol Rupiah"

        def konversi_ratusan(n):
            if n == 0:
                return ""
            elif n < 10:
                return angka_str[n]
            elif n < 20:
                if n == 10:
                    return "Sepuluh"
                elif n == 11:
                    return "Sebelas"
                else:
                    return angka_str[n - 10] + " Belas"
            elif n < 100:
                return angka_str[n // 10] + " Puluh " + angka_str[n % 10]
            else:
                ratus = n // 100
                if ratus == 1:
                    return "Seratus " + konversi_ratusan(n % 100)
                else:
                    return angka_str[ratus] + " Ratus " + konversi_ratusan(n % 100)

        if angka < 1000:
            return konversi_ratusan(angka).strip() + " Rupiah"
        elif angka < 1000000:
            ribu = angka // 1000
            if ribu == 1:
                return ("Seribu " + konversi_ratusan(angka % 1000)).strip() + " Rupiah"
            else:
                return (konversi_ratusan(ribu) + " Ribu " + konversi_ratusan(angka % 1000)).strip() + " Rupiah"
        elif angka < 1000000000:
            juta = angka // 1000000
            sisa = angka % 1000000
            ribu = sisa // 1000
            ratus = sisa % 1000
            hasil = konversi_ratusan(juta) + " Juta "
            if ribu > 0:
                hasil += konversi_ratusan(ribu) + " Ribu "
            if ratus > 0:
                hasil += konversi_ratusan(ratus)
            return hasil.strip() + " Rupiah"
        else:
            return "Angka terlalu besar"

    def simpan_data(self):
        try:
            query = """INSERT INTO biaya_iklan
                       (no_invoice, tanggal, kd_advertiser, kd_iklan, frekwensi, jumlah_bayar, pph, total_bayar, terbilang)
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            val = (
                self.form.noInvoiceLineEdit.text(),
                self.form.tanggalLineEdit.text(),
                self.form.kodeAdvertiserComboBox.currentData(),
                self.form.kodeIklanComboBox.currentData(),
                self.form.frekwensiLineEdit.text(),
                self.form.jumlahBayarLineEdit.text(),
                self.form.pPHLineEdit.text(),
                self.form.totalBayarLineEdit.text(),
                self.form.terbilangLineEdit.text()
            )
            self.cursor.execute(query, val)
            self.db.commit()
            QMessageBox.information(self, "Sukses", "Data berhasil disimpan!")
            self.clear_form()
            self.load_data()
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", str(e))

    def ubah_data(self):
        try:
            no_invoice = self.form.noInvoiceLineEdit.text()
            query = """UPDATE biaya_iklan SET tanggal=%s, kd_advertiser=%s, kd_iklan=%s, frekwensi=%s,
                       jumlah_bayar=%s, pph=%s, total_bayar=%s, terbilang=%s WHERE no_invoice=%s"""
            val = (
                self.form.tanggalLineEdit.text(),
                self.form.kodeAdvertiserComboBox.currentData(),
                self.form.kodeIklanComboBox.currentData(),
                self.form.frekwensiLineEdit.text(),
                self.form.jumlahBayarLineEdit.text(),
                self.form.pPHLineEdit.text(),
                self.form.totalBayarLineEdit.text(),
                self.form.terbilangLineEdit.text(),
                no_invoice
            )
            self.cursor.execute(query, val)
            self.db.commit()
            QMessageBox.information(self, "Sukses", "Data berhasil diubah!")
            self.clear_form()
            self.load_data()
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", str(e))

    def hapus_data(self):
        no_invoice = self.form.noInvoiceLineEdit.text()
        if not no_invoice:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin dihapus!")
            return
        self.cursor.execute("DELETE FROM biaya_iklan WHERE no_invoice=%s", (no_invoice,))
        self.db.commit()
        QMessageBox.information(self, "Sukses", "Data berhasil dihapus!")
        self.clear_form()
        self.load_data()

    def load_data(self):
        try:
            self.cursor.execute("SELECT * FROM biaya_iklan ORDER BY tanggal DESC")
            hasil = self.cursor.fetchall()
            self.form.tableWidget.setRowCount(0)
            for r, row_data in enumerate(hasil):
                self.form.tableWidget.insertRow(r)
                for c, col_data in enumerate(row_data):
                    self.form.tableWidget.setItem(r, c, QTableWidgetItem(str(col_data)))
            self.form.tableWidget.resizeColumnsToContents()
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", str(e))

    def pilih_data(self, row, column):
        self.form.noInvoiceLineEdit.setText(self.form.tableWidget.item(row, 0).text())
        self.form.tanggalLineEdit.setText(self.form.tableWidget.item(row, 1).text())
        kode_adv = self.form.tableWidget.item(row, 2).text()
        kode_ikl = self.form.tableWidget.item(row, 3).text()
        idx_adv = self.form.kodeAdvertiserComboBox.findData(kode_adv)
        idx_ikl = self.form.kodeIklanComboBox.findData(kode_ikl)
        if idx_adv >= 0:
            self.form.kodeAdvertiserComboBox.setCurrentIndex(idx_adv)
        if idx_ikl >= 0:
            self.form.kodeIklanComboBox.setCurrentIndex(idx_ikl)
        self.form.frekwensiLineEdit.setText(self.form.tableWidget.item(row, 4).text())
        self.form.jumlahBayarLineEdit.setText(self.form.tableWidget.item(row, 5).text())
        self.form.pPHLineEdit.setText(self.form.tableWidget.item(row, 6).text())
        self.form.totalBayarLineEdit.setText(self.form.tableWidget.item(row, 7).text())
        self.form.terbilangLineEdit.setText(self.form.tableWidget.item(row, 8).text())

    def clear_form(self):
        self.form.noInvoiceLineEdit.clear()
        self.form.tanggalLineEdit.setText(QDate.currentDate().toString("yyyy-MM-dd"))
        self.form.frekwensiLineEdit.clear()
        self.form.jumlahBayarLineEdit.clear()
        self.form.pPHLineEdit.clear()
        self.form.totalBayarLineEdit.clear()
        self.form.terbilangLineEdit.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Form_BiayaIklan()
    window.show()
    sys.exit(app.exec())
