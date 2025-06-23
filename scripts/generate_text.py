from scripts.claude_client import get_client  # Import function to get client
import traceback  # For capturing error traces
from claude._exceptions import BadRequestError  #type: ignore


def generate_text(prompt, model, result_var, temperature, max_tokens, stop_sequence, SetVar, PrintException):
    """
    Genera texto usando el cliente de Claude AI y asigna el resultado a la variable especificada.
    
    :param prompt: El prompt de entrada para la generación de texto.
    :param model: El modelo a usar para la generación de texto.
    :param result_var: Nombre de la variable para almacenar el texto generado.
    :param temperature: Temperatura para la generación (entre 0 y 2).
    :param max_tokens: Número máximo de tokens a generar.
    :param stop_sequence: Secuencia opcional para detener la generación.
    :param SetVar: Función para establecer variables en Rocketbot.
    :param PrintException: Función para imprimir excepciones en Rocketbot.
    """
    try:
        print("\n=== Generating text with Claude AI ===")
        
        # Establecer resultado por defecto
        SetVar(result_var, None)
        
        # Obtener el cliente
        client = get_client()
        if not client:
            error_msg = "ERROR: You must connect to Claude AI before using this command. Please run the connection module first."
            print(error_msg)
            raise Exception(error_msg)

        # Validar parámetros requeridos
        if not prompt:
            error_msg = "ERROR: Prompt is required."
            print(error_msg)
            raise Exception(error_msg)
            
        if not model:
            error_msg = "ERROR: Model is required."
            print(error_msg)
            raise Exception(error_msg)

        # Convertir parámetros a sus tipos correctos
        try:
            temp = float(temperature) if temperature else 0.7
            max_tok = int(max_tokens) if max_tokens else 100
            stop = [stop_sequence] if stop_sequence else None
        except ValueError as e:
            error_msg = f"ERROR: Error converting parameters: {str(e)}"
            print(error_msg)
            raise Exception(error_msg)

        print("\nGeneration parameters:")
        print(f"- Model: {model}")
        print(f"- Temperature: {temp}")
        print(f"- Maximum tokens: {max_tok}")
        print(f"- Stop sequence: {stop}")
        
        print("\nGenerating response...")
        # Crear la solicitud de chat completion
        try:
            response = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model=model,
                temperature=temp,
                max_completion_tokens=max_tok,
                stop=stop
            )
        except BadRequestError as e:
            error_str = str(e)
            if "model_decommissioned" in error_str:
                error_msg = f"ERROR: The model '{model}' has been discontinued and is no longer supported.\n\nTo see available models you can:\n1. Run the 'Get available models' command from the module\n2. Check the official documentation at https://console.claude.com/docs/models"
                print(error_msg)
                raise Exception(error_msg)
            elif "does not support chat completions" in error_str:
                error_msg = f"ERROR: The model '{model}' is not compatible with text generation. This model is designed for another purpose (e.g., audio transcription). Please use a chat model like llama or gemma."
                print(error_msg)
                raise Exception(error_msg)
            raise e

        # Extraer el texto generado
        generated_text = response.choices[0].message.content
        
        print("\n✓ Text generated successfully!")
        
        # Guardar el resultado
        SetVar(result_var, generated_text)

    except Exception as e:
        error_msg = f"Error generating text: {str(e)}"
        print(error_msg)
        print("\nError details:")
        print(traceback.format_exc())
        if PrintException:
            PrintException()
        raise Exception(error_msg)
