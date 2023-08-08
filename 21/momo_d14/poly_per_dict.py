from collections import defaultdict
from math import ceil

def init_dic(polymer:str):
    poly = {}

    for a,b in zip(polymer, polymer[1:]):
        if a+b not in poly:
            poly[a+b] = 1
        else: poly[a+b] += 1

    return poly

def poly_step(poly:dict, rules:list):
    changes = defaultdict(int)

    for r in rules:
        if r[0] in poly:
            n = poly[r[0]]
            changes[r[0]] -= n
            changes[r[0][0]+r[1]] += n
            changes[r[1]+ r[0][1]] += n

    for d, v in changes.items():
        if d in poly:
            poly[d] += v
        else: poly[d] = v

    return poly

def count_letters(poly:dict):
    count = defaultdict(int)

    for k, v in poly.items():
        count[k[0]] += v/2
        count[k[1]] += v/2

    for k, v in count.items():
        count[k] = ceil(v)

    sort = sorted(count.values())
    final = sort[-1] - sort[0]
    return final

if __name__ == "__main__":
    with open("input") as file:
        polymer = file.readline().strip()
        rules = [l.strip().split(" -> ") for l in file.readlines()[1:]]

    poly = init_dic(polymer)

    for i in range(40):
        poly = poly_step(poly, rules)
    
    final = count_letters(poly)
    print(final)