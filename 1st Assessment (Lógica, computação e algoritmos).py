## Assessment for Pivotto's class

# Varáveis Globais:
renda_mensal = float(input("Digite aqui a sua renda mensal: "))
moradia = float(input("Quais seus gastos totais com moradia? " ))
educacao = float(input("Quanto você investe mensalmente em sua educação? "))
transporte = float(input("Quanto você gasta mensalmente em transporte? "))


def diagnostico(renda_mensal, moradia, educacao, transporte):
    # impressões
    print("Gastos percentuais:")
    print("Seus gastos totais com moradia são de R$", (moradia/renda_mensal)*100, "% de sua renda total.")
    print("Seus gastos totais com educação são de", (educacao / renda_mensal) * 100, "% de sua renda total.")
    print("Seus gastos totais com transporte são de", (transporte / renda_mensal) * 100, "% de sua renda total.")
    # impressões


    if (moradia <= 0.3*renda_mensal and educacao <= 0.2*renda_mensal and transporte <= 0.15*renda_mensal):
       print("Seus gastos estão dentro da margem recomendada, sua economia está saudável!")
    else:
        if (moradia > 0.3*renda_mensal):
            print("Seus gastos totais com moradia são de", (moradia/renda_mensal)*100, "% de sua renda total. Idealmente, o máximo de sua renda comprometida com moradia deveria ser de até R$ ", 0.3*renda_mensal)
        if (educacao > 0.2*renda_mensal):
            print("Seus gastos totais com educação são de", (educacao/renda_mensal)*100, "% de sua renda total. Idealmente, o máximo de sua renda comprometida com educação deveria ser de até R$ ", 0.2*renda_mensal)
        if (transporte > 0.15*renda_mensal):
            print("Seus gastos totais com moradia são de", (transporte/renda_mensal)*100, "% de sua renda total. Idealmente, o máximo de sua renda comprometida com transporte deveria ser de até R$ ", 0.15*renda_mensal)
diagnostico (renda_mensal, moradia, educacao, transporte)
