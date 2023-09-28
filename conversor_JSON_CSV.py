import csv
import json
itens = []
with open('dados.json', mode ='r', encoding='utf-8') as arquivo_json:
    leitor_json = json.load(arquivo_json)
    for dict in leitor_json:
        itens.append(list(dict.values())) # aqui eu guardo todos os valores do dicionário em uma lista
    print(itens)