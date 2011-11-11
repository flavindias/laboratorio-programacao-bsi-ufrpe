# -*- coding: cp1252 -*-
import os
os.system('cls')
print ("===============================================================================")
print ("")
print ("                                                               TELA DE GERENCIA")
print ("")
print ("===============================================================================")
print ("")
print ("-------------------------------------------------------------------------------")
print ("")
print ("1 - COMERCIALIZAR PRODUTO")
print ("2 - CADASTRAR CLIENTE")
print ("")
print ("3 - ADICIONAR NOVO PRODUTO")
print ("4 - EDITAR PRODUTO")
print ("5 - REMOVER PRODUTO")
print ("")
print ("6 - ADICIONAR FUNCIONARIO")
print ("7 - EDITAR FUNCIONARIO")
print ("8 - REMOVER FUNCIONARIO")
print ("")
print ("9 - IMPRIMIR RELATORIO")
print ("0 - SAIR")
print ("")
print ("-------------------------------------------------------------------------------")
print ("")

validador_opcao = False
opcao = raw_input("DIGITE AQUI A OPCAO DESEJADA: ")

while validador_opcao == False:
    
    if opcao == "1":
        validador_opcao == True
        #import venda
        
    elif opcao == "2":
        validador_opcao == True
        import cadastro

    elif opcao == "3":
        validador_opcao == True
        #import adicionar_produto

    elif opcao == "4":
        validador_opcao == True
        #import editar_produto

    elif opcao == "5":
        validador_opcao == True
        #import remover_produto

    elif opcao == "6":
        validador_opcao == True
        #import adicionar_funcionario

    elif opcao == "7":
        validador_opcao == True
        #import editar_fucionario

    elif opcao == "8":
        validador_opcao == True
        #import remover_funcionario

    elif opcao == "9":
        validador_opcao == True
        #import imprimir_relatorio

    elif opcao == "0":
        validador_opcao == True
        import home

    else:
        print ("OPCAO INVALIDA!")
