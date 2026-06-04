# 🧠 Enjambre de Consultoría IA

Este proyecto implementa un sistema multi-agente (enjambre) diseñado para responder consultas técnicas, matemáticas y de investigación. Utiliza un modelo de lenguaje grande (LLM) alojado en Azure OpenAI para orquestar la toma de decisiones y ejecutar herramientas específicas.

La arquitectura se basa en un patrón de enrutamiento semántico: un "Director de Operaciones" analiza la consulta del usuario y delega la tarea al agente especialista más capacitado (Investigador o Analista).

## 🏗️ Arquitectura y Flujo

1.  **Interfaz de Usuario:** Construida con [Streamlit](https://streamlit.io/), proporciona un entorno web limpio y minimalista.
2.  **Enrutador (Router AI):** Un modelo clasificador estricto que determina la intención del usuario (Cálculo o Investigación) basándose en *Natural Language Processing (NLP)*.
3.  **Agentes Especializados:**
    * **Investigador Senior:** Conectado a la API de Wikipedia para recuperar información factual y estructurada.
    * **Analista de Datos:** Equipado con un motor de cálculo local (`numexpr`) para resolver ecuaciones matemáticas complejas sin gastar tokens extra en el LLM.
4.  **Ejecución de Herramientas (*Tool Calling*):** Se utiliza el decorador `@tool` nativo de LangChain para asegurar que los datos estructurados enviados por Azure OpenAI (JSON) se interpreten correctamente, evitando errores de validación y fallos de formato.

## 🚀 Instalación y Configuración

Sigue estos pasos para desplegar el proyecto en tu entorno local.

### 1. Clonar el repositorio
```bash
git clone [https://github.com/SheimaeTajamar/workflowIA.git](https://github.com/SheimaeTajamar/workflowIA.git)
cd workflowIA
python -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser # Solo si hay problemas de permisos
.\venv\Scripts\Activate.ps1


pip install streamlit langchain langchain-openai langchain-classic langchain-community wikipedia numexpr

$env:AZURE_OPENAI_API_KEY="TU_API_KEY_AQUI"
$env:AZURE_OPENAI_ENDPOINT="[https://modelon8n.openai.azure.com/](https://modelon8n.openai.azure.com/)"
$env:AZURE_OPENAI_API_VERSION="2025-01-01-preview"

streamlit run app.py
