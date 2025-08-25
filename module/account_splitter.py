from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel,
    QPushButton, QWidget, QVBoxLayout, QFileDialog, QMessageBox)
from PyQt6.QtCore import Qt,QSize
import os
import csv
import tempfile
import shutil

class AccountSplitter(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #list init
        self.mandiri_list: list = []
        self.bsi_list: list = []
        
        # window init
        self.setWindowTitle('Account Splitter')
        self.setFixedSize(QSize(323,230))
        
        # widget init
        self.label_file_name = QLabel('Belum Ada File Terpilih', self)
        self.label_file_name.setStyleSheet('font-style: italic; color: yellow')
        self.button_file_chooser = QPushButton('Pilih File', self)
        self.button_process_data = QPushButton('Proses Data',self)
        self.copyright_label = QLabel('© 2025 Husni',self)
        
        #layout setting
        layout = QVBoxLayout()
        layout.setContentsMargins(10,10,10,10)
        layout.addWidget(self.label_file_name,1, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.button_file_chooser,1)
        layout.addWidget(self.button_process_data,1)
        layout.addWidget(self.copyright_label,0, Qt.AlignmentFlag.AlignCenter)
        
        #container setting
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        
        # Widget Signal
        self.button_file_chooser.clicked.connect(self.file_chooser_handler)
        self.button_process_data.clicked.connect(self.split_data_handler)
    
    # functions
    def file_chooser_handler(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open CSV File', filter='CSV File (*.csv)')
        self.label_file_name.setText(file_path)
        self.label_file_name.setStyleSheet('font-style: italic; color: green')
    
    def split_data_handler(self):
        try:
            self.fullpath_filename: str = self.label_file_name.text()
            self.base_name: str = os.path.basename(self.fullpath_filename)
            self.filename, self.fileextension = os.path.splitext(self.base_name)
            
            self.mandiri_filename: str = f'{self.filename}_MANDIRI{self.fileextension}'
            self.bsi_filename: str = f'{self.filename}_BSI{self.fileextension}'
            
            self.splitting_data()
            self.writing_split_data()
            self.ordering_csv_number()
            QMessageBox.information(self,'Sukses','File Telah Diproses')
        
        except FileNotFoundError:
            QMessageBox.warning(self,'Error', 'File Belum Dipilih')
    
    def splitting_data(self):
        with open(f'{self.fullpath_filename}', 'r', encoding='utf8') as csv_reader:
            reader = csv.DictReader(csv_reader, delimiter='|')
            next(reader)
            for data in reader:
                # check if length of "NO_REKENING" is greater than 10
                if len(data['NO_REKENING']) > 10:
                    self.mandiri_list.append(data)
                else:
                    self.bsi_list.append(data)
        
    def writing_split_data(self):
        self.csv_header: list = [
            'NO', #0
            'NAMA_SUPPLIER',#1
            'NAMA_PEMILIK_REKENING',#2
            'NO_REKENING',#3
            'JUMLAH_UANG']#4
        
        #write mandiri data to csv file
        with open(self.mandiri_filename, 'w', encoding='utf8', newline='') as mandiri_writer:
            writer_mandiri = csv.DictWriter(mandiri_writer, delimiter='|', fieldnames=self.csv_header)
            writer_mandiri.writeheader()
            writer_mandiri.writerows(self.mandiri_list)
        
        # write BSI data to csv file
        with open(self.bsi_filename, 'w', encoding='utf8', newline='') as bsi_writer:
            writer_bsi = csv.DictWriter(bsi_writer, delimiter='|', fieldnames=self.csv_header)
            writer_bsi.writeheader()
            writer_bsi.writerows(self.bsi_list)
    
    def ordering_csv_number(self):
        # oredering MANDIRI number
        with open(self.mandiri_filename, 'r', encoding='utf8') as mandiri_reader, \
            tempfile.NamedTemporaryFile(mode='w+t', delete=False, encoding='utf8', newline='') as mandiri_temp_writer:
                m_reader = csv.reader(mandiri_reader, delimiter='|')
                m_writer = csv.writer(mandiri_temp_writer, delimiter='|')
                next(m_reader)
                m_writer.writerow(self.csv_header)
                for mandiri_index_number, mandiri_data in enumerate(m_reader, start=1):
                    m_writer.writerow([mandiri_index_number, *mandiri_data[1:5]]) # write to temp file
        
        # replace temp file to original file
        shutil.move(mandiri_temp_writer.name, self.mandiri_filename)
        
        # ordering BSI Number
        with open(self.bsi_filename, 'r', encoding='utf8') as bsi_reader, \
            tempfile.NamedTemporaryFile(mode='w+t', delete=False, encoding='utf8', newline='') as bsi_temp_writer:
                b_reader = csv.reader(bsi_reader, delimiter='|')
                b_writer = csv.writer(bsi_temp_writer, delimiter='|')
                next(b_reader)
                b_writer.writerow(self.csv_header)
                for bsi_index_number, bsi_data in enumerate(b_reader, start=1):
                    b_writer.writerow([bsi_index_number, *bsi_data[1:5]])
        
        shutil.move(bsi_temp_writer.name, self.bsi_filename)
        
if __name__ == '__main__':
    app = QApplication([])
    window = AccountSplitter()
    window.show()
    app.exec()