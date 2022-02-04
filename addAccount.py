from io import open

file = open('accounts.txt','a')

user = input('Ingrese user: ')
password = input('Ingrese password')

account = '{usuario}|{password};'

file.write(account)

file.close()