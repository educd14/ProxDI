import sqlite3
import os
from sqlite3 import Error

"""
Clase donde se encuentran las funciones/metodos
de manipulación de la base de datos
"""

def connect():
    """Crea conexion a base de datos.
    :param: No recibe ningún parámetro.
    :return: Object Connection o null
    """
    conn = None
    try:
        path = os.path.dirname(os.path.abspath(__file__))
        db = os.path.join(path, 'proyectotienda.db')
        conn = sqlite3.connect(db)
        return conn
    except Error as e:
        print(e)
    return conn


def disconnect(conn):
    """Cierra la conexión a base de datos.
        :param conn: Conexion de la base de datos.
        :return: No devuelve ningún parámetro.
        """
    try:
        if conn is not None:
            conn.close()
    except conn.DatabaseError as erroSQL:
        print("Error al cerrar conexión.")


def query(conn, query):
    """Query para crear tablas o insertar datos
    :param conn: Object Connection
    :param query: statement
    :return: No devuelve ningún prámetro.
    """
    try:
        c = conn.cursor()
        c.execute(query)
        conn.commit()
    except Error as e:
        print()


def insertTablaClientes(dni, nome, apelido, sexo, telefono, direccion):
    """Inserta una nueva fila en la tabla Clientes.
    :param dni: Dni
    :param nome: Nome
    :param apelido: Apelido
    :param sexo: Sexo
    :param telefono: Telefono
    :param direccion: Direccion
    :return: No devuelve ningún parámetro.
    """
    if (
            dni != "" and nome != "" and apelido != "" and sexo != "" and telefono != "" and direccion != "" ):
        conn = connect()
        cursor = conn.cursor()

        try:

            sql = "INSERT INTO clientes (dni,nome,apelido,sexo,telefono,direccion) VALUES (?, ?, ?, ?, ?, ?)"
            parametros = (dni, nome, apelido, sexo, telefono, direccion)

            cursor.execute(sql, parametros)

            conn.commit()

        except conn.OperationalError as e:
            print("Error")

        except conn.DatabaseError as e2:
            print("El DNI del cliente ya existe en la base de datos")

        finally:
            cursor.close()
            disconnect(conn)
    else:
        print("Faltan valores para insertar el cliente")


def insertTablaProdutos(id, produto, precio):
    """Inserta una nueva fila en la tabla Produtos.
    :param id: id
    :param produto: produto
    :param precio: Precio
    :return: Ningún parámetro devuelto.
    """
    if (
            id != "" and produto != "" and precio != ""):
        conn = connect()
        cursor = conn.cursor()

        try:

            sql = "INSERT INTO produtos(id, produto, precio) VALUES (?, ?, ?)"
            parametros = (id, produto, precio)
            cursor.execute(sql, parametros)
            conn.commit()

        except conn.OperationalError as e:
            print(e)

        except conn.DatabaseError as e2:
            print("La ID del produto ya existe")
        finally:
            cursor.close()
            disconnect(conn)
    else:
        print("Faltan valores para insertar el producto")


def deleteTablaProductos(id):
    """Elimina el produto dado el id
    :param id: id del produto.
    :return: Ningún parámetro devuelto.
    """
    conn = connect()
    cursor = conn.cursor()
    try:

        cursor.execute("DELETE FROM produtos WHERE id = '" + id + "'")
        conn.commit()
        print("Eliminado")

    except conn.OperationalError as err:
        print(err)

    except conn.DatabaseError as err2:
        print(err2)

    finally:
        cursor.close()
        disconnect(conn)

def updateTablaProdutos(id, produto, precio):
    """Modifica los datos de un produto existente dado la clave primaria ID.
    :param id: id
    :param produto: produto
    :param precio: precio
    :return: No devuelve ningún parámetro.
    """
    if (id != "" and produto != "" and precio != ""):

        conn = connect()
        cursor = conn.cursor()
        try:

            sql = "UPDATE produtos SET produto = ?, precio = ? where id = ?"
            parametros = (produto, precio, id)

            cursor.execute(sql, parametros)

            conn.commit()

        except conn.OperationalError as e:
            print(e)

        except conn.DatabaseError as e2:
            print(e2)

        finally:
            cursor.close()
            disconnect(conn)
    else:
        print("Faltan valores para modificar el cliente")



