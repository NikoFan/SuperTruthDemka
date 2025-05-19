import psycopg
from DATABASE.config import *


def calculate(
        prod_type, material_type, count: int, param_1: float, param_2: float
)-> int:
    if (count < 0 or param_1 < 0 or param_2 < 0 or
        prod_type == None or material_type == None):
        return -1

    ac_1 = param_1 * param_2
    ac_2 = ac_1 * prod_type
    lost = material_type.replace('%', '')
    lost = float(lost)

    final = ac_2 * count
    lost_final = final * lost
    return int(final + lost_final)

conn = psycopg.connect(
                user=user,
                host=host,
                password=password,
                dbname=dbname
            )
def products_types():
    query = """
    select *
    from products_type;
    """
    cursor = conn.cursor()
    cursor.execute(query)
    result = {}

    for row in cursor.fetchall():
        result[row[0]] = row[1]
    return result

def materials_types():
    query = """
    select *
    from materials_type;
    """
    cursor = conn.cursor()
    cursor.execute(query)
    result = {}

    for row in cursor.fetchall():
        result[row[0]] = row[1]
    return result

for k, v in materials_types().items():
    print("Наименование: ",k, "Параметр:", v)

arg = input("Введите выбранныйтериал: ")
try:
    material_arg = materials_types()[arg]
except Exception:
    material_arg = None


for k, v in products_types().items():
    print("Наименование: ",k, "Параметр:", v)

arg = input("Введите выбранный продукт: ")
try:
    products_arg = products_types()[arg]
except Exception:
    products_arg = None


try:
    count = int(input("Введите количество: "))
except Exception as e:
    count = -1

try:
    param_1 = float(input("Введите параметр 1: "))
    param_2 = float(input("Введите параметр 2: "))

except Exception as e:
    param_1 = -1
    param_2 = -1

print("Результат расчетов: ", calculate(products_arg,
                                        material_arg,
                                        count,
                                        param_1,
                                        param_2))