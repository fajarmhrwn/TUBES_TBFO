from CYK import *
from convertCFG import *
from splitter import *
import sys

Terminal,Variables,Productions = [],[],[]
variablesJar = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "K1", "L1", "M1", "N1", "O1", "P1", "Q1", "R1", "S1", "T1", "U1", "V1", "W1", "X1", "Y1", "Z1",
"A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2", "J2", "K2", "L2", "M2", "N2", "O2", "P2", "Q2", "R2", "S2", "T2", "U2", "V2", "W2", "X2", "Y2", "Z2",
"A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "I3", "J3", "K3", "L3", "M3", "N3", "O3", "P3", "Q3", "R3", "S3", "T3", "U3", "V3", "W3", "X3", "Y3", "Z3",
"A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4", "J4", "K4", "L4", "M4", "N4", "O4", "P4", "Q4", "R4", "S4", "T4", "U4", "V4", "W4", "X4", "Y4", "Z4",
"A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5", "J5", "K5", "L5", "M5", "N5", "O5", "P5", "Q5", "R5", "S5", "T5", "U5", "V5", "W5", "X5", "Y5", "Z5"]
if len(sys.argv) == 2:
    Terminal, Variables, Productions = loadGrammar('test.txt')
    Productions = ConvertToCNF(Productions, Variables, Terminal)
    cnf = converttoDict(Productions)
    word = split(sys.argv[1])
    if CYK(word, cnf):
        print("Valid")
    else:
        print("Invalid")
elif len(sys.argv) == 3:
    Terminal, Variables, Productions = loadGrammar(sys.argv[2])
    Productions = ConvertToCNF(Productions, Variables, Terminal)
    word = split(sys.argv[1])
    cnf = converttoDict(Productions)
    if CYK(word,cnf):
        print("Accepted")
    else:
        print("Syntax Error")
else:
    print("Masukkan File")

