from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt,QSize

class AccountSplitter(QMainWindow):
    def __init__(self):
        super().__init__()
        # window init
        self.setWindowTitle('Account Splitter')
        self.setFixedSize(QSize(270,123))
        
        # widget init
        self.label_file_name = QLabel('Belum Ada File Terpilih')
        self.label_file_name.setStyleSheet('font-style: italic; color: red')
        self.button_file_chooser = QPushButton('Pilih File')
        self.button_process_data = QPushButton('Process Data')
        
        #layout setting
        layout = QVBoxLayout()
        layout.addWidget(self.label_file_name,1, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.button_file_chooser,1)
        layout.addWidget(self.button_process_data,1)
        
        #container setting
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)

if __name__ == '__main__':
    app = QApplication([])
    window = AccountSplitter()
    window.show()
    app.exec()