class PostoGasolina:

    def __init__(self):
        self.carregar()

    def setRazaoSocial(self, novoRazao):
        self.razaoSocial = novoRazao.upper()
    def getRazaoSocial(self):
        return self.razaoSocial

    def setCNPJ(self, novoCNPJ):
        self.CNPJ = novoCNPJ
    def getCNPJ(self):
        return self.CNPJ

    def salvar(self):
        self.linhas = []
        self.arquivo = open('..\\Arquivos\\BancoDados.txt','r')
        self.linhas = self.arquivo.readlines()
        self.linhas[2] = self.razaoSocial+'\n'
        self.linhas[3] = self.CNPJ+'\n'
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
        for self.i in range(2,4):
            self.linhas[self.i] = self.linhas[self.i].rstrip('\n')
        self.razaoSocial = self.linhas[2]
        self.CNPJ = self.linhas[2]
