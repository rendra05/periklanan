import mysql.connector
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class FormPenyiaran(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Load UI
        ui_file = QFile("formPenyiaran.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.form = loader.load(ui_file, self)
        ui_file.close()

        self.setLayout(self.form.layout())
        self.setWindowTitle("Form Penyiaran")

        # Koneksi ke database MySQL
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # ubah jika ada password
            database="periklanan"
        )
        self.cursor = self.db.cursor()

        # Cari semua widget input (case-insensitive)
        self._find_widgets()

        # Hubungkan tombol
        self.form.simpanButton.clicked.connect(self.simpan_data)
        self.form.ubahButton.clicked.connect(self.ubah_data)
        self.form.hapusButton.clicked.connect(self.hapus_data)

        # Hubungkan event klik tabel untuk mengisi form
        self.form.tableWidget.cellClicked.connect(self.isi_form_dari_tabel)

        # Tampilkan data awal
        self.tampilkan_data()

    def _find_widgets(self):
        """Mencari widget dengan berbagai kemungkinan nama"""
        # Kemungkinan nama untuk setiap field (sesuai dengan file .ui)
        widget_mappings = {
            'id_siar': ['iDSiarLineEdit', 'idSiarLineEdit', 'idSiaran', 'lineEdit_idSiar'],
            'kd_iklan': ['kodeIklanLineEdit', 'kdIklan', 'lineEdit_kdIklan'],
            'produk': ['produkLineEdit', 'lineEdit_produk'],
            'periode': ['periodeLineEdit', 'lineEdit_periode'],
            'air_time': ['airTimeLineEdit', 'lineEdit_airTime'],
            'tgl_mulai': ['tglMulaiLineEdit', 'lineEdit_tglMulai'],
            'tgl_selesai': ['tglSelesaiLineEdit', 'lineEdit_tglSelesai']
        }

        # Cari widget yang sebenarnya ada
        self.widgets = {}
        for field, possible_names in widget_mappings.items():
            widget = None
            for name in possible_names:
                if hasattr(self.form, name):
                    widget = getattr(self.form, name)
                    break

            if widget is None:
                QMessageBox.warning(self, "Peringatan",
                    f"Widget untuk field '{field}' tidak ditemukan!\n"
                    f"Nama yang dicoba: {', '.join(possible_names)}\n\n"
                    f"Periksa nama widget di Qt Designer.")

            self.widgets[field] = widget

    def tampilkan_data(self):
        try:
            self.cursor.execute("SELECT * FROM penyiaran")
            hasil = self.cursor.fetchall()
            self.form.tableWidget.setRowCount(0)
            for row_num, row_data in enumerate(hasil):
                self.form.tableWidget.insertRow(row_num)
                for col_num, data in enumerate(row_data):
                    self.form.tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(data)))
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def isi_form_dari_tabel(self, row, col):
        """Mengisi form ketika user klik pada baris tabel"""
        try:
            fields = ['id_siar', 'kd_iklan', 'produk', 'periode', 'air_time', 'tgl_mulai', 'tgl_selesai']
            for i, field in enumerate(fields):
                widget = self.widgets.get(field)
                if widget and self.form.tableWidget.item(row, i):
                    widget.setText(self.form.tableWidget.item(row, i).text())
        except Exception as e:
            QMessageBox.warning(self, "Peringatan", f"Error saat mengisi form: {str(e)}")

    def simpan_data(self):
        try:
            # Ambil nilai dari widget
            id_siar = self.widgets['id_siar'].text() if self.widgets.get('id_siar') else ''
            kd_iklan = self.widgets['kd_iklan'].text() if self.widgets.get('kd_iklan') else ''
            produk = self.widgets['produk'].text() if self.widgets.get('produk') else ''
            periode = self.widgets['periode'].text() if self.widgets.get('periode') else ''
            air_time = self.widgets['air_time'].text() if self.widgets.get('air_time') else ''
            tgl_mulai = self.widgets['tgl_mulai'].text() if self.widgets.get('tgl_mulai') else ''
            tgl_selesai = self.widgets['tgl_selesai'].text() if self.widgets.get('tgl_selesai') else ''

            # Validasi input tidak boleh kosong
            if not id_siar:
                QMessageBox.warning(self, "Peringatan", "ID Siar tidak boleh kosong")
                return

            sql = ("INSERT INTO penyiaran (id_siar, kd_iklan, produk, periode, air_time, tgl_mulai, tgl_selesai) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s)")
            val = (id_siar, kd_iklan, produk, periode, air_time, tgl_mulai, tgl_selesai)

            self.cursor.execute(sql, val)
            self.db.commit()
            QMessageBox.information(self, "Sukses", "Data berhasil disimpan")
            self.tampilkan_data()
            self.kosongkan_form()
        except mysql.connector.IntegrityError as e:
            QMessageBox.critical(self, "Error", f"ID Siar sudah ada atau terjadi kesalahan: {str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def ubah_data(self):
        # Ambil ID Siar
        id_siar = self.widgets['id_siar'].text() if self.widgets.get('id_siar') else ''

        # Validasi: pastikan ada data yang dipilih atau ID Siar diisi
        if not id_siar:
            QMessageBox.warning(self, "Peringatan", "Pilih data dari tabel atau isi ID Siar yang ingin diubah")
            return

        try:
            # Cek apakah data dengan id_siar tersebut ada
            self.cursor.execute("SELECT * FROM penyiaran WHERE id_siar=%s", (id_siar,))
            if not self.cursor.fetchone():
                QMessageBox.warning(self, "Peringatan", f"Data dengan ID Siar '{id_siar}' tidak ditemukan")
                return

            # Ambil nilai dari widget
            kd_iklan = self.widgets['kd_iklan'].text() if self.widgets.get('kd_iklan') else ''
            produk = self.widgets['produk'].text() if self.widgets.get('produk') else ''
            periode = self.widgets['periode'].text() if self.widgets.get('periode') else ''
            air_time = self.widgets['air_time'].text() if self.widgets.get('air_time') else ''
            tgl_mulai = self.widgets['tgl_mulai'].text() if self.widgets.get('tgl_mulai') else ''
            tgl_selesai = self.widgets['tgl_selesai'].text() if self.widgets.get('tgl_selesai') else ''

            sql = ("UPDATE penyiaran SET kd_iklan=%s, produk=%s, periode=%s, air_time=%s, "
                   "tgl_mulai=%s, tgl_selesai=%s WHERE id_siar=%s")
            val = (kd_iklan, produk, periode, air_time, tgl_mulai, tgl_selesai, id_siar)

            self.cursor.execute(sql, val)
            self.db.commit()
            QMessageBox.information(self, "Sukses", "Data berhasil diubah")
            self.tampilkan_data()
            self.kosongkan_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def hapus_data(self):
        # Ambil ID Siar
        id_siar = self.widgets['id_siar'].text() if self.widgets.get('id_siar') else ''

        # Validasi: pastikan ada data yang dipilih atau ID Siar diisi
        if not id_siar:
            QMessageBox.warning(self, "Peringatan", "Pilih data dari tabel atau isi ID Siar yang ingin dihapus")
            return

        try:
            # Konfirmasi sebelum menghapus
            reply = QMessageBox.question(
                self,
                "Konfirmasi",
                f"Apakah Anda yakin ingin menghapus data dengan ID Siar '{id_siar}'?",
                QMessageBox.Yes | QMessageBox.No
            )

            if reply == QMessageBox.No:
                return

            self.cursor.execute("DELETE FROM penyiaran WHERE id_siar=%s", (id_siar,))

            if self.cursor.rowcount == 0:
                QMessageBox.warning(self, "Peringatan", f"Data dengan ID Siar '{id_siar}' tidak ditemukan")
                return

            self.db.commit()
            QMessageBox.information(self, "Sukses", "Data berhasil dihapus")
            self.tampilkan_data()
            self.kosongkan_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def kosongkan_form(self):
        for widget in self.widgets.values():
            if widget:
                widget.clear()

    def closeEvent(self, event):
        """Tutup koneksi database saat form ditutup"""
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if hasattr(self, 'db') and self.db:
            self.db.close()
        event.accept()
