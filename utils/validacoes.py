import re

# ===================================================
# VALIDAÇÃO DE E-MAIL
# ===================================================

def email_valido(email):
    """
    Verifica se o e-mail informado possui um formato válido.
    Retorna True ou False.
    """

    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    return re.match(padrao, email) is not None
