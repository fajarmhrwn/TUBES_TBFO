import re
import fa as fa
f = open("tes.py", "r")
inputfile = f.read()
f.close()

'''output = re.split(r'\s+'r'\n'r'\n'r'\n'r'\n'r'\n', inputfile) ini cara pertama tp ada galatnya anj
output = inputfile.split(" ") iniyg bisa'''
output = inputfile.split(" ")
print(output)
#statement 
operator = ['=', '!=', '==', '>=', '<=', '<', '>', ':', ',', '/', '-', r'\+', r'\*', r'\*\*', r'\'', r'\"', r'\'\'\'', r'\(', r'\)', 'none', 'not', 'true', 'false', r'\{', r'\}', r'\[', r'\]', 'for', '#', 'elif', 'else', 'while', 'break', 'continue', 'pass', 'def', 'return', 'range', 'raise', 'class', 'from', 'import', 'with', '%', r'\n', ' ']
operator2 = ['=', '!=', '==', '>=', '<=', '<', '>', ':', ',', '/', '-', '+', '*', '**', "'", '"', '(', ')', 'none', 'not', 'true', 'false', '{', '}', '[', ']', 'for', '#', 'elif', 'else', 'while', 'break', 'continue', 'pass', 'def', 'return', 'range', 'raise', 'class', 'from', 'import', 'with', '%']

# split the target string with the following pattern
for op in operator:
    tempResult = []    
    for statement in output:
        elmt = re.split(r'[A..z]*(' + op + r')[A..z]*', statement)
        
        for splitted in elmt:
            tempResult.append(splitted) 
    output = tempResult

print(output)
tempResult = []
valid = True
for statement in output:
    if statement in operator2:
        tempResult.append(statement)
    elif statement == '\n' :
        tempResult.append('newline')
    elif statement == 'in' or statement == 'if':
        tempResult.append(statement)
    elif(fa.isVariable(statement)):
        tempResult.append('a')
    elif(fa.isNumber(statement)):
        tempResult.append('1')
    else:
        continue
print(tempResult)

