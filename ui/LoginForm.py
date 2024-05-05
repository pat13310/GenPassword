from PySide6.QtWidgets import QWidget, QMainWindow
from UI_WindowLogin import Ui_WindowLogin
from util.GenPassword import GenPassword


class LoginForm(QWidget, Ui_WindowLogin):
    def __init__(self, password=""):
        super().__init__()

        # Run the setupUi method to create the GUI layout as defined in the .app file
        self.setupUi(self)
        # Here you can connect signals and slots, and set any additional properties if needed
        self.pushButton.clicked.connect(self.test_password)
        self.generator = GenPassword(password=password)

    def test_password(self):
        if self.generator.validate(self.lineEdit.text()):
            self.label.setText("Mot de passe correct!")
            self.label.setStyleSheet('color: green;background-color: white;')
            print("Mot de passe correct!")
        else:
            self.label.setText("Mot de passe incorrect!")
            self.label.setStyleSheet('color: orangered;background-color:lightgray;')
            print("Mot de passe incorrect!")


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = LoginForm()
    window.setWindowTitle("Test du Login")
    window.show()
    sys.exit(app.exec())
