from database.banco import conectar


def criar_tabelas():

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            nome TEXT NOT NULL,

            matricula TEXT,

            cargo TEXT,

            email TEXT,

            login TEXT UNIQUE,

            senha TEXT,

            perfil TEXT,

            status TEXT

        )
    """)

    conexao.commit()

    conexao.close()
def inserir_usuario(
    nome,
    matricula,
    cargo,
    email,
    login,
    senha,
    perfil,
    status
):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO usuarios
        (
            nome,
            matricula,
            cargo,
            email,
            login,
            senha,
            perfil,
            status
        )

        VALUES
        (?, ?, ?, ?, ?, ?, ?, ?)

    """, (

        nome,
        matricula,
        cargo,
        email,
        login,
        senha,
        perfil,
        status

    ))

    conexao.commit()

    conexao.close()
