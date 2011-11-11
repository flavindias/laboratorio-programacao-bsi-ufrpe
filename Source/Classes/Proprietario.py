class Proprietario:

    def __init__(self):
        self.carregar()

    def setNome(self, novoNome):
        self.nome = novoNome.upper()
    def getNome(self):
        return self.nome

    def setCPF(self, novoCPF):
        self.CPF = novoCPF
    def getCPF(self):
        return self.CPF

    def salvar(self):
        self.linhas = []
        self.arquivo = open('..\\Arquivos\\BancoDados.txt','r')
        self.linhas = self.arquivo.readlines()
        self.linhas[0] = self.nome+'\n'
        self.linhas[1] = self.CPF+'\n'
        self.arquivo.close()
        self.string = ''
        for self.i in range(len(self.linhas)):
            self.string = self.string+self.linhas[self.i]
        self.arquivo = open('..\\Arquivos\\BancoDados.txt','w')
        self.arquivo.write(self.string)
        self.arquivo.close()

    def carregar(self):
        self.arquivo = open('..\\Arquivos\\BancoDados.txt','r')
        self.linhas = self.arquivo.readlines()
        for self.i in range(2):
            self.linhas[self.i] = self.linhas[self.i].rstrip('\n')
        self.nome = self.linhas[0]
        self.CPF = self.linhas[1]
