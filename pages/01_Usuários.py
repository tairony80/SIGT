import streamlit as st

from database.models import (
    inserir_usuario,
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

    st.info(
        "A listagem de usuários será criada na Aula 6 - Parte 2."
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
