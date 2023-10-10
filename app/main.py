from input import CVParser
from processing import extract as extract
import processing.spacy.spacy as spacy

def main():
    a = CVParser("../inputData/pdf/Amsterdam-Modern-Resume-Template.pdf")
    documentString = a.convertToString()

    extraction = extract.extract(documentString)

    print(extraction)

if __name__ == "__main__":
    main()