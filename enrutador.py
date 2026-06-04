# enrutador.py
from azure_config import obtener_modelo_azure
from langchain_core.prompts import ChatPromptTemplate

def clasificar_intencion(consulta: str) -> str:
    """
    Analiza el prompt del usuario y decide el flujo a seguir.
    """
    llm_router = obtener_modelo_azure(temperatura=0.0)
    
    prompt_router = ChatPromptTemplate.from_messages([
        ("system", "You are a strict NLP intent classification pipeline. Your ONLY function is to analyze the user's input and route it to the correct downstream agent. CRITICAL GUARDRAILS: 1. You must NEVER answer the user's query, solve equations, or provide conversational text. 2. You must output exactly ONE word from the allowed categories below. Do not include punctuation, markdown, or explanations. ALLOWED CATEGORIES: - If the user's input contains mathematical operations, requests for calculations, numerical logic, or data counting, output exactly: calculo - If the user's input asks for factual information, definitions, historical events, theory, or general knowledge, output exactly: investigacion"),
        ("human", "{consulta}")
    ])
    
    cadena_clasificacion = prompt_router | llm_router
    respuesta = cadena_clasificacion.invoke({"consulta": consulta})
    
    return respuesta.content.strip().lower()