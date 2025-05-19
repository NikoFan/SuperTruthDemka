from PySide6.QtWidgets import QMessageBox


def send_I_message(text):
    message = QMessageBox()
    message.setText(text)
    message.setIcon(QMessageBox.Icon.Information)
    message.setStandardButtons(QMessageBox.StandardButton.Yes)
    message.setWindowTitle("Мозаика")
    message.exec()

def send_W_message(text):
    message = QMessageBox()
    message.setText(text)
    message.setIcon(QMessageBox.Icon.Warning)
    message.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    message.setWindowTitle("Мозаика")
    res = message.exec()
    return res < 20_000

def send_C_message(text):
    message = QMessageBox()
    message.setText(text)
    message.setIcon(QMessageBox.Icon.Critical)
    message.setStandardButtons(QMessageBox.StandardButton.Yes)
    message.setWindowTitle("Мозаика")
    message.exec()