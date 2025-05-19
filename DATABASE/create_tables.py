import psycopg
from config import *

create_suppliers = """
create table suppliers (
supplier_name text primary key not null,
supplier_type varchar(3) not null,
supplier_inn varchar(10) not null,
supplier_rate int not null,
supplier_date date not null
);
"""

create_product_type = """
create table products_type (
product_type_name text primary key not null,
product_type_coef real not null
);
"""

create_material_type = """
create table materials_type (
material_type_name text primary key not null,
material_type_lost_percent text not null
);
"""

create_materials = """
create table materials (
material_name text primary key not null,
material_type_name_fk text not null,
foreign key (material_type_name_fk) references materials_type(material_type_name)
on update cascade,
material_cost real not null,
material_count real not null,
material_minimum_count real not null,
material_paket_size int not null,
material_edinisa text not null
);
"""

create_material_suppliers = """
create table material_suppliers (
material_name_fk text not null,
foreign key (material_name_fk) references materials(material_name)
on update cascade,

supplier_name_fk text not null,
foreign key (supplier_name_fk) references suppliers(supplier_name)
on update cascade,

primary key (material_name_fk, supplier_name_fk)
);
"""


def create_tables(table_name, conn):
    cursor = conn.cursor()
    cursor.execute(table_name)
    conn.commit()
    cursor.close()

conn = psycopg.connect(
    user=user,
    host=host,
    password=password,
    dbname=dbname
)

create_tables(create_suppliers, conn)
create_tables(create_product_type, conn)
create_tables(create_material_type, conn)
create_tables(create_materials, conn)
create_tables(create_material_suppliers, conn)







