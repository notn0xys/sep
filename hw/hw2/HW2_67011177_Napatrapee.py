import sys
from PySide6.QtWidgets import *

class StoreDetails(QWidget):
    def __init__(self, go_back_callback, parent=None):
        super().__init__(parent)
        self.go_back_callback = go_back_callback
        
        self.header = QLabel("Store Details")
        self.header.setStyleSheet("font-size: 18pt; font-weight: bold;")
        
        self.name_label = QLabel()
        self.address_label = QLabel()
        self.desc_label = QLabel()        
        
        back_btn = QPushButton("Back to Creator")
        back_btn.clicked.connect(self.go_back_callback)
        
        layout = QVBoxLayout()
        layout.addWidget(self.header)
        layout.addWidget(self.name_label)
        layout.addWidget(self.address_label)
        layout.addWidget(self.desc_label)
        layout.addWidget(back_btn)
        layout.addStretch()
        self.setLayout(layout)

    def update_info(self, name, address, description, image_path):
        self.name_label.setText(f"Store Name: {name}")
        self.address_label.setText(f"Address: {address}")
        self.desc_label.setText(f"Description: {description}")

class StoreCreator(QWidget):
    def __init__(self, switch_callback, parent=None):
        super().__init__(parent)
        self.switch_callback = switch_callback
        self.image_path = None

        header = QLabel("Welcome to your new online store")
        header.setStyleSheet("font-size: 18pt; font-weight: bold;")

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter store name")
        
        self.address_input = QLineEdit()
        self.address_input.setPlaceholderText("Enter store address")
        
        self.desc_input = QTextEdit()
        self.desc_input.setPlaceholderText("Enter store description")
        self.desc_input.setMaximumHeight(100)


        create_btn = QPushButton("Create Store")
        create_btn.clicked.connect(self.on_create)

        layout = QVBoxLayout()
        layout.addWidget(header)
        layout.addWidget(QLabel("Name:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Address:"))
        layout.addWidget(self.address_input)
        layout.addWidget(QLabel("Description:"))
        layout.addWidget(self.desc_input)
        layout.addWidget(create_btn)
        layout.addStretch()

        self.setLayout(layout)

    def on_create(self):
        name = self.name_input.text().strip()
        address = self.address_input.text().strip()
        desc = self.desc_input.toPlainText().strip()
        
        if not name:
            QMessageBox.warning(self, "Validation Error", "Please enter a store name.")
            return
            
        self.switch_callback(name, address, desc, self.image_path)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Store Manager")
        self.setMinimumWidth(500)
        self.setMinimumHeight(600)
        
        self.stack = QStackedWidget()
        
        self.creator_page = StoreCreator(self.show_details)
        self.details_page = StoreDetails(self.show_creator)
        
        self.stack.addWidget(self.creator_page)
        self.stack.addWidget(self.details_page)
        
        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)
        
    def show_details(self, name, address, desc, image_path):
        self.details_page.update_info(name, address, desc, image_path)
        self.stack.setCurrentWidget(self.details_page)
        
    def show_creator(self):
        self.stack.setCurrentWidget(self.creator_page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


