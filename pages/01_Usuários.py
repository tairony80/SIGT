import streamlit as st
import pandas as pd

from database.models import (
    inserir_usuario,
    listar_usuarios,
    login_existe,
    excluir_usuario
)

from database.seguranca import criptografar_senha
from utils.validacoes import email_valido

# ===================================================
# CONFIGURAÇÃO DA PÁGINA
# ===================================================

st.set_page_config(
    page_title="Usuários",
    page_icon="👤",
    layout="wide"
)

st.title("👤 Cadastro de Usuários")

st.divider()

# ===================================================
# FORMULÁRIO
# ===================================================

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

# ===================================================
# BOTÃO SALVAR
# ===================================================

if st.button("💾 Salvar"):

    if not nome.strip():
        st.error("Informe o nome.")
        st.stop()

    if not email.strip():
        st.error("Informe o e-mail.")
        st.stop()

    if not email_valido(email):
        st.error("E-mail inválido.")
        st.stop()

    if not login.strip():
        st.error("Informe o login.")
        st.stop()

    if not senha.strip():
        st.error("Informe a senha.")
        st.stop()

    if login_existe(login):
        st.error("Este login já está cadastrado.")
        st.stop()

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

    st.rerun()

# ===================================================
# LISTA DE USUÁRIOS
# ===================================================

st.divider()

st.subheader("📋 Usuários cadastrados")

usuarios = listar_usuarios()

if len(usuarios) == 0:

    st.info("Nenhum usuário cadastrado.")

else:

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

# ===================================================
# EXCLUSÃO
# ===================================================

st.divider()

st.subheader("🗑️ Excluir usuário")

if len(usuarios) > 0:

    id_usuario = st.selectbox(
        "Selecione o usuário",
        options=df["ID"].tolist(),
        format_func=lambda x: f"{x} - {df[df['ID']==x]['Nome'].values[0]}"
    )

    if st.button("🗑️ Excluir"):

        excluir_usuario(id_usuario)

        st.success("Usuário excluído com sucesso!")

        st.rerun()
