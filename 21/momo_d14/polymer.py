import numpy as np

def split_blocks(polymer):
    blocks =[ "".join([a,b])for a, b in zip(polymer, polymer[1:])]
    return blocks

def join_blocks(blocks):
    polymer = "".join(blocks[0])

    for b in blocks[1:]:
       polymer = polymer + "".join(b[1:])

    return polymer

def compare(b):
    for rule in rules:
        if b == rule[0]:
            b = b[0] + rule[1] +b[1]
            break

def pair_insertion(blocks, rules):
   
    for i, b in enumerate(blocks):
        for rule in rules:
            if b == rule[0]:
                blocks[i] = b[0] + rule[1] +b[1]
                break    

    return blocks

def rearrange_blocks(liste):
    new_list = []

    for b in liste:
        new_list.append(liste[0:1])
        new_list.append(liste[1:2])

    return new_list

def count_elements(polymer):
    polymer = [e for e in polymer]
    elements, count = np.unique(polymer, return_counts=True)
    
    diff = count.max()-count.min()
    print(diff)

if __name__ == "__main__":
    with open("input") as file:
        polymer = file.readline().strip()
        rules = [l.strip().split(" -> ") for l in file.readlines()]

    blocks = split_blocks(polymer)
    for i in range(40):
        polymer = pair_insertion(blocks, rules)
        blocks = rearrange_blocks(blocks)
        print(i)
    
    polymer = join_blocks(blocks)
    count_elements(polymer)
    #print(polymer)
    #print(len(polymer))