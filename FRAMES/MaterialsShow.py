from PySide6.QtWidgets import (QFrame, QScrollArea, QPushButton,
                               QWidget, QLabel, QVBoxLayout,
                               QHBoxLayout)
from PySide6.QtGui import QPixmap
from FRAMES import CreateMaterials, UpdateMaterials

class ShowMaterialsClass(QFrame):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller
        self.db = controller.db
        self.layout = QVBoxLayout(self)
        self.setup_ui()

    def setup_ui(self):
        title = QLabel("Список материалов")
        title.setObjectName("Title")
        self.layout.addWidget(title)

        self.set_picture()

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        container = QWidget()
        container_l = QVBoxLayout(container)

        for elements in self.db.take_materials_data():
            card = QWidget()
            card.setObjectName("card")
            card_l = QVBoxLayout(card)


            # Создание кнопки Тип / Наименование
            hbox_1 = QHBoxLayout()
            title_btn = QPushButton(f"{elements['type']} | {elements['name']}")
            title_btn.setObjectName("title_btn")
            title_btn.setAccessibleName(elements['name'])
            title_btn.clicked.connect(
                self.open_update_window
            )

            hbox_1.addWidget(title_btn)
            hbox_1.addStretch()

            fin_count = elements['min_count']
            if int(elements['min_count']) > int(elements['count']):
                fin_count = int(elements['count']) - int(elements['min_count'])

            # Создание кнопки Минимальное количество
            hbox_2 = QHBoxLayout()
            min_btn = QPushButton(f"Минимальное количество: {fin_count} {elements['edinica']}")
            min_btn.setObjectName("btn")
            min_btn.setAccessibleName(elements['name'])
            min_btn.clicked.connect(
                self.open_update_window
            )

            cost_btn = QPushButton(f"Стоимость партии: {round(abs(float(elements['cost']) * fin_count), 2)}р")
            cost_btn.setObjectName("btn")
            cost_btn.setAccessibleName(elements['name'])
            cost_btn.clicked.connect(
                self.open_update_window
            )

            hbox_2.addWidget(min_btn)
            hbox_2.addStretch()
            hbox_2.addWidget(cost_btn)

            # Создание кнопки Количество на складе
            hbox_3 = QHBoxLayout()

            count_btn = QPushButton(f"Количество на складе:\t\t\t\t\t\t\t {elements['count']} {elements['edinica']}")
            count_btn.setObjectName("btn")
            count_btn.setAccessibleName(elements['name'])
            count_btn.clicked.connect(
                self.open_update_window
            )

            hbox_3.addWidget(count_btn)
            hbox_3.addStretch()

            # Создание кнопки Количество на складе
            hbox_4 = QHBoxLayout()

            price_btn = QPushButton(f"Цена: {elements['cost']} / Единица измерения: {elements['edinica']}")
            price_btn.setObjectName("btn")
            price_btn.setAccessibleName(elements['name'])
            price_btn.clicked.connect(
                self.open_update_window
            )

            hbox_4.addWidget(price_btn)
            hbox_4.addStretch()

            card_l.addLayout(hbox_1)
            card_l.addLayout(hbox_2)
            card_l.addLayout(hbox_3)
            card_l.addLayout(hbox_4)

            container_l.addWidget(card)

        scroll_area.setWidget(container)
        self.layout.addWidget(scroll_area)

        create_material_btn = QPushButton("Создать материал")
        create_material_btn.setObjectName("big_btn")
        create_material_btn.clicked.connect(
            lambda : self.controller.switch_window(CreateMaterials.CreateMaterialsClass)
        )

        self.layout.addWidget(create_material_btn)


    def open_update_window(self):
        sender_name = self.sender().accessibleName()
        self.controller.switch_window(UpdateMaterials.UpdateMaterialsClass,
                                      sender_name)


    def set_picture(self):
        """ Установка фотографии """
        socket = QLabel()
        picture = QPixmap("/home/spirit2/Desktop/DemoExamTruthVariantOne/Мозаика.png")

        socket.setScaledContents(True)
        socket.setFixedSize(100, 100)
        socket.setPixmap(picture)

        hbox = QHBoxLayout()
        hbox.addWidget(QWidget())
        hbox.addWidget(socket)
        hbox.addWidget(QWidget())
        self.layout.addLayout(hbox)
