def loadGrammar(filePath):
    file = open(filePath).read()
    Terminal = file.split("Variables:\n")[0].replace("Terminals:\n","").replace("\n","")
    Variabel = file.split("Variables:\n")[1].split("Productions:\n")[0].replace("\n","")
    Productions = file.split("Productions:\n")[1].replace("\n","").split(";")
    fixProductions = []
    for i in Productions:
        temp = i.replace(" ","").split("->")
        array = []
        rule = temp[1].split("|")
        fixProductions.append([temp[0],rule])
    return Terminal, Variabel, fixProductions
(a,b,c) = loadGrammar("test.txt")

def setofOneTerminal(productions, variables, terminal):
    set = {}
    for rule in productions:
        if rule[0] in variables and rule[1][0] in terminal and len(rule[1]) == 1:
            set[rule[1][0]] = rule[0]
    return set

def subtitutedRule(rules, variables):
	unitaryList, simplified_rules = [], []
	for rule in rules:
		if rule[0] in variables and rule[1][0] in variables and len(rule[1]) == 1 :
			unitaryList.append( [rule[0], rule[1][0]] )
		else:
			simplified_rules.append(rule)
	for ruleUnit in unitaryList:
		for rule in rules:
			if ruleUnit[1]==rule[0] and ruleUnit[0]!=rule[0]:
				simplified_rules.append( [ruleUnit[0],rule[1]])
    return simplified_rules

def ConvertToCNF(productions, variables, terminal):
    variables.append("S'")
    productions = [['S',[variables[0]]]] + productions
    new_Productions = []
    setofOneProductions = setofOneTerminal(productions, variables, terminal)
    index = 0
    for rule in productions: # Mengganti rule yang memuat terminal dan Variabel menjadi Variabel semua
        if rule[0] in variables and rule[1][0] in terminal and len(rule[1]) == 1:
            new_Productions.append(rule)
        else:
            for j in terminal:
                for i,value in enumerate(rule[1]):
                    if j == value and not j in setofOneProductions:
                        index = index+1
                        setofOneProductions[j] = "A"+str(index)
                        variables.append(setofOneProductions[j])
                        new_Productions.append([setofOneProductions[j],[j]])
                        rule[1][i] = setofOneProductions[j]
                    elif j == value :
                        rule[1][i] = setofOneProductions[j]
            new_Productions.append([rule])
    productions = new_Productions #Menghapus non-unit production
    new_Productions = []
    index = 0
    for rule in productions:
        if len(rule[1]) <= 2:
            new_Productions.append(rule)
        else:
            index = index+1
            VarName = "B"+str(index)
            variables.append(VarName+"1")
            new_Productions.append([rule[0],[rule[1][0]]+[VarName+"1"]])
            for i in range(1,len(rule[1])-2):
                var1,var2 = VarName+str(i),VarName+str(i+1)
                variables.append(var2)
                new_Productions.append([var1,[rule[1][i],var2]])
            new_Productions.append([VarName+str(len(rule[1])-1),rule[1][len(rule[1])-2:len(rule[1])]])
    productions = new_Productions #Menghapus non-unit production
    j = 0






    




