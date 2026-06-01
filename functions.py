def calcular_media(values):
    return sum(int(value) for value in values) / len(values)

def gerar_tabela(months, changes, total_months, net_amount, average, changes_average, profits_increase, profits_reduction):
    print('Análise Financeira')
    print('-'*30)
    print(f'Total de meses: {total_months}')
    print(f'Total: $ {net_amount}')
    print(f'Média: $ {average:.2f}')
    print(f'Variação da média: $ {changes_average:.2f}')
    print(f'Maior aumento nos lucros: {months[changes.index(profits_increase) + 1]} ($ {profits_increase})')
    print(f'Maior redução nos lucros: {months[changes.index(profits_reduction) + 1]} ($ {profits_reduction})')

def gerar_relatorio(months, changes, total_months, net_amount, average, changes_average, profits_increase, profits_reduction):
    with open('relatorios/analise_financeira.txt', 'w', encoding='utf-8') as relatorio:
        relatorio.write(f'Análise Financeira\n')
        relatorio.write(f'{"-"*30}\n')
        relatorio.write(f'Total de meses: {total_months}\n')
        relatorio.write(f'Total: $ {net_amount}\n')
        relatorio.write(f'Média: $ {average:.2f}\n')
        relatorio.write(f'Variação da média: $ {changes_average:.2f}\n')
        relatorio.write(f'Maior aumento nos lucros: {months[changes.index(profits_increase) + 1]} ($ {profits_increase})\n')
        relatorio.write(f'Maior redução nos lucros: {months[changes.index(profits_reduction) + 1]} ($ {profits_reduction})\n')