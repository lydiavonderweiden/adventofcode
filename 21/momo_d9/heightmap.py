import numpy as np

def search_minima(matrix):
    minima = []

    n, m = matrix.shape

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

if __name__  == "__main__":
    with open("input") as file:
        f = [lines.strip() for lines in file.readlines()]
    
    input = []
    for lines in f:
        input.append([int(n) for n in lines])
    
    input = np.array(input)
    results = search_minima(input)
    results = np.array(results)
    
    risk = calculate_risk(results)
    print(risk)
    
