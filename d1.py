import numpy as np


def p1():
    data = np.loadtxt('data/d1.txt', delimiter='   ', dtype=int)
    sorted_data = np.sort(data, axis=0)
    result = np.absolute(sorted_data[:, 0] - sorted_data[:, 1]).sum()
    return result


def p2():
    data = np.loadtxt('data/d1.txt', delimiter='   ', dtype=int)
    unique_values, counts = np.unique(data[:, 1], return_counts=True)
    value_counts = {v: c for v, c in zip(unique_values, counts)}
    result = np.multiply(data[:, 0], np.vectorize(lambda x: value_counts.get(x, 0))(data[:, 0])).sum()
    return result


if __name__ == '__main__':
    print(f'The answer to the first part of day one is: {p1()}')
    print(f'The answer to the second part of day one is: {p2()}')
