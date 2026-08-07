import streamlit as st
import pandas as pd

from database.models import (
    inserir_usuario,
    listar_usuarios,
    login_existe
)


from database.seguranca import criptografar_senha
from utils.validacoes import email_valido


# =====================================================
# CONFIGURAÇÃO DA PÁGINA
# =====================================================

st.set_page_config(
    page_title="Usuários",
    page_icon="👤",
    layout="wide"
)

st.title("👤 Gestão de Usuários")

st.caption("Sistema Integrado de Termografia - SIGT")

st.divider()


# =====================================================
# ABAS
# =====================================================

aba1, aba2, aba3, aba4 = st.tabs(
    [
        "➕ Cadastro",
        "📋 Usuários",
        "✏️ Editar",
        "🗑️ Excluir"
    ]
)


# =====================================================
# ABA 1
# CADASTRO
# =====================================================

with aba1:

    st.subheader("Novo Usuário")

    col1, col2 = st.columns(2)

    with col1:

        nome = st.text_input("Nome")

        matricula = st.text_input("Matrícula")

        cargo = st.text_input("Cargo")

        email = st.text_input("E-mail")

    with col2:

        login = st.text_input("Login")

        senha = st.text_input(
            "Senha",
            type="password"
        )

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

    st.divider()

    if st.button(
        "💾 Salvar Usuário",
        use_container_width=True
    ):

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

            st.error("Este login já existe.")

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


# =====================================================
# ABA 2
# =====================================================

with aba2:

    st.subheader("📋 Usuários Cadastrados")

    usuarios = listar_usuarios()

    if len(usuarios) == 0:

        st.warning("Nenhum usuário cadastrado.")

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


# =====================================================
# ABA 3
# =====================================================

with aba3:

    st.info(
        "A edição de usuários será criada na Aula 6 - Parte 3."
    )


# =====================================================
# ABA 4
# =====================================================

with aba4:

    st.info(
        "A exclusão de usuários será criada na Aula 6 - Parte 4."
    )

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total", len(df))

with col2:
    st.metric(
        "Administradores",
        len(df[df["Perfil"] == "Administrador"])
    )

with col3:
    st.metric(
        "Inspetores",
        len(df[df["Perfil"] == "Inspetor"])
    )

with col4:
    st.metric(
        "Visualizadores",
        len(df[df["Perfil"] == "Visualizador"])
    )

st.divider()

pesquisa = st.text_input(
    "🔍 Pesquisar usuário"
)

if pesquisa:

    filtro = df["Nome"].str.contains(
        pesquisa,
        case=False,
        na=False
    )

    df = df[filtro]

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

