# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generatorpwdGAVYXt.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_GeneratorPassword(object):
    def setupUi(self, GeneratorPassword):
        if not GeneratorPassword.objectName():
            GeneratorPassword.setObjectName(u"GeneratorPassword")
        GeneratorPassword.resize(600, 300)
        self.verticalLayout = QVBoxLayout(GeneratorPassword)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(GeneratorPassword)
        self.lineEdit.setObjectName(u"lineEdit")
        font = QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"background-color: white;\n"
"border: 1px solid rgb(85, 0, 255);\n"
"border-radius:  4px;\n"
"padding:4px;")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_2 = QPushButton(GeneratorPassword)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(50, 28))
        self.pushButton_2.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_2.setBaseSize(QSize(0, 0))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_2.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(GeneratorPassword)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(100, 0))
        self.label_2.setMaximumSize(QSize(200, 16777215))
        font1 = QFont()
        font1.setPointSize(11)
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.spinBox = QSpinBox(GeneratorPassword)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMinimumSize(QSize(0, 32))
        self.spinBox.setStyleSheet(u"background-color: white;\n"
"")

        self.horizontalLayout_2.addWidget(self.spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.comboBox = QComboBox(GeneratorPassword)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 32))
        self.comboBox.setStyleSheet(u"background-color: white;\n"
"border: 1px solid rgb(85, 0, 255);\n"
"border-radius:  4px;\n"
"")

        self.verticalLayout.addWidget(self.comboBox)

        self.pushButton = QPushButton(GeneratorPassword)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(200, 45))
        self.pushButton.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton.setBaseSize(QSize(0, 0))
        self.pushButton.setFont(font1)
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

        self.label = QLineEdit(GeneratorPassword)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: transparent;\n"
"border: 1px solid rgb(85, 0, 127);\n"
"border-radius: 4px;\n"
"padding : 24px 0;\n"
"\n"
"color: rgb(85, 0, 255);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(GeneratorPassword)

        QMetaObject.connectSlotsByName(GeneratorPassword)
    # setupUi

    def retranslateUi(self, GeneratorPassword):
        GeneratorPassword.setWindowTitle(QCoreApplication.translate("GeneratorPassword", u"G\u00e9n\u00e9rateur de mots de passe", None))
        self.pushButton_2.setText(QCoreApplication.translate("GeneratorPassword", u"Auto", None))
        self.label_2.setText(QCoreApplication.translate("GeneratorPassword", u"Longueur du mot de passe :", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("GeneratorPassword", u"NORMAL", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("GeneratorPassword", u"MD5", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("GeneratorPassword", u"SHA1", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("GeneratorPassword", u"SHA256", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("GeneratorPassword", u"BCRYPT", None))

        self.pushButton.setText(QCoreApplication.translate("GeneratorPassword", u"Encrypter", None))
    # retranslateUi

