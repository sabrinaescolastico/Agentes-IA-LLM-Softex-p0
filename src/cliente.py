import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

LLM_API_URL = os.getenv("LLM_API_URL", "https://llm-internal.softex:9001")
LLM_MODEL = os.getenv("LLM_MODEL", "qwen3.5:9b-q4_K_M")

def chamar_llm(prompt_texto: str) -> str:
    """
    Envia um prompt para a API REST da LLM e retorna o texto gerado.
    Trata erros básicos de conexão e status HTTP.
    """
    # Endpoint padrão do Ollama para geração
    url = f"{LLM_API_URL}/api/generate"
    
    payload = {
        "model": LLM_MODEL,
        "prompt": prompt_texto,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=payload, timeout=30)
        
        # Tratamento de erros HTTP específicos
        if response.status_code == 401:
            raise PermissionError("Erro 401: Não autorizado. Verifique suas credenciais de acesso.")
        elif response.status_code == 429:
            raise ConnectionError("Erro 429: Limite de requisições excedido. Tente novamente mais tarde.")
        elif response.status_code != 200:
            raise RuntimeError(f"Erro na API da LLM: Status {response.status_code} - {response.text}")
            
        data = response.json()
        return data.get("response", "Nenhuma resposta retornada pelo modelo.")

    except requests.exceptions.Timeout:
        raise TimeoutError("A requisição para a LLM expirou (Timeout). O servidor demorou muito para responder.")
    except requests.exceptions.ConnectionError:
        raise ConnectionError("Falha de conexão com a LLM. Verifique se a URL está correta ou se a API está ativa.")