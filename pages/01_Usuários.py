import streamlit as st
import pandas as pd

from database.models import inserir_usuario, listar_usuarios
from database.seguranca import criptografar_senha

st.set_page_config(
    page_title="Usuários",
    page_icon="👤"
)

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

if st.button("💾 Salvar"):

    senha_hash = criptografar_senha(senha)

    inserir_usuario(
        nome,
        matricula,
        cargo,
        email,
        login,
        senha_hash,
        perfil,
        status
    )

    st.success("Usuário cadastrado com sucesso!")

st.divider()

st.subheader("Usuários cadastrados")

usuarios = listar_usuarios()

df = pd.DataFrame(
    usuarios,
    columns=[
        "ID",
        "Nome",
        "Matrícula",
        "Cargo",
        "E-mail",
        "Login",
        "Perfil",
        "Status"
    ]
)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)
