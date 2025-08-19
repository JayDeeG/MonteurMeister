from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
)
from PySide6.QtGui import QFont
import sys


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MonteurMeister - Login")
        self.setFixedSize(300, 200)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Willkommen bei MonteurMeister")
        self.label.setFont(QFont("Roboto", 12))
        layout.addWidget(self.label)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Benutzername")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Passwort")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.check_login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "admin" and password == "passwort":
            QMessageBox.information(self, "Login erfolgreich", "Willkommen, Admin!")
            self.close()
            # Hier später das Dashboard starten
        else:
            QMessageBox.warning(self, "Login fehlgeschlagen", "Falsche Zugangsdaten!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
