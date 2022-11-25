def CYK(word, grammar):
    '''CYK algorithm, returns True if word is in the grammar and if it is not , return false and what is the error'''
    # Initialize table
    errorWord = []
    table = [[[] for i in range(len(word))] for j in range(len(word))]
    # Fill the diagonal
    for i in range(len(word)):
        for rule in grammar.items():
            for terminal in rule[1]:
                if len(terminal) == 1 and word[i] == terminal[0]:
                    table[i][i].append(rule[0])
                elif len(terminal) == 1 and word[i] != terminal[0]:
                    errorWord.append(word[i])
    # Fill table
    for i in range(2, len(word)+1) :
        for j in range(len(word)-i+1):
            for k in range(j, j+i-1):
                for rule in grammar.items():
                    for terminal in rule[1]:
                        if len(terminal) == 2 and terminal[0] in table[j][k] and terminal[1] in table[k+1][j+i-1]:
                            table[j][j+i-1].append(rule[0])
                        elif len(terminal) == 2 and not(terminal[0] in table[j][k] and terminal[1] in table[k+1][j+i-1]):
                            errorWord.append(terminal[0])
                            errorWord.append(terminal[1])
    # Check if S is in the last cell
    if 'S0' in table[0][len(word)-1]:
        return True
    else:
        print("Error: ", errorWord)
        return False
