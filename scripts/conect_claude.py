from claude import Claude  # type: ignore
from scripts.claude_client import set_client  # Import function to set client
import traceback  # Para capturar el trace completo del error

# Global variable to store connection
global mod_model_claude

try:
    if not mod_model_claude:  # type: ignore
        mod_model_claude = None
except NameError:
    mod_model_claude = None


def connect_to_claude(api_key, result_var, SetVar, PrintException):
    """
    Conectar a ClaudeAI usando el SDK oficial y almacenar la conexión globalmente.

    :param api_key: API key para autenticar con ClaudeAI.
    :param result_var: Nombre de la variable para almacenar el resultado.
    :param SetVar: Función para establecer variables en Rocketbot.
    :param PrintException: Función para imprimir excepciones en Rocketbot.
    """
    global mod_model_claude

    try:
        # Establecer el resultado como False por defecto
        SetVar(result_var, False)
        
        print("Starting connection with ClaudeAI...")
        print(f"Validating API key: {'*' * (len(api_key)-4) + api_key[-4:] if isinstance(api_key, str) else 'Not provided'}")
        
        # Validar que se proporcione la api_key
        if not isinstance(api_key, str):
            error_msg = "ERROR: API key must be a text string."
            print(error_msg)
            raise Exception(error_msg)
        
        api_key = api_key.strip()
        if not api_key:
            error_msg = "ERROR: API key is required. Please provide a valid API key."
            print(error_msg)
            raise Exception(error_msg)
            
        if not api_key.startswith("gsk_"):
            error_msg = "ERROR: API key must start with 'gsk_'. Please verify you are using a valid Claude API key."
            print(error_msg)
            raise Exception(error_msg)

        print("Attempting to initialize Claude client...")
        # Inicializar el cliente de Claude y almacenarlo globalmente
        client = Claude(api_key=api_key)

        try:
            # print("\nListando modelos disponibles...")
            # Obtener la lista de modelos
            models_response = client.models.list()
            
            # Extraer y mostrar los modelos disponibles
            # print("\nModelos disponibles:")
            available_models = []
            for model in models_response.data:
            #     print(f"- {model.id}")
                available_models.append(model.id)
            
            if not available_models:
                print("Warning! No available models found.")
            
            # Almacenar el cliente globalmente
            set_client(client)
            SetVar(result_var, True)
            print("\n✓ Connection established successfully!")

        except Exception as sdk_error:
            error_msg = ""
            if "401" in str(sdk_error):
                error_msg = "ERROR: Invalid or expired API key. Please verify your credentials and try again."
            else:
                error_msg = f"ERROR connecting to ClaudeAI: {str(sdk_error)}"
            print(error_msg)
            print("Detalles del error:")
            print(traceback.format_exc())
            raise Exception(error_msg)

    except Exception as e:
        # En caso de fallo, asegurarse de que la variable de resultado sea False
        SetVar(result_var, False)
        print("\nError completo:")
        print(traceback.format_exc())
        if PrintException:
            PrintException()
        raise e