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

    if nome == "":
        st.error("Informe o nome.")
        st.stop()

    if login == "":
        st.error("Informe o login.")
        st.stop()

    if senha == "":
        st.error("Informe a senha.")
        st.stop()

    if not email_valido(email):
        st.error("E-mail inválido.")
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

    st.success("Usuário cadastrado com sucesso!")

st.divider()

st.subheader("Usuários cadastrados")

lista = {}

for usuario in usuarios:
    chave = f"{usuario[0]} - {usuario[1]}"
    lista[chave] = usuario

selecionado = st.selectbox(
    "Selecione o usuário",
    options=list(lista.keys())
)

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

st.divider()

st.subheader("Excluir usuário")

id_usuario = st.number_input(
    "ID do usuário",
    min_value=1,
    step=1
)

if st.button("🗑️ Excluir usuário"):
    excluir_usuario(id_usuario)
    st.success("Usuário excluído com sucesso!")
    st.rerun()

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

