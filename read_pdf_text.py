import PyPDF2
from variables import pdf_src
import re

page_text_dict = {}
search_regex = r"Figure \d-\d"

"""
def useRegex(input):
    pattern = re.compile(r"^[a-zA-Z]+ 2-\\d1 [a-zA-Z]+.*$")
    return pattern.match(input, re.IGNORECASE, re.MULTILINE)
"""

with open(pdf_src, "rb") as pdf_file_obj:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    for i in range(pdf_reader.numPages):
        page = pdf_reader.getPage(i)
        text = page.extractText()
        # text = re.findall(search_regex, text)
        # text_split = re.split(search_regex, text)
        text_split = text.split('\n')
        text = " ".join(text_split)
        text_split = text.split(".")
        new_text_split = []
        for split in text_split:
            new_text_split.append(f"[{split}]")
        if text is not None:
            page_text_dict[i] = new_text_split
        else:
            page_text_dict[i] = [""]
        print(page.getContents())


with open("page_text.txt", "w", encoding="utf-8") as txt_file:
    for page, text in page_text_dict.items():
        #print(str(page))
        #print(f"\t{text}")
        txt_file.writelines(text)
        txt_file.write("\n")


