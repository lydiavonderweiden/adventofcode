import numpy as np

def fold(dots, fold_along, line):
    if fold_along.endswith('x'):
        dots = fold_vertical(dots, line)
    elif fold_along.endswith('y'):
        dots = fold_horizontal(dots, line)
    
    return dots

def fold_vertical(dots, line):
    left = dots[:, 0:line]
    right = dots[:,line+1:np.shape(dots)[1]]
    right = np.flip(right, axis=1)

    if np.shape(right) != np.shape(left):
        diff = np.shape(left)[1]-np.shape(right)[1]
        zeros = np.zeros((np.shape(left)[0], diff))

        right = np.concatenate((zeros, right), axis=1)

    dots = left+right

    return dots

def fold_horizontal(dots, line):
    upper = dots[0:line]
    lower = dots[line+1:np.shape(dots)[0]]
    lower = np.flip(lower, axis=0)

    if np.shape(lower) != np.shape(upper):
        diff = np.shape(upper)[0]-np.shape(lower)[0]
        zeros = np.zeros((diff, np.shape(upper)[1]))

        lower = np.concatenate((zeros, lower), axis=0)

    dots = upper + lower

    return dots

def count_dots(dots):
    return np.size(np.nonzero(dots))/2



if __name__ == "__main__":
    #x, y = np.genfromtxt('test', dtype=int, delimiter=',', skip_footer=2, unpack=True)
    x, y = np.genfromtxt('input', dtype=int, delimiter=',', skip_footer=12, unpack=True)
    #the right tools for the job, these ain't it
    fold_along, line = np.genfromtxt('input', dtype=str, delimiter='=', skip_header=802, unpack=True, autostrip=True)
    #fold_along, line = np.genfromtxt('test', dtype=str, delimiter='=', skip_header=19, unpack=True, autostrip=True)


    line = np.array([int(i) for i in line])

    x_max = x.max()
    y_max = y.max()

    dots = np.zeros((y_max+1, x_max+1))

    for x_koord, y_koord in zip(x,y):
        dots[y_koord][x_koord] = 1

    for f, l in zip(fold_along, line):
        print(f)
        dots = fold(dots, f, l)
    #dots = fold(dots, fold_along[1], line[1])

    print(dots)

    print(count_dots(dots))
    np.savetxt('results.txt', dots, fmt='%1.0f')
