from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt,QSize

class AccountSplitter(QMainWindow):
    def __init__(self):
        super().__init__()
        # window init
        self.setWindowTitle('Account Splitter')
        self.setFixedSize(QSize(323,230))
        
        # widget init
        self.label_file_name = QLabel('Belum Ada File Terpilih', self)
        self.label_file_name.setStyleSheet('font-style: italic; color: red')
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
        
if __name__ == '__main__':
    app = QApplication([])
    window = AccountSplitter()
    window.show()
    app.exec()