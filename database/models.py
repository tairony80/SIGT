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
def listar_usuarios():

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""

        SELECT
            id,
            nome,
            matricula,
            cargo,
            email,
            login,
            perfil,
            status

        FROM usuarios

        ORDER BY nome

    """)

    usuarios = cursor.fetchall()

    conexao.close()

    return usuarios

def login_existe(login):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        "SELECT id FROM usuarios WHERE login=?",
        (login,)
    )

    usuario = cursor.fetchone()

    conexao.close()

    return usuario is not None

def buscar_usuario_login(login):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        """
        SELECT
            id,
            nome,
            login,
            senha,
            perfil,
            status
        FROM usuarios
        WHERE login = ?
        """,
        (login,)
    )

    usuario = cursor.fetchone()

    conexao.close()

    return usuario
