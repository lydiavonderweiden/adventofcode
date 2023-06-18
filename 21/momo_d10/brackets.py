def check_line(line):
    opened = []
    for n in line:
        match n:
            case '(' | '[' | '{' | '<' : opened.append(n)
            case ')' : 
                if opened[-1] == '(' : opened.pop()
                else: return (3, '')
            case ']' :
                if opened[-1] == '[' : opened.pop()
                else: return (57, '')
            case '}' :
                if opened[-1] == '{' : opened.pop()
                else: return (1197, '')
            case '>' :
                if opened[-1] == '<' : opened.pop()
                else: return (25137, '')

    return (0, opened)

def complete(leftover):
    leftover.reverse()

    score = 0

    for l in leftover:
        match l:
            case '(' : score = score*5+1
            case '[' : score = score*5+2
            case '{' : score = score*5+3
            case '<' : score = score*5+4

    return score

def search_midscore(complete_scoring):
    complete_scoring.sort()
    index = len(complete_scoring) // 2
    return complete_scoring[index]


if __name__ == "__main__":
    with open("input.txt") as file:
        input = [line.strip('\n') for line in file.readlines()]

    score = 0
    complete_scoring = []

    for line in input:
        score_line, leftover = check_line(line)
        if score_line == 0:
            complete_scoring.append(complete(leftover))
        else:
            score = score + score_line



    print(score)
    print(search_midscore(complete_scoring))