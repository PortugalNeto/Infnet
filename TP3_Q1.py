#Teste de Perfomance 3, questão 1;
print("**********************************")
print("Bem-vindo ao Pivotto lanches Ltda.")
print("**********************************")

#Essa variável será a entrada do total de consumo
consumo = float(input("\nQuanto foi o valor total do seu consumo? "))

#Abaixo saberemos o número de pessoas que irão pagar a conta com o fluxo de exceção (pelo menos uma pessoa pagará toda a conta);
pessoas = int(input("\nQuantas pessoas irão rachar a conta? "))
while pessoas < 1 :
    print("Aqui se come aqui se paga! Por favor informe um valor válido de pessoas!")
    pessoas = int(input("Quantas pessoas irão rachar a conta? "))

#Aqui será definido o valor da taxa de serviço:
taxa = float(input("\nQuanto deseja pagar de taxa percentual (entre 0 e 100%) pelo serviço prestado? Não se apegue aos bens materiais: "))
while taxa < 0 or taxa > 100 :
    print("Por favor, um valor entre zero e cem por cento!")
    taxa = int(input("\nQuanto deseja pagar de taxa percentual? "))

#Calculamos agora o total da conta com o serviço e o valor por pessoa e imprimimos na tela:
total_conta = round(consumo * (1 + taxa/100), 2)
total_pessoa = round(total_conta / pessoas, 2)
total_conta = str(total_conta).replace('.', ',')
total_pessoa = str(total_pessoa).replace('.', ',')
print(f"\nO valor total da conta com a taxa é de R$ {total_conta} e o valor por pessoa de R$ {total_pessoa}.\n")
print("Volte sempre!")
