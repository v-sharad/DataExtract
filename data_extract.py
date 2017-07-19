from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

output = StringIO()
manager = PDFResourceManager()
converter = TextConverter(manager, output, laparams=LAParams())
interpreter = PDFPageInterpreter(manager, converter)

infile = open(r'C:\Users\venkats4\Desktop\bslf.pdf', 'rb')
pagenums = set([1])
for page in PDFPage.get_pages(infile, pagenums):
    interpreter.process_page(page)

infile.close()
converter.close()
text = output.getvalue()
output.close()


with open(r'C:\Users\venkats4\Desktop\data.txt','w') as text_file:
    text_file.write(text)