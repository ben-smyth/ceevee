from input import CVParser


def main():
    a = CVParser("../inputData/docx/coolfreecv_resume_en_06_n.docx")
    string = a.convertToString()

    print(string) 


if __name__ == "__main__":
    main()
