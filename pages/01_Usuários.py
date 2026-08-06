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
from database.models import inserir_usuario
status = st.selectbox(
    "Status",
    [
        "Ativo",
        "Inativo"
    ]
)

if st.button("💾 Salvar"):

    inserir_usuario(
        nome,
        matricula,
        cargo,
        email,
        login,
        senha,
        perfil,
        status
    )

    st.success("Usuário cadastrado com sucesso!")
