def p1():
    with open('data/d2.txt') as f:
        data = [[int(n) for n in line.rstrip().split(' ')] for line in f]

    result = 0
    for report in data:
        if is_report_safe(report):
            result += 1

    return result


def p2():
    with open('data/d2.txt') as f:
        data = [[int(n) for n in line.rstrip().split(' ')] for line in f]

    result = 0
    for report in data:
        if is_report_safe(report):
            result += 1
            continue
        else:
            for i in range(len(report)):
                sub_report = report[:i] + report[(i+1):]
                if is_report_safe(sub_report):
                    result += 1
                    break

    return result


def is_report_safe(report):
    diff = report[1] - report[0]
    if (abs(diff) > 3) or (diff == 0):
        return False
    elif diff > 0:
        ascending = True
    else:
        ascending = False
    for i in range(2, len(report)):
        diff = report[i] - report[i - 1]
        if ascending:
            if (diff < 1) or (diff > 3):
                return False
        else:
            if (diff < -3) or (diff > -1):
                return False
    return True


if __name__ == '__main__':
    print(f'The answer to the first part of day two is {p1()}')
    print(f'The answer to the second part of day two is {p2()}')
