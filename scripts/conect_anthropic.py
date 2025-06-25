from anthropic import Anthropic #type: ignore
import traceback
from claude_client import set_claude_client

def connect_to_anthropic(api_key, result_var, SetVar, PrintException):
    """
    Conectar a ClaudeAI usando el SDK oficial.

    Args:
        api_key: API key para autenticar con ClaudeAI
        result_var: Nombre de la variable para almacenar el resultado
        SetVar: Función para establecer variables en Rocketbot
        PrintException: Función para imprimir excepciones en Rocketbot
    """
    try:
        # Establecer el resultado como False por defecto
        SetVar(result_var, False)
        
        print("Starting connection with Claude AI...")
        print(f"API Key (masked): {'*' * (len(api_key)-4) + api_key[-4:] if api_key else 'Not provided'}")
        
        # Validaciones básicas
        if not api_key or not isinstance(api_key, str):
            raise ValueError("API key must be a valid string")
            
        if not api_key.startswith("sk-"):
            raise ValueError("API key must start with 'sk-'")
        
        # Intentar crear el cliente y listar modelos
        client = Anthropic(api_key=api_key)
        set_claude_client(client)
        models = client.models.list()
        
        # Mostrar modelos disponibles
        print("Available models:", [model.id for model in models.data])
        SetVar(result_var, True)
        print("✓ Connection established successfully!")
        
    except Exception as e:
        print(f"Error during connection: {str(e)}")
        print(traceback.format_exc())
        SetVar(result_var, False)
        if PrintException:
            PrintException()
        raise