from PySide6.QtWidgets import (QMainWindow,
                               QApplication, QStackedWidget)

import sys
from DATABASE.Database import Database



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


styles = """
#Title {
font-size: 30px;
font-weight: bold;
qproperty-alignment: AlignCenter;
}

#card {
border: 2px solid black;
}

#btn {
border: none;
}

#title_btn {
border: none;
font-size: 22px;
font-weight: bold;
}
"""

app = QApplication(sys.argv)
app.setStyleSheet(styles)
app.setFont("Comic Sans MS")

main = MainClass()
main.show()
app.exec()