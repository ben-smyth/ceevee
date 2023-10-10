from input import CVParser
from processing.extract import extract

def main():
    a = CVParser("../inputData/pdf/Grace-ResumeViking-11.pdf")
    documentString = a.convertToString()

    extraction = extract(documentString)

    print(extraction)

if __name__ == "__main__":
    main()