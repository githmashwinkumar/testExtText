import PyPDF2
import os


pdfDir = 'D:\\Newfolder\\Freelancing\\Upwork\\testExtText\\pdfs'
for filename in os.listdir(pdfDir):
    if filename.endswith('.pdf'):
        with open(os.path.join(pdfDir, filename)) as f:
            print('--- filename --- ' + filename)
            pdfReader = PyPDF2.PdfReader(pdfDir + '\\' + filename)
            numPages = len(pdfReader.pages)
            page = pdfReader.pages[0]
            text = page.extract_text()
            print("Number of Pages:", numPages)
            print("Text:\n"+text)
            print("***************************************************************************")

#text = extract_text('D:\\Newfolder\\CV\\AshwinKumarHM.pdf')

#pattern = re.compile(r"[a-zA-Z]+,{1}\s{1}")
#matches = pattern.findall(text)
#print(matches)

#stringoftext = text.split(' ')
#print(stringoftext)
