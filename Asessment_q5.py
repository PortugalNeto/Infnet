import matplotlib.pyplot as plt

pib = open("Assessment_PIBs.csv", 'r')

pibs = pib.read()

pib.close()

pibs = pibs.splitlines()

# Definindo o cabeçalho e separando-o dos valores que serão manipulados
cabecalho = pibs[0]
cabecalho = cabecalho.split(',')
pibs = pibs[1:]

paises = []
anos = []

for i in range(0, len(pibs)):
  pibs[i] = pibs[i].split(',')
  paises.append(pibs[i][0])
  del pibs[i][0]

for item in range(1, 9):
  anos.append(cabecalho[item])

 

# Definindo nossa PRIMEIRA Função: busca de país e ano;
def pais_e_ano():
  pais = input("Digite o País que se deseja verificar o PIB: ")
  if pais in paises:
    ano = input("Digite o ano desejado (de 2013 a 2020): ")
    if ano in anos:
      print(f"PIB {pais} em {ano} é de US$ {pibs[paises.index(pais)][anos.index(ano)]} trilhões.")
    else:
      print("O ano não está disponível!")
  else:
    print("País indisponível")

pais_e_ano()

def variacao_periodo(paises, anos, pibs):
  for linha in range(0, 15):
    variacao = (float(pibs[linha][7]) / float(pibs[linha][0]) -1) * 100
    comprimento = len(paises[linha])
    
    print(f"\n\u2022 Variação percentual {paises[linha]}" + "_"*(25 - comprimento) + f"{variacao:.2f} % no período de 2013 a 2020")
variacao_periodo(paises, anos, pibs)

def graf_plot(pibs, anos, paises):

  pais = input("\nEscolha um país para ver o gráfico de variação do PIB (2013 a 2020): ")
  for i in range(0, 8):
    pibs[paises.index(pais)][i] = float(pibs[paises.index(pais)][i])
  print(pibs[paises.index(pais)])
  plt.plot(anos, pibs[paises.index(pais)])
  plt.title('Evolução do Pib')
  plt.xlabel('Anos')
  plt.ylabel('PIB em US$ trilhões')
  plt.ylim([min(pibs[paises.index(pais)]), max(pibs[paises.index(pais)])])  

  plt.show()
    
graf_plot(pibs, anos, paises)
