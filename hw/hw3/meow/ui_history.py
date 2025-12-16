# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_HistoryPage(object):
    def setupUi(self, HistoryPage):
        if not HistoryPage.objectName():
            HistoryPage.setObjectName(u"HistoryPage")
        HistoryPage.resize(381, 320)
        self.mainLayout = QVBoxLayout(HistoryPage)
        self.mainLayout.setSpacing(8)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(8, 8, 8, 8)
        self.titleLabel = QLabel(HistoryPage)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.mainLayout.addWidget(self.titleLabel)

        self.scrollArea = QScrollArea(HistoryPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollWidget = QWidget()
        self.scrollWidget.setObjectName(u"scrollWidget")
        self.scrollWidget.setGeometry(QRect(0, 0, 363, 270))
        self.historyLayout = QVBoxLayout(self.scrollWidget)
        self.historyLayout.setSpacing(6)
        self.historyLayout.setObjectName(u"historyLayout")
        self.historyLayout.setContentsMargins(4, 4, 4, 4)
        self.spacerItem = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.historyLayout.addItem(self.spacerItem)

        self.scrollArea.setWidget(self.scrollWidget)

        self.mainLayout.addWidget(self.scrollArea)


        self.retranslateUi(HistoryPage)

        QMetaObject.connectSlotsByName(HistoryPage)
    # setupUi

    def retranslateUi(self, HistoryPage):
        HistoryPage.setWindowTitle(QCoreApplication.translate("HistoryPage", u"History", None))
        self.titleLabel.setStyleSheet(QCoreApplication.translate("HistoryPage", u"font-size: 18px; font-weight: bold;", None))
        self.titleLabel.setText(QCoreApplication.translate("HistoryPage", u"History Container", None))
    # retranslateUi

