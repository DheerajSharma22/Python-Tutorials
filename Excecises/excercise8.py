from pypdf import PdfWriter
import os

os.chdir("D:/Python Tutorials/Excecises/pdfs")

merger = PdfWriter()

for file in os.listdir():
    if (file.endswith(".pdf")):
        merger.append(fileobj=file)
    
merger.write("Result.pdf")
merger.close()