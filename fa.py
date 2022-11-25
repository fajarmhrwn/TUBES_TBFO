# isinya fa masih kosongan
def cekVar(name):
    '''Check if it is a variable name'''
    jsKey = ['await','break','case','catch','class','const','continue','debugger','default'	,'delete', 'do'	,'else'	,'enum'	,'export','extends','false','finally','for','function','if','implements','import','in','instanceof','interface','let','new','null','package','private','protected','public','return','super','switch','static','this','throw','try','true','typeof','var','void','while','with','yield']
    if name in jsKey:
        return False
    else:
        if name[0] != '_' or not(name[0].isalpha()) or name[0] != '$':
            return False
        else:
            state = False
            for i in name[1:]:
                if i.isalnum() or i == '_' or i == '$' or i.isalpha():
                    state = True
            return state


def cekNum(num):
    '''Check if it is a number'''
    for i in num:
        if i.isdigit():
            return True
    return False