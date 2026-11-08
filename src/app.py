from src.cliente import chamar_llm

def main():
    print("=== Sumarizador Inteligente de Anotações Universitárias (P0) ===")
    print("Cole abaixo suas anotações de aula ou reunião (pressione Enter duas vezes para enviar):")
    
    # Captura múltiplas linhas de entrada do usuário
    linhas = []
    while True:
        try:
            linha = input()
            if linha == "":
                break
            linhas.append(linha)
        except EOFError:
            break
            
    texto_usuario = "\n".join(linhas)
    
    if not texto_usuario.strip():
        print("Nenhum texto foi fornecido. Encerrando.")
        return

    prompt_formatado = (
        "Por favor, atue como um assistente acadêmico. "
        "Abaixo estão minhas anotações brutas de aula/reunião. "
        "Gere um resumo estruturado contendo: "
        "1. Principais Tópicos, "
        "2. Decisões/Conclusões e "
        "3. Tarefas/Pendências (Action Items).\n\n"
        f"Anotações:\n{texto_usuario}"
    )

    print("\nProcessando resumo com a LLM...")
    try:
        resumo = chamar_llm(prompt_formatado)
        print("\n--- Resumo Gerado ---")
        print(resumo)
        print("---------------------")
    except Exception as e:
        print(f"\n[Erro]: {e}")

if __name__ == "__main__":
    main()