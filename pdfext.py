import PyPDF2
import os


def print_lines_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(pdf_path)
            #PyPDF2.PdfFileReader(file)
        pageind = 0

        pgno = len(pdf_reader.pages)
            #pdf_reader.getNumPages()
        for i in range(0,pgno):
            PgOb = pdf_reader.pages[pageind]
                #pdf_reader.getPage(i)
            Text = PgOb.extract_text()
            pageind = pageind + 1
                #extractText()
            print(Text)
            print('------------------')

pdfDir = 'D:\\Newfolder\\CV\\Freelance\\UpWork'
    #'D:\\Newfolder\\Freelancing\\Upwork\\testExtText\\pdfs'

pdf_file_path = 'D:\\Newfolder\\CV\\Freelance\\UpWork\\List-of-participants-Dec-20-2023.pdf'
print_lines_from_pdf(pdf_file_path)

