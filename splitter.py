import re 
from fa import *

def line_splitter(input_file):
    """Split a line into a list of words"""
    with open(input_file) as f:
        lines = f.readlines()
    return lines

def split(input_file):
    f = open(input_file, "r")
    inputfile = f.read()
    f.close()

    '''output = re.split(r'\s+'r'\n'r'\n'r'\n'r'\n'r'\n', inputfile) ini cara pertama tp ada galatnya anj
    output = inputfile.split(" ") iniyg bisa'''
    output = inputfile.split(" ")
    # print(output)
    #statement 
    operator = ['=', '!=', '==', '>=', '<=', '<', '>', ':', ',', '/', '-', r'\+', r'\*', r'\*\*', r'\'', r'\"', r'\'\'\'', r'\(', r'\)', 'none', 'not', 'true', 'false', r'\{', r'\}', r'\[', r'\]', 'for', '#', 'elif', 'else', 'while', 'break', 'continue', 'pass', 'def', 'return', 'range', 'raise', 'class', 'from', 'import', 'with', '%', '\n']
    operator2 = ['=', '!=', '==', '>=', '<=', '<', '>', ':', ',', '/', '-', '+', '*', '**', "'", '"', '(', ')', 'none', 'not', 'true', 'false', '{', '}', '[', ']', 'for', '#', 'elif', 'else', 'while', 'break', 'continue', 'pass', 'def', 'return', 'range', 'raise', 'class', 'from', 'import', 'with', '%','\n']

    # split the target string with the following pattern
    for op in operator:
        tempResult = []    
        for statement in output:
            elmt = re.split(r'[A..z]*(' + op + r')[A..z]*', statement)
            
            for splitted in elmt:
                tempResult.append(splitted) 
        output = tempResult

    # print(output)
    temp = []
    valid = True
    # print(output,"===")
    for statement in output:
        if statement in operator2:
            temp.append(statement)
            # print("didalam operator",statement)
        else:
            if statement == 'as' or statement == 'is' or statement == 'or' or statement == 'in' or statement == 'if' or statement == 'and':
                temp.append(statement)
                # print("asdkk",statement)
            else:
                # print("variabel:-",statement)
                if(cekVar(statement)):
                    # print(statement)
                    temp.append('a')
                elif(cekNum(statement)):
                    # print(statement)
                    temp.append('1')
                elif statement == '':
                    continue
    for i in range(len(temp)):
        if temp[i] == '\n':
            temp[i] = 'newline'
    return temp,valid
