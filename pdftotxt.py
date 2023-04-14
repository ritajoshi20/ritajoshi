import PyPDF2

# Load the PDF file
pdf_file = open('Resume.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
text = ''
#print(len(pdf_reader.pages))
for page in range(len(pdf_reader.pages)):
    text += pdf_reader.pages[page].extract_text()

pdf_file.close()

text_file = open('Resume.txt', 'w', encoding='utf-8')
text_file.write(text)
text_file.close()