# herramientas.py
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import tool
import numexpr as ne

# Configuración de la API de Wikipedia
api_wrapper = WikipediaAPIWrapper(top_k_results=2, doc_content_chars_max=2000, lang="es")

@tool
def tool_wikipedia(consulta: str) -> str:
    """
    Útil para buscar información factual, conceptos, historia o definiciones en Wikipedia. 
    La entrada DEBE ser únicamente el concepto clave (1 o 2 palabras máximo).
    """
    try:
        termino = str(consulta) if not isinstance(consulta, dict) else str(list(consulta.values())[0])
        return api_wrapper.run(termino)
    except Exception as e:
        return f"Error en Wikipedia: {str(e)}. Intenta buscar un concepto más corto."

@tool
def tool_calculadora(expresion: str) -> str:
    """
    Útil para resolver cálculos numéricos o problemas matemáticos. 
    La entrada DEBE ser exclusivamente una expresión matemática pura (ej: '144**0.5 * 5' o '2 + 2').
    """
    try:
        if isinstance(expresion, dict):
            expresion = list(expresion.values())[0]
            
        exp_limpia = str(expresion).replace("`", "").replace("math", "").strip()
        resultado = ne.evaluate(exp_limpia)
        return str(resultado)
    except Exception as e:
        return f"Error al calcular: {str(e)}. Intenta replantear la operación matemática."