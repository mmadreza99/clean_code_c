import re
from file import out_file


def clean_tab(file_name, text):
    tabs = 0
    result = ''

    for line in text.split('\n'):
        if line == '':                                              # Clear blank lines
            continue
        
        line = re.sub(r'^\s+', r'', line)                           # clean space befor line
        
        if '}' in line:                                             # remove tab
            tabs -= 1                                           
        
        line = ''.join('    ' * tabs + line)
        
        if '{' in line:                                             # Add tab
            tabs += 1 
        
        result += line + '\n'
    return out_file(file_name, result)
