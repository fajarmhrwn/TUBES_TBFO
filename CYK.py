def CYK(word, grammar):
    '''CYK algorithm, returns True if word is in the grammar and if it is not , return false and what is the error'''
    # Initialize table
    table = [[set([]) for i in range(len(word[0]))] for j in range(len(word[0]))]
    # Fill the diagonal
    for i in range(len(word[0])):
        for rule in grammar.items():
            for terminal in rule[1]:
                if len(terminal) == 1 and word[0][i] == terminal[0]:
                    table[i][i].add(rule[0])
    # Fill table
    for i in range(2, len(word[0])+1) :
        for j in range(len(word[0])-i+1):
            for k in range(j, j+i-1):
                for rule in grammar.items():
                    for terminal in rule[1]:
                        if len(terminal) == 2 and terminal[0] in table[j][k] and terminal[1] in table[k+1][j+i-1]:
                            table[j][j+i-1].add(rule[0])
    # Check if S is in the last cell
    if 'S0' in table[0][len(word[0])-1]:
        return True
    else:
        return False
