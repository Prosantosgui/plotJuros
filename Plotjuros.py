import matplotlib.pyplot as plt
montante_inicial = float(input('Montante inicial igual a: '))
rendimento_periodo = float(input('Rendimento por período igual a(%): '))
valor_aporte = float(input('Valor do aporte igual a: '))
total_periodos = int(input('Total de períodos: '))

def calcular_juros_compostos(montante_inicial, rendimento_periodo, valor_aporte,total_periodos):
    periodos = []
    montante = []
    for i in range(total_periodos):
        montante_inicial =(montante_inicial + ((montante_inicial/100)) * rendimento_periodo)+valor_aporte
        print(f'\t{i+1} periodo, R$ {round(montante_inicial,2): .2f}')
        periodos.append(i+1)
        montante.append(round(montante_inicial,2))
        
    eixo_x = periodos
    eixo_y = montante
    plt.plot(periodos,montante, 'p-g')
    plt.title('Evolução do valor acumulado')
    plt.xlabel('Períodos')
    plt.ylabel('Montante')
    plt.show()
        
calcular_juros_compostos(montante_inicial, rendimento_periodo, valor_aporte, total_periodos)