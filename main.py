from PyQt6.QtWidgets import QTabWidget, QApplication, QMainWindow,QVBoxLayout, QWidget
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from module.account_splitter import AccountSplitter
from module.nominal_changer import NominalChanger

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        version_number = 'v1.0.0'
        self.setWindowIcon(QIcon('./icon/modifier.png'))
        self.setWindowTitle(f'CSV Bulanan Modifier_{version_number}')
        self.setFixedSize(QSize(357,300))
        self.setContentsMargins(6,6,6,6)
        
        self.account_splitter = AccountSplitter()
        self.nominal_changer = NominalChanger()
        
        tab_widget = QTabWidget(self)
        tab_widget.addTab(self.nominal_changer,QIcon('./icon/change.png'),'Nominal Changer')
        tab_widget.addTab(self.account_splitter,QIcon('./icon/split.png'),'Account Splitter')
        
        layout = QVBoxLayout()
        layout.addWidget(tab_widget)
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()