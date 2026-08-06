import hashlib

def criptografar_senha(senha):

    senha_hash = hashlib.sha256(
        senha.encode()
    ).hexdigest()

    return senha_hash
