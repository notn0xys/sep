# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'store_generator.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_StoreGenerator(object):
    def setupUi(self, StoreGenerator):
        if not StoreGenerator.objectName():
            StoreGenerator.setObjectName(u"StoreGenerator")
        StoreGenerator.resize(363, 448)
        self.verticalLayout = QVBoxLayout(StoreGenerator)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(StoreGenerator)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Segoe UI Historic"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.nameInput = QLineEdit(StoreGenerator)
        self.nameInput.setObjectName(u"nameInput")

        self.verticalLayout.addWidget(self.nameInput)

        self.descriptionInput = QTextEdit(StoreGenerator)
        self.descriptionInput.setObjectName(u"descriptionInput")

        self.verticalLayout.addWidget(self.descriptionInput)

        self.themeCombo = QComboBox(StoreGenerator)
        self.themeCombo.addItem("")
        self.themeCombo.addItem("")
        self.themeCombo.addItem("")
        self.themeCombo.addItem("")
        self.themeCombo.addItem("")
        self.themeCombo.setObjectName(u"themeCombo")

        self.verticalLayout.addWidget(self.themeCombo)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.imagePathInput = QLineEdit(StoreGenerator)
        self.imagePathInput.setObjectName(u"imagePathInput")

        self.hboxLayout.addWidget(self.imagePathInput)

        self.browseImageButton = QPushButton(StoreGenerator)
        self.browseImageButton.setObjectName(u"browseImageButton")

        self.hboxLayout.addWidget(self.browseImageButton)


        self.verticalLayout.addLayout(self.hboxLayout)

        self.historyButton = QPushButton(StoreGenerator)
        self.historyButton.setObjectName(u"historyButton")

        self.verticalLayout.addWidget(self.historyButton)

        self.previewButton = QPushButton(StoreGenerator)
        self.previewButton.setObjectName(u"previewButton")

        self.verticalLayout.addWidget(self.previewButton)


        self.retranslateUi(StoreGenerator)

        QMetaObject.connectSlotsByName(StoreGenerator)
    # setupUi

    def retranslateUi(self, StoreGenerator):
        StoreGenerator.setWindowTitle(QCoreApplication.translate("StoreGenerator", u"Store Generator", None))
        self.label.setText(QCoreApplication.translate("StoreGenerator", u"Store Generator", None))
        self.nameInput.setPlaceholderText(QCoreApplication.translate("StoreGenerator", u"Store Name", None))
        self.descriptionInput.setPlaceholderText(QCoreApplication.translate("StoreGenerator", u"Store Description", None))
        self.themeCombo.setItemText(0, QCoreApplication.translate("StoreGenerator", u"Black / White", None))
        self.themeCombo.setItemText(1, QCoreApplication.translate("StoreGenerator", u"Purple / Black", None))
        self.themeCombo.setItemText(2, QCoreApplication.translate("StoreGenerator", u"Blue / Light", None))
        self.themeCombo.setItemText(3, QCoreApplication.translate("StoreGenerator", u"Green / Dark", None))
        self.themeCombo.setItemText(4, QCoreApplication.translate("StoreGenerator", u"Orange / Gray", None))

        self.imagePathInput.setPlaceholderText(QCoreApplication.translate("StoreGenerator", u"Image path...", None))
        self.browseImageButton.setText(QCoreApplication.translate("StoreGenerator", u"Browse", None))
        self.historyButton.setText(QCoreApplication.translate("StoreGenerator", u"History", None))
        self.previewButton.setText(QCoreApplication.translate("StoreGenerator", u"Preview Store", None))
    # retranslateUi

