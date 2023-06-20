import numpy as np

def cycle(input, flashcount):
    input += 1

    while np.size(np.nonzero(input > 9)):
        poi = np.nonzero(input > 9)
        
        flashcount += np.size(poi)/2
        input[poi] = 0
        for (p) in zip(poi[0], poi[1]):
            input = cascade(input, p)


    return input, flashcount

def cascade(input, point):
    if point[0] != 0 and point[0] != 9:
        n = [point[0]-1, point[0], point[0]+1]
    elif point[0] == 0:
        n = [point[0], point[0]+1]
    else:  n = [point[0]-1, point[0]]

    if point[1] != 0 and point[1] != 9:
        m = [point[1]-1, point[1], point[1]+1]
    elif point[1] == 0:
        m = [point[1], point[1]+1]
    else:  m = [point[1]-1, point[1]]

    for i in n:
        for j in m:
            if input[i][j] != 0:
                input[i][j] += 1

    return input

if __name__ == "__main__":
    with open("input") as file:
        f = [lines.strip() for lines in file.readlines()]   
    input = []
    for lines in f:
        input.append(np.array([int(n) for n in lines]))
    
    input = np.array(input)

    flashcount = 0

    #for i in range(100):
    #    input, flashcount = cycle(input, flashcount)
        #print(input)
        #print(flashcount)

    stepcount = 0

    while np.size(np.nonzero(input == 0)) != 200:
        stepcount += 1
        input, flashcount = cycle(input, flashcount)
        print(stepcount)
    
    print(flashcount)
    print(stepcount)
    #print(input)