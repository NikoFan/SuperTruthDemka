from DATABASE.config import *
import psycopg
from check import main
from Material import Material

class Database:

    def __init__(self):
        self.connection = self.connect_to_db()

    def connect_to_db(self) -> psycopg.connect:
        try:
            conn = psycopg.connect(
                user=user,
                host=host,
                password=password,
                dbname=dbname
            )
            return conn

        except Exception as e:
            print(e)
            return None

    def take_materials_data(self) -> list:
        """
        Получение данных о всех материалах
        :return: list
        """

        try:
            query = """
            select *
            from materials;"""
            cursor = self.connection.cursor()
            cursor.execute(query)

            result = []
            for row in cursor.fetchall():
                result.append(
                    {
                        'name':row[0],
                        'type':row[1],
                        'cost':row[2],
                        'count':row[3],
                        'min_count':row[4],
                        'size':row[5],
                        'edinica':row[6]
                    }
                )

            return result

        except Exception as e:
            print(e)
            return []


    def take_all_materials_types(self) -> list:
        """ Получение списка типов материала """
        try:
            query = """
            select material_type_name
            from materials_type;
            """
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = []

            for i in cursor.fetchall():
                result.append(i[0])

            return result
        except Exception as e:
            print(e)
            return []


    def create_materials_data(self, materials_data: dict) -> bool:
        """ Добавление данных в таблицу """
        try:
            if not main(materials_data):
                return False

            query = f"""
            insert into materials
            values(
            '{materials_data["material_name"]}',
            '{materials_data["material_type"]}',
            {materials_data["material_cost"]},
            {materials_data["material_count"]},
            {materials_data["material_min_count"]},
            {materials_data["material_paket_count"]},
            '{materials_data["material_edinica"]}'
            );
            """

            cursor  =self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            return True

        except Exception as e:
            print(e)
            return False


    def take_material_info(self):
        try:
            name = Material().get_material()
            print(name)
            query = f"""
            select *
            from materials
            where material_name = '{name}';
            """

            result = dict()
            cursor = self.connection.cursor()
            cursor.execute(query)
            for row in cursor.fetchall():
                result = {
                        'name': row[0],
                        'type': row[1],
                        'cost': row[2],
                        'count': row[3],
                        'min_count': row[4],
                        'size': row[5],
                        'edinica': row[6]
                    }

            print(result)
            return result
        except Exception as e:
            print("-", e)
            return dict()


    def update_materials_data(self, materials_data: dict) -> bool:
        """ обновление данных в таблицу """
        try:
            if not main(materials_data):
                return False
            name = Material().get_material()

            query = f"""
            update materials
            set
            material_name='{materials_data["material_name"]}',
            material_type_name_fk='{materials_data["material_type"]}',
            material_cost={materials_data["material_cost"]},
            material_count={materials_data["material_count"]},
            material_minimum_count={materials_data["material_min_count"]},
            material_paket_size={materials_data["material_paket_count"]},
            material_edinisa='{materials_data["material_edinica"]}'
            where material_name = '{name}';
            """

            cursor  =self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()

            return True

        except Exception as e:
            print(e)
            return False

    def take_suppliers_list(self):
        """ Получение списка поставщиков """
        try:
            name = Material.get_material()
            query = f"""
            select s.supplier_name, s.supplier_type,
            s.supplier_inn, s.supplier_rate, s.supplier_rate
            from suppliers s
            join material_suppliers ms
            on ms.supplier_name_fk = s.supplier_name
            where material_name_fk = '{name}';
            """

            cursor = self.connection.cursor()
            cursor.execute(query)
            result = []
            for row in cursor.fetchall():
                result.append(
                    {
                        "name":row[0],
                        "type":row[1],
                        "inn":row[2],
                        "rate":row[3],
                        "date":row[4],
                    }
                )

            return result
        except Exception as e:
            print(e)
            return []