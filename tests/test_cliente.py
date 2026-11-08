import pytest
import requests
import requests_mock
from src.cliente import chamar_llm

def test_chamar_llm_sucesso():
    """Testa se a função retorna corretamente a resposta simulada da API."""
    url_mock = "https://llm-internal.softex:9001/api/generate"
    
    with requests_mock.Mocker() as m:
        m.post(url_mock, json={"response": "Resumo gerado com sucesso pelo mock!"}, status_code=200)
        
        resultado = chamar_llm("Texto de teste")
        assert resultado == "Resumo gerado com sucesso pelo mock!"

def test_chamar_llm_erro_conexao():
    """Testa se levanta exceção adequada em caso de falha de conexão."""
    url_mock = "https://llm-internal.softex:9001/api/generate"
    
    with requests_mock.Mocker() as m:
        m.post(url_mock, exc=requests.exceptions.ConnectionError)
        
        with pytest.raises(ConnectionError):
            chamar_llm("Texto de teste")