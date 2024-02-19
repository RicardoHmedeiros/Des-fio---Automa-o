from comissao import Comissao
from wrong_pay import CorrecaoDePagamentos
from cotas import TotalCotas

if __name__ == "__main__":

    #   Parte 1 do desafio
    arq_vendas = ('Arquivos/Vendas.xlsx')
    valor = Comissao(arq_vendas)
    valor.Pagar()
    
    #   Parte 1.2 do desafio
    arq_pagamentos = ('Respostas/resultados.xlsx')
    correcao = CorrecaoDePagamentos(arq_vendas,arq_pagamentos)
    correcao.ajuste()

    #   Parte 2 do desafio
    arq_cotas = ('Arquivos/Partnership.docx')
    cotas = TotalCotas(arq_cotas)
    cotas.Quantidade()

