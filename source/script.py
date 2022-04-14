print("""

    \       /  ///// /   /
    \ / | \ /  /---  /---/
    \/  |   \/ /////  /   /

""".replace('/', '\\'))

print("Welcome to the https://github.com/weh-gh/script-pl")

process = input('Process select (Create - 1, Run - 0)')
if process == '1':
    filename = input('File name: ')
    file_extension = input('File extension: ')
    with open(filename + file_extension, 'w') as my_file:
        if file_extension == '.wh':
            my_file.write('Main\n\nMiddle\n\nReMiddle')
            print("File created!")
            process = input("If you want to create your own skeleton of this language, press enter.")
if process == '0':
    filename = input('File name: ')
    file_extension = input('File extension: ')
    try:
        with open(filename + file_extension):
            pass
    except:
        with open(filename + file_extension, 'w') as my_file:
            if file_extension == '.wh':
                my_file.write('Main\n\nMiddle\n\nReMiddle')

    with open(filename + file_extension) as my_file:
        print('Running...\n-----------------------------------------')
        read = my_file.readlines()
        i = 0
        if file_extension == '.wh':
            ifmain = False
            var_a = ''
            var_b = ''
            var_c = ''
            while True:
                # try:
                    rood = read[i]
                    rood = rood.replace('&a&', var_a)
                    rood = rood.replace('&b&', var_b)
                    rood = rood.replace('&c&', var_c)
                    if rood == 'Main\n':
                        ifmain = True
                    if rood == 'End\n':
                        break
                    if 'print() = ' in rood and ifmain == True:
                        rood = rood.replace('print() = ', '')
                        rood = rood.replace('\n', '')
                        print(rood)

                    if 'var() = ' in rood and ifmain == True:
                        rood = rood.replace('var() = ', '')
                        rood = rood.replace('\n', '')                        
                        rooda = rood.split('/')
                        if rooda[0] == 'a':
                            var_a = rooda[1]

                        if rooda[0] == 'b':
                            var_b = rooda[1]

                        if rooda[0] == 'c':
                            var_c = rooda[1]

                    i += 1
                # except:
                    # break
