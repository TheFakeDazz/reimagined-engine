def word_count():
    while True:
        try:
            namee = input('Enter the full name of your file: ')
            if namee == 'quit':
                break
            open_file = open(namee)
            read_file = open_file.read()
            replace_new = read_file.replace('\n', " ")
            separate = replace_new.split(' ')
            value = ''
            while value in separate:
                separate.remove(value)
            count = len(separate)
            return f'Word Count: {count}'
            break
        except FileNotFoundError:
            print('Your file was not found')