def updateTablaClientes(dni, nome, apelido, sexo, telefono, direccion):
    """Modifica los datos de un cliente existente dado la clave primaria DNI.
    :param dni: Dni
    :param nome: Nome
    :param apelido: Apelido
    :param sexo: Sexo
    :param telefono: Telefono
    :param direccion: Direccion
    :return: No devuelve ningún parámetro.
    """
    if (dni != "" and nome != "" and apelido != "" and sexo != "" and telefono != "" and direccion != "" ):

        conn = connect()
        cursor = conn.cursor()
        try:

            sql = "UPDATE clientes SET nome = ?, apelido = ?, sexo = ?, telefono = ?, direccion = ? where dni = ?"
            parametros = (nome, apelido, sexo, telefono, direccion, dni)

            cursor.execute(sql, parametros)

            conn.commit()

        except conn.OperationalError as e:
            print(+e)

        except conn.DatabaseError as e2:
            print(e2)

        finally:
            cursor.close()
            disconnect(conn)
    else:
        print("Faltan valores para modificar el cliente")


def deleteTablaClientes(dni):
    """Elimina un cliente dado su DNI.
    :param dni: DNI del cliente a eliminar.
    :return: Ningún parámetro es devuelto.
    """
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM clientes WHERE dni = '" + dni + "'")
        conn.commit()
        print("Eliminado")

    except conn.OperationalError as err:
        print(err)

    except conn.DatabaseError as err2:
        print(err2)

    finally:
        cursor.close()
        disconnect(conn)


def selectTablaClientes():
    """Consulta de todos los clientes.
    :param: No recibe ningún parámetro.
    :return: Lista de todos los clientes existentes.
    """
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM clientes")
        datos = cursor.fetchall()
        return datos
    except conn.OperationalError as err:
        print(err)

    except conn.DatabaseError as err2:
        print(err2)

    finally:
        cursor.close()
        disconnect(conn)


def selectTablaClientesDni(dni):
    """Consulta de cliente a través del DNI.
    :param dni: DNI del cliente que se quiere encontrar.
    :return: Lista de datos del cliente.
    """
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM clientes WHERE dni = '" + dni + "'")
        datos = cursor.fetchall()
        return datos
    except conn.OperationalError as err:
        print(err)

    except conn.DatabaseError as err2:
        print(err2)

    finally:
        cursor.close()
        disconnect(conn)



def selectTablaProductos():
    """Consulta todos los produtos.
    :param: No recibe ningún parámetro.
    :return: Lista de todos los produtos.
    """
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produtos")
        datos = cursor.fetchall()
        return datos
    except conn.OperationalError as err:
        print(err)
    except conn.DatabaseError as err2:
        print(err2)
    finally:
        cursor.close()
        disconnect(conn)


def tablas():
    """Crea las tablas y las inserciones necesarias.
    :param: No recibe ningún parámetro.
    :return: No devuelve ningún parámetro.
    """
    query_tabla_clientes = """CREATE TABLE IF NOT EXISTS clientes(
                                     dni TEXT PRIMARY KEY, 
                                     nome TEXT NOT NULL, 
                                     apelido TEXT NOT NULL,
                                     sexo TEXT NOT NULL,
                                     telefono TEXT NOT NULL, 
                                     direccion TEXT NOT NULL
                                     )
    """
    query_tabla_produtos = """CREATE TABLE IF NOT EXISTS produtos(
                                     id integer PRIMARY KEY, 
                                     produto TEXT NOT NULL, 
                                     precio float NOT NULL
                                     )
    """

    query_insert_clientes = """INSERT INTO clientes (dni,nome,apelido,sexo,telefono,direccion)
    VALUES 
   ('53242337F', 'Alfredo', 'Dominguez', 'M', '986172748', 'Garcia Barbon 77'),
   ('93758295N', 'Maria', 'Garzon', 'F', '986352378', 'Zaragoza 62'),
   ('58394052G', 'Eugenia', 'Val', 'F', '986642347', "Valencia 24"),
   ('28503758L', 'Eduardo', 'Collazo', 'M', '986152764', 'Pintor Colmeiro 12') 
    """

    query_insert_produtos = """INSERT INTO produtos (id,produto,precio)
        VALUES 
       (1, 'Pantalla LED 20"', 119.99),
       (2, 'Nvidia 1060 GTX', 156.95),
       (3, 'Teclado Corsair', 34.99),
       (4, 'SDD Seagate', 54.99) 
        """

    conn = connect()

    if conn is not None:
        #Tablas
        query(conn, query_tabla_clientes)
        query(conn, query_tabla_produtos)
        #Inserts
        query(conn,query_insert_clientes)
        query(conn,query_insert_produtos)
        disconnect(conn)
    else:
        print("Fallo en la conexión.")
        disconnect(conn)