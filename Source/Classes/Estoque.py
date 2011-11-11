class Estoque:

    def __init__(self):
        self.carregar()

    def getProduto(self):
        return self.produto
    def setProduto(self, novoProduto):
        self.produto = novoProduto

    def getQtde(self):
        return self.qtde
    def setQtde(self,novaQtde):
        self.qtde = novaQtde

    def carregar(self):
        self.arquivo = open('..\\Arquivos\\BancoDados.txt', 'r')
        self.linha = self.arquivo.readlines()
        self.linha[4] = self.linha[4].rstrip('\n')
        self.linha[4] = self.linha[4].split('|')
        self.linha[7] = self.linha[7].rstrip('\n')
        self.linha[7] = self.linha[7].split('|')
        self.produtos = []
        self.qtdes = []
        for self.i in range(len(self.linha[4])):
            self.produtos.append(self.linha[4][self.i])
            self.qtdes.append(self.linha[7][self.i])
        self.arquivo.close()

    def salvar(self):
        self.string = ''
        for self.i in range(len(self.produtos)):
            self.string = self.string+self.qtdes[self.i]+'|'                        
        self.arquivo = open('..\\Arquivos\\BancoDados.txt','r')
        self.linhas = self.arquivo.readlines()
        self.linhas[7] = self.string+'/n'
        self.string = ''
        for self.i in range(len(self.linhas)):
            self.string = self.string+self.linhas[self.i]
        self.arquivo.close()
        self.arquivo = open('..\\Arquivos\\BancoDados.txt','w')
        self.arquivo.write(self.string)
        self.arquivo.close()

    def iniciarProduto(self):
        self.qtdes.append('0')

    def excluirProduto(self, valor):
        del self.qtdes[valor]

    def addQuantidade(self, valor):
        self.qtde = float(self.qtde)
        self.qtde += float(valor)
        self.qtde = str(self.qtde)

    def retirarQuantidade(self, valor):
        self.qtde = float(self.qtde)
        if float(valor) < self.qtde:
            self.qtde += float(self.qtde)
            return True
        else:
            return False
