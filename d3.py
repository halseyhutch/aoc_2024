import re


def p1():
    with open('data/d3.txt') as f:
        lines = f.readlines()
        input = ' '.join(lines)

    valid_instructions = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', input)
    result = sum([int(x) * int(y) for (x, y) in valid_instructions])

    return result


def p2():
    with open('data/d3.txt') as f:
        input = ' '.join(line.strip() for line in f)
        
    input_clean = re.sub(r"don\'t\(\).*?(do\(\))", "", input)
    # this is cheating a bit
    input_clean = re.sub(r"don\'t\(\)(?:(?!don\'t\(\)).)*?$", "", input_clean)
    input_clean = re.sub(r"don\'t\(\)(?:(?!don\'t\(\)).)*?$", "", input_clean)

    valid_instructions = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', input_clean)
    result = sum([int(x) * int(y) for (x, y) in valid_instructions])

    return result


if __name__ == '__main__':
    print(f'The answer to the first part of day three is {p1()}')
    print(f'The answer to the second part of day three is {p2()}')
