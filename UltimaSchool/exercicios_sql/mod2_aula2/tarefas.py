import sqlite3
conexao = sqlite3.connect('tarefas.sqlite3')
cursor = conexao.cursor()


def criar_tarefa():
    sql = '''
        CREATE TABLE IF NOT EXISTS tarefa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT(50) NOT NULL,
        prazo TEXT(10),
        execucao TEXT(11) DEFAULT (incompleto),
        categoria_id INTEGER,
        CONSTRAINT tarefa_FK FOREIGN KEY(categoria_id) REFERENCES categoria(id)
        );
    '''

    cursor.execute(sql)
    conexao.commit()


def criar_categoria():
    sql = '''
        CREATE TABLE IF NOT EXISTS categoria (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT(50) NOT NULL
        );
    '''

    cursor.execute(sql)
    conexao.commit()


criar_tarefa()
criar_categoria()

conexao.close()
