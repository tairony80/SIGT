import streamlit as st

# =====================================================
# CONFIGURAÇÃO DA PÁGINA
# =====================================================

st.set_page_config(
    page_title="SIGT",
    page_icon="🌡️",
    layout="wide"
)

# =====================================================
# CABEÇALHO
# =====================================================

st.title("🌡️ SIGT")

st.subheader("Sistema Integrado de Termografia")

st.caption("Engenharia de Manutenção Preditiva")

st.divider()

# =====================================================
# BOAS-VINDAS
# =====================================================

st.success("Bem-vindo ao Sistema Integrado de Termografia.")

st.write(
    """
    Utilize o menu lateral para acessar os módulos do sistema.
    """
)

st.divider()

# =====================================================
# INDICADORES
# =====================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👥 Usuários", "0")

with col2:
    st.metric("⚙️ Equipamentos", "0")

with col3:
    st.metric("🌡️ Inspeções", "0")

with col4:
    st.metric("⚠️ Pendências", "0")

st.divider()

# =====================================================
# ÚLTIMAS INSPEÇÕES
# =====================================================

st.subheader("Últimas inspeções")

st.info("Nenhuma inspeção cadastrada.")

st.divider()

# =====================================================
# RODAPÉ
# =====================================================

st.caption("SIGT - Sistema Integrado de Termografia | Versão 1.0")
