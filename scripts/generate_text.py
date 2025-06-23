from claude_client import get_claude_client  # Import function to get client
import traceback  # For capturing error traces
from anthropic._exceptions import BadRequestError, RateLimitError, APIError, NotFoundError  #type: ignore
from typing import Optional, List, Union


def generate_text(
    prompt: str,
    model: str,
    result_var: str,
    temperature: Optional[Union[float, str]] = None,
    max_tokens: Optional[Union[int, str]] = None,
    stop_sequence: Optional[str] = None,
    system_prompt: Optional[str] = None,
    SetVar=None,
    PrintException=None
):
    """
    Genera texto usando el cliente de ClaudeAI y asigna el resultado a la variable especificada.

    Args:
        prompt: El prompt de entrada para la generación de texto.
        model: El modelo a usar para la generación de texto.
        result_var: Nombre de la variable para almacenar el texto generado.
        temperature: Temperatura para la generación (entre 0 y 1).
        max_tokens: Número máximo de tokens a generar.
        stop_sequence: Secuencia opcional para detener la generación.
        system_prompt: Prompt del sistema para dar contexto o instrucciones al modelo.
        SetVar: Función para establecer variables en Rocketbot.
        PrintException: Función para imprimir excepciones en Rocketbot.
    """
    try:
        print("\n=== Generating text with ClaudeAI ===")
        
        # Establecer resultado por defecto
        SetVar(result_var, None)
        
        # Obtener el cliente
        client = get_claude_client()
        if not client:
            error_msg = "ERROR: You must connect to ClaudeAI before using this command. Please run the connection module first."
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
            if not (0 <= temp <= 1):
                print(f"WARNING: Temperature {temp} is outside recommended range [0-1]. Clamping to range.")
                temp = max(0, min(temp, 1))
                
            max_tok = int(max_tokens) if max_tokens else 1024
            stop_sequences = [stop_sequence] if stop_sequence else None
            
        except ValueError as e:
            error_msg = f"ERROR: Error converting parameters: {str(e)}"
            print(error_msg)
            raise Exception(error_msg)

        # Preparar los mensajes
        messages = []
        
        # Agregar mensaje del sistema si existe
        if system_prompt:
            messages.append({
                "role": "system",
                "content": system_prompt
            })
            
        # Agregar el prompt del usuario
        messages.append({
            "role": "user",
            "content": prompt
        })

        print("\nGeneration parameters:")
        print(f"- Model: {model}")
        print(f"- Temperature: {temp}")
        print(f"- Maximum tokens: {max_tok}")
        print(f"- Stop sequences: {stop_sequences}")
        if system_prompt:
            print(f"- System prompt: {system_prompt[:100]}..." if len(system_prompt) > 100 else system_prompt)
        
        # Validar tokens antes de generar
        try:
            token_count = client.messages.count_tokens(
                messages=messages,
                model=model
            )
            print(f"\nToken count:")
            print(f"- Input tokens: {token_count.input}")
            print(f"- Output tokens (max): {max_tok}")
            print(f"- Total tokens: {token_count.input + max_tok}")
            
        except Exception as e:
            print(f"WARNING: Could not validate token count: {str(e)}")
        
        print("\nGenerating response...")
        # Crear la solicitud de chat completion
        try:
            response = client.messages.create(
                messages=messages,
                model=model,
                temperature=temp,
                max_tokens=max_tok,
                stop_sequences=stop_sequences
            )
            
        except BadRequestError as e:
            error_str = str(e)
            if "model_decommissioned" in error_str:
                error_msg = f"ERROR: The model '{model}' has been discontinued and is no longer supported.\n\nTo see available models you can:\n1. Run the 'Get available models' command from the module\n2. Check the official documentation at https://console.anthropic.com/docs/models"
                print(error_msg)
                raise Exception(error_msg)
            elif "does not support messages" in error_str:
                error_msg = f"ERROR: The model '{model}' is not compatible with text generation. This model is designed for another purpose. Please use a chat model like claude-3-opus or claude-3-sonnet."
                print(error_msg)
                raise Exception(error_msg)
            elif "token_limit_exceeded" in error_str:
                error_msg = f"ERROR: The total number of tokens (input + output) exceeds the model's limit. Try reducing your input text or maximum output tokens."
                print(error_msg)
                raise Exception(error_msg)
            raise e

        except NotFoundError as e:
            error_msg = f"ERROR: The model '{model}' was not found. This could mean:\n" \
                      f"1. The model name is incorrect\n" \
                      f"2. The model is not available in your region\n" \
                      f"3. The model requires special access\n\n" \
                      f"To see available models you can:\n" \
                      f"1. Run the 'Get available models' command from the module\n" \
                      f"2. Check the official documentation at https://console.anthropic.com/docs/models"
            print(error_msg)
            raise Exception(error_msg)
            
        except RateLimitError:
            error_msg = "ERROR: Rate limit exceeded. Please wait a moment before trying again."
            print(error_msg)
            raise Exception(error_msg)
            
        except APIError as e:
            error_str = str(e)
            if "404" in error_str and "not_found" in error_str.lower():
                error_msg = f"ERROR: The model '{model}' was not found. This could mean:\n" \
                          f"1. The model name is incorrect\n" \
                          f"2. The model is not available in your region\n" \
                          f"3. The model requires special access\n\n" \
                          f"To see available models you can:\n" \
                          f"1. Run the 'Get available models' command from the module\n" \
                          f"2. Check the official documentation at https://console.anthropic.com/docs/models"
            else:
                error_msg = f"ERROR: An API error occurred: {str(e)}\n" \
                          f"This could be due to:\n" \
                          f"1. Network connectivity issues\n" \
                          f"2. Server-side problems\n" \
                          f"3. Invalid API key or authentication issues\n\n" \
                          f"Please try again in a few moments. If the problem persists, verify your connection and API key."
            print(error_msg)
            raise Exception(error_msg)

        # Extraer el texto generado
        generated_text = response.content[0].text
        
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
