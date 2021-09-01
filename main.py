from clean_space import clean_space


def open_file(name):
    with open(name, 'r') as file:
        text = file.read()
        return text    
    

if __name__ == "__main__":
    star = '*' * 50
    space = ' ' * 15
    text = open_file("code_c.txt")
    print(f'\n{star}\n{space}:before clean code : \n{star}\n\n{text}')
    
    clean_text = clean_space(text)
    print(f'\n{star}\n {space}:after clean code : \n{star}\n\n{clean_text}')
