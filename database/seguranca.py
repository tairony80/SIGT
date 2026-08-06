import hashlib


# ===================================================
# CRIPTOGRAFAR SENHA
# ===================================================

def criptografar_senha(senha):
    """
    Recebe uma senha em texto e retorna o hash SHA-256.
    """

    return hashlib.sha256(
        senha.encode()
    ).hexdigest()


# ===================================================
# VERIFICAR SENHA
# ===================================================

def verificar_senha(senha_digitada, senha_banco):
    """
    Compara a senha digitada com a senha armazenada no banco.
    """

    senha_hash = criptografar_senha(senha_digitada)

    return senha_hash == senha_banco
