import numpy as np

def search_minima(matrix):
    minima = []

    n, m = matrix.shape

    #Für Java oder so wäre das vollkommen okay, aber python ist das nicht
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                if matrix[j+1, i]>matrix[j,i] and matrix[j, i+1]>matrix[j,i]:
                    minima.append(matrix[j,i])
            elif i == m-1 and j == n-1:
                if matrix[j-1, i] > matrix[j,i] and matrix[j,i-1]>matrix[j,i]:
                    minima.append(matrix[j,i])
            elif i == m-1:
                if matrix[j-1, i] > matrix[j,i] and matrix[j,i-1]>matrix[j,i] and matrix[j+1, i] > matrix[j,i]:
                    minima.append(matrix[j,i])
            elif j == n-1:
                if matrix[j-1, i] > matrix[j,i] and matrix[j,i+1]>matrix[j,i] and matrix[j, i-1] > matrix[j,i]:
                    minima.append(matrix[j,i])
            elif i == 0:
                if matrix[j-1, i] > matrix[j,i] and matrix[j,i+1]>matrix[j,i] and matrix[j+1, i] > matrix[j,i]:
                    minima.append(matrix[j,i])
            elif j == 0:
                if matrix[j+1, i] > matrix[j,i] and matrix[j,i+1]>matrix[j,i] and matrix[j, i-1] > matrix[j,i]:
                    minima.append(matrix[j,i])
            else:
                if matrix[j-1, i] > matrix[j,i] and matrix[j,i+1]>matrix[j,i] and matrix[j, i-1] > matrix[j,i] and matrix[j+1, i]> matrix[j,i]:
                    minima.append(matrix[j,i])

    return minima

def calculate_risk(minima):
    minima = minima+1
    risk = minima.sum()
    #print(minima)

    return risk

def find_basins(input):
    basins = []

    while( np.size(np.nonzero(input-9),1 ) > 0):
        points = np.nonzero(input-9)
        input, size = calculate_basin(input, (points[0][0], points[1][0]), 0)
        basins.append(size)

    return basins

def calculate_basin(input, point, size):
    if input[point[0]][point[1]] != 9:
        input[point[0]][point[1]] = 9
        size = size+1
        #rekursion!
        if point[0] != 0: #left
            input, size = calculate_basin(input, (point[0]-1, point[1]), size)
        if point[0] < input.shape[0]-1: #right
            input, size = calculate_basin(input, (point[0]+1, point[1]), size)
        if point[1] < input.shape[1]-1: #up
            input, size = calculate_basin(input, (point[0], point[1]+1), size)
        if point[1]!=  0:#len(input)-1:  #down
            input, size = calculate_basin(input, (point[0], point[1]-1), size)
    return input, size

def calculate_basin_results(basins):
    basins = np.array(sorted(basins))
    result = np.multiply(basins[-1], basins[-2])
    result = np.multiply(result, basins[-3])
    return result
    


if __name__  == "__main__":
    with open("input") as file:
    #with open("test") as file:
        f = [lines.strip() for lines in file.readlines()]
    
    input = []
    for lines in f:
        input.append(np.array([int(n) for n in lines]))
    
    input = np.array(input)
    
    results = search_minima(input)
    results = np.array(results)

    risk = calculate_risk(results)
    print(risk)
    liste = np.nonzero(input-9)
    basins = find_basins(input)
    result = calculate_basin_results(basins)
    print(result)


    
