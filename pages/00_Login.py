import streamlit as st

from database.models import buscar_usuario_login
from database.seguranca import verificar_senha

st.set_page_config(
    page_title="Login",
    page_icon="🔐"
)

st.title("🔐 Login do SIGT")

login = st.text_input("Usuário")

senha = st.text_input(
    "Senha",
    type="password"
)

if st.button("Entrar"):

    usuario = buscar_usuario_login(login)

    if usuario is None:

        st.error("Usuário não encontrado.")

    else:

        if verificar_senha(
            senha,
            usuario[3]
        ):

            st.success("Login realizado com sucesso!")

        else:

            st.error("Senha incorreta.")
