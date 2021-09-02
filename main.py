from clean_space import clean_space
from file import open_file
from static import SPACE, STAR

if __name__ == "__main__":
    file_name = input(">>> Enter your file name : ")

    text = open_file(file_name)
    clean_text = clean_space(file_name, text)

    #print(f'\n{star}\n{space}:before clean code : \n{star}\n\n{text}')
    print(f'\n{STAR}\n {SPACE}:after clean code: \n{STAR}\n\n{clean_text}')
