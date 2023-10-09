from input.pdf import pdfInput


def main():
    a = pdfInput("../inputData/pdf/Amsterdam-Modern-Resume-Template-1.pdf")
    string = a.convertToString()

    print(string) 


if __name__ == "__main__":
    main()
