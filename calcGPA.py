import PyPDF2 as pdf
def main():
    print("-------------")
    print("Simple GPA Calculator")
    print("Input : Credit Hours : 12.5 OR 25")
    print("Input : Mark : 0 - 100")
    print("-------------")
    fileName = input("Enter the name of the file (make sure its in the same directory as this program\n")
    pdfFileObj = open(fileName, "rb")
    pdfRead = pdf.PdfFileReader(pdfFileObj)
    numpages = pdfRead.numPages
    allText = ""
    for ii in range(numpages):
        pageObj = pdfRead.getPage(ii)
        allText += (pageObj.extractText())


    #marks
    
    allText = allText.replace("25.0", " 25.0 ")
    allText = allText.replace("15.5", " 15.5 ")
    allText = allText.replace("Semester", " Semester ")
    allText = allText.replace("\n", " ENDOFLINE ")
    allText = allText.split(" ")

    indexOfMarks = allText.index("Semester")
    allText = allText[indexOfMarks:]

    #print(allText)
    totalProduct = 0.0
    totalCreditHours = 0.0
    for ii in range(len(allText)):
        if allText[ii] == "25.0" :
            mark = int(allText[ii+1][1:3])

            totalCreditHours += 25.0
            totalProduct += (25.0 * calcVal(mark))

        elif allText[ii] == "12.5":
            mark = int(allText[ii+1][1:3])

            totalCreditHours += 12.5
            totalProduct += (12.5 * calcVal(mark))

    print("GPA: " + str(totalProduct/totalCreditHours))

def calcVal(mark):
    if 100.0 >= mark >= 80.0:
        qualityPoint = 4.0
    elif 79.0 >= mark >= 70.0:
        qualityPoint = 3.67
    elif mark <= 69 and mark >= 60:
        qualityPoint = 3.00
    elif mark <= 50 and mark >= 59:
        qualityPoint = 2.33
    elif mark <= 45 and mark >= 49:
        qualityPoint = 1.67
    elif mark <= 30 and mark >= 44:
        qualityPoint = 1.33
    else:
        qualityPoint = 0.0

    return qualityPoint
if __name__ == "__main__":
    main()

