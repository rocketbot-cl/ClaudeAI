# Variable global para almacenar la conexión
claude_client = None

def set_claude_client(client):
    """
    Establece el cliente global de ClaudeAI.
    
    Args:
        client: Cliente de Anthropic inicializado
    """
    global claude_client
    claude_client = client

def get_claude_client():
    """
    Obtiene el cliente global de ClaudeAI.
    
    Returns:
        El cliente de Anthropic o None si no está inicializado
    """
    global claude_client
    return claude_client