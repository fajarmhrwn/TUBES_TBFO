import re
s = 'if'
status = re.split(r'[A..z]*(=)[A..z]*', s)
for i in status:
    print(i)
