from CYK import *
from convertCFG import *
from splitter import *
import sys

Terminal,Variables,Productions = [],[],[]
if len(sys.argv) == 2:
    Terminal, Variables, Productions = loadGrammar('grammar.txt')
    Productions = ConvertToCNF(Productions, Variables, Terminal)
    saveCNF(Productions)
    cnf = converttoDict(Variables, Terminal, Productions)
    word = split(sys.argv[1])
    if CYK(word,cnf):
        print("Accepted")
    else:
        print("Syntax Error")
elif len(sys.argv) == 3:
    Terminal, Variables, Productions = loadGrammar(sys.argv[2])
    Productions = ConvertToCNF(Productions, Variables, Terminal)
    saveCNF(Productions)
    cnf = converttoDict(Variables, Terminal, Productions)
    word = split(sys.argv[1])
    if CYK(word,cnf):
        print("Accepted")
    else:
        print("Syntax Error")
else:
    print("Masukkan File")

