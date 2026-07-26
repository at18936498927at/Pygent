# -*- coding: utf-8 -*-
# type: ignore
################################################################################
## Form generated from reading UI file 'pyside6.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QTextBrowser,
    QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        self.messageEdit = QTextEdit(Form)
        self.messageEdit.setObjectName(u"messageEdit")
        self.messageEdit.setGeometry(QRect(210, 510, 371, 81))
        self.messageEdit.setStyleSheet(u"QTextEdit{\n"
"background: white;\n"
"border: 1px black;\n"
"border-radius: 10px;\n"
"}")
        self.sendButton = QPushButton(Form)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setGeometry(QRect(600, 560, 24, 24))
        self.sendButton.setStyleSheet(u"QPushButton{\n"
"background: white;\n"
"border: 1px black;\n"
"border-radius: 12px;\n"
"}")
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(0, 0, 801, 501))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Agent", None))
        self.messageEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Enter text...", None))
        self.sendButton.setText("")
    # retranslateUi


