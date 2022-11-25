def state1(cc):
    '''State 1'''
    if cc == '_' or cc.isalpha() or cc == '$':
        return 2
    elif cc == '.':
        return 3
    else :
        return 3

def state2(cc):
    '''state 2'''
    if cc == '_' or cc.isalpha() or cc == '$' or cc.isnumeric():
        return 2
    elif cc == '.':
        return 6
    else:
        return 3
    
def state3(cc):
    '''state 3'''
    return 3

def state4(cc):
    '''State 4'''
    if cc.isnumeric():
        return 4
    else:
        return 5
    
def state5(cc):
    '''State 5'''
    return 5

def state6(nama):
    '''State 6'''
    jsKey = ['await','break','case','catch','class','const','continue','debugger','default'	,'delete', 'do'	,'else'	,'enum'	,'export','extends','false','finally','for','function','if','implements','import','in','instanceof','interface','let','new','null','package','private','protected','public','return','super','switch','static','this','throw','try','true','typeof','var','void','while','with','yield']
    if nama in jsKey:
        return 3
    else:
        return 6

def cekVar(name):
    '''Check if it is a variable name'''
    name = name+'.'
    state = 1
    for i in name:
        if state == 1:
            state = state1(i)
        if state == 2:
            state = state2(i)
        if state == 3:
            state = state3(i)
        if state == 6:
            state = state6(name[:-1])
    if state == 6:
        return True
    else:
        return False

def cekNum(num):
    '''Check if it is a number'''
    state = 1
    for i in num:
        if state == 1:
            state = state4(i)
        if state == 4:
            state = state4(i)
        if state == 5:
            state = state5(i)
    if state == 4:
        return True
    else:
        return False
    