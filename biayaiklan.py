import sys
import mysql.connector
from PySide6.QtWidgets import QWidget, QApplication, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QDate
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
from PySide6.QtGui import QTextDocument



class Form_BiayaIklan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("formBiayaiklan.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.form = loader.load(ui_file, self)
        ui_file.close()

        self.setLayout(self.form.layout())
        self.setWindowTitle("Form Biaya Iklan")

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="periklanan"
        )
        self.cursor = self.db.cursor()

        self.form.tanggalLineEdit.setText(
            QDate.currentDate().toString("yyyy-MM-dd")
        )

        self.form.simpanButton.clicked.connect(self.simpan_data)
        self.form.ubahButton.clicked.connect(self.ubah_data)
        self.form.hapusButton.clicked.connect(self.hapus_data)
        self.form.cetakButton.clicked.connect(self.cetak_data)


        self.form.jumlahBayarLineEdit.textChanged.connect(self.on_jumlah_changed)
        self.form.pPHLineEdit.textChanged.connect(self.on_pph_changed)

        self.load_combo_advertiser()
        self.load_combo_iklan()
        self.load_data()

        self.form.tableWidget.cellClicked.connect(self.pilih_data)

    def load_combo_advertiser(self):
        self.cursor.execute(
            "SELECT kd_advertiser, nama_advertiser FROM advertiser"
        )
        data = self.cursor.fetchall()
        self.form.kodeAdvertiserComboBox.clear()
        for row in data:
            self.form.kodeAdvertiserComboBox.addItem(
                f"{row[0]} - {row[1]}",
                row[0]
            )

    def load_combo_iklan(self):
        self.cursor.execute(
            "SELECT kd_iklan, produk FROM iklan"
        )
        data = self.cursor.fetchall()
        self.form.kodeIklanComboBox.clear()
        for row in data:
            self.form.kodeIklanComboBox.addItem(
                f"{row[0]} - {row[1]}",
                row[0]
            )

    def format_rupiah(self, text):
        angka = ''.join(filter(str.isdigit, text))
        if not angka:
            return ""
        return "{:,}".format(int(angka)).replace(",", ".")

    def parse_rupiah(self, text):
        return int(text.replace(".", "")) if text else 0

    def on_jumlah_changed(self):
        self.form.jumlahBayarLineEdit.blockSignals(True)
        self.form.jumlahBayarLineEdit.setText(
            self.format_rupiah(self.form.jumlahBayarLineEdit.text())
        )
        self.form.jumlahBayarLineEdit.blockSignals(False)
        self.hitung_total()

    def on_pph_changed(self):
        self.form.pPHLineEdit.blockSignals(True)
        self.form.pPHLineEdit.setText(
            self.format_rupiah(self.form.pPHLineEdit.text())
        )
        self.form.pPHLineEdit.blockSignals(False)
        self.hitung_total()

    def hitung_total(self):
        jumlah = self.parse_rupiah(self.form.jumlahBayarLineEdit.text())
        pph = self.parse_rupiah(self.form.pPHLineEdit.text())
        total = max(jumlah - pph, 0)

        self.form.totalBayarLineEdit.setText(
            self.format_rupiah(str(total))
        )
        self.form.terbilangLineEdit.setText(
            self.angka_ke_terbilang(total)
        )

    def angka_ke_terbilang(self, angka):
        satuan = ["", "Satu", "Dua", "Tiga", "Empat", "Lima", "Enam", "Tujuh", "Delapan", "Sembilan"]

        if angka == 0:
            return "Nol Rupiah"

        def ratusan(n):
            hasil = ""
            if n >= 100:
                hasil += "Seratus " if n // 100 == 1 else satuan[n // 100] + " Ratus "
                n %= 100
            if n >= 20:
                hasil += satuan[n // 10] + " Puluh "
                n %= 10
            if n >= 10:
                hasil += "Sepuluh " if n == 10 else "Sebelas " if n == 11 else satuan[n - 10] + " Belas "
                n = 0
            if n > 0:
                hasil += satuan[n] + " "
            return hasil.strip()

        if angka < 1000:
            return ratusan(angka) + " Rupiah"

        if angka < 1_000_000:
            ribu = angka // 1000
            sisa = angka % 1000
            hasil = "Seribu " if ribu == 1 else ratusan(ribu) + " Ribu "
            if sisa:
                hasil += ratusan(sisa)
            return hasil.strip() + " Rupiah"

        if angka < 1_000_000_000:
            juta = angka // 1_000_000
            sisa = angka % 1_000_000
            hasil = ratusan(juta) + " Juta "
            ribu = sisa // 1000
            ratus = sisa % 1000
            if ribu:
                hasil += ratusan(ribu) + " Ribu "
            if ratus:
                hasil += ratusan(ratus)
            return hasil.strip() + " Rupiah"

        return "Angka terlalu besar"

    def simpan_data(self):
        query = (
            "INSERT INTO biaya_iklan "
            "(no_invoice, tanggal, kd_advertiser, kd_iklan, frekwensi, "
            "jumlah_bayar, pph, total_bayar, terbilang) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )

        val = (
            self.form.noInvoiceLineEdit.text(),
            self.form.tanggalLineEdit.text(),
            self.form.kodeAdvertiserComboBox.currentData(),
            self.form.kodeIklanComboBox.currentData(),
            self.form.frekwensiLineEdit.text(),
            self.parse_rupiah(self.form.jumlahBayarLineEdit.text()),
            self.parse_rupiah(self.form.pPHLineEdit.text()),
            self.parse_rupiah(self.form.totalBayarLineEdit.text()),
            self.form.terbilangLineEdit.text()
        )

        self.cursor.execute(query, val)
        self.db.commit()

        QMessageBox.information(self, "Sukses", "Data berhasil disimpan")
        self.clear_form()
        self.load_data()

    def ubah_data(self):
        query = (
            "UPDATE biaya_iklan SET tanggal=%s, kd_advertiser=%s, kd_iklan=%s, "
            "frekwensi=%s, jumlah_bayar=%s, pph=%s, total_bayar=%s, terbilang=%s "
            "WHERE no_invoice=%s"
        )

        val = (
            self.form.tanggalLineEdit.text(),
            self.form.kodeAdvertiserComboBox.currentData(),
            self.form.kodeIklanComboBox.currentData(),
            self.form.frekwensiLineEdit.text(),
            self.parse_rupiah(self.form.jumlahBayarLineEdit.text()),
            self.parse_rupiah(self.form.pPHLineEdit.text()),
            self.parse_rupiah(self.form.totalBayarLineEdit.text()),
            self.form.terbilangLineEdit.text(),
            self.form.noInvoiceLineEdit.text()
        )

        self.cursor.execute(query, val)
        self.db.commit()

        QMessageBox.information(self, "Sukses", "Data berhasil diubah")
        self.clear_form()
        self.load_data()

    def hapus_data(self):
        no_invoice = self.form.noInvoiceLineEdit.text()
        if not no_invoice:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin dihapus")
            return

        self.cursor.execute(
            "DELETE FROM biaya_iklan WHERE no_invoice=%s",
            (no_invoice,)
        )
        self.db.commit()

        QMessageBox.information(self, "Sukses", "Data berhasil dihapus")
        self.clear_form()
        self.load_data()

    def load_data(self):
        self.cursor.execute(
            "SELECT * FROM biaya_iklan ORDER BY tanggal DESC"
        )
        hasil = self.cursor.fetchall()
        self.form.tableWidget.setRowCount(0)

        for r, row_data in enumerate(hasil):
            self.form.tableWidget.insertRow(r)
            for c, col_data in enumerate(row_data):
                self.form.tableWidget.setItem(
                    r,
                    c,
                    QTableWidgetItem(str(col_data))
                )

        self.form.tableWidget.resizeColumnsToContents()

    def pilih_data(self, row, column):
        self.form.noInvoiceLineEdit.setText(self.form.tableWidget.item(row, 0).text())
        self.form.tanggalLineEdit.setText(self.form.tableWidget.item(row, 1).text())

        kode_adv = self.form.tableWidget.item(row, 2).text()
        kode_ikl = self.form.tableWidget.item(row, 3).text()

        self.form.kodeAdvertiserComboBox.setCurrentIndex(
            self.form.kodeAdvertiserComboBox.findData(kode_adv)
        )
        self.form.kodeIklanComboBox.setCurrentIndex(
            self.form.kodeIklanComboBox.findData(kode_ikl)
        )

        self.form.frekwensiLineEdit.setText(self.form.tableWidget.item(row, 4).text())
        self.form.jumlahBayarLineEdit.setText(self.format_rupiah(self.form.tableWidget.item(row, 5).text()))
        self.form.pPHLineEdit.setText(self.format_rupiah(self.form.tableWidget.item(row, 6).text()))
        self.form.totalBayarLineEdit.setText(self.format_rupiah(self.form.tableWidget.item(row, 7).text()))
        self.form.terbilangLineEdit.setText(self.form.tableWidget.item(row, 8).text())

    def cetak_data(self):
        if not self.form.noInvoiceLineEdit.text():
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin dicetak")


        html = f"""
        <h2>Invoice Biaya Iklan</h2>
        <table border="1" cellpadding="6" cellspacing="0">
            <tr><td>No Invoice</td><td>{self.form.noInvoiceLineEdit.text()}</td></tr>
            <tr><td>Tanggal</td><td>{self.form.tanggalLineEdit.text()}</td></tr>
            <tr><td>Kode Advertiser</td><td>{self.form.kodeAdvertiserComboBox.currentData()}</td></tr>
            <tr><td>Kode Iklan</td><td>{self.form.kodeIklanComboBox.currentData()}</td></tr>
            <tr><td>Frekwensi</td><td>{self.form.frekwensiLineEdit.text()}</td></tr>
            <tr><td>Jumlah Bayar</td><td>{self.form.jumlahBayarLineEdit.text()}</td></tr>
            <tr><td>PPH</td><td>{self.form.pPHLineEdit.text()}</td></tr>
            <tr><td>Total Bayar</td><td>{self.form.totalBayarLineEdit.text()}</td></tr>
            <tr><td>Terbilang</td><td>{self.form.terbilangLineEdit.text()}</td></tr>
        </table>
        """

        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec():
            doc = QTextDocument()
            doc.setHtml(html)
            doc.print_(printer)




    def clear_form(self):
        self.form.noInvoiceLineEdit.clear()
        self.form.tanggalLineEdit.setText(
            QDate.currentDate().toString("yyyy-MM-dd")
        )
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
