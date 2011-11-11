class Relatorios:
        
    def gerarRelatorio(self, diaInicio, mesInicio, anoInicio, diaFim, mesFim, anoFim):
        self.listaDados = []
        self.__arquivo = open('..\\Arquivos\\Relatorio.txt', 'r')
        self.__linhas = self.__arquivo.readlines()
        for self.__i in range(len(self.__linhas)):
            self.__linhas[self.__i] = self.__linhas[self.__i].rstrip('\n')
            self.__linhas[self.__i] = self.__linhas[self.__i].split('|')
            for self.__j in range(7):
                self.__linhas[self.__i][self.__j] = self.__linhas[self.__i][self.__j].split(',')
            if int(self.__linhas[self.__i][6][0]) <= int(anoFim) and int(self.__linhas[self.__i][6][0]) >= int(anoInicio):
                self.listaDados.append(self.__linhas[self.__i])
        self.__arquivo.close()
        self.__posicao = []
        for self.__i in range(len(self.listaDados)):
            if int(self.listaDados[self.__i][6][0]) == int(anoInicio) and int(self.listaDados[self.__i][6][1]) < int(mesInicio):
                self.__posicao.append(self.__i)
            if int(self.listaDados[self.__i][6][0]) == int(anoFim) and int(self.listaDados[self.__i][6][1]) > int(mesFim):
                self.__posicao.append(self.__i)
        self.__posicao = list(set(self.__posicao))
        for self.__i in self.__posicao:
            del self.listaDados[self.__i]
        self.__posicao = []
        for self.__i in range(len(self.listaDados)):
            if int(self.listaDados[self.__i][6][0]) == int(anoInicio) and int(self.listaDados[self.__i][6][1]) == int(mesInicio) and (self.listaDados[self.__i][6][2]) < int(diaInicio):
                self.__posicao.append(self.__i)
            if int(self.listaDados[self.__i][6][0]) == int(anoFim) and int(self.listaDados[self.__i][6][1]) == int(mesFim) and int(self.listaDados[self.__i][6][2]) > int(diaFim):
                self.__posicao.append(self.__i)
        self.__posicao = list(set(self.__posicao))
        for self.__i in self.__posicao:
            del self.listaDados[self.__i]
        del diaInicio, mesInicio, anoInicio, diaFim, mesFim, anoFim
        return self.listaDados

    def printRelatorioDetalhado(self):
        if self.listaDados == []:
            return False
        else:
            print 'PARA MELHOR VISUALIZAR O RELATORIO MAXIMIZE A TELA\n'
            print 'VEND:    DOC.CLIENT:  DATA:               PROD:       QUANT:      TOTAL:'
            for self.__i in range(len(self.listaDados)):
                for self.__j in range(len(self.listaDados[self.__i][2])):
                    if self.__j == 0:
                        print str(self.listaDados[self.__i][0][0])+'    '+str(self.listaDados[self.__i][1][0])+'  '+str(self.listaDados[self.__i][6][2])+'/'+str(self.listaDados[self.__i][6][1])+'/'+str(self.listaDados[self.__i][6][0])+' '+str(self.listaDados[self.__i][6][3])+':'+str(self.listaDados[self.__i][6][4])+':'+str(self.listaDados[self.__i][6][5])+'   '+str(self.listaDados[self.__i][2][0])+'    '+str(self.listaDados[self.__i][3][0])+' X '+str(self.listaDados[self.__i][4][0])
                    elif self.__j == len(self.listaDados[self.__i][2])-1:
                        print '                                          '+str(self.listaDados[self.__i][2][self.__j])+'        '+str(self.listaDados[self.__i][3][self.__j])+' X '+str(self.listaDados[self.__i][4][self.__j])+'   '+str(self.listaDados[self.__i][5][0])
                    else:
                        print '                                          '+str(self.listaDados[self.__i][2][self.__j])+'    '+str(self.listaDados[self.__i][3][self.__j])+' X '+str(self.listaDados[self.__i][4][self.__j])
                print ''
            print 'FIM'
            return True

    def printRelatorioResumido(self):
        if self.listaDados == []:
            return False
        else:
            print 'PARA MELHOR VISUALIZAR O RELATORIO MAXIMIZE A TELA\n'
            print 'VEND:    DOC.CLIENT:  DATA:                                        TOTAL:'
            for self.__i in range(len(self.listaDados)):
                print str(self.listaDados[self.__i][0][0])+'    '+str(self.listaDados[self.__i][1][0])+'  '+str(self.listaDados[self.__i][6][2])+'/'+str(self.listaDados[self.__i][6][1])+'/'+str(self.listaDados[self.__i][6][0])+' '+str(self.listaDados[self.__i][6][3])+':'+str(self.listaDados[self.__i][6][4])+':'+str(self.listaDados[self.__i][6][5])+'   '+'                         '+str(self.listaDados[self.__i][5][0])
            print'\nFIM'
            return True
        
