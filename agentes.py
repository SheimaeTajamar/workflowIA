# agentes.py
from azure_config import obtener_modelo_azure
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent

# Importamos las herramientas que creamos en herramientas.py
from herramientas import tool_wikipedia, tool_calculadora

def ejecutar_agente_investigador(consulta: str):
    """Agente que utiliza Wikipedia para buscar información factual."""
    llm = obtener_modelo_azure(temperatura=0.2)
    herramientas = [tool_wikipedia]
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Eres un Investigador Senior especializado en tecnología. Usa la herramienta de Wikipedia para buscar la información necesaria y responde a la consulta del usuario de forma detallada, clara y profesional."),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    
    agente = create_tool_calling_agent(llm, herramientas, prompt)
    ejecutor = AgentExecutor(agent=agente, tools=herramientas, verbose=True)
    
    return ejecutor.invoke({"input": consulta})["output"]

def ejecutar_agente_analista(consulta: str):
    """Agente que utiliza la calculadora para resolver problemas numéricos."""
    llm = obtener_modelo_azure(temperatura=0.0)
    herramientas = [tool_calculadora]
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Eres un Analista de Datos experto. Usa tu herramienta de Calculadora para resolver la consulta numérica o matemática del usuario de forma autónoma. Muestra los pasos brevemente y da el resultado final."),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    
    agente = create_tool_calling_agent(llm, herramientas, prompt)
    ejecutor = AgentExecutor(agent=agente, tools=herramientas, verbose=True)
    
    return ejecutor.invoke({"input": consulta})["output"]