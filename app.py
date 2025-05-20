from PySide6.QtWidgets import (QMainWindow,
                               QApplication, QStackedWidget)

import sys
from DATABASE.Database import Database

from Messages import send_W_message


from Material import Material
from FRAMES import MaterialsShow

class MainClass(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Мозаика")
        self.resize(900, 800)
        self.db = Database()

        frame = MaterialsShow.ShowMaterialsClass(self)

        self.navigator = QStackedWidget()
        self.navigator.addWidget(frame)

        self.setCentralWidget(self.navigator)

    def switch_window(self, frame, material_name=None):
        """ Переход между окнами """
        Material().set_material(material_name)
        goal_frame = frame(self)
        self.navigator.removeWidget(goal_frame)
        self.navigator.addWidget(goal_frame)
        self.navigator.setCurrentWidget(goal_frame)

    def closeEvent(self, event, /):
        if send_W_message("Вы точно хотите закрыть приложение?"):
            event.accept()
        else:
            event.ignore()


styles = """
QComboBox {
color: black;
}


QLabel {
font-size: 20px;
padding-left: 6px;
}

#Title {

font-size: 30px;
font-weight: bold;
qproperty-alignment: AlignCenter;
}

#card {
border: 2px solid black;
background: #ABCFCE;
}

#btn {
border: none;
background: red;
}

#big_btn {
background: #546F94;
}

#title_btn {
border: none;
font-size: 22px;
font-weight: bold;
}

#label_hint {
padding-left: 10px;
}


#edit_hint {
font-size: 20px;
padding: 10px;
}
"""

app = QApplication(sys.argv)
app.setStyleSheet(styles)
app.setFont("Comic Sans MS")

main = MainClass()
main.show()
app.exec()