import csv
import json
itens = []
try:
    with open('dados.json', mode ='r', encoding='utf-8') as arquivo_json:
        print(f'Arquivo {arquivo_json.name} encontrado...')
        leitor_json = json.load(arquivo_json) # o leitor_json serve basicamente como um ponteiro 
        for dict in leitor_json:
            itens.append(list(dict.values())) # aqui eu guardo todos os valores do dicionário em uma lista
        print(f'Processando {len(itens)} registros...')
        with open('dados.csv', mode='w', encoding='utf-8', newline='') as arquivo_csv: # O newline ignora pulo de linhas
            escritor_csv = csv.writer(arquivo_csv)
            for linha in itens:
                escritor_csv.writerow(linha)
            print(f'Arquivo {arquivo_csv.name} gerado com sucesso!')
except FileNotFoundError:
    print('Arquivo não encontrado.')