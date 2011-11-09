'''
Created on 23/10/2011

@author: Emeson Santana & Isabella Rocha
'''
import login
import os
import time

class Main:
    def registrarP(self, lista):
        self.Error = True
        try:
            self.arq = open('C:\\programacao\\bd\\professores\\%s.txt' %('n_id'), 'r')
            self.id = int(self.arq.readline())
            self.id += 1
            self.arq.close()
            print'Numero de Identificacao: %s' %(self.id)
            self.arq = open('C:\\programacao\\bd\\professores\\%s.txt' %('n_id'), 'w')
            self.arq.write(str(self.id))
            self.arq.close()
            self.arq = open('C:\\programacao\\bd\\professores\\%s.txt' %(str(self.id)), 'w')
            for self.i in range(0, len(lista)):
                lista[self.i] += '\n'
            self.arq.writelines(lista)
            self.arq.close()
            self.arq = open('C:\\programacao\\bd\\professores\\%s.txt' %('pesquisa'), 'a')
            self.arq.write('%s-%s' %(str(self.id), lista[0]))
            self.arq.close()
            self.Error = False
        except:
            self.Error =True
        self.id = None
        return self.Error
    def excluirP(self, numero):#Numero = Numero de Matricula
        self.Error = True
        try:
            self.arq = open('C:\\programacao\\bd\\professores\\%s.txt' %(numero), 'r')
            self.arq.close()
            os.remove('C:\\programacao\\bd\\professores\\%s.txt' %(numero))
            self.arq = open('C:\\programacao\\bd\\professores\\%s.txt' %('pesquisa'), 'r')
            self.Lista = self.arq.readlines()
            self.arq.close()
            for self.i in range(len(self.Lista)):
                self.Lista[self.i] = self.Lista[self.i].split('-')
                if self.Lista[self.i][0] == str(numero):
                    del self.Lista[self.i]
            for self.i in range(len(self.Lista)):
                self.Lista[self.i] = self.Lista[self.i][0] + '-' + self.Lista[self.i][1]
            self.arq = open('C:\\programacao\\bd\\professores\\%s.txt' %('pesquisa'), 'w')
            self.arq.writelines(self.Lista)
            self.arq.close()
            self.Error = False
        except:
            self.Error = True
        self.Lista = []
        return self.Error
    def visualizarP(self, numero):#Verificar se a id existe
        try:
            self.arq = open('C:\\programacao\\bd\\professores\\%s.txt' %(numero), 'r')
            self.Lista = self.arq.readlines()
            for self.i in range(len(self.Lista)):
                self.Lista[self.i] = self.Lista[self.i].rstrip('\n')
        except:
            True
        return self.Lista
    def editarP(self,lista):
        self.Error = True
        try:
            self.id = lista[0]
            self.verif = lista[1]
            self.arq = open('C:\\programacao\\bd\\professores\\%s.txt' %(self.id), 'w')
            del lista[0]
            for self.i in range(len(lista)):
                lista[self.i] = lista[self.i] + '\n'
            self.arq.writelines(lista)
            self.arq.close()
            self.arq = open('C:\\programacao\\bd\\professores\\%s.txt' %('pesquisa'), 'r')
            self.Lista = self.arq.readlines()
            self.arq.close()
            for self.i in range(len(self.Lista)):
                self.Lista[self.i] = self.Lista[self.i].split('-')
                if (self.Lista[self.i][0] == str(self.id)) and (self.Lista[self.i][1] != self.verif):
                    self.Lista[self.i][1] = self.verif
            for self.i in range(len(self.Lista)):
                self.Lista[self.i] = self.Lista[self.i][0] + '-' + self.Lista[self.i][1]
                if self.Lista[self.i].find('\n') == -1:
                    self.Lista[self.i] = self.Lista[self.i] + '\n'
            self.arq = open('C:\\programacao\\bd\\professores\\%s.txt' %('pesquisa'), 'w')
            self.arq.writelines(self.Lista)
            self.arq.close()
            self.Error = False
        except:
            self.Error = True
        self.id = None
        self.verif = None
        self.Lista = []
        return self.Error
    def registrarA(self, lista):
        self.Error = True
        try:
            self.arq = open('C:\\programacao\\bd\\alunos\\%s.txt' %('n_matricula'), 'r')
            self.matricula = int(self.arq.readline())
            self.matricula += 1
            self.arq.close()
            print'Numero de Matricula: %s' %(self.matricula)
            self.arq = open('C:\\programacao\\bd\\alunos\\%s.txt' %('n_matricula'), 'w')
            self.arq.write(str(self.matricula))
            self.arq.close()
            self.arq = open('C:\\programacao\\bd\\alunos\\%s.txt' %(str(self.matricula)), 'w')
            for self.i in range(0, len(lista)):
                lista[self.i] += '\n'
            self.arq.writelines(lista)
            self.arq.close()
            self.arq = open('C:\\programacao\\bd\\alunos\\%s.txt' %('pesquisa'), 'a')
            self.arq.write('%s-%s' %(str(self.matricula), lista[0]))
            self.arq.close()
            self.Error = False
        except:
            self.Error =True
        self.matricula = None
        return self.Error
    def excluirA(self, numero):#Numero = Numero de Matricula
        self.Error = True
        try:
            self.arq = open('C:\\programacao\\bd\\alunos\\%s.txt' %(numero), 'r')
            self.arq.close()
            os.remove('C:\\programacao\\bd\\alunos\\%s.txt' %(numero))
            self.arq = open('C:\\programacao\\bd\\alunos\\%s.txt' %('pesquisa'), 'r')
            self.Lista = self.arq.readlines()
            self.arq.close()
            for self.i in range(len(self.Lista)):
                self.Lista[self.i] = self.Lista[self.i].split('-')
                if self.Lista[self.i][0] == str(numero):
                    del self.Lista[self.i]
            for self.i in range(len(self.Lista)):
                self.Lista[self.i] = self.Lista[self.i][0] + '-' + self.Lista[self.i][1]
            self.arq = open('C:\\programacao\\bd\\alunos\\%s.txt' %('pesquisa'), 'w')
            self.arq.writelines(self.Lista)
            self.arq.close()
            self.Error = False
        except:
            self.Error = True
        self.Lista = []
        return self.Error
    def visualizarA(self, numero):#Verificar se a matricula existe
        try:
            self.arq = open('C:\\programacao\\bd\\alunos\\%s.txt' %(numero), 'r')
            self.Lista = self.arq.readlines()
            for self.i in range(len(self.Lista)):
                self.Lista[self.i] = self.Lista[self.i].rstrip('\n')
        except:
            True
        return self.Lista
    def editarA(self,lista):
        self.Error = True
        try:
            self.matricula = lista[0]
            self.verif = lista[1]
            self.arq = open('C:\\programacao\\bd\\alunos\\%s.txt' %(self.matricula), 'w')
            del lista[0]
            for self.i in range(len(lista)):
                lista[self.i] = lista[self.i] + '\n'
            self.arq.writelines(lista)
            self.arq.close()
            self.arq = open('C:\\programacao\\bd\\alunos\\%s.txt' %('pesquisa'), 'r')
            self.Lista = self.arq.readlines()
            self.arq.close()
            for self.i in range(len(self.Lista)):
                self.Lista[self.i] = self.Lista[self.i].split('-')
                if (self.Lista[self.i][0] == str(self.matricula)) and (self.Lista[self.i][1] != self.verif):
                    self.Lista[self.i][1] = self.verif
            for self.i in range(len(self.Lista)):
                self.Lista[self.i] = self.Lista[self.i][0] + '-' + self.Lista[self.i][1]
                if self.Lista[self.i].find('\n') == -1:
                    self.Lista[self.i] = self.Lista[self.i] + '\n'
            self.arq = open('C:\\programacao\\bd\\alunos\\%s.txt' %('pesquisa'), 'w')
            self.arq.writelines(self.Lista)
            self.arq.close()
            self.Error = False
        except:
            self.Error = True
        self.matricula = None
        self.verif = None
        self.Lista = []
        return self.Error
    def __init__(self):
        self.__arq = None
        self.__num = None
        self.__Error = None
        self.__login = ''
        self.__senha = ''
        self.__input_output = 1
        self.__ctrl = 0
        self.__ver = ''
        self.__lista = ['','','','','','','','','','','','','','','','','','','','']
        
        while self.__input_output != 0:
            os.system('cls')
            print"##############################################################"
            print"#                   Sistema Academico                        #"
            print"##############################################################"
            print"          ,_"
            print"          | `""---..._____"
            print"          -...______   ",' _````""""""""`|'
            print'                 \   ```` ``"---...__  |'
            print"                 |`              |   ``!"
            print"                 |               |     A"
            print"                 |               /\   /#\       ."
            print"                 /`--..______..-'  |  ###"
            print"                |   /  `\    /`--. |  ###"
            print"               _|  |  .-;`-./;-.  ||  ###"
            print"              / \  \ /\_|    |_/\ //\ ##'"
            print"              |  `-' \__/ _  \__/ |  |`#"
            print"              \_,                 /_/"
            print"                 `\              /"
            print"                   '.  '.__.'  .'"
            print"                     `-,____,-'"
            print'                      /"""I""\                  .'
            print"                     /`---'--'\                 ."
            print"##############################################################"
            print"#", time.strftime ( "%a, %d %b %Y                                    %H:%M "),"#"
            print"##############################################################"
            ########################################
            if self.__ctrl == 0:
                print''
                self.__login = raw_input('Login: ')
                self.__senha = raw_input('Senha: ')
                if login.verificar(self.__login, self.__senha):
                        self.__ctrl = 1
                        self.__login = None
                        self.__senha = None
                        continue
                else:
                    print'Login ou Senha Invalido!'
                    time.sleep(3)
                    continue
            ########################################
            elif self.__ctrl == 1:
                print''
                print'0 - Sair'
                print''
                print'1 - Gerenciamento de Aluno'
                print''
                print'2 - Gerenciamento de Professores'
                print''
                print''
                self.__ver = raw_input('Digite o valor da funcionalidade que quer acessar: ')
                print''
                if self.__ver in ['0','1','2']:
                    if self.__ver == '1':
                        self.__ctrl = 2
                        self.__ver = None
                        continue
                    elif self.__ver == '2':
                        self.__ctrl = 7
                        self.__ver = None
                        continue
                    else:
                        self.__ctrl = 0
                        self.__ver = None
                        continue
                else:
                    print'Opcao Invalida!'
                    self.__ver = None
                    time.sleep(3)
                    continue
            #########################################
            elif self.__ctrl == 2:
                print''
                print'                  Gerenciamento de Alunos'
                print''
                print'0 - Voltar ao menu Anterior'
                print''
                print'1 - Registrar Aluno'
                print''
                print'2 - Editar Dados'
                print''
                print'3 - Excluir Registro'
                print''
                print'4 - Visualizar Dados'
                print''
                self.__ver = raw_input('Digite o valor da funcionalidade que quer acessar: ')
                if self.__ver in ['0','1','2','3','4']:
                    if self.__ver == '0':
                        self.__ctrl = 1
                        self.__ver = None
                        continue
                    elif self.__ver == '1':
                        self.__ctrl = 3
                        self.__ver = None
                        continue
                    elif self.__ver == '2':
                        self.__ctrl = 4
                        self.__ver = None
                        continue
                    elif self.__ver == '3':
                        self.__ctrl = 5
                        self.__ver = None
                        continue
                    elif self.__ver == '4':
                        self.__ctrl = 6
                        self.__ver = None
                        continue
                else:
                    print'Opcao Invalida!'
                    self.__ver = None
                    time.sleep(3)
                    continue
            elif self.__ctrl == 3:
                print''
                print'                    Registrar Aluno(a)'
                self.__ver = 0
                for self.i in ['Nome: ','Serie: ','Ano de Ingresso: ','Turno: ','CPF: ','RG: ','Sexo: ','Data de Nascimento: ','Nome da Mae: ','Nome do Pai: ','Email: ','Telefone: ','CEP: ','Rua: ','Numero: ','Complemento: ','Bairro: ','Cidade: ','Estado: ','Pais: ']:
                    if self.__ver == 0:
                        print''
                        print'#Dados Pessoais'
                        print''
                    elif self.__ver == 12:
                        print''
                        print'#Endereco'
                        print''
                    self.__lista[self.__ver] = raw_input(self.i)
                    self.__ver += 1
                self.__Error = self.registrarA(self.__lista)
                if  self.__Error == False:
                    print''
                    print''
                    print'Aluno Registrado com Sucesso!'
                    self.__ctrl = 2
                    self.__lista = []
                    time.sleep(3)
                    continue
                else:
                    print''
                    print''
                    print'Falha ao Registrar, Tente Novamente!'
                    self.__ctrl = 2
                    self.__lista = []
                    time.sleep(3)
                    continue
            elif self.__ctrl == 4:
                print''
                print'                     Editar Registro de Aluno(a)'
                print''
                self.num_matricula = raw_input('Digite o Numero de Matricula do Aluno(a): ')
                if os.path.exists('C:\\programacao\\bd\\alunos\\%s.txt' %(self.num_matricula)):
                    self.__lista = self.visualizarA(self.num_matricula)
                    print''
                    self.__ver = 0
                    for self.i in ['Nome: ','Serie: ','Ano de Ingresso: ','Turno: ','CPF: ','RG: ','Sexo: ','Data de Nascimento: ','Nome da Mae: ','Nome do Pai: ','Email: ','Telefone: ','CEP: ','Rua: ','Numero: ','Complemento: ','Bairro: ','Cidade: ','Estado: ','Pais: ']:
                        print self.__ver,' - ',self.i,self.__lista[self.__ver]
                        self.__ver += 1
                    print'20 - Sair'
                    self.nova_lista = ['Novo Nome: ','Nova Serie: ','Novo Ano de Ingresso: ','Novo Turno: ','Novo CPF: ','Novo RG: ','Novo Sexo: ','Nova Data de Nascimento: ','Novo Nome da Mae: ','Novo Nome do Pai: ','Novo Email: ','Novo Telefone: ','Novo CEP: ','Nova Rua: ','Novo Numero: ','Novo Complemento: ','Novo Bairro: ','Nova Cidade: ','Novo Estado: ','Novo Pais: ']
                    self.__num = raw_input('Digite o valor relativo ao que deseja editar: ')
                    if int(self.__num) in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
                        if int(self.__num) != 20:
                            self.__lista[int(self.__num)] = raw_input(self.nova_lista[int(self.__num)])
                            self.__lista = [self.num_matricula] + self.__lista
                            self.__Error = self.editarA(self.__lista)
                            if self.__Error == False:
                                print''
                                print'Editado com Sucesso!'
                                self.__ctrl = 2
                                self.num_matricula = None
                                self.__lista = []
                                self.nova_lista = []
                                self.__num = None
                                time.sleep(3)
                                continue
                            else:
                                print''
                                print'Falha ao Editar!'
                                self.__ctrl = 2
                                self.num_matricula = None
                                self.__lista = []
                                self.nova_lista = []
                                self.__num = None
                                time.sleep(3)
                                continue
                        else:
                            self.__ctrl = 2
                            self.num_matricula = None
                            self.__lista = []
                            self.nova_lista = []
                            self.__num = None
                            continue
                else:
                    print''
                    print'Numero de Matricula Invalido!'
                    self.__ctrl = 2
                    self.num_matricula = None
                    time.sleep(3)
                    continue
            elif self.__ctrl == 5:
                print''
                print'                        Excluir Registro de Aluno(a)'
                print''
                self.num_matricula = raw_input('Digite o Numero de Matricula: ')
                if os.path.exists('C:\\programacao\\bd\\alunos\\%s.txt' %(self.num_matricula)):
                    self.__lista = self.visualizarA(self.num_matricula)
                    print'Tem certeza que quer Excluir o Registro do Aluno(a) %s?' %(self.__lista[0])
                    print''
                    print'1 - Sim'
                    print'2 - Nao'
                    print''
                    self.__ver = raw_input()
                    if self.__ver in ['1','2']:
                        if self.__ver == '1':
                            self.__Error = self.excluirA(self.num_matricula)
                            if self.__Error == False:
                                print''
                                print'Registro do Aluno(a) %s Excluido com Sucesso!' %(self.__lista[0])
                                self.__ctrl = 2
                                self.num_matricula = None
                                self.__lista = []
                                self.__ver = None
                                time.sleep(3)
                                continue
                            else:
                                print''
                                print'Nao foi possivel Excluir o Registro do Aluno(a) %s!' %(self.__lista[0])
                                self.__ctrl = 2
                                self.num_matricula = None
                                self.__lista = []
                                self.__ver = None
                                time.sleep(3)
                                continue
                        else:
                            self.__ctrl = 2
                            self.num_matricula = None
                            self.__lista = []
                            self.__ver = None
                            continue
                    else:
                        print''
                        print'Opcao Invalida!'
                        self.__ctrl = 2
                        self.num_matricula = None
                        self.__lista = []
                        self.__ver = None
                        time.sleep(3)
                        continue
                else:
                    print''
                    print'Opcao Invalida!'
                    self.__ctrl = 2
                    self.num_matricula = None
                    self.__lista = []
                    self.__ver = None
                    time.sleep(3)
                    continue
            elif self.__ctrl == 6:
                print''
                print'                     Visualizar Registro de Aluno(a)'
                print''
                self.num_matricula = raw_input('Digite o Numero de Matricula do Aluno(a): ')
                if os.path.exists('C:\\programacao\\bd\\alunos\\%s.txt' %(self.num_matricula)):
                    self.__lista = self.visualizarA(self.num_matricula)
                    print''
                    self.__ver = 0
                    for self.i in ['Nome: ','Serie: ','Ano de Ingresso: ','Turno: ','CPF: ','RG: ','Sexo: ','Data de Nascimento: ','Nome da Mae: ','Nome do Pai: ','Email: ','Telefone: ','CEP: ','Rua: ','Numero: ','Complemento: ','Bairro: ','Cidade: ','Estado: ','Pais: ']:
                        print self.i,self.__lista[self.__ver]
                        self.__ver += 1
                    print''
                    self.__num = raw_input('PRESSIONE ENTER PARA VOLTAR AO MENU ANTERIOR')
                    self.__ctrl = 2
                    self.__ver = None
                    self.__num = None
                    self.__lista = []
                    self.num_matricula = None
                    continue
                else:
                    print''
                    print'Numero de Matricula Invalido!'
                    self.__ctrl = 2
                    self.num_matricula = None
                    time.sleep(3)
                    continue
            elif self.__ctrl == 7:
                print''
                print'                  Gerenciamento de Professores'
                print''
                print'0 - Voltar ao menu Anterior'
                print''
                print'1 - Registrar Professor'
                print''
                print'2 - Editar Dados'
                print''
                print'3 - Excluir Registro'
                print''
                print'4 - Visualizar Dados'
                print''
                self.__ver = raw_input('Digite o valor da funcionalidade que quer acessar: ')
                if self.__ver in ['0','1','2','3','4']:
                    if self.__ver == '0':
                        self.__ctrl = 1
                        self.__ver = None
                        continue
                    elif self.__ver == '1':
                        self.__ctrl = 8
                        self.__ver = None
                        continue
                    elif self.__ver == '2':
                        self.__ctrl = 9
                        self.__ver = None
                        continue
                    elif self.__ver == '3':
                        self.__ctrl = 10
                        self.__ver = None
                        continue
                    elif self.__ver == '4':
                        self.__ctrl = 11
                        self.__ver = None
                        continue
                else:
                    print'Opcao Invalida!'
                    self.__ver = None
                    time.sleep(3)
                    continue
            elif self.__ctrl == 8:
                print''
                print'                    Registrar Professor(a)'
                self.__ver = 0
                for self.i in ['Nome: ','Disciplina: ','CPF: ','RG: ','Sexo: ','Data de Nascimento: ','Email: ','Telefone: ','CEP: ','Rua: ','Numero: ','Complemento: ','Bairro: ','Cidade: ','Estado: ','Pais: ']:
                    if self.__ver == 0:
                        print''
                        print'#Dados Pessoais'
                        print''
                    elif self.__ver == 8:
                        print''
                        print'#Endereco'
                        print''
                    self.__lista[self.__ver] = raw_input(self.i)
                    self.__ver += 1
                self.__Error = self.registrarP(self.__lista)
                if  self.__Error == False:
                    print''
                    print''
                    print'Professor Registrado com Sucesso!'
                    self.__ctrl = 7
                    self.__lista = []
                    time.sleep(3)
                    continue
                else:
                    print''
                    print''
                    print'Falha ao Registrar, Tente Novamente!'
                    self.__ctrl = 7
                    self.__lista = []
                    time.sleep(3)
                    continue
            elif self.__ctrl == 9:
                print''
                print'                     Editar Registro de Professor(a)'
                print''
                self.num_matricula = raw_input('Digite o Numero de Identificacao do Professor(a): ')
                if os.path.exists('C:\\programacao\\bd\\professores\\%s.txt' %(self.num_matricula)):
                    self.__lista = self.visualizarP(self.num_matricula)
                    print''
                    self.__ver = 0
                    for self.i in ['Nome: ','Disciplina: ','CPF: ','RG: ','Sexo: ','Data de Nascimento: ','Email: ','Telefone: ','CEP: ','Rua: ','Numero: ','Complemento: ','Bairro: ','Cidade: ','Estado: ','Pais: ']:
                        print self.__ver,' - ',self.i,self.__lista[self.__ver]
                        self.__ver += 1
                    print'16 - Sair'
                    self.nova_lista = ['Novo Nome: ','Nova Disciplina: ','Novo CPF: ','Novo RG: ','Novo Sexo: ','Nova Data de Nascimento: ','Novo Email: ','Novo Telefone: ','Novo CEP: ','Nova Rua: ','Novo Numero: ','Novo Complemento: ','Novo Bairro: ','Nova Cidade: ','Novo Estado: ','Novo Pais: ']
                    self.__num = raw_input('Digite o valor relativo ao que deseja editar: ')
                    if int(self.__num) in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]:
                        if int(self.__num) != 16:
                            self.__lista[int(self.__num)] = raw_input(self.nova_lista[int(self.__num)])
                            self.__lista = [self.num_matricula] + self.__lista
                            self.__Error = self.editarP(self.__lista)
                            if self.__Error == False:
                                print''
                                print'Editado com Sucesso!'
                                self.__ctrl = 7
                                self.num_matricula = None
                                self.__lista = []
                                self.nova_lista = []
                                self.__num = None
                                time.sleep(3)
                                continue
                            else:
                                print''
                                print'Falha ao Editar!'
                                self.__ctrl = 7
                                self.num_matricula = None
                                self.__lista = []
                                self.nova_lista = []
                                self.__num = None
                                time.sleep(3)
                                continue
                        else:
                            self.__ctrl = 7
                            self.num_matricula = None
                            self.__lista = []
                            self.nova_lista = []
                            self.__num = None
                            continue
                else:
                    print''
                    print'Numero de Identificacao Invalido!'
                    self.__ctrl = 7
                    self.num_matricula = None
                    time.sleep(3)
                    continue
            elif self.__ctrl == 10:
                print''
                print'                        Excluir Registro de Professor(a)'
                print''
                self.num_matricula = raw_input('Digite o Numero de Identificacao: ')
                if os.path.exists('C:\\programacao\\bd\\professores\\%s.txt' %(self.num_matricula)):
                    self.__lista = self.visualizarP(self.num_matricula)
                    print'Tem certeza que quer Excluir o Registro do Professor(a) %s?' %(self.__lista[0])
                    print''
                    print'1 - Sim'
                    print'2 - Nao'
                    print''
                    self.__ver = raw_input()
                    if self.__ver in ['1','2']:
                        if self.__ver == '1':
                            self.__Error = self.excluirP(self.num_matricula)
                            if self.__Error == False:
                                print''
                                print'Registro do Professor(a) %s Excluido com Sucesso!' %(self.__lista[0])
                                self.__ctrl = 7
                                self.num_matricula = None
                                self.__lista = []
                                self.__ver = None
                                time.sleep(3)
                                continue
                            else:
                                print''
                                print'Nao foi possivel Excluir o Registro do Professor(a) %s!' %(self.__lista[0])
                                self.__ctrl = 7
                                self.num_matricula = None
                                self.__lista = []
                                self.__ver = None
                                time.sleep(3)
                                continue
                        else:
                            self.__ctrl = 7
                            self.num_matricula = None
                            self.__lista = []
                            self.__ver = None
                            continue
                    else:
                        print''
                        print'Opcao Invalida!'
                        self.__ctrl = 7
                        self.num_matricula = None
                        self.__lista = []
                        self.__ver = None
                        time.sleep(3)
                        continue
                else:
                    print''
                    print'Opcao Invalida!'
                    self.__ctrl = 7
                    self.num_matricula = None
                    self.__lista = []
                    self.__ver = None
                    time.sleep(3)
                    continue
            elif self.__ctrl == 11:
                print''
                print'                     Visualizar Registro de Professor(a)'
                print''
                self.num_matricula = raw_input('Digite o Numero de Identificacao do Professor(a): ')
                if os.path.exists('C:\\programacao\\bd\\professores\\%s.txt' %(self.num_matricula)):
                    self.__lista = self.visualizarP(self.num_matricula)
                    print''
                    self.__ver = 0
                    for self.i in ['Nome: ','Disciplina: ','CPF: ','RG: ','Sexo: ','Data de Nascimento: ','Email: ','Telefone: ','CEP: ','Rua: ','Numero: ','Complemento: ','Bairro: ','Cidade: ','Estado: ','Pais: ']:
                        print self.i,self.__lista[self.__ver]
                        self.__ver += 1
                    print''
                    self.__num = raw_input('PRESSIONE ENTER PARA VOLTAR AO MENU ANTERIOR')
                    self.__ctrl = 7
                    self.__ver = None
                    self.__num = None
                    self.__lista = []
                    self.num_matricula = None
                    continue
                else:
                    print''
                    print'Numero de Identificacao Invalido!'
                    self.__ctrl = 7
                    self.num_matricula = None
                    time.sleep(3)
                    continue
                
NewMain = Main()
