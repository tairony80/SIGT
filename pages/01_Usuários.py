import streamlit as st

st.set_page_config(page_title="Usuários", page_icon="👤")

st.title("👤 Cadastro de Usuários")

st.divider()

nome = st.text_input("Nome")

matricula = st.text_input("Matrícula")

cargo = st.text_input("Cargo")

email = st.text_input("E-mail")

login = st.text_input("Login")

senha = st.text_input("Senha", type="password")

perfil = st.selectbox(
    "Perfil",
    [
        "Administrador",
        "Inspetor",
        "Visualizador"
    ]
)

status = st.selectbox(
    "Status",
    [
        "Ativo",
        "Inativo"
    ]
)

st.button("💾 Salvar")
