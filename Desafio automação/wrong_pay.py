import pandas as pd

class CorrecaoDePagamentos:
    def __init__(self,past_pay ,real_pay):
        self.tabela_past = pd.read_excel(past_pay, sheet_name='Pagamentos') #   Leitura dos arquivos
        self.tabela_real = pd.read_excel(real_pay)
        self.correct_pay = []       #  Lista para adicionar as respotas

    
    def ajuste(self):
        for _,past_table in self.tabela_past.iterrows():    #   Intera sobre a tabela com os valores errados
            for _,new_table in self.tabela_real.iterrows(): #   Intera sobre a tabela com os valores corretos
                #   Acha os vendedores para comparar em cada tabela
                if new_table['Nome do Vendedor'] == past_table['Nome do Vendedor']:
                    if new_table['Comissão'] != past_table['Comissão']: #   Testa se os valores de comissão estão diferentes
                        #   Se sim adiciona na lista do pagamento correto o nome, valor errado e o certo
                        self.correct_pay.append({'Nome do Vendedor': new_table['Nome do Vendedor'],
                        'Valor Errado': past_table['Comissão'], 'Valor Certo': new_table['Comissão']})

        #   Trasforma a lista de respotas em um dataFrame e salva em um arquivo .xlsx
        exit_table = pd.DataFrame(self.correct_pay)
        exit_table.to_excel('Respostas/pagamentos_corretos.xlsx', index=False)

