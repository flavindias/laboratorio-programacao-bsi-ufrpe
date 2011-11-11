# -*- coding: cp1252 -*-

import time
import os
os.system('cls')
a = time.localtime()
b = str(a[2])+("/")+str(a[1])+("/")+str(a[0])+(" - ")+str(a[3])+(":")+str(a[4])
print ("===============================================================================")
print ("                      Bem vindo ao Posto de Gasolina         "), (b) 
print ("===============================================================================")
print ("")
print ("                       MMMMMMMMMMMMMMMMMMM    MM")
print ("                       MMMMMMMMMMMMMMMMMMMM   MMMM")
print ("                       MM               MMM     MMMM")
print ("                       MM               .MM       MMM.")
print ("                       MM               .MM        MMM")
print ("                       MM               ?MM        MMMM")
print ("                       MM               ?MM,.       MMMM")
print ("                       MM               ?MM.        MMM")
print ("                       MM               ?MM.        MMM")
print ("                       MM,              =MM,        MM")
print ("                       MM8.,,          MMMM,        :M")
print ("                       MMMMMMMMMMMMMMMMMMMMMMM,      MM")
print ("                       MMMMMMMMMMMMMMMMMMMM.MMM      MM")
print ("                       MMMMMMMMMMMMMMMMMMMM  MM      MM")
print ("                       MMMMMMMMMMMMMMMMMMMM  MM      MM.")
print ("                       MMMMMMMMMMMMMMMMMMMM  +M      ZMM")
print ("                       MMMMMMMMMMMMMMMMMMMM  ,M.      MM")
print ("                       MMMMMMMMMMMMMMMMMMMM .$M.      MMD")
print ("                       MMMMMMMMMMMMMMMMMMMM  $M       .MM")
print ("                       MMMMMMMMMMMMMMMMMMMM .MM        MM")
print ("                       MMMMMMMMMMMMMMMMMMMM  MM        MM")
print ("                       MMMMMMMMMMMMMMMMMMMM  .MM       MN")
print ("                       MMMMMMMMMMMMMMMMMMMM   MMD     MM")
print ("                       MMMMMMMMMMMMMMMMMMMM   .MMMMMMMM.")
print ("                     . MMMMMMMMMMMMMMMMMMMM .")
print ("                     MMMMMMMMMMMMMMMMMMMMMMMM")
print ("                     MMMMMMMMMMMMMMMMMMMMMMMM")
print ("")
print ("                                                                  versao: 1.0.0")
print ("===============================================================================")
print ("                                  TELA DE LOGIN")
print ("===============================================================================")
print ("")

validar_login = False

while validar_login == False:

    login = raw_input("DIGITE O SEU LOGIN: ").upper()
    senha = raw_input("DIGITE SUA SENHA: ")

    if login == "FUNCIONARIO":
        if senha == "123":
            validar_login = True
            import menu_principal
        else:
            print ("SENHA INVALIDA")
            print ("")
    elif login == "GERENTE":
        if senha == "123":
            validar_login = True
            import menu_principal
        else:
            print ("SENHA INVALIDA")
            print ("")
    else:
        print ("LOGIN INVALIDO")
    #if para verificar se o funcionario é cadastrado, buscando na lista de funcionarios
        #if 
        #validar_login = True
    #else:
        #print ("LONGIN INVALIDO")
