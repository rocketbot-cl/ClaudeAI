from claude_client import get_claude_client  # Import function to get client
import traceback  # For capturing error traces


def get_models(result_var, SetVar, PrintException):
    """
    Obtiene la lista de modelos disponibles usando el cliente global de ClaudeAI.

    Args:
        result_var: Nombre de la variable para almacenar la lista de modelos
        SetVar: Función para establecer variables en Rocketbot
        PrintException: Función para imprimir excepciones en Rocketbot
    """
    try:
        print("\n=== Getting list of ClaudeAI models ===")
        
        # Establecer resultado por defecto
        SetVar(result_var, [])
        
        # Obtener el cliente
        client = get_claude_client()
        if not client:
            error_msg = "ERROR: You must connect to ClaudeAI before using this command. Please run the connection module first."
            print(error_msg)
            raise Exception(error_msg)

        print("Getting available models...")
        # Obtener la lista de modelos
        response = client.models.list()

        # Extraer los IDs de los modelos y organizarlos
        model_ids = sorted([model.id for model in response.data])
        
        if not model_ids:
            print("Warning! No available models found.")
        else:
            print("\nAvailable models:")
            for model_id in model_ids:
                print(f"- {model_id}")

        # Guardar la lista en la variable de resultado
        SetVar(result_var, model_ids)
        print("\n✓ Model list retrieved successfully!")

    except Exception as e:
        error_msg = f"Error getting model list: {str(e)}"
        print(error_msg)
        print("\nError details:")
        print(traceback.format_exc())
        if PrintException:
            PrintException()
        raise Exception(error_msg)