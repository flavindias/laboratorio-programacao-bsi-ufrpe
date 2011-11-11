import time

class Vendas:

    def __init__(self):
        self.produtos = []
        self.precos = []
        self.qtdes = []

    def getProduto(self):
        return self.produto
    def setProduto(self, novoProduto):
        self.produto = novoProduto.upper()
    def addCarrinho(self):
        if self.produto in self.produtos:
            return False
        else:
            self.produtos.append(self.produto)
            self.__addQtde()
            self.__addPreco()
            return True
    def delCarrinho(self):
        if self.produto in self.produtos:
            self.valor = self.produtos.index(self.produto)
            del self.produtos[self.valor]
            del self.precos[self.valor]
            del self.qtdes[self.valor]
            return True
        else:
            return False

    def getQtde(self):
        return self.qtde
    def setQtde(self, novoQtde):
        self.qtde = novoQtde
    def __addQtde(self):
        self.qtdes.append(self.qtde)


    def getPreco(self):
        return self.preco
    def setPreco(self, novoPreco):
        self.preco = novoPreco
    def __addPreco(self):
        self.precos.append(self.preco)

    def getDocComprador(self):
        return self.usuario
    def setDocComprador(self, novoDocComprador):
        self.docComprador = novoDocComprador

    def calcTotal(self):
        self.total = 0
        for self.j in range(len(self.produtos)):
            self.total += eval(self.precos[self.j])*eval(self.qtdes[self.j])
        return self.total

    def datar(self):
        self.data = time.localtime()

    def getDataAno(self):
        return self.data[0]
    def getDataMes(self):
        return self.data[1]
    def getDataDia(self):
        return self.data[2]
    def getDataHora(self):
        return self.data[3]
    def getDataMin(self):
        return self.data[4]
    def getDataSeg(self):
        return self.data[5]

    def salvar(self):
        self.__lista = []
        self.__lista.append(login.getUsuario())
        self.__lista.append(self.docComprador)
        self.__lista.append('')
        self.__lista.append('')
        self.__lista.append('')
        for self.i in range(len(self.produtos)):
            self.__lista[2] += self.produtos[self.i]+','
            self.__lista[3] += self.qtdes[self.i]+','
            self.__lista[4] += self.precos[self.i]+','
        self.__lista[2] = self.__lista[2][:-1]
        self.__lista[3] = self.__lista[3][:-1]
        self.__lista[4] = self.__lista[4][:-1]
        self.__lista.append(self.calcTotal())
        self.__lista.append('')
        for self.i in range(6):
            self.__lista[6] += str(self.data[self.i])+','
        self.__lista[6] = self.__lista[6][:-1]
        self.__string = ''
        for self.i in range(len(self.__lista)):
            self.__string += str(self.__lista[self.i])+'|'
        self.__string = self.string[:-1]+'\n'
        self.__arquivo = open('..\\Arquivos\\Relatorio.txt', 'a')
        self.__arquivo.write(self.__string)
        self.__arquivo.close()
        
