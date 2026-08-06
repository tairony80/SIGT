from database.banco import conectar


# ===================================================
# CRIAÇÃO DAS TABELAS
# ===================================================

def criar_tabelas():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (

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


# ===================================================
# CADASTRO DE USUÁRIOS
# ===================================================

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


# ===================================================
# LISTAR USUÁRIOS
# ===================================================

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


# ===================================================
# VERIFICAR LOGIN
# ===================================================

def login_existe(login):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(

        "SELECT id FROM usuarios WHERE login = ?",

        (login,)

    )

    usuario = cursor.fetchone()

    conexao.close()

    return usuario is not None


# ===================================================
# BUSCAR USUÁRIO PELO LOGIN
# ===================================================

def buscar_usuario_login(login):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""

        SELECT

            id,
            nome,
            login,
            senha,
            perfil,
            status

        FROM usuarios

        WHERE login = ?

    """, (login,))

    usuario = cursor.fetchone()

    conexao.close()

    return usuario


# ===================================================
# ATUALIZAR USUÁRIO
# ===================================================

def atualizar_usuario(
    id_usuario,
    nome,
    matricula,
    cargo,
    email,
    login,
    perfil,
    status
):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""

        UPDATE usuarios

        SET

            nome = ?,
            matricula = ?,
            cargo = ?,
            email = ?,
            login = ?,
            perfil = ?,
            status = ?

        WHERE id = ?

    """, (

        nome,
        matricula,
        cargo,
        email,
        login,
        perfil,
        status,
        id_usuario

    ))

    conexao.commit()
    conexao.close()


# ===================================================
# EXCLUIR USUÁRIO
# ===================================================

def excluir_usuario(id_usuario):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(

        "DELETE FROM usuarios WHERE id = ?",

        (id_usuario,)

    )

    conexao.commit()
    conexao.close()
