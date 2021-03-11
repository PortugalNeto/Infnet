print("Bem-vindo ao Sistema Nacional Eleitoral!\n")
i = 1
while i >= 1 and i < 2:
    idade = int(input("Por favor, informe a sua idade. "))

    # Verificação da idade
    while idade < 1:
        print("\nValor de idade informado inválido!\n")
        idade = int(input("Por favor, informe a sua idade: \n"))

    if idade < 16:
        print("\nVocê ainda não possui idade para votar.\n")

    elif idade >= 18 and idade < 70:
        print("\nSeu voto ou a justicativa de ausência é obrigatório!\n")

    elif idade >= 16 and idade < 18 or idade >= 70:
        print("\nSeu voto é facultativo.\n")

    i = int(input("Para repetir o prgrama digite 1, para finalizá-lo digite 2: "))
