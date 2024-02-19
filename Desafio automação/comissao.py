import pandas as pd

class Comissao:
    def __init__(self, table):
        self.table = pd.read_excel(table)    # Leitura do arquivo recebido
        self.results = []    # Lista para colocar os resultados de comissão


    def Pagar(self):
        #   Intera sobre o arquivo e recebe os valores de nome, valor, canal de vendas
        for _, line in self.table.iterrows():
            vendedor = line['Nome do Vendedor']
            venda = self.__convert_to_float(line['Valor da Venda']) #   Converte os valores da planinha pra float
            tipo = line['Canal de Venda']
            self.__addPlaninha(vendedor,venda,tipo)     # Usa o método para adicionar esse valor a resultados

        self.__valor_gerente()      #   Se necessario retira a parte do gerente
        self.__gerar_planinha()     #   Gera a planinha
  


    def __addPlaninha(self,vendedor,venda,tipo):
        valor = venda * 0.10        #   Recebe os 10% de comissão do valor vendido
        if tipo == 'Online':        #   Subtrai mas 20% dos 10% caso seja online a venda
            total = valor * 0.80
        else:
            total = valor       #   Caso contrario só recebe o valor sem o decrecimo 

        #   Se o vendedor já foi adicionado na lista de resposta só incrementa os valores de venda
        if (self.__is_in(vendedor)):
            for line in self.results:
                if line['Nome do Vendedor'] == vendedor:
                    line['Comissão Total'] += valor
                    line['Comissão'] += total
        #    Caso contrario adiciona o vendedor e as vendas
        else:       
            self.results.append({'Nome do Vendedor': vendedor, 'Comissão Total': valor, 'Comissão': total})

    #   Função para definir se o vendedor já está na lista
    def __is_in(self, nome):
        #   Se em self.results tiver alguem com o mesmo nome recebido retorna verdadeiro
        return any(result['Nome do Vendedor'] == nome for result in self.results) 
    
    #   Converte os valores da tabela original para float
    def __convert_to_float(self, string_value):
            n_float = string_value.replace('R$', '').replace(',', '') # Troca os valores R$ e as virgulas por espaços vazios
            return float(n_float)

    #   Faz a retirada de 10% caso o valor da comissão total passe de 1500
    def __valor_gerente(self):
        for line in self.results:
            if line['Comissão'] >= 1500:
                line['Comissão'] *= 0.90

    #   Gera a planinha das respostas do self.results
    def __gerar_planinha(self):
        #   Intera sobre a lista de respostas e adiciona o R$ e .00 no final dos números para colocar na tabela final de respotas
        for result in self.results:
            result['Comissão Total'] = f'R$ {result["Comissão Total"]:.2f}'
            result['Comissão'] = f'R$ {result["Comissão"]:.2f}'

        #   Trasforma a lista de respotas em um dataFrame e salva em um arquivo .xlsx
        exit_table = pd.DataFrame(self.results)
        exit_table.to_excel('Respostas/resultados.xlsx', index=False)

    



        

        

            
