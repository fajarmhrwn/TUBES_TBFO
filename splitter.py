import re 
import fa as fa

def line_splitter(input_file):
    """Split a line into a list of words"""
    with open(input_file) as f:
        lines = f.readlines()
    return lines

def split(input_file):
    # lihat punya aira
    f=open(input_file,'r')
    lines=f.read()
    f.close()
    
    output = []
    # split the target string on the occurance of one or more whitespace characters
    inputfile = inputfile.split(" ")
    for statement in inputfile:
        if statement != '':
            output.append(statement)

    operator = ['=', '!=', '==', '>=', '<=', '<', '>', ':', ',', '/', '-', r'\+', r'\*', r'\*\*', r'\'', r'\"', r'\'\'\'', r'\(', r'\)', 'none', 'not', 'true', 'false', r'\{', r'\}', r'\[', r'\]', 'for', '#', 'elif', 'else', 'while', 'break', 'continue', 'pass', 'def', 'return', 'range', 'raise', 'class', 'from', 'import', 'with', '%', '\n']
    operator2 = ['=', '!=', '==', '>=', '<=', '<', '>', ':', ',', '/', '-', '+', '*', '**', "'", '"', '(', ')', 'none', 'not', 'true', 'false', '{', '}', '[', ']', 'for', '#', 'elif', 'else', 'while', 'break', 'continue', 'pass', 'def', 'return', 'range', 'raise', 'class', 'from', 'import', 'with', '%', '\n']
