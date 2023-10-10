from input import CVParser
from processing import extract as extract


def main():
    a = CVParser("../inputData/pdf/Amsterdam-Modern-Resume-Template.pdf")
    documentString = a.convertToString()

    print(documentString)

    print("\n---\n")

    print(extract(documentString))


if __name__ == "__main__":
    main()