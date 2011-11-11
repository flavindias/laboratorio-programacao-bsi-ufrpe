# -*- coding: cp1252 -*-
import os
os.system('cls')
print ("===============================================================================")
print ("")
print ("                                                               AREA DE CADASTRO")
print ("")
print ("===============================================================================")
print ("")
print ("-------------------------------------------------------------------------------")
print ("")
print (" INSIRA SEUS DADOS!")
print ("")
print ("-------------------------------------------------------------------------------")
print ("")

value1 = False
value2 = False

while value1 == False:
    cpf = raw_input("Digite o CPF aqui: ")
    if (len(cpf)) != 11:
        print "Formato errado. Tente de novo (apenas numeros)"
    else:
        value1 = True

while value2 == False:
    print ("")
    senha = raw_input("Digite sua SENHA: ")
    confirmasenha = raw_input("REPITA sua SENHA: ")
    if senha == confirmasenha:
        value2 = True
    else:
        print ("As senhas digitadas foram diferentes, repita a operação!")

print ("CADASTRO REALIZADO COM SUCESSO!")
import home
