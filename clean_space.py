import re
from clean_tab import clean_tab


def clean_space(text):

    text = re.sub(r',([a-z,&,0-9])',r', \1',text)                   #Add spaces after commas
    text = re.sub(r' ,',r',',text)                                  #remove space before commas
    text = re.sub(r' ]',r']',text)                                  #remove space in []   
    text = re.sub(r'\[ ',r'[',text)                                 #remove space in [] 
    text = re.sub(r'([a-z]) (\[)',r'\1\2',text)                     #remove space in [] 
    text = re.sub(r'\( ',r'\(',text)                                #remove space in () 
    text = re.sub(r' \)',r'\)',text)                                #remove space in () 
    text = re.sub(r'([a-z,0-9])=([a-z,0-9])',r'\1 = \2',text)       #Add space in = 
    text = re.sub(r'([a-z,0-9])==([a-z,0-9])',r'\1 == \2',text)     #Add space in ==
    text = re.sub(r'(])=',r'\1 =',text)                             #Add space in = 
    text = re.sub(r'([a-z,0-9])\+([a-z,0-9])',r'\1 + \2',text)      #Add space in +
    text = re.sub(r'([a-z,0-9])\-([a-z,0-9])',r'\1 - \2',text)      #Add space in +
    text = re.sub(r'([a-z,0-9])<([a-z,0-9])',r'\1 < \2',text)       #Add space in <
    text = re.sub(r'([a-z,0-9])<=([a-z,0-9])',r'\1 <= \2',text)     #Add space in <=
    text = re.sub(r'([a-z,0-9])>=([a-z,0-9])',r'\1 >= \2',text)     #Add space in >=
    text = re.sub(r'([a-z,0-9])>([a-z,0-9])',r'\1 > \2',text)       #Add space in >
    text = re.sub(r';([a-z+])',r'; \1',text)                        #Add space after ";"
    text = re.sub(r'(for.*)\n.+({)',r'\1\2',text)                   #clean for 
    text = re.sub(r'(for.*\)).+({)',r'\1\2',text)                   #clean for (int main.+)\n{
    text = re.sub(r'( main.+)\n{',r'\1{\n',text)                    #clean main { 
    text = re.sub(r'(\(.*?\){)',r'\1\n',text)                       #clean () as in { 
    text = re.sub(r'(;)(})',r'\1\n\2',text)                         #clean () as in { 
    
    return clean_tab(text)
