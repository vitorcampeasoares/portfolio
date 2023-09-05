import sqlite3
conexao = sqlite3.connect('eventos.sqlite3')
cursor = conexao.cursor()


def criar_organizador():
    sql = '''
        CREATE TABLE IF NOT EXISTS organizador (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT(50) NOT NULL,
        email TEXT(50),
        cpf TEXT(11),
        CONSTRAINT organizador_UN UNIQUE (cpf)
        );
    '''

    cursor.execute(sql)
    conexao.commit()


def criar_evento():
    sql = '''
        CREATE TABLE IF NOT EXISTS evento (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT(50) NOT NULL,
        agenda TEXT(10),
        organizador_id INTEGER,
        CONSTRAINT organizador_FK FOREIGN KEY(organizador_id) REFERENCES organizador(id)
        );
    '''

    cursor.execute(sql)
    conexao.commit()


criar_organizador()
criar_evento()

conexao.close()
