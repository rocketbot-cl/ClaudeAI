from claude_client import get_claude_client
import traceback
import os
import base64
from anthropic._exceptions import BadRequestError, RateLimitError, APIError, NotFoundError  #type: ignore
from typing import Optional, List, Union

def process_document(
    prompt: str,
    file_path: str,
    model: str,
    result_var: str,
    temperature: Optional[Union[float, str]] = None,
    max_tokens: Optional[Union[int, str]] = None,
    SetVar=None,
    PrintException=None
):
    """
    Procesa un documento (imagen o PDF) enviándolo a Claude junto con un prompt.
    """
    try:
        print("\n=== Processing document with ClaudeAI ===")
        
        SetVar(result_var, None)
        
        client = get_claude_client()
        if not client:
            error_msg = "ERROR: You must connect to ClaudeAI before using this command. Please run the connection module first."
            print(error_msg)
            raise Exception(error_msg)

        if not prompt:
            error_msg = "ERROR: Prompt is required."
            print(error_msg)
            raise Exception(error_msg)
            
        if not file_path or not os.path.exists(file_path):
            error_msg = f"ERROR: File path is required and must exist. Path: {file_path}"
            print(error_msg)
            raise Exception(error_msg)

        if not model:
            error_msg = "ERROR: Model is required."
            print(error_msg)
            raise Exception(error_msg)

        # Determinar el media type basado en la extensión
        ext = os.path.splitext(file_path)[1].lower()
        media_type = None
        block_type = "image"
        
        if ext in ['.png']:
            media_type = "image/png"
        elif ext in ['.jpg', '.jpeg']:
            media_type = "image/jpeg"
        elif ext in ['.gif']:
            media_type = "image/gif"
        elif ext in ['.webp']:
            media_type = "image/webp"
        elif ext == '.pdf':
            media_type = "application/pdf"
            block_type = "document"
        else:
            # Si no es una imagen soportada o PDF, intentamos leer como texto
            print(f"File extension {ext} not directly supported as image/document. Reading as text...")
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    file_content = f.read()
                prompt = f"{prompt}\n\nDocument content:\n{file_content}"
                block_type = "text"
            except Exception as e:
                error_msg = f"ERROR: Could not read file as text: {str(e)}"
                print(error_msg)
                raise Exception(error_msg)

        # Convertir parámetros
        try:
            temp = float(temperature) if temperature else 0.7
            max_tok = int(max_tokens) if max_tokens else 1024
        except ValueError as e:
            error_msg = f"ERROR: Error converting parameters: {str(e)}"
            print(error_msg)
            raise Exception(error_msg)

        # Preparar mensaje
        content = []
        if block_type in ["image", "document"]:
            with open(file_path, "rb") as f:
                data = base64.b64encode(f.read()).decode("utf-8")
            
            content.append({
                "type": block_type,
                "source": {
                    "type": "base64",
                    "media_type": media_type,
                    "data": data
                }
            })
            content.append({"type": "text", "text": prompt})
        else:
            content = prompt

        messages = [{"role": "user", "content": content}]

        print(f"- Model: {model}")
        print(f"- File: {file_path} ({block_type})")
        
        # Necesitamos el header de beta para PDFs
        extra_headers = {}
        if block_type == "document":
            extra_headers = {"anthropic-beta": "pdfs-2024-09-25"}

        print("\nGenerating response...")
        response = client.messages.create(
            messages=messages,
            model=model,
            temperature=temp,
            max_tokens=max_tok,
            extra_headers=extra_headers if extra_headers else None
        )
        
        generated_text = response.content[0].text
        print("\n✓ Document processed successfully!")
        SetVar(result_var, generated_text)

    except Exception as e:
        error_msg = f"Error processing document: {str(e)}"
        print(error_msg)
        if PrintException:
            PrintException()
        raise Exception(error_msg)