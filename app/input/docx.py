from input.input import BaseInput

class docxInput(BaseInput):
    # def convertToString(self):
    #     # Open the docx file
    #     doc = docx.Document(self.input_path)

    #     fullText=[]

    #     for para in doc.paragraphs:
    #         fullText.append(para.text)
        
    #     return '\n'.join(fullText)
    def convertToString(self):
        return super().convertToString()