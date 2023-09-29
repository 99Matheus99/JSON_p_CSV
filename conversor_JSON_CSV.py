import csv
import json
itens = []
with open('dados.json', mode ='r', encoding='utf-8') as arquivo_json:
    leitor_json = json.load(arquivo_json)
    for dict in leitor_json:
        itens.append(list(dict.values())) # aqui eu guardo todos os valores do dicionário em uma lista
with open('dados.csv', mode='w', encoding='utf-8', newline='') as arquivo_csv: # O newline ignora pulo de linhas
    escritor_csv = csv.writer(arquivo_csv)
    for linha in itens:
        escritor_csv.writerow(linha)