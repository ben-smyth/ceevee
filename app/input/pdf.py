import PyPDF2
from input.input import BaseInput

class pdfInput(BaseInput):
    def convertToString(self):
        with open(self.input_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''

            # Loop through each page of the PDF
            for page in range(len(reader.pages)):
                page_text = reader.pages[page].extract_text()
                text += page_text

        return text
        