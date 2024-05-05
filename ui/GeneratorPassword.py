import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton

from Ui_GeneratorPassword import Ui_GeneratorPassword  # Replace with the correct module name
from util.GenPassword import GenPassword, EncryptionMethod


class GeneratorPassword(QWidget, Ui_GeneratorPassword):
    def __init__(self):
        super().__init__()

        # Run the setupUi method to create the GUI layout as defined in the .app file
        self.setupUi(self)
        self.pushButton.clicked.connect(self.encrypt_password)
        self.pushButton_2.clicked.connect(self.auto_generate)
        self.spinBox.setMinimum(8)
        self.spinBox.setMaximum(32)
        self.spinBox.valueChanged.connect(self.update_length)
        self.generator = GenPassword()

        self.bouton_copier = QPushButton(self.label)
        self.bouton_copier.setMinimumSize(QSize(25, 24))
        self.bouton_copier.setMaximumSize(QSize(25, 24))
        self.bouton_copier.setText('C')
        self.bouton_copier.clicked.connect(self.copier_texte)
        self.bouton_copier.setStyleSheet("QPushButton { border-radius:4px; border: 1px solid rgb(170, 170, 255);}  QPushButton:hover { background-color:  rgb(80, 80, 255);color:white; }")
        self.bouton_copier.move(550 - 20, 10)
        self.bouton_copier.raise_()
        self.bouton_copier.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

    def copier_texte(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.generator.get_password(True))
    def encrypt_password(self):
        method = self.comboBox.currentText().upper()
        password = self.lineEdit.text()
        self.label.setText("")
        if len(password) == 0:
            QMessageBox.information(self, 'Mot de Passe absent', 'Veuillez entrer un mot de passe.')
            self.lineEdit.setFocus()
            return

        if len(password) != self.generator.get_length():
            QMessageBox.information(self, 'Mot de Passe incorrect', 'Veuillez définir la bonne longueur du mot de '
                                                                    'passe.')
            self.lineEdit.setFocus()
            return

        self.generator.set_password(self.lineEdit.text())
        if method == "SHA256":
            self.generator.encrypt(EncryptionMethod.SHA256)
        elif method == "SHA1":
            self.generator.encrypt(EncryptionMethod.SHA1)
        elif method == "MD5":
            self.generator.encrypt(EncryptionMethod.MD5)
        elif method == "BCRYPT":
            self.generator.encrypt(EncryptionMethod.BCRYPT)
        elif method == "NORMAL":
            self.generator.encrypt(EncryptionMethod.NOCRYPT)

        # Perform encryption based on selected_method and password_to_encrypt
        # Update self.ui.label or any other UI elements as needed
        self.label.setText(str(self.generator.get_password(True)))

    def auto_generate(self):
        # For example, generate a password and set it in the line edit
        self.lineEdit.setText(self.generator.generate())

    def update_length(self):
        self.generator.set_length(self.spinBox.value())


# Running the application
if __name__ == '__main__':
    app = QApplication([])
    window = GeneratorPassword()
    window.show()
    sys.exit(app.exec())
