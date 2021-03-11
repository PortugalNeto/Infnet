vencedor = None
notas = []
nomes = []
vencedor_nota = None
posicoes = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']

for i in range(0, 5):

    nome = input(f"Informe nome do {posicoes[i]} participante: ")
    nomes.append(nome)
    nota = float(input(f"Informe a nota do {posicoes[i]} participante: "))
    while nota < 0 or nota > 10:
        print("Digite um valor de nota válido (entre zero e 10)")
        nota = float(input(f"Informe a nota do {posicoes[i]} participante: "))
    notas.append(nota)

vencedor_nota = max(notas)
vencedor = nomes[notas.index(vencedor_nota)]
vencedor_nota = str(vencedor_nota).replace('.', ',')
print (f'O vencedor é {vencedor} com nota de: ', vencedor_nota)
