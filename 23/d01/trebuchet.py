def find_values(liste):
    values = []

    for l in liste:
        length = len(l)
        i = 0
        while i < length and l[i].isalpha():
            i += 1
        forward = l[i]
        i = length-1
        while i > 0 and l[i].isalpha():
            i -= 1
        backward = l[i]
        values.append(int(forward+backward))


    return(sum(values))
        
def clean_up(liste):
    new_list = []
    for l in liste:
    
        print(l)
        i=3
        while i < len(l)+1:
            if "one" in l[0:i]: 
                l = l.replace("one", "1e", 1) 
                i -= 2
            if "two" in l[0:i]: 
                l = l.replace("two", "2o", 1)
                i -= 2
            if "three" in l[0:i]: 
                l = l.replace("three", "3e", 1)
                i -= 4
            if "four" in l[0:i]: 
                l = l.replace("four", "4", 1)
                i -= 3
            if "five" in l[0:i]: 
                l = l.replace("five", "5e", 1)
                i -= 3
            if "six" in l[0:i]: 
                l = l.replace("six", "6", 1)
                i -= 2
            if "seven" in l[0:i]: 
                l = l.replace("seven", "7n", 1)
                i -= 4
            if "eight" in l[0:i]: 
                l = l.replace("eight", "8t", 1)
                i -= 3
            if "nine" in l[0:i]: 
                l = l.replace("nine", "9e", 1)
                i -= 3
            i += 1
        print(l)
        new_list.append(l)
    return new_list

if __name__ == "__main__":
    with open('input.txt') as f:
        liste = [l.removesuffix('\n') for l in f.readlines()]
    liste = clean_up(liste)
    summe = find_values(liste)
    print(summe)