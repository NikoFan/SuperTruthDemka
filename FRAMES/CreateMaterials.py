from PySide6.QtWidgets import (QFrame, QScrollArea, QPushButton,
                               QWidget, QLabel, QVBoxLayout,
                               QHBoxLayout, QLineEdit, QComboBox)

from FRAMES import MaterialsShow
from Messages import *
class CreateMaterialsClass(QFrame):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller
        self.db = controller.db
        self.layout = QVBoxLayout(self)
        self.setup_ui()

    def setup_ui(self):
        title = QLabel("Добавление/Редактирование")
        title.setFixedHeight(100)
        title.setObjectName("Title")
        self.layout.addWidget(title)

        self.label_pattern("Наименование материала")
        self.material_name = self.edit_pattern("Введите материал")

        self.label_pattern("Тип материала")
        self.material_type = QComboBox()
        self.material_type.addItems(self.db.take_all_materials_types())
        print(self.db.take_all_materials_types())
        self.layout.addWidget(self.material_type)

        self.label_pattern("Количество на складе")
        self.material_count = self.edit_pattern("Введите кол-во на складе")

        self.label_pattern("Единица измерения")
        self.material_edin = self.edit_pattern("Введите ед. измерения")

        self.label_pattern("Количество в упаковке")
        self.material_paket_count = self.edit_pattern("Введите кол-во в упаковке")

        self.label_pattern("Минимальное количество")
        self.material_min_count = self.edit_pattern("Введите минимальное кол-во")

        self.label_pattern("Цена единицы материала")
        self.material_cost = self.edit_pattern("Введите цена")

        add_material = QPushButton("Добавить материал")
        add_material.setObjectName("big_btn")
        add_material.clicked.connect(
            self.create_material_func
        )
        self.layout.addWidget(add_material)

        back_btn = QPushButton("Назад")
        back_btn.setObjectName("big_btn")
        back_btn.clicked.connect(
            lambda : self.controller.switch_window(MaterialsShow.ShowMaterialsClass)
        )
        self.layout.addWidget(back_btn)


    def create_material_func(self):
        """ Функция форматирования данных для создания """
        material_data = {
            "material_name": self.material_name.text(),
            "material_type": self.material_type.currentText(),
            "material_cost": self.material_cost.text(),
            "material_paket_count": self.material_paket_count.text(),
            "material_count": self.material_count.text(),
            "material_min_count": self.material_min_count.text(),
            "material_edinica": self.material_edin.text()
        }

        if send_W_message("Вы проверили данные и готовы к созданию?"):
            if self.db.create_materials_data(material_data):
                send_I_message("Материал добавлен!")
                return
            send_C_message("Ошибка создания! Проверьте данные!")

    def label_pattern(self, text: str) -> QLabel:
        """ Паттерн для создания текстовой подсказки """
        label = QLabel(text)
        label.setObjectName("label_hint")
        self.layout.addWidget(label)

        return label

    def edit_pattern(self, text: str) -> QLineEdit:
        """ Паттерн для создания текстовой подсказки """
        edit = QLineEdit()
        edit.setPlaceholderText(text)
        edit.setObjectName("edit_hint")
        self.layout.addWidget(edit)

        return edit