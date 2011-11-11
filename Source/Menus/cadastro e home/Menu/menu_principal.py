# -*- coding: cp1252 -*-
import os
os.system('cls')

print ("===============================================================================")
print ("")
print ("                                                                 MENU PRINCIPAL")
print ("")
print ("===============================================================================")
print ("")
print ("-------------------------------------------------------------------------------")
print ("")
print ("1 - REALIZAR VENDAS")
print ("")
print ("2 - GESTAO DE CLIENTES")
print ("")
print ("3 - GESTAO DE USUARIOS")
print ("")
print ("4 - GESTAO DE PRODUTOS")
print ("")
print ("5 - RELATORIOS")
print ("")
print ("0 - SAIR")
print ("")
print ("-------------------------------------------------------------------------------")
print ("")

opcao = raw_input("Digite aque a sua opcao: ")

if opcao == "1":
    #import tela_vendas
    print ("FUNCAO AINDA NAO IMPLEMENTADA!")

elif opcao == "2":
    #import tela_clientes
    print ("FUNCAO AINDA NAO IMPLEMENTADA!")
    
elif opcao == "3":
    #import tela_usuario
    print ("FUNCAO AINDA NAO IMPLEMENTADA!")

elif opcao == "4":
    #import tela_produto
    print ("FUNCAO AINDA NAO IMPLEMENTADA!")

elif opcao == "5":
    #import tela_relatorios
    print ("FUNCAO AINDA NAO IMPLEMENTADA!")

elif opcao == "0":
    import home

else:
    print ("ENTRADA INVALIDA!")
