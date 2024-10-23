from PyPDF2 import PdfReader

with open("list.txt", "r") as file:
    lines = [line.rstrip() for line in file]

for path in lines :
    reader = PdfReader("allpdfs/"+path)
    totalPages = len(reader.pages)
    text_file = open("alltxts/"+path[:-3]+"txt", "w", encoding="utf-8")

    for page in reader.pages[2:-1] :
        extracted_text = page.extract_text().strip()
        extracted_text = extracted_text[:-6]
        for i in range(10) :
            extracted_text = extracted_text.replace("  ", " ")
        extracted_text = extracted_text.replace("\n \n", "\n")
        extracted_text = extracted_text.replace("\n \n", "\n")
        extracted_text = extracted_text.replace("", "-")
        extracted_text = extracted_text.replace("", "∙")
        extracted_text = extracted_text.replace("￭", "∙")
        text_file.write(extracted_text)
        
    print (path+" completed")
    text_file.close()
