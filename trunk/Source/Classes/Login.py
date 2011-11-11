class Login:

    def __init__(self):
        self.carregar()

    def getUsuario(self):
        return self.__usuario

    def getSenha(self):
        return self.senha

    def getSenhas1(self):
        self.carregar()
        return self.senhas[0]

    def carregar(self):
        self.arquivo = open('..\\Arquivos\\Senha.txt', 'r')
        self.linhas = self.arquivo.readlines()
        for self.i in range(2):
            self.linhas[self.i] = self.linhas[self.i].rstrip('\n')
            self.linhas[self.i] = self.linhas[self.i].rstrip(' ')
            self.linhas[self.i] = self.linhas[self.i].split(',')

        self.usuarios = []
        for self.i in range(len(self.linhas[0])):
            self.usuarios.append(self.linhas[0][self.i])

        self.senhas = []
        for self.i in range(len(self.linhas[1])):
            self.senhas.append(self.linhas[1][self.i])

        self.arquivo.close()

    def salvar(self):
        self.string1 = ""
        self.string2 = ""
        
        for self.i in range(len(self.usuarios)):
            self.string1 = self.string1+self.usuarios[self.i]+','

        for self.i in range(len(self.senhas)):
            self.string2 = self.string2+self.senhas[self.i]+','
    
        self.arquivo = open('..\\Arquivos\\Senha.txt', 'w')
        self.arquivo.write(self.string1[:-1]+'\n'+self.string2[:-1])
        self.arquivo.close()

    def addUsuario(self, usuario, senha):
        self.carregar()
        self.__usuario = usuario.upper()
        self.__senha = senha
        if self.__usuario in self.usuarios:
            return False
        else:
            self.usuarios.append(self.__usuario)
            self.senhas.append(self.__senha)
            self.salvar()
            return True
        
    def delUsuario(self, usuario):
        self.carregar()
        self.__usuario = usuario.upper()
        if self.__usuario in self.usuarios:
            self.__valor = self.usuarios.index(self.__usuario)
            del self.usuarios[self.__valor]
            del self.senhas[self.__valor]
            self.salvar()
            return True
        else:
            return False

    def altUsuario(self, novoUsuario):
        self.carregar()
        self.__novo = novoUsuario.upper()
        if self.__usuario in self.usuarios and not(self.__novo in self.usuarios):
            self.usuarios[self.usuarios.index(self.__usuario)] = self.__novo
            self.salvar()
            return True
        else:
            return False

    def altSenha(self, usuario, novaSenha):
        self.carregar()
        self.__novo = novaSenha
        self.__usuario = usuario.upper()
        if self.__usuario in self.usuarios:
            self.senhas[self.usuarios.index(self.__usuario)] = self.__novo
            self.salvar()
            return True
        else:
            return False
            
    def altUsuarioSenha(self, usuario, novoUsuario, novaSenha):
        self.carregar()
        self.__usuario = usuario.upper()
        self.__novoUsuario = novoUsuario.upper()
        self.__novaSenha = novaSenha
        if self.__usuario in self.usuarios:
            self.senhas[self.usuarios.index(self.__usuario)] = self.__novaSenha
            self.usuarios[self.usuarios.index(self.__usuario)] = self.__novoUsuario
            self.salvar()
            return True
        else:
            return False
    
    def validar(self, usuario, senha):
        self.carregar()
        self.__usuario = usuario.upper()
        self.__senha = senha
        if self.__usuario in self.usuarios:
            if self.__senha == self.senhas[self.usuarios.index(self.__usuario)]:
                return True
            else:
                return False
        else:
            return False
