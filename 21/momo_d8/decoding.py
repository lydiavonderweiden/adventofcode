def load():
    input = open("input")
    #input = open("test.txt")
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
    decode = decode_twothreefive(twothreefive, decode)    

    return decode
                
def decode_zerosixnine(zerosixnine, decode):
    four = decode[4]
    one = decode[1]

    for num in zerosixnine:
        if all([f in num for f in four]):
            decode[9] = num
        elif not all([f in num for f in one]):
            decode[6] = num
        else: decode[0] = num
          
    return decode
            
def decode_twothreefive(twothreefive, decode):
    one = decode[1]
    six = decode[6]

    for f in one:
        if f not in six: test = f

    for num in twothreefive:
        if all([f in num for f in one]):
            decode[3] = num
        elif test in num:
            decode[2] = num
        else: decode[5] = num

    return decode

def decode_output(output, decode):
    num = []
    keys = [i for i in range(10)]
    for o in output:
        for k in keys:
            test = decode[k]
            if len(o) == len(test):
                code = [s in o for s in test]
                if all(code):
                    num.append(str(k))

    result = ''.join(num)

    return int(result)

    
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

    sum = 0

    for s, o in zip(sig, out):
        decode = decode_signal(s)
        sum = sum + decode_output(o, decode)
        print(sum)