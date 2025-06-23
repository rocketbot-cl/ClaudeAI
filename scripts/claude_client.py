# Variable global para almacenar la conexión
mod_model_claude = None

def set_client(client):
    """
    Establece el cliente global de claude.
    """
    global mod_model_claude
    mod_model_claude = client

def get_client():
    """
    Obtiene el cliente global de claude.
    """
    global mod_model_claude
    return mod_model_claude