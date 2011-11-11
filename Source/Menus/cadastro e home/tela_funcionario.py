# -*- coding: cp1252 -*-
import os
os.system('cls')

print ("===============================================================================")
print ("")
print ("                                                            TELA DE FUNCIONARIO")
print ("")
print ("===============================================================================")
print ("")
print ("-------------------------------------------------------------------------------")
print ("")
print ("1 - COMERCIALIZAR PRODUTO")
print ("2 - CADASTRAR CLIENTE")
print ("0 - SAIR")
print ("")
print ("-------------------------------------------------------------------------------")
print ("")

validar_opcao = False

while validar_opcao == False:
    
    opcao = raw_input("DIGITE AQUI A OPCAO DESEJADA: ")

    if opcao == "1":
        #import vendas
        print ("FUNCAO AINDA NÂO IMPLEMENTADA!")

    elif opcao == "2":
        import cadastro

    elif opcao == "0":
        import home

    else:
        print ("FUNCAO INVALIDA")
