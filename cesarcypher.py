def cesar(i, shift, mode):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    ALPH = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters = alph + ALPH
    cypher = letters[shift-1:-1] + letters[0:shift]
    if mode == 0:
        message = i.translate(str.maketrans(letters, cypher))
    elif mode == 1:
        message = i.translate(str.maketrans(cypher, letters))
    else:
        print('Mode must be either 0 or 1')
    print(message)



print('<3'*50) #Makes it look pretty :)
i = input('Enter your message: ')
print('<3'*50)
mode = eval(input('Enter 0 for encryption or 1 for decryption: '))
print('<3'*50)
shift = eval(input('Enter an integer for your shift: '))
print('<3'*50)
cesar(i, shift, mode)
print('<3'*50)
