def load():
    input = open("input")
    values = [line.strip("\n").split(" | ") for line in input.readlines()]
    
    signal = []
    output = []
    for val in values:
        signal.append(val[0])
        output.append(val[1])

    return signal, output


def split_output(output):
    out = []
    for line in output:
        strings = line.split()
        for s in strings:
            out.append(s)
    return out

def split_lines(input):
    inp = [i.split() for i in input]
    return inp

def decode_signal(sig):
        #print(signal)

    decode = {}
    twothreefive = []
    zerosixnine = []
        
    for s in sig:
            
        match len(s):
            case 2: decode[1] = s
            case 4: decode[4] = s
            case 3: decode[7] = s
            case 7: decode[8] = s
            case 5: twothreefive.append(s)
            case 6: zerosixnine.append(s)

    decode = decode_zerosixnine(zerosixnine, decode)    

    print(decode)
    return decode
                
def decode_zerosixnine(zerosixnine, decode):
    four = decode[4]
    one = decode[1]

    for num in zerosixnine:
        test = [f in num for f in four]
        if all(test):
            decode[9] = num
        elif not all([f in num for f in one]):
            decode[6] = num
        else: decode[0] = num
          
    return decode
            
def decode_twothreefive(twothreefive, decode):
    one = decode[1]
    four = decode[4]
    

    return decode
    
def count_numbers(out):
    counts = 0

    for s in out:
        lenght = len(s)
        if lenght == 2 or lenght == 3 or lenght == 4 or lenght == 7:
            counts += 1

    return counts

if __name__ == "__main__":
    signal, output = load()
    out = split_output(output)
    counts = count_numbers(out)
    
    sig = split_lines(signal)
    out = split_lines(output)

    for s, o in zip(sig, out):
        decode = decode_signal(s)