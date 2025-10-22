# Peça a senha e valide o acesso.
import os
os.system('clear')

password = 'clashroyale'

input_password = input(str('Insira sua senha: '))
os.system('clear')

if input_password == password:
    access = True
else:
    access = False

if access:
    print('Senha Correta.\n\nAcesso Validado')
else:
    print('Senha Incorreta.\n\nAcesso Negado')