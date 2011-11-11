class Produto:

    def __init__(self):
        self.carregar()
        self.produtos = []
        self.precos = []
        self.caracts = []
        self.qtdes = []

    def carregar(self):
        self.__arquivo = open('..\\Arquivos\\Produtos.txt', 'r')
        self.__linha = self.__arquivo.readlines()
        if self.__linha != []:
            for self.__i in range(4):
                self.__linha[self.__i] = self.__linha[self.__i].rstrip('\n')
                self.__linha[self.__i] = self.__linha[self.__i].split('|')
            self.produtos = []
            self.precos = []
            self.caracts = []
            self.qtdes = []
            for self.__i in range(len(self.__linha[0])):
                self.produtos.append(self.__linha[0][self.__i])
                self.precos.append(self.__linha[1][self.__i])
                self.caracts.append(self.__linha[2][self.__i])
                self.qtdes.append(self.__linha[3][self.__i])
            return True
        else:
            return False
        self.__arquivo.close()
 
    def salvar(self):
        self.__string1 = ''
        self.__string2 = ''
        self.__string3 = ''
        self.__string4 = ''
        for self.__i in range(len(self.produtos)):
            self.__string1 = self.__string1+self.produtos[self.__i]+'|'
            self.__string2 = self.__string2+self.precos[self.__i]+'|'
            self.__string3 = self.__string3+self.caracts[self.__i]+'|'
            self.__string4 = self.__string4+self.qtdes[self.__i]+'|'
        self.__arquivo = open('..\\Arquivos\\Produtos.txt','r')
        self.__linhas = self.__arquivo.readlines()
        self.__linhas[0] = self.__string1[:-1]+'\n'
        self.__linhas[1] = self.__string2[:-1]+'\n'
        self.__linhas[2] = self.__string3[:-1]+'\n'
        self.__linhas[3] = self.__string4[:-1]+'\n'
        self.__arquivo.close()
        self.__arquivo = open('..\\Arquivos\\Produtos.txt', 'w')
        self.__string = ''
        for self.__i in range(4):
            self.__string = self.__string+self.__linhas[self.__i]
        self.__arquivo.write(self.__string)
        self.__arquivo.close()

    def addProduto(self, nome, preco, caracteristica):
        self.carregar()
        self.__nome = nome.upper()
        self.__preco = preco
        self.__caract = caracteristica.upper()
        if self.validar(self.__nome):
            return False
        else:
            self.produtos.append(self.__nome)
            self.precos.append(self.__preco)
            self.caracts.append(self.__caract)
            self.qtdes.append('0')
            self.salvar()
            return True

    def delProduto(self, nome):
        self.carregar()
        self.__nome = nome.upper()
        if self.validar(self.__nome):
            self.__posicao = self.produtos.index(self.__nome)
            del self.produtos[self.__posicao]
            del self.precos[self.__posicao]
            del self.caracts[self.__posicao]
            del self.qtdes[self.__posicao]
            self.salvar()
            return True
        else:
            return False

    def altProdutoNome(self, nome, novoNome):
        self.__nome = nome.upper()
        self.__novo = novoNome.upper()
        self.carregar()
        if self.validar(self.__nome):
            self.produtos[self.produtos.index(self.__nome)] = self.__novo
            self.salvar()
            return True
        else:
            return False

    def altProdutoPreco(self, nome, novoPreco):
        self.carregar()
        self.__nome = nome.upper()
        if self.validar(self.__nome):
            self.__novo = novoPreco
            self.precos[self.produtos.index(self.__nome)] = self.__novo
            self.salvar()
            return True
        else:
            return False

    def altProdutoCaract(self, nome, novoCaract):
        self.carregar()
        self.__nome = nome.upper()
        if self.validar(self.__nome):
            self.__novo = novoCaract.upper()
            self.caracts[self.produtos.index(self.__nome)] = self.__novo
            self.salvar()
            return True
        else:
            return False

    def altProdutoQtde(self, nome, novaQtde):
        self.carregar()
        self.__nome = nome.upper()
        if self.validar(self.__nome):
            self.__novo = novaQtde
            self.qtdes[self.produtos.index(self.__nome)] = self.__novo
            self.salvar()
            return True
        else:
            return False

    def validar(self, nome):
        self.carregar()
        self.__nome = nome.upper()
        if self.__nome in self.produtos:
            return True
        else:
            return False

    def getPreco(self, nome):
        self.carregar()
        self.__nome = nome.upper()
        return self.precos[self.produtos.index(self.__nome)]

    def getCaract(self, nome):
        self.carregar()
        self.__nome = nome.upper()
        return self.caracts[self.produtos.index(self.__nome)]
