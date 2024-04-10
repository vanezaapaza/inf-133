import sqlite3
conn = sqlite3.connect("personal_db.db")

def insertVentas(nombre, fecha_creacion):
    conn.execute(
    f"""
    INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion) 
    VALUES ('{nombre}', '{fecha_creacion}')
    """
    )


def insertCargo(nombre, nivel, fecha_creacion):
    conn.execute(
    f"""
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion) 
    VALUES ('{nombre}', '{nivel}', '{fecha_creacion}')
    """
    )

def insertEmpleado(nombre, apellido_paterno, apellido_materno, fecha_contratacion, departamento_id, cargo_id, fecha_creacion):
    conn.execute(
    f"""
    INSERT INTO EMPLEADOS (nombre, apellido_paterno, apellido_materno, fecha_contratacion, departamento_id, cargo_id, fecha_creacion) 
    VALUES ('{nombre}', '{apellido_paterno}', '{apellido_materno}', '{fecha_contratacion}', '{departamento_id}', '{cargo_id}', '{fecha_creacion}')
    """
    )

def insertSalario(empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion):
    conn.execute(
    f"""
    INSERT INTO EMPLEADOS (empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion) 
    VALUES ('{empleado_id}', '{salario}', '{fecha_inicio}', '{fecha_fin}', '{fecha_creacion}')
    """
    )

insertVentas("Ventas", "10-04-2020")
insertVentas("Marketing", "11-04-2020")

insertCargo("Gerente de Ventas", "Senior", "10-04-2020")
insertCargo("Analista de Marketing", "Junior", "11-04-2020")
insertCargo("Representante de Ventas", "Junior", "12-04-2020")

insertEmpleado()

insertSalario()

conn.commit()
conn.close()