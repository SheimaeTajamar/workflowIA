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
2. Crear y activar un entorno virtual
Se recomienda encarecidamente utilizar un entorno virtual aislado (venv) para evitar conflictos con otras librerías del sistema.

En Windows (PowerShell):

PowerShell
python -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser # Solo si hay problemas de permisos
.\venv\Scripts\Activate.ps1
3. Instalar las dependencias
Asegúrate de que tu entorno virtual esté activado ((venv)) y ejecuta:

Bash
pip install streamlit langchain langchain-openai langchain-classic langchain-community wikipedia numexpr
4. Configurar las variables de entorno
El proyecto utiliza un modelo desplegado en Azure OpenAI. Necesitas definir tus credenciales en el entorno antes de lanzar la aplicación. NO subas nunca tus claves reales a GitHub.

En tu consola (PowerShell), define las siguientes variables sustituyendo "TU_API_KEY_AQUI" por tu clave real:

PowerShell
$env:AZURE_OPENAI_API_KEY="TU_API_KEY_AQUI"
$env:AZURE_OPENAI_ENDPOINT="[https://modelon8n.openai.azure.com/](https://modelon8n.openai.azure.com/)"
$env:AZURE_OPENAI_API_VERSION="2025-01-01-preview"
Nota: Por defecto, el código asume que el despliegue se llama gpt-4o-mini. Puedes cambiarlo ajustando $env:AZURE_OPENAI_DEPLOYMENT_NAME.

5. Ejecutar la aplicación
Inicia el servidor local de Streamlit:

Bash
streamlit run app.py
La aplicación se abrirá automáticamente en tu navegador web (típicamente en http://localhost:8501).

📁 Estructura del Proyecto
app.py: Punto de entrada de la aplicación y definición de la interfaz gráfica con Streamlit.

agentes.py: Lógica de creación y ensamblaje de los agentes especialistas.

enrutador.py: Lógica de clasificación semántica para decidir qué agente debe actuar.

herramientas.py: Definición de las capacidades físicas (Wikipedia y Calculadora NumExpr) usando el decorador @tool.

azure_config.py: Módulo de conexión y autenticación con Azure OpenAI.

🔧 Tecnologías Utilizadas
Python 3

LangChain & LangChain-Classic: Orquestación de agentes y gestión de prompts.

Azure OpenAI: Motor LLM principal para inferencia y tool calling.

Streamlit: Framework para el desarrollo del frontend web interactivo.

NumExpr: Motor de evaluación matemática ultrarrápido para cálculos locales.

Desarrollado como parte del proyecto de consultoría en Inteligencia Artificial.


### ¿Qué hacer ahora?

1.  Crea el archivo `README.md` en tu carpeta del proyecto y pega el contenido anterior.
2.  En tu consola (PowerShell), ejecuta:
    ```powershell
    git add README.md
    git commit -m "Añadida documentación README.md"
    git push
    ```
¡Y listo! Tu repositorio de GitHub tendrá ahora un aspecto completamente profesional.
