import numpy as np

if __name__ == "__main__":
    field = np.genfromtxt("test.txt", dtype=str,delimiter=1, comments=None)
    print(field)