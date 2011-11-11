class Cliente:

    def __init__(self):
        self.nomes = []
        self.documentos = []
        self.enderecos = []
        self.automovels = []
        self.placas = []
        self.carregar()

    def getNome(self):
        return self.nome
    def getDocumento(self):
        return self.documento
    def getEndereco(self):
        return self.endereco
    def getAutomovel(self):
        return self.automovel
    def getPlaca(self):
        return self.placa

    def setNome(self, novoNome):
        self.nome = novoNome
    def setDocumento(self, novoDocuemento):
        self.documento = novoDocuemento
    def setEndereco(self, novoEndereco):
        self.endereco = novoEndereco
    def setAutomovel(self, novoAutomovel):
        self.automovel = novoAutomovel
    def setPlaca(self, novaPlaca):
        self.placa = novaPlaca

    def carregar(self):
        self.arquivo = open('..\\Arquivos\\BancoDados.txt', 'r')
        self.linhas = self.arquivo.readlines()
        for self.i in range(8,13):
            self.linhas[self.i] = self.linhas[self.i].rstrip('n')
            self.linhas[self.i] = self.linhas[self.i].split('|')
        for self.i in range(len(self.linhas[8])):
            self.nomes.append(self.linhas[8][self.i])
            self.documentos.append(self.linhas[9][self.i])
            self.enderecos.append(self.linhas[10][self.i])
            self.automovels.append(self.linhas[11][self.i])
            self.placas.append(self.linhas[12][self.i])        
        self.arquivo.close()

    def salvar(self):
        self.arquivo = open('..\\Arquivos\\BancoDados.txt', 'r')
        self.linhas = self.arquivo.readlines()
        self.string1=''
        self.string2=''
        self.string3=''
        self.string4=''
        self.string5=''
        for self.i in range(len(self.nomes)):
            self.string1 = self.string1+self.nomes[self.i]+'|'
            self.string2 = self.string2+self.documentos[self.i]+'|'
            self.string3 = self.string3+self.enderecos[self.i]+'|'
            self.string4 = self.string4+self.automovels[self.i]+'|'
            self.string5 = self.string5+self.placas[self.i]+'|'
        self.linhas[8] = self.string1+'\n'
        self.linhas[9] = self.string2+'\n'
        self.linhas[10] = self.string3+'\n'
        self.linhas[11] = self.string4+'\n'
        self.linhas[12] = self.string5+'\n'
        self.string = ''
        for self.i in range(len(self.linhas)):
            self.string = self.string+self.linhas[self.i]
        self.arquivo.close()
        self.arquivo = open('..\\Arquivos\\BancoDados.txt', 'w')
        self.arquivo.write(self.string)
        self.arquivo.close()
