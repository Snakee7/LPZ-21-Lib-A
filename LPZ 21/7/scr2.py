print('SCR2.PY START\n')

try:
    while True:
        data = input()
        print(data)
except EOFError:
    pass

print('\nSCR2 END')