# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from advertiser import form_advertiser

class Main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("form.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formUtama = loader.load(ui_file, self)
        ui_file.close()

        if hasattr(self.formUtama, "menuBar"):
            self.setMenuBar(self.formUtama.menuBar())

        self.setCentralWidget(self.formUtama)
        self.resize(self.formUtama.size())

        self.formUtama.actionAdvertiser.triggered.connect(self.bukaAdvertiser)
        self.formUtama.actionIklan.triggered.connect(self.bukaIklan)
        self.formUtama.actionPenyiaran.triggered.connect(self.bukaPenyiaran)
        self.formUtama.actionBiaya_Iklan.triggered.connect(self.bukaBiayaIklan)


    def bukaAdvertiser(self):
        from advertiser import form_advertiser
        self.buka = form_advertiser()
        self.buka.show()

    def bukaIklan(self):
        from iklan import form_iklan
        self.buka = form_iklan()
        self.buka.show()

    def bukaPenyiaran(self):
        from penyiaran import FormPenyiaran
        self.buka = FormPenyiaran()
        self.buka.show()

    def bukaBiayaIklan(self):
        from biayaiklan import Form_BiayaIklan
        self.buka = Form_BiayaIklan()
        self.buka.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
