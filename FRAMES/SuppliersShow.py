from PySide6.QtWidgets import (QFrame, QScrollArea, QPushButton,
                               QWidget, QLabel, QVBoxLayout,
                               QHBoxLayout)
from FRAMES import MaterialsShow

class ShowSuppliersClass(QFrame):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller
        self.db = controller.db
        self.layout = QVBoxLayout(self)
        self.setup_ui()

    def setup_ui(self):
        title = QLabel("Список поставщиков")
        title.setObjectName("Title")
        self.layout.addWidget(title)


        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        container = QWidget()
        container_l = QVBoxLayout(container)

        for elements in self.db.take_suppliers_list():
            card = QWidget()
            card.setObjectName("card")
            card_l = QVBoxLayout(card)

            name = QLabel(f"Имя: {elements['name']}")
            type_s = QLabel(f"Тип партнера: {elements['type']}")
            inn = QLabel(f"ИНН: {elements['inn']}")
            rate = QLabel(f"Рейтинг: {elements['rate']}")
            date = QLabel(f"Дата: {elements['date']}")

            card_l.addWidget(name)
            card_l.addWidget(type_s)
            card_l.addWidget(inn)
            card_l.addWidget(rate)
            card_l.addWidget(date)





            container_l.addWidget(card)

        scroll_area.setWidget(container)
        self.layout.addWidget(scroll_area)

        back_btn = QPushButton("Назад")
        back_btn.setObjectName("big_btn")
        back_btn.clicked.connect(
            lambda : self.controller.switch_window(MaterialsShow.ShowMaterialsClass)
        )

        self.layout.addWidget(back_btn)
