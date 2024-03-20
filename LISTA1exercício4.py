def apresentar_questao(pergunta, alternativas, resposta_correta):
    # Imprime a pergunta na tela
    print(pergunta)
    
    # Apresenta as alternativas ao usuário
    for letra, alternativa in zip("abcde", alternativas):
        print(f"{letra}) {alternativa}")
    
    # Solicita ao usuário que digite sua resposta
    resposta_usuario = input("Digite a letra correspondente à sua resposta: ").lower()
    
    # Verifica se a resposta do usuário está correta e exibe o resultado
    if resposta_usuario == resposta_correta:
        print(f"Você respondeu alternativa {resposta_usuario}. A resposta correta é a alternativa {resposta_correta}.")
    else:
        print(f"Você respondeu alternativa {resposta_usuario}. A resposta correta é a alternativa {resposta_correta}.")

def main():
    # Exemplo de questão
    pergunta = "Qual é o verdadeiro nome do super-herói Batman?"
    alternativas = ["Bruce Wayne", "Clark Kent", "Peter Parker", "Tony Stark", "Steve Rogers"]
    resposta_correta = 'a'
    
    # Apresenta a questão ao usuário e verifica a resposta
    apresentar_questao(pergunta, alternativas, resposta_correta)

if __name__ == "__main__":
    main()
