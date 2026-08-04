import PyPDF2
import os

#criar uma parsta de entrada
if not os.path.exists("entrada"):
    os.makedirs("entrada")

#criar uma pasta de saída
if not os.path.exists("saida"):
    os.makedirs("saida")

#criar um objeto PdfMerger para consolidar os PDFs
juntar_pdf = PyPDF2.PdfMerger()

lista_arquivos = os.listdir("entrada")
lista_arquivos.sort()




