import hashlib

def criptografar_senha(senha):

    senha_hash = hashlib.sha256(
        senha.encode()
    ).hexdigest()

    return senha_hash

def verificar_senha(senha_digitada, senha_banco):

    senha_hash = criptografar_senha(senha_digitada)

    return senha_hash == senha_banco
