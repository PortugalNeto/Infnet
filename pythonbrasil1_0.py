# notas de 100, 50, 10, 5 e 1;
# valor entre 10 e 600;


saca = 0
while not(saca >= 10 and saca <= 600):
    saca = int(input("Neste terminal está disponível o valor de 10 a 600 reais. Quanto você deseja sacar? "))

if (saca > 100):
    restodecem = saca % 100
    notascem = int((saca / 100))
    print(f"Recebe {notascem} nota(s) de cem reais.")

if (saca > 50):
    restodecinquenta = restodecem % 50
    notascinquenta = int((restodecem / 50))
    print(f"Recebe {notascinquenta} nota(s) de cinquenta reais.")

if (saca > 10):
    restodedez = restodecinquenta % 10
    notasdez = int((restodecinquenta / 10))
    print(f"Recebe {notasdez} nota(s) de dez reais.")

if (saca > 5):
    restodecinco = restodedez % 5
    notascinco = int((restodedez / 5))
    print(f"Recebe {notascinco} nota(s) de cinco reais.")

if (restodecinco > 0):
    print(f"Recebe {restodecinco} nota(s) de um real.")
