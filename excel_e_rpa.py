import xlsxwriter
import os

#cria um arquivo .xlsx no caminho indicado e o nome expecificado
nomeCaminhoArquivo = "E:\\testando.xlsx"
planilhaCriada = xlsxwriter.Workbook(nomeCaminhoArquivo)
sheet1 = planilhaCriada.add_worksheet()

#cria a planilha e popula
sheet1.write("A1", "Nome")
sheet1.write("A2", "Alice")
sheet1.write("B1", "Idade")
sheet1.write("B2", "25")
sheet1.write("C1", "Sexo")
sheet1.write("C2", "Feminino")


planilhaCriada.close()


#abre o arquivo criado, no caso, "testando.xlsx"
os.startfile(nomeCaminhoArquivo)
