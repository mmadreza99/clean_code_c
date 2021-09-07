def open_file(name_file):
    with open(name_file, 'r') as file:
        text = file.read()
        return text  


def generator_name(name):
    return '_done.'.join(name.split('.'))


def out_file(file_name, result):
    file_name = generator_name(file_name)
    with open(file_name, 'w') as file:
        file.write(result)
        print(f'successful to create file {file_name}')
        return result