from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QWidget,
    QGridLayout, QLabel, QLineEdit, QMessageBox,QFileDialog)
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIntValidator
import csv
import os

class NominalChanger(QMainWindow):
    def __init__(self):
        super().__init__()
        # Main Window
        self.setWindowTitle('Nominal Modifier')
        self.setFixedSize(QSize(323,230))
        
        # Initialize Widget
        self.label_file_location = QLabel('Lokasi File CSV',self)
        self.label_choosed_file = QLabel('Belum Ada File Terpilih',self)
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
        self.button_process.clicked.connect(self.process_change_handler)
    
    # Functions
    def file_handler(self):
        file_path, _ = QFileDialog.getOpenFileName(self,caption='Open CSV File',filter="CSV Files (*.csv)")
        self.label_choosed_file.setText(file_path)
        
    def process_change_handler(self):
        self.nominal_update_list: list = []
        self.fullpath_filename: str = self.label_choosed_file.text()
        self.first_nominal: str = self.edit_first_nominal.text().strip()
        self.last_nominal: str = self.edit_last_nominal.text().strip()
        base_name: str = os.path.basename(self.fullpath_filename)
        self.file_name, self.file_extension = os.path.splitext(base_name)
        self.saved_file_name: str = f'{self.file_name}_MODIFIED{self.file_extension}'
        
        if self.first_nominal == '' and self.last_nominal == '':
            QMessageBox.warning(self, 'Error', 'Nominal Awal / Nominal Akhir Kosong')
            return
        
        else: 
            try:
                self.reading_file()
                self.writing_file()
                    
            except FileNotFoundError:
                QMessageBox.warning(self, 'Error', 'File Belum Dipilih')
    
    def reading_file(self):
        # open and read choosen file
        with open(self.fullpath_filename, 'r', encoding='utf8') as csv_reader:
            reader = csv.DictReader(csv_reader, delimiter='|')
            for index, data in enumerate(reader, start=1):
                if data:
                    # replace number
                    if data['JUMLAH_UANG'] == self.first_nominal:
                        data['JUMLAH_UANG'] = self.last_nominal
                    data['NO'] = index
                    # save file to list
                    self.nominal_update_list.append(data)

    def writing_file(self):
        csv_header: list = [
            'NO',
            'NAMA_SUPPLIER',
            'NAMA_PEMILIK_REKENING',
            'NO_REKENING',
            'JUMLAH_UANG']
          
        with open(self.saved_file_name, 'w', encoding='utf8', newline='') as csv_writer:
            writer = csv.DictWriter(csv_writer, delimiter='|', fieldnames=csv_header)
            writer.writeheader()
            writer.writerows(self.nominal_update_list)
            QMessageBox.information(self, 'Sukses', 'File Sudah Diproses')
        
if __name__ == '__main__':
    app = QApplication([])
    window = NominalChanger()
    window.show()
    app.exec() 