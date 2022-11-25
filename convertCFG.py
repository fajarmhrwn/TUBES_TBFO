def loadGrammar(filePath):
    file = open(filePath).read()
    Terminal = file.split("Variables:\n")[0].replace("Terminals:\n","").replace("\n","")
    Variabel = file.split("Variables:\n")[1].split("Productions:\n")[0].replace("\n","")
    Productions = file.split("Productions:\n")[1].replace("\n","").split(";")
    Variabel = Variabel.split(" ")
    Terminal = Terminal.split(" ")
    fixProductions = []
    for i in Productions:
        var = i.split(" -> ")[0].replace(" ","")
        term = i.split(" -> ")[1].split(" | ")
        for j in term:
            fixProductions.append([var,j.split(" ")])
    return Terminal, Variabel, fixProductions

def setofOneTerminal(productions, variables, terminal):
    set = {}
    for rule in productions:
        if rule[0] in variables and rule[1][0] in terminal and len(rule[1]) == 1:
            set[rule[1][0]] = rule[0]
    return set

def subtitutedRule(rules, variables):
    unitaryRule, nonUnitaryRule = [], []
    for rule in rules:
        if len(rule[1]) == 1 and rule[1][0] in variables:
            unitaryRule.append([rule[0],rule[1][0]])
        else:
            nonUnitaryRule.append(rule)
    for rule in unitaryRule:
        for rule2 in rules:
            if rule[1] == rule2[0] and rule2[0]!=rule[0]:
                nonUnitaryRule.append([rule[0],rule2[1]])
    return nonUnitaryRule

def ConvertToCNF(productions, variables, terminal):
    variables.append('S0')
    productions = [['S0',[variables[0]]]] + productions
    temp = []
    setofOneProductions = setofOneTerminal(productions, variables, terminal)
    index = 0
    for rule in productions: # Mengganti rule yang memuat terminal dan Variabel menjadi Variabel semua
        if rule[0] in variables and rule[1][0] in terminal and len(rule[1]) == 1:
            temp.append(rule)
        else:
            for j in terminal:
                for i,value in enumerate(rule[1]):
                    if j == value and not j in setofOneProductions:
                        index = index+1
                        setofOneProductions[j] = "A"+str(index)
                        variables.append(setofOneProductions[j])
                        temp.append(setofOneProductions[j],[j])
                        rule[1][i] = setofOneProductions[j]
                    elif j == value :
                        rule[1][i] = setofOneProductions[j]
            temp.append(rule)
    productions = temp #Menghapus non-unit production
    temp = []
    index = 0
    for rule in productions:
        if len(rule[1]) <= 2:
            temp.append(rule)
        else:
            index = index+1
            VarName = "B"+str(index)
            variables.append(VarName+"1")
            temp.append([rule[0],[rule[1][0]]+[VarName+"1"]])
            i = 1
            for i in range(1,len(rule[1])-2):
                var1,var2 = VarName+str(i),VarName+str(i+1)
                variables.append(var2)
                temp.append([var1,[rule[1][i],var2]])
            temp.append([VarName+str(len(rule[1])-2), rule[1][(len(rule[1]))-2:len(rule[1])]])
    productions = temp 
    j = 0
    result = []
    result = subtitutedRule(productions, variables)
    temp = subtitutedRule(result, variables)
    while temp != result and j < 1000:
        result = subtitutedRule(temp, variables)
        temp = subtitutedRule(result, variables)
        j = j+1
    return result

def saveCNF(productions):
    file = open("CNF.txt","w")
    temp = {}
    for rule in productions:
        if rule[0] in temp:
            temp[rule[0]] += " | "+" ".join(rule[1])
        else:
            temp[rule[0]] = " ".join(rule[1])
    Grammar = ""
    for key,value in temp.items():
        Grammar += key+" -> "+value+"\n"
    file.write(Grammar)

def converttoDict(productions):
    temp = {}
    for rule in productions:
        if rule[0] in temp:
            temp[rule[0]].append(rule[1])
        else:
            temp[rule[0]] = []
            temp[rule[0]].append(rule[1])
    return temp