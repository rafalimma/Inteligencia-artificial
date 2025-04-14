import csv

def buscalarcgura():
    with open("ed02-puzzle8.csv", 'rb') as file:
        estado_inicial = csv.reader(file)
        ...