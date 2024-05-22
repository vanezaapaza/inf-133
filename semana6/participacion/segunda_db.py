import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("restaurante.db")

# Crear tabla de platos
try:
    conn.execute(
        """
        CREATE TABLE PLATOS (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            precio INTEGER NOT NULL,
            categoria TEXT NOT NULL
        );
        """
    )
except sqlite3.OperationalError:
    print("La tabla PLATOS ya existe")

# Insertar datos en la tabla PLATOS
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('pizza', 10.99, 'italiana')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('hamburguesa', 8.99, 'americana')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('sushi', 12.99, 'japonesa')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('ensalada', 6.99, 'vegetariana')
    """
)
# Consultar datos de la tabla PLATOS
print("PLATOS:")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)

# Crear tabla de mesas
try:
    conn.execute(
        """
        CREATE TABLE MESAS (
            id INTEGER PRIMARY KEY,
            numero INTEGER NOT NULL
        );
        """
    )
except sqlite3.OperationalError:
    print("La tabla MESAS ya existe")

# Insertar datos en la tabla MESAS
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (1)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (2)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (3)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (4)
    """
)
# Consultar datos de la tabla MESAS
print("\nMESAS:")
cursor = conn.execute("SELECT * FROM MESAS")
for row in cursor:
    print(row)

# Crear tabla de pedidos
try:
    conn.execute(
        """
        CREATE TABLE PEDIDOS (
            id INTEGER PRIMARY KEY,
            plato_id INTEGER NOT NULL,
            mesa_id INTEGER NOT NULL,
            cantidad INTEGER NOT NULL,
            fecha DATE NOT NULL,
            FOREIGN KEY (plato_id) REFERENCES PLATOS(id),
            FOREIGN KEY (mesa_id) REFERENCES MESAS(id)
        );
        """
    )
except sqlite3.OperationalError:
    print("La tabla PEDIDOS ya existe")

# Insertar datos en la tabla PEDIDOS
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha) 
    VALUES (1, 2, 2, '2024-04-01')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha) 
    VALUES (2, 3, 1, '2024-04-01')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha) 
    VALUES (3, 1, 3, '2024-04-02')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha) 
    VALUES (4, 4, 1, '2024-04-02')
    """
)
# Consultar datos de la tabla PEDIDOS
print("\nPEDIDOS:")
cursor = conn.execute("SELECT * FROM PEDIDOS")
for row in cursor:
    print(row)

# Consultar datos de PEDIDOS con INNER JOIN
print("\nPEDIDOS: INNER JOIN")
cursor = conn.execute(
    """
    SELECT PLATOS.nombre, PLATOS.precio, MESAS.numero, PEDIDOS.fecha 
    FROM PEDIDOS
    JOIN PLATOS ON PEDIDOS.plato_id = PLATOS.id 
    JOIN MESAS ON PEDIDOS.mesa_id = MESAS.id
    """
)
for row in cursor:
    print(row)

# Actualizar una fila de la tabla de PLATOS
conn.execute(
    """
    UPDATE PLATOS
    SET precio = 9.99
    WHERE id = 2 AND nombre = 'hamburguesa'
    """
)
# Cambia la categoría del plato con id 3 (Sushi) a "Fusión"
conn.execute(
    """
    UPDATE PLATOS
    SET categoria = 'fusion'
    WHERE id = 3 AND nombre = 'sushi'
    """
)
   
# Consultar datos de la tabla PEDIDOS después de actualizar
print("\nPLATOS:")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)

# Eliminar una fila de la tabla de platos Elimina el plato con id 4 (Ensalada) de la tabla de platos
conn.execute(
    """
    DELETE FROM PLATOS
    WHERE id = 4 AND nombre = 'ensalada'
    """
)
# DESPUES DE ELIMINAR UN PLATO
print("\nPLATOS:")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)
# Elimina el pedido con id 3
conn.execute(
    """
    DELETE FROM PEDIDOS
    WHERE id = 3
    """
)
# DESPUES DE ELIMINAR UN PEDIDO
print("\nPEDIDOS:")
cursor = conn.execute("SELECT * FROM PEDIDOS")
for row in cursor:
    print(row)
# Confirmar cambios
conn.commit()

# Cerrar conexión
conn.close()
