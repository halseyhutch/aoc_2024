import numpy as np

def p1():
    with open('data/d4.txt') as f:
        data = [[str(n) for n in line.rstrip()] for line in f]
        data = np.array(data)

    word = 'XMAS'
    res = 0
    n = len(word)

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            # down
            if (i + len(word)) <= data.shape[0]:
                if ''.join(data[i:(i+n), j]) in [word, word[::-1]]:
                    res += 1
            # down and right
            if ((i + len(word)) <= data.shape[0]) and ((j + len(word)) <= data.shape[1]):
                if ''.join(data[i:(i+n), j:(j+n)].diagonal()) in [word, word[::-1]]:
                    res += 1
            # right
            if (j + len(word)) <= data.shape[1]:
                if ''.join(data[i, j:(j+n)]) in [word, word[::-1]]:
                    res += 1
            # up and right
            if ((i + 1 - len(word)) >= 0) and ((j + len(word)) <= data.shape[1]):
                if ''.join(np.flipud(data[(i+1-n):(i+1), j:(j+n)]).diagonal()) in [word, word[::-1]]:
                    res += 1
    
    return res


def p2():
    with open('data/d4.txt') as f:
        data = [[str(n) for n in line.rstrip()] for line in f]
        data = np.array(data)
    
    matches = [
        np.array(['M', 'S', 'A', 'M', 'S']),
        np.array(['M', 'M', 'A', 'S', 'S']),
        np.array(['S', 'S', 'A', 'M', 'M']),
        np.array(['S', 'M', 'A', 'S', 'M'])
    ]

    res = 0
    for i in range(data.shape[0] - 2):
        for j in range(data.shape[1] - 2):
            sub_matrix = data[i:(i+3), j:(j+3)]
            for match in matches:
                if (sub_matrix[[0, 0, 1, 2, 2], [0, 2, 1, 0, 2]] == match).all():
                    res += 1
                    # a pattern can't be multiple matches
                    continue

    return res
    

if __name__ == '__main__':
    print(f'The answer to the first part of day three is {p1()}')
    print(f'The answer to the second part of day three is {p2()}')
