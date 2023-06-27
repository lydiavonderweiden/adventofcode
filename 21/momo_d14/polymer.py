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

def pair_insertion(polymer, rules):
    blocks = split_blocks(polymer)

    for i, b in enumerate(blocks):
        for rule in rules:
            if b == rule[0]:
                blocks[i] = b[0] + rule[1] +b[1]
                break
    
    polymer = join_blocks(blocks)

    return polymer

if __name__ == "__main__":
    with open("test") as file:
        polymer = file.readline().strip()
        rules = [l.strip().split(" -> ") for l in file.readlines()]

    
    polymer = pair_insertion(polymer, rules)
    print(polymer)
