import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, encoding="utf-8") as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        filtered = []
        for row in jobs_reader:
            filtered.append(row)
        return filtered
