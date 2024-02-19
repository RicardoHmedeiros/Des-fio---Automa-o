from docx import Document
import re
import pandas as pd

class TotalCotas:
    def __init__(self, Documento):
        self.document = Document(Documento)    
        self.cotas_total = []

    def Quantidade(self):
        #   Uso o import re para encontrar um padrão para achar os socios e suas cotas da empresa
        #   Onde as partes procuradas estão entre () no caso um de uma sequencia de caracteres (.*?) e outra uma de digitos (\d+)
        pattern = r"\d+\.\s+(.*?),.*?CPF\s+\d{3}\.\d{3}\.\d{3}-\d{2}.*?detentor[ao]* de (\d+) cotas"

        for linha in self.document.paragraphs:    #   Recebe uma linha do documento
            socio_cotas = re.search(pattern, linha.text)    # Testa se o padrão procurado está na linha atual
            if socio_cotas:     #   Se a linha bater com o padrão estabelecido
                nome_socio = socio_cotas.group(1)   #   Recebe o valor do socio de (.*?)
                numero_cotas = int(socio_cotas.group(2))    #   Recebe o valor das cotas de (\d+)
                self.cotas_total.append({'Nomes dos Socios': nome_socio, 'Cotas': numero_cotas})    # Adiciona o nome e cotas as respostas


        #   Trasforma a lista de respotas em um dataFrame e salva em um arquivo .xlsx
        exit_table = pd.DataFrame(self.cotas_total)
        exit_table.to_excel('Respostas/Cotas_totais.xlsx', index=False)

