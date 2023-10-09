from input.pdf import pdfInput
from input.docx import docxInput


def _findType(file_path: str) -> str:
    with open(file_path, 'rb') as f:
        # Read the first 4 bytes of the file
        file_signature = f.read(8)

        # Check the file signature to determine the file type
        if file_signature == b'\x50\x4b\x03\x04\x14\x00\x06\x00':
            return 'docx'
        elif file_signature[0:4] == b'\x25\x50\x44\x46':
            return 'pdf'
        else:
            raise ValueError("File type not supported")
        

def CVParser(file_path: str):
    file_type = _findType(file_path)
    if file_type == 'docx':
        print("filetype: docx")
        return docxInput(file_path)
    elif file_type == 'pdf':
        print("filetype: pdf")
        return pdfInput(file_path)
    else:
        raise ValueError("File type not supported")