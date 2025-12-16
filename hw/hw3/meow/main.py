import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QDialog, QFileDialog,
    QLabel, QFrame, QVBoxLayout
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from ui_store_generator import Ui_StoreGenerator
from ui_store_preview import Ui_StorePreviewDialog
from ui_history import Ui_HistoryPage
themes = {
    "Black / White": """
        QWidget { background: white; color: black; }
    """,
    "Purple / Black": """
        QWidget { background: #1e1b2e; color: #c084fc; }
    """,
    "Blue / Light": """
        QWidget { background: #e0f2fe; color: #075985; }
    """,
    "Green / Dark": """
        QWidget { background: #052e16; color: #bbf7d0; }
    """,
    "Orange / Gray": """
        QWidget { background: #374151; color: #fb923c; }
    """
}

class StorePreview(QDialog, Ui_StorePreviewDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.closeButton.clicked.connect(self.close)
    def setdata(self, name, description, theme, image_path):
        self.previewName.setText(name)
        self.previewDescription.setText(description)
        self.setStyleSheet(themes.get(theme, ""))
        if image_path:
                    pixmap = QPixmap(image_path)
                    if not pixmap.isNull():
                        self.imagePreview.setPixmap(
                            pixmap.scaled(
                                200, 200,
                                Qt.KeepAspectRatio,
                                Qt.SmoothTransformation
                            )
                        )
class HistoryWindow(QDialog, Ui_HistoryPage):
    def __init__(self,historyData, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.populate_history(historyData)
    def populate_history(self, history_data):
            while self.historyLayout.count():
                item = self.historyLayout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()

            for entry in history_data:
                card = self.create_history_card(entry)
                self.historyLayout.addWidget(card)

            self.historyLayout.addStretch()
    def create_history_card(self, entry):
            frame = QFrame()
            frame.setFrameShape(QFrame.StyledPanel)

            layout = QVBoxLayout(frame)

            name = QLabel(f"{entry['name']}")
            desc = QLabel(entry["description"])
            theme = QLabel(f"Theme: {entry['theme']}")

            layout.addWidget(name)
            layout.addWidget(desc)
            layout.addWidget(theme)

            if entry["image"]:
                img = QLabel()
                pixmap = QPixmap(entry["image"])
                if not pixmap.isNull():
                    img.setPixmap(
                        pixmap.scaled(150, 150, Qt.KeepAspectRatio)
                    )
                    layout.addWidget(img)

            return frame


class StoreGeneratorWindow(QWidget, Ui_StoreGenerator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.history = []
        self.previewButton.clicked.connect(self.open_preview)
        self.browseImageButton.clicked.connect(self.browse_image)
        self.historyButton.clicked.connect(self.open_history)
    def browse_image(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Image",
            "",
            "Images (*.png *.jpg *.jpeg)"
        )
        if path:
            self.imagePathInput.setText(path)
    def open_preview(self):
        data = {
            "name": self.nameInput.text(),
            "description": self.descriptionInput.toPlainText(),
            "theme": self.themeCombo.currentText(),
            "image": self.imagePathInput.text()
        }

        self.history.append(data)

        dialog = StorePreview(self)
        dialog.setdata(
            data["name"],
            data["description"],
            data["theme"],
            data["image"]
        )
        dialog.exec()
    def open_history(self):
        history = HistoryWindow(self.history, self)
        history.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StoreGeneratorWindow()
    window.show()
    sys.exit(app.exec())
