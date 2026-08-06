import streamlit as st
from datetime import datetime
from database.criar_banco import inicializar_banco

# ==========================
# CONFIGURAÇÃO DA PÁGINA
# ==========================

st.set_page_config(
     page_title="SIGT",
    page_icon="🌡️",
    layout="wide",
    initial_sidebar_state="expanded"
)
   # Inicializa o banco de dados
inicializar_banco()
# ==========================
# MENU LATERAL
# ==========================

with st.sidebar:

    st.image(
        "https://img.icons8.com/color/96/thermal-camera.png",
        width=90
    )

    st.title("SIGT")

    st.caption("Sistema Integrado de Termografia")

    st.divider()

    st.success("Versão 0.1")

# ==========================
# TÍTULO
# ==========================

st.title("🌡️ Sistema Integrado de Termografia")

st.write(
    "Bem-vindo ao sistema de gerenciamento das inspeções termográficas."
)

st.divider()

# ==========================
# DATA
# ==========================

st.write("📅", datetime.now().strftime("%d/%m/%Y"))
st.write("⏰", datetime.now().strftime("%H:%M:%S"))

st.divider()

# ==========================
# DASHBOARD
# ==========================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Inspeções Hoje", 0)

with c2:
    st.metric("Pendentes", 0)

with c3:
    st.metric("Concluídas", 0)

with c4:
    st.metric("Críticas", 0)

st.divider()

st.info(
    "SIGT - Sistema Integrado de Termografia"
)

st.caption(
    "Desenvolvido em Python + Streamlit"
)
