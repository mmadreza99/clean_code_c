import re


def clean_tab(text):
    tabs = 0
    result=''

    for line in text.split('\n'):
        if line == '':                                               #Clear blank lines
            continue
        
        line = re.sub(r'^\s+',r'', line)                             #clean space befor line
        
        if '}' in line :                                             #remove tab 
            tabs -= 1                                           
        
        line = ''.join('    ' * tabs + line)
        
        if '{' in line :                                             #Add tab
            tabs += 1 
        
        result += line + '\n'
    return result

