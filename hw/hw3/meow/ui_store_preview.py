# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'store_preview.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_StorePreviewDialog(object):
    def setupUi(self, StorePreviewDialog):
        if not StorePreviewDialog.objectName():
            StorePreviewDialog.setObjectName(u"StorePreviewDialog")
        StorePreviewDialog.resize(317, 413)
        self.verticalLayout = QVBoxLayout(StorePreviewDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.previewName = QLabel(StorePreviewDialog)
        self.previewName.setObjectName(u"previewName")
        font = QFont()
        font.setPointSize(12)
        self.previewName.setFont(font)
        self.previewName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.previewName)

        self.imagePreview = QLabel(StorePreviewDialog)
        self.imagePreview.setObjectName(u"imagePreview")
        self.imagePreview.setMinimumSize(QSize(200, 200))
        self.imagePreview.setFrameShape(QFrame.Shape.Box)
        self.imagePreview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.imagePreview)

        self.previewDescription = QLabel(StorePreviewDialog)
        self.previewDescription.setObjectName(u"previewDescription")
        self.previewDescription.setWordWrap(True)

        self.verticalLayout.addWidget(self.previewDescription)

        self.closeButton = QPushButton(StorePreviewDialog)
        self.closeButton.setObjectName(u"closeButton")

        self.verticalLayout.addWidget(self.closeButton)


        self.retranslateUi(StorePreviewDialog)

        QMetaObject.connectSlotsByName(StorePreviewDialog)
    # setupUi

    def retranslateUi(self, StorePreviewDialog):
        StorePreviewDialog.setWindowTitle(QCoreApplication.translate("StorePreviewDialog", u"Store Preview", None))
        self.previewName.setText(QCoreApplication.translate("StorePreviewDialog", u"Store Name", None))
        self.imagePreview.setText(QCoreApplication.translate("StorePreviewDialog", u"Image Preview", None))
        self.previewDescription.setText(QCoreApplication.translate("StorePreviewDialog", u"Description", None))
        self.closeButton.setText(QCoreApplication.translate("StorePreviewDialog", u"Close", None))
    # retranslateUi

