from io import open
import sys

def addAccount():
    file = open('accounts','a',encoding='UTF-8')

    user = input('Ingrese user: ')
    password = input('Ingrese password: ')
    where = input('Ingrese lugar de la password: ')

    a = f"{user}|{password}|{where};"

    file.write(a)

    file.close()

sys.modules[__name__] = addAccount