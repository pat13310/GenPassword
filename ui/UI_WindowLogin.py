# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginnDxYiG.app'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QVBoxLayout)


class Ui_WindowLogin(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(348, 125)
        Form.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.944772, y2:0.892, stop:0 rgba(30, 0, 89, 255), stop:0.483254 rgba(133, 94, 255, 255), stop:1 rgba(255, 170, 255, 255))")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: white;\n"
                                    "border: 1px solid rgb(85, 0, 255);\n"
                                    "border-radius:  4px;\n"
                                    "padding:2px;")

        self.verticalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(200, 0))
        self.pushButton.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton.setBaseSize(QSize(0, 0))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
                                      "	background-color: rgb(170, 170, 255);\n"
                                      "	border: 1px solid rgb(85, 0, 255);\n"
                                      "	\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::hover{\n"
                                      "	background-color: rgb(85, 0, 255);\n"
                                      "	border: 1px solid rgb(85, 0, 255);\n"
                                      "	color:white;\n"
                                      "	\n"
                                      "}")
        self.pushButton.setFlat(False)

        self.verticalLayout.addWidget(self.pushButton)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: gray;\n"
                                 "border: 1px solid rgb(85, 0, 127);\n"
                                 "border-radius: 4px;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.label.setText("")
    # retranslateUi

