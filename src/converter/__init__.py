from converter import Converter


def prepareTextFile(pdf_file_destination, text_file_destination):
    """This function prepares data"""
    # Initialize converter object
    converter = Converter()

    if file.endswith(".pdf"):
        # PDF = Converter()
        converter.pdfToImage(pdf_file_destination)
        converter.imageToText(text_file_destination)
        converter.removeImages()
    else:
        print("Unknown Extension we only except [png,jpg,jpeg and pdf] extensions")


pdf_files = [
    "2003-2.pdf",
    "2003-4.pdf",
    "2003-8.pdf",
    "2003-11.pdf",
    "2003-15.pdf",
    "2003-21.pdf",
    "2003-27.pdf",
    "2003-30.pdf",
    "2003-36.pdf",
    "2003-39.pdf",
    "2003-48.pdf",
    "2003-55.pdf",
    "2003-60.pdf",
]

for file in pdf_files:
    prepareTextFile(f"corpus/pdf/{file}", f"corpus/text/{file[:-4]}.txt")
# prepareTextFile("corpus/pdf/2002-15.pdf", "corpus/text/2002-15.txt")
