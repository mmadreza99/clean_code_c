def readline_cammnd():
    text = ''
    get_text = True
    while get_text:
        input_text =  input('->')
        if len(input_text) > 0 and input_text[0] == '}':
            get_text = False
        text += input_text + '\n'
    return text