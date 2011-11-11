#import Proprietario
#import PostoGasolina
import Produto
import Login
#import Estoque
#import Relatorios
#import Cliente
#import Vendas
import time
import os
#import Cor

#proprietario = Proprietario.Proprietario()
#postoGasolina = PostoGasolina.PostoGasolina()
produto = Produto.Produto()
login = Login.Login()
#estoque = Estoque.Estoque()
#relatorio = Relatorios.Relatorios()
#cliente = Cliente.Cliente()
#venda = Vendas.Vendas()

class Menu:

    def menuCabecalho(self, usuario, menu):
        os.system('cls')
        self.__temp = time.localtime()
        self.__str = str(self.__temp[2])+("/")+str(self.__temp[1])+("/")+str(self.__temp[0])+(" - ")+str(self.__temp[3])+(":")+str(self.__temp[4])
        print ("===============================================================================")
        print ("                        BEM VINDO AO SOFTPOSTO             "), (self.__str) 
        print ("===============================================================================")
        if usuario == '':
            print ('')
        else:
            print ('USUARIO: ')+str(usuario)
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
        print ("                        ")+str(menu)
        print ("===============================================================================")
        print ("")

    def menuPrimeiroLogar(self):
        self.menuCabecalho('','LOGIN')
        print 'ESTE EH SEU PRIMEIRO LOGIN. CADASTRE UM NOVO USUARIO E SENHA.\n'
        self.__login = ''
        self.__senha = ''
        self.__val = True
        while 1==1:
            if self.__val:
                self.__login = raw_input('LOGIN: ')
                self.__senha = raw_input('SENHA: ')
                self.__rptSenha = raw_input('CONFIRME A SENHA: ')
                if self.__login != '' and self.__senha != '':
                    if self.__senha == self.__rptSenha:
                        if login.altUsuarioSenha('admin', self.__login, self.__senha):
                            self.__msg = raw_input('\nBEM VINDO AO SOFTPOSTO.\nPRESSIONE ENTER.')
                            self.logado = self.__login.upper()
                            return self.menuPrincipal()
                self.__val = False
            else:
                os.system('cls')
                self.menuCabecalho('','LOGIN')
                print 'USUARIO OU SENHA DIGITADA INVALIDA, OU O USUARIO JA ESTA CADASTRADO. TENTE NOVAMENTE.'
                self.__login = raw_input('LOGIN: ')
                self.__senha = raw_input('SENHA: ')
                self.__rptSenha = raw_input('CONFIRME A SENHA: ')
                if self.__login != '' and self.__senha != '':
                    if self.__senha == self.__rptSenha:
                        if login.altUsuarioSenha('admin', self.__login, self.__senha):
                            self.__msg = raw_input('\nBEM VINDO AO SOFTPOSTO.\nPRESSIONE ENTER.')
                            self.logado = self.__login.upper()
                            return self.menuPrincipal()
                    else:
                        self.__msg = raw_input('\nSENHAS NAO COMPATIVEIS.\nPRESSIONE ENTER PARA TENTAR NOVAMENTE.')

    def menuLogarLogin(self):
        self.menuCabecalho('','LOGIN')
        self.__login = raw_input('LOGIN: ')
        self.__senha = raw_input('SENHA: ')
        if login.validar(self.__login, self.__senha):
            self.__msg = raw_input('\nBEM VINDO AO SOFTPOSTO.\nPRESSIONE ENTER.')
            self.logado = self.__login.upper()
            return self.menuPrincipal()
        else:
            print 'USUARIO OU SENHA INVALIDA.'
            self.__msg = raw_input('PRESSIONE ENTER PARA TENTAR NOVAMENTE')
            return self.menuLogarLogin()

    def iniciar(self):
        login.carregar()
        if login.getSenhas1() == 'admin':
            return self.menuPrimeiroLogar()
        else:
            return self.menuLogarLogin()
        
    def menuPrincipal(self):
        self.menuCabecalho(self.logado,'MENU PRINCIPAL')
        print 'OPCAO 1 - GERENCIAR FUNCIONARIOS'
        print 'OPCAO 2 - GERENCIAR PRODUTOS\n'
        print 'OPCAO 0 - SAIR\n'
        self.__opcao = raw_input('DIGITE A OPCAO DESEJADA: ')
        if self.__opcao == '0':
            return exit()
        elif self.__opcao == '1':
            return self.menuFuncionarios()
        elif self.__opcao == '2':
            return self.menuProdutos()
        else:
            self.__msg = raw_input('\nOPCAO INVALIDA. \nPRESSIONE ENTER PARA TENTAR NOVAMENTE.')
            return self.menuPrincipal()

    def menuFuncionarios(self):
        self.menuCabecalho(self.logado,'GERENCIAMENTO DE FUNCIONARIOS')
        print 'OPCAO 1 - ADICIONAR FUNCIONARIO'
        print 'OPCAO 2 - ALTERAR SENHA DE FUNCIONARIO'
        print 'OPCAO 3 - EXCLUIR FUNCIONARIO'
        print 'OPCAO 4 - VERIFICAR LISTA DE USUARIOS\n'
        print 'OPCAO 0 - RETORNAR AO MENU PRINCIPAL\n'
        self.__opcao = raw_input('DIGITE A OPCAO DESEJADA: ')
        if self.__opcao == '0':
            return self.menuPrincipal()
        elif self.__opcao == '1':
            return self.menuFuncionariosAdd()
        elif self.__opcao == '2':
            return self.menuFuncionariosAlt()
        elif self.__opcao == '3':
            return self.menuFuncionariosExc()
        elif self.__opcao == '4':
            return self.menuFuncionariosVer()
        else:
            self.__msg = raw_input('\nOPCAO INVALIDA. \nPRESSIONE ENTER PARA TENTAR NOVAMENTE.')
            return self.menuFuncionarios()

    def menuFuncionariosAdd(self):
        self.menuCabecalho(self.logado,'ADICIONAR FUNCIONARIO')
        print 'PARA CANCELAR A ACAO MANTENHA QUALQUER UM DOS CAMPOS VAZIO E PRESSIONE ENTER.\n'
        self.__login = raw_input('DIGITE O NOVO USUARIO: ')
        self.__senha = raw_input('DIGITE A SENHA: ')
        self.__rptSenha = raw_input('REPITA A SENHA: ')
        if self.__login != '' and self.__senha != '':
            if self.__senha == self.__rptSenha: 
                if login.addUsuario(self.__login, self.__senha):
                    self.__msg = raw_input('OPERACAO REALIZADA COM SUCESSO.\nPRESSIONE ENTER PARA VOLTAR AO MENU ANTERIOR.')
                    return self.menuFuncionarios()
                else:
                    self.__msg = raw_input('USUARIO JA EXISTE. TENTE NOVAMENTE COM OUTRO USUARIO.\nPRESSIONE ENTER PARA RETORNAR.')
                    return self.menuFuncionariosAdd()
            else:
                self.msg = raw_input("\nSENHAS DIGITADAS SAO DIFERENTES.\nPRESSIONE ENTER PARA TENTAR NOVAMENTE.")
                return self.menuFuncionariosAdd()
        else:
            self.__msg = raw_input('OPERACAO CANCELADA.\nPRESSIONE ENTER PARA VOLTAR AO MENU ANTERIOR.')
            return self.menuFuncionarios()

    def menuFuncionariosAlt(self):
        self.menuCabecalho(self.logado,'EDITAR FUNCIONARIO')
        print 'PARA CANCELAR A ACAO MANTENHA QUALQUER UM DOS CAMPOS VAZIO E PRESSIONE ENTER.\n'
        self.__login = raw_input('DIGITE O USUARIO: ')
        self.__senha = raw_input('DIGITE A NOVA SENHA: ')
        self.__rptSenha = raw_input('REPITA A SENHA: ')
        if self.__login != '' and self.__senha != '':
            if self.__senha == self.__rptSenha:
                if login.altSenha(self.__login, self.__senha):
                    self.__msg = raw_input('OPERACAO REALIZADA COM SUCESSO.\nPRESSIONE ENTER PARA VOLTAR AO MENU ANTERIOR.')
                    return self.menuFuncionarios()
                else:
                    self.__msg = raw_input('USUARIO NAO ENCONTRADO.\nPRESSIONE ENTER PARA TENTAR NOVAMENTE.')
                    return self.menuFuncionariosAlt()
            else:
                self.__msg = raw_input('\nSENHAS DIGITADAS SAO DIFERENTES.\nPRESSIONE ENTER PARA TENTAR NOVAMENTE.')
                return self.menuFuncionariosAlt()
        else:
            self.__msg = raw_input('OPERACAO CANCELADA.\nPRESSIONE ENTER PARA VOLTAR AO MENU ANTERIOR.')
            return self.menuFuncionarios()
            
    def menuFuncionariosExc(self):
        self.menuCabecalho(self.logado,'EXCLUIR FUNCIONARIO')
        print 'PARA CANCELAR A ACAO MANTENHA O CAMPO VAZIO E PRESSIONE ENTER.\n'
        self.__login = raw_input('DIGITE O USUARIO A SER EXCLUIDO: ')
        if self.__login != '':
            if self.__login.upper() ==  login.usuarios[0]:
                self.__msg = raw_input('VOCE NAO PODE EXCLUIR O USUARIO GERENTE.\nPRESSIONE ENTER PARA VOLTAR AO MENU ANTERIOR.')
                return self.menuFuncionarios()
            else:
                if login.delUsuario(self.__login):
                    self.__msg = raw_input('OPERACAO REALIZADA COM SUCESSO.\nPRESSIONE ENTER PARA VOLTAR AO MENU ANTERIOR.')
                    return self.menuFuncionarios()
                else:
                    self.__msg = raw_input('USUARIO NAO ENCONTRADO.\nPRESSIONE ENTER PARA TENTAR NOVAMENTE.')
                    return self.menuFuncionariosExc()
        else:
            self.__msg = raw_input('OPERACAO CANCELADA.\nPRESSIONE ENTER PARA VOLTAR AO MENU ANTERIOR.')
            return self.menuFuncionarios()
        
    def menuFuncionariosVer(self):
        self.menuCabecalho(self.logado,'EXCLUIR FUNCIONARIO')
        login.carregar()
        print 'ATUALMENTE, ESTES SAO OS USUARIOS CADASTRADOS: \n'
        for self.__i in range(len(login.usuarios)):
            print ('                    ')+login.usuarios[self.__i]
        self.__msg = raw_input('\nPRESSIONE ENTER PARA VOLTAR AO MENU ANTERIOR.')
        return self.menuFuncionarios()
        
    def menuProdutos(self):
        self.menuCabecalho(self.logado,'GERENCIAMENTO DE PODUTOS')
        print 'OPCAO 1 - ADICIONAR PRODUTO'
        print 'OPCAO 2 - ALTERAR DADOS DO PRODUTO'
        print 'OPCAO 3 - EXCLUIR PRODUTO'
        print 'OPCAO 4 - VERIFICAR LISTA DE PRODUTOS\n'
        print 'OPCAO 0 - RETORNAR AO MENU PRINCIPAL\n'
        self.__opcao = raw_input('DIGITE A OPCAO DESEJADA: ')
        if self.__opcao == '0':
            return self.menuPrincipal()
        elif self.__opcao == '1':
            return self.menuProdutosAdd()
        elif self.__opcao == '2':
            return self.menuProdutosAlt()
        elif self.__opcao == '3':
            return self.menuProdutosExc()
        elif self.__opcao == '4':
            return self.menuProdutosVer()
        else:
            self.__msg = raw_input('\nOPCAO INVALIDA.\nPRESSIONE ENTER PARA TENTAR NOVAMENTE.')
            return self.menuProdutos()

    def menuProdutosAdd(self):
        self.menuCabecalho(self.logado,'ADICIONAR PRODUTO')
        print ('PARA CANCELAR A ACAO MANTENHA QUALQUER UM DOS CAMPOS VAZIO E PRESSIONE ENTER.\n')
        self.__nome = raw_input('DIGITE O NOME DO PRODUTO: ')
        self.__preco = raw_input('DIGITE O PRECO DO PRODUTO: ')
        self.__carac = raw_input('DIGITE CARACTERISTICAS DO PRODUTO: ')
        if self.__nome != '' and self.__preco != '' and self.__carac != '':
            try:
                float(self.__preco)
                if produto.addProduto(self.__nome, self.__preco, self.__carac):
                    self.__msg = raw_input('OPERACAO REALIZADA COM SUCESSO.\nPRESSIONE ENTER PARA VOLTAR AO MENU ANTERIOR.')
                    return self.menuProdutos()
                else:
                    self.__msg = raw_input('ESTE PRODUTO JA ESTA CADASTRADO.\nPRESSIONE ENTER PARA TENTAR NOVAMENTE.')
                    return self.menuProdutosAdd()
            except:
                self.__msg = raw_input('DIGITE APENAS NUMEROS PARA O PRECO. PARA CENTAVOS, SEPARE-OS COM "."\nPRESSIONE ENTER PARA TENTAR NOVAMENTE.')
                return self.menuProdutosAdd()
        else:
            self.__msg = raw_input('OPERACAO CANCELADA.\nPRESSIONE ENTER PARA VOLTAR AO MENU ANTERIOR.')
            return self.menuProdutos()

    def menuProdutosAlt(self):
        self.menuCabecalho(self.logado,'ALTERAR DADOS DOS PRODUTOS')
        print 'OPCAO 1 - ALTERAR NOME'
        print 'OPCAO 2 - ALTERAR PRECO'
        print 'OPCAO 3 - ALTERAR CARACTERISTICAS\n'
        print 'OPCAO 0 - RETORNAR AO MENU PRINCIPAL\n'
        self.__opcao = raw_input('DIGITE A OPCAO DESEJADA: ')
        if self.__opcao == '0':
            return self.menuProdutos()
        elif self.__opcao == '1':
            return self.menuProdutosAltNome()
        elif self.__opcao == '2':
            return self.menuProdutosAltPreco()
        elif self.__opcao == '3':
            return self.menuProdutosAltCaract()
        else:
            self.__msg = raw_input('\nOPCAO INVALIDA.\nPRESSIONE ENTER PARA TENTAR NOVAMENTE.')
            return self.menuProdutos()

    def menuProdutosAltNome(self):
        self.menuCabecalho(self.logado,'ALTERAR NOME DOS PRODUTOS')
        print ('PARA CANCELAR A ACAO MANTENHA QUALQUER UM DOS CAMPOS VAZIO E PRESSIONE ENTER.\n')
        self.__nome = raw_input('DIGITE O NOME DO PRODUTO A SER ALTERADO: ')
        self.__novo = raw_input('DIGITE O NOVO NOME: ')
        if self.__nome != '' and self.__novo != '':
            if produto.altProdutoNome(self.__nome, self.__novo):
                self.__msg = raw_input('OPERACAO REALIZADA COM SUCESSO.\nPRESSIONE ENTER PARA VOLTAR AO MENU ANTERIOR.')
                return self.menuProdutosAlt()
            else:
                self.__msg = raw_input('ESTE PRODUTO NAO ESTA CADASTRADO.\nPRESSIONE ENTER PARA TENTAR NOVAMENTE.')
                return self.menuProdutosAlt()
        else:
            self.__msg = raw_input('OPERACAO CANCELADA.\nPRESSIONE ENTER PARA VOLTAR AO MENU ANTERIOR.')
            return self.menuProdutosAlt()

    def menuProdutosAltPreco(self):
        self.menuCabecalho(self.logado,'ALTERAR PRECO DOS PRODUTOS')
        print ('PARA CANCELAR A ACAO MANTENHA O CAMPO NOME VAZIO E PRESSIONE ENTER.\n')
        self.__nome = raw_input('DIGITE O NOME DO PRODUTO A SER ALTERADO: ')
        if self.__nome == '':
            self.__msg = raw_input('OPERACAO CANCELADA.\nPRESSIONE ENTER PARA VOLTAR AO MENU ANTERIOR.')
            return self.menuProdutosAlt()
        elif produto.validar(self.__nome):
            print ('\nATUALMENTE O PRECO DESTE PRODUTO EH:'), produto.getPreco(self.__nome)
            self.__novo = raw_input('\nDIGITE O NOVO VALOR DO PRODUTO: ')
            if self.__novo != '':
                try:
                    float(self.__novo)
                    produto.altProdutoPreco(self.__nome, self.__novo)
                    self.__msg = raw_input('OPERACAO REALIZADA COM SUCESSO.\nPRESSIONE ENTER PARA VOLTAR AO MENU ANTERIOR.')
                    return self.menuProdutosAlt()
                except:
                    self.__msg = raw_input('DIGITE APENAS NUMEROS PARA O PRECO. PARA CENTAVOS, SEPARE-OS COM "."\nPRESSIONE ENTER PARA TENTAR NOVAMENTE.')
                    return self.menuProdutosAltPreco()
            else:
                self.__msg = raw_input('CAMPO EM BRANCO.\nPRESSIONE ENTER PARA TENTAR NOVAMENTE.')
                return self.menuProdutosAltPreco()
        else:
            self.__msg = raw_input('PRODUTO NAO CADASTRADO.\nPRESSIONE ENTER PARA TENTAR NOVAMENTE.')
            return self.menuProdutosAltPreco()
            
    def menuProdutosAltCaract(self):
        self.menuCabecalho(self.logado,'ALTERAR CARACTERISTICAS DO PRODUTO')
        print ('PARA CANCELAR A ACAO MANTENHA O CAMPO NOME VAZIO E PRESSIONE ENTER.\n')
        self.__nome = raw_input('DIGITE O NOME DO PRODUTO A SER ALTERADO: ')
        if self.__nome == '':
            self.__msg = raw_input('OPERACAO CANCELADA.\nPRESSIONE ENTER PARA VOLTAR AO MENU ANTERIOR.')
            return self.menuProdutosAlt()
        elif produto.validar(self.__nome):
            print ('\nATUALMENTE A CARACTERISTICA DESTE PRODUTO EH:'), produto.getCaract(self.__nome)
            self.__novo = raw_input('\nDIGITE AS NOVAS CARACTERISTICAS DO PRODUTO: ')
            if self.__novo != '':
                produto.altProdutoCaract(self.__nome, self.__novo)
                self.__msg = raw_input('OPERACAO REALIZADA COM SUCESSO.\nPRESSIONE ENTER PARA VOLTAR AO MENU ANTERIOR.')
                return self.menuProdutosAlt()
            else:
                self.__msg = raw_input('CAMPO EM BRANCO.\nPRESSIONE ENTER PARA TENTAR NOVAMENTE.')
                return self.menuProdutosAltCaract()
        else:
            self.__msg = raw_input('PRODUTO NAO CADASTRADO.\nPRESSIONE ENTER PARA TENTAR NOVAMENTE.')
            return self.menuProdutosAltPreco()
        
    def menuProdutosExc(self):
        self.menuCabecalho(self.logado,'EXCLUIR PRODUTO')
        print ('PARA CANCELAR A ACAO MANTENHA O CAMPO VAZIO E PRESSIONE ENTER.\n')
        self.__nome = raw_input('DIGITE O NOME DO PRODUTO: ')
        if self.__nome != '':
            if produto.delProduto(self.__nome):
                self.__msg = raw_input('OPERACAO REALIZADA COM SUCESSO.\nPRESSIONE ENTER PARA VOLTAR AO MENU ANTERIOR.')
                return self.menuProdutos()
            else:
                self.__msg = raw_input('ESTE PRODUTO NAO ESTA CADASTRADO.\nPRESSIONE ENTER PARA TENTAR NOVAMENTE.')
                return self.menuProdutosExc()
        else:
            self.__msg = raw_input('OPERACAO CANCELADA.\nPRESSIONE ENTER PARA VOLTAR AO MENU ANTERIOR.')
            return self.menuProdutos()
        
    def menuProdutosVer(self):
        self.menuCabecalho(self.logado, 'VISUALIANDO PRODUTOS')
        if produto.carregar():
            print 'ATUALMENTE ESTE(S) EH(SAO) OS PRODUTOS CADASTRADOS NO SISTEMA.'
            for self.__i in range(len(produto.produtos)):
                print ('\nNOME:'), produto.produtos[self.__i]
                print ('PRECO:'), produto.precos[self.__i]
                print ('CARACTERISTICAS:'), produto.caracts[self.__i]
            self.__msg = raw_input('\nPRESSIONE ENTER PARA VOLTAR AO MENU ANTERIOR.')
            return self.menuProdutos()
        else:
            self.__msg = raw_input('NAO FOI ENCONTRADO NENHUM PRODUTO PARA INFORMAR.\nPRESSIONE ENTER PARA VOLTAR AO MENU ANTERIOR.')
    
a = Menu()
a.iniciar()
