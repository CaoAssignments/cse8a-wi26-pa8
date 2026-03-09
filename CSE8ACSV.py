## Last Modified: 3/2026 by Paul Cao
import csv

def load_csv(filename):
    data = []
    with open(filename) as file_object:
        for row in csv.DictReader(file_object, delimiter=','):
            data.append(row)
    return data