import matplotlib.pyplot

renda = 10000
juros_periodo = (0.54/100)
t = 1
periodos = []
renda_periodo = []

while (t <= 120):

    renda = renda * (juros_periodo + 1) + 1000
    print(f"Após {t} períodos, a renda será de R$ {renda}")
    periodos.append(t)
    t = t +1
    renda_periodo.append(renda)

matplotlib.pyplot.plot(periodos, renda_periodo)
matplotlib.pyplot.show()
