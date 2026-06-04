# app.py
import streamlit as st

# Importamos la lógica desde nuestros nuevos módulos
from enrutador import clasificar_intencion
from agentes import ejecutar_agente_investigador, ejecutar_agente_analista

# ==========================================
# CONFIGURACIÓN DE LA INTERFAZ (UI)
# ==========================================
st.set_page_config(
    page_title="Enjambre IA | Consultoría",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Enjambre de Consultoría IA")
st.markdown("Introduce tu consulta. Nuestro **Router AI** decidirá qué especialista debe resolverla.")
st.divider()

# ==========================================
# EJECUCIÓN PRINCIPAL (FORMULARIO WEB)
# ==========================================
with st.form(key="formulario_consulta"):
    consulta_usuario = st.text_area(
        "Consulta Técnica o Matemática", 
        placeholder="Ej: ¿Qué es el modelo Transformer? o ¿Cuánto es la raíz cuadrada de 144 por 5?"
    )
    boton_enviar = st.form_submit_button(label="Enviar Consulta al Enjambre")

if boton_enviar:
    if not consulta_usuario.strip():
        st.warning("⚠️ Por favor, introduce una consulta antes de enviar.")
    else:
        with st.spinner("El Director de Operaciones está analizando la solicitud..."):
            intencion = clasificar_intencion(consulta_usuario)
            st.info(f"🔀 El Router ha clasificado la consulta como: **{intencion.upper()}**")
            
        with st.spinner("El Agente especializado está trabajando en la respuesta..."):
            try:
                if intencion == "calculo":
                    respuesta_final = ejecutar_agente_analista(consulta_usuario)
                    agente_usado = "Analista de Datos"
                else: 
                    respuesta_final = ejecutar_agente_investigador(consulta_usuario)
                    agente_usado = "Investigador Senior"
                
                st.success(f"✅ Tarea completada por: **{agente_usado}**")
                
                with st.container(border=True):
                    st.markdown("### Respuesta del Agente")
                    st.markdown(respuesta_final)
                    
            except Exception as e:
                st.error(f"❌ Ha ocurrido un error durante la ejecución del agente: {str(e)}")