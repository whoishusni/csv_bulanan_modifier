from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QWidget,
    QGridLayout, QLabel, QLineEdit, QMessageBox,QFileDialog)
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIntValidator
import csv
from urllib.parse import urlparse
import os

class NominalChanger(QMainWindow):
    def __init__(self):
        super().__init__()
        # Main Window
        self.setWindowTitle('Nominal Modifier')
        self.setFixedSize(QSize(323,230))
        
        # Initialize Widget
        self.label_file_location = QLabel('Lokasi File CSV',self)
        self.label_choosed_file = QLabel('Belum Ada File Dipilih',self)
        self.label_choosed_file.setStyleSheet("font-style: italic; color: yellow;")
        
        self.button_file_dialog = QPushButton('Pilih File',self)
        
        self.label_first_nominal = QLabel('Nominal Awal',self)
        self.edit_first_nominal = QLineEdit(self)
        self.edit_first_nominal.setPlaceholderText('Hanya Input Angka...')
        self.edit_first_nominal.setValidator(QIntValidator())
        
        self.label_last_nominal = QLabel('Nominal Akhir',self)
        self.edit_last_nominal = QLineEdit(self)
        self.edit_last_nominal.setPlaceholderText('Hanya Input Angka...')
        self.edit_last_nominal.setValidator(QIntValidator())
        
        self.button_process = QPushButton('Proses Data',self)
        
        self.copyright_label = QLabel('© 2025 Husni',self)
        
        # Layout Setting
        layout = QGridLayout()
        layout.setContentsMargins(10,10,10,10)
        layout.setVerticalSpacing(8)
        
        layout.addWidget(self.label_file_location, 0, 0, 1,2)
        layout.addWidget(self.label_choosed_file, 1, 0)
        layout.addWidget(self.button_file_dialog, 1, 1)

        layout.addWidget(self.label_first_nominal, 2, 0, 1, 2)
        layout.addWidget(self.edit_first_nominal, 3, 0, 1, 2)

        layout.addWidget(self.label_last_nominal, 4, 0, 1, 2)
        layout.addWidget(self.edit_last_nominal, 5, 0, 1, 2)
        
        layout.addWidget(self.button_process,6,0,1,2)
        layout.addWidget(self.copyright_label,7,0,1,2, Qt.AlignmentFlag.AlignCenter)
        
        # Container Setting
        container = QWidget(self)
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        
        # Widget Signal / Slot / Event
        self.button_file_dialog.clicked.connect(self.file_handler)
        self.button_process.clicked.connect(self.process_file)
    
    # Functions
        
    def file_handler(self):
        file_name, _ = QFileDialog.getOpenFileName(self,caption='Open CSV File',filter="CSV Files (*.csv)")
        self.label_choosed_file.setText(file_name)
        
    def process_file(self):
        self.nominal_update_list: list = []
        self.raw_file_name = self.label_choosed_file.text()
        self.first_nominal = self.edit_first_nominal.text().strip()
        self.last_nominal = self.edit_last_nominal.text().strip()
        base_name = os.path.basename(self.raw_file_name)
        self.file_name, self.file_extension = os.path.splitext(base_name)
        self.saved_file_name = f'{self.file_name}_MODIFIED{self.file_extension}'
        
        if self.first_nominal == '' and self.last_nominal == '':
            QMessageBox.warning(self, 'Error', 'Nominal Awal / Nominal Akhir Kosong')
            return
        
        else: 
            try:
                self.writing_file()
                    
            except FileNotFoundError:
                QMessageBox.warning(self, 'Error', 'File Belum Dipilih')
    
    def writing_file(self):
        csv_header = [
                        'NO',
                        'NAMA_SUPPLIER',
                        'NAMA_PEMILIK_REKENING',
                        'NO_REKENING',
                        'JUMLAH_UANG']
                
        with open(self.raw_file_name, 'r', encoding='utf8') as csv_reader:
            reader = csv.DictReader(csv_reader, delimiter='|')
            for data in reader:
                if data['JUMLAH_UANG'] == self.first_nominal:
                    data['JUMLAH_UANG'] = self.last_nominal
                self.nominal_update_list.append(data)
        
        with open(self.saved_file_name, 'w', encoding='utf8', newline='') as csv_writer:
            writer = csv.DictWriter(csv_writer, delimiter='|', fieldnames=csv_header)
            writer.writeheader()
            writer.writerows(self.nominal_update_list)
            
            QMessageBox.information(self, 'Sukses', 'File Sudah Diproses')
    
    def ordering_number(self):
        ...
        
if __name__ == '__main__':
    app = QApplication([])
    window = NominalChanger()
    window.show()
    app.exec() 