import re


def email_valido(email):

    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    return re.match(padrao, email) is not None
