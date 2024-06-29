variavel = []
numero_secreto = "MQO=" 


print("Como vai funcionar este desafio: \n")
print("O jogo consiste em voce acertar o numero secreto que esta em formato de um hash.")
print("Porem é melhor, voce colocar o numero em decimal para descobrir as dicas do numero secreto")
print(f"\nVoce tem  5 tentativas\n")
print("Responda algumas perguntas antes de iniciar: ")
print("\n")

pedir_nome = input("Digite seu usuario: ").lower()
print(f"\nBem vindo: Sr.{pedir_nome}\n")

for contador in range(5,-1,-1):


    pedir_mensagem = input(f"Sr.{pedir_nome} descubra o numero secreto: ").upper()
    
    if numero_secreto in pedir_mensagem:
        print(f"Sr.{pedir_nome} acertou o hash\n")
        print(f"Success 200: {contador} tentativas!!")
        print(f"Valor do hash: {numero_secreto}")
        quit()

    elif pedir_mensagem == "1":
        print("\nVoce acertou em decimal, agora coloca na base certa do hash")
        print(f"{contador} tentativas\n")
    
    elif pedir_mensagem == "2":
        print(f"\nError 404: {contador} tentativas\n")

    elif "1" not in pedir_mensagem:
        print("\nUma dica - Decifra esse hash - \n")
        print("O numero nao esta entre Mwo= e MTAK\n") 
        print(f"{contador} tentativas\n")
    
print("Tente Novamente!!!")

        
        
