import functions as func

with open('registros/dados_financeiros.csv', encoding='utf-8') as registro:
    dados = [linha.strip() for linha in registro.readlines()[1:]]

    meses = [item.split(',')[0] for item in dados]
    valores = [int(item.split(',')[1]) for item in dados]
    mudancas = [valores[i] - valores[i - 1] for i in range(1, len(valores))]

    total_meses = len(meses)
    total_liquido = sum(value for value in valores)
    media = func.calcular_media(valores) 
    media_mudancas = func.calcular_media(mudancas)
    maior_aumento_lucros = max(mudancas)
    maior_reducao_lucros = min(mudancas)

    func.gerar_tabela(meses, mudancas, total_meses, 
                        total_liquido, media, media_mudancas, 
                        maior_aumento_lucros, maior_reducao_lucros)
    
    func.gerar_relatorio(meses, mudancas, total_meses, 
                        total_liquido, media, media_mudancas, 
                        maior_aumento_lucros, maior_reducao_lucros)
    
    print(f'\nRelatório da análise emitido com sucesso!')