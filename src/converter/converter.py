from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os
import re


path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Images/")


class Converter:

    image_counter = 1
    # The init method opens the text file so we don't need seperate open log method
    def ocr_pdf_to_text(self, pdf_file_destination, text_file_destination):
        """This function prepares data"""
        if pdf_file_destination.endswith(".pdf"):
            self.pdfToImage(pdf_file_destination)
            self.imageToText(text_file_destination)
            self.removeImages()

        else:
            print("Unknown Extension we only except [png,jpg,jpeg and pdf] extensions")

    def pdfToImage(self, pathToPDF):
        """This Methods Converts PDF to images"""

        print("Converting PDF to images..")
        # Store all the pages of the PDF in a variable
        pages = convert_from_path(pathToPDF, 500)

        for page in pages:
            # Declaring filename for each page of PDF as JPG
            # For each page, filename will be: PDF page 1 -> page_1.jpg  # PDF page n -> page_n.jpg
            filename = f"page_{str(self.image_counter)}.jpg"
            # Save the image of the page in system
            page.save(path + filename, "JPEG")
            # Increment the counter to update filename
            self.image_counter = self.image_counter + 1
        print("Done")

    def imageToText(self, file, optionalImage=None):
        """
        Recognizing text from the images using OCR
        """
        print("Recognizing text from the images using OCR...")
        # Variable to get count of total number of pages
        filelimit = self.image_counter
        # Creating a text file to write the output
        # outfile = "Data/newfile.txt"
        # outfile = f'{file}.txt'
        # Open the file in append mode so that
        # All contents of all images are added to the same file
        f = open(file, "a")

        # Run this if there's image
        if optionalImage != None:
            image = optionalImage
            # Recognize the text as string in image using pytesserct and display original Turkish Language
            text = str(((pytesseract.image_to_string(Image.open(image), lang="tur"))))

            text = text.replace("-\n", "")

            # Finally, write the processed text to the file.
            f.write(text)

        # Iterate from 1 to total number of pages
        for i in range(1, filelimit):
            # filename = os.path.join(os.path.dirname(
            #     os.path.realpath(__file__)), "Images/page_"+str(i)+".jpg")
            # filename = "Images/page_"+str(i)+".jpg"
            filename = f"{path}page_{str(i)}.jpg"
            print(filename)
            # Recognize the text as string in image using pytesserct and display original Turkish Language
            text = str(
                ((pytesseract.image_to_string(Image.open(filename), lang="tur")))
            )

            text = text.replace("-\n", "")

            # text = re.sub(r'\s{2,}', '\n', text)
            # Finally, write the processed text to the file.
            f.write(text)

        f.close()
        print("Done")

    def removeImages(self):
        print("Removing Images From Images Directory")
        # Variable to get count of total number of pages
        filelimit = self.image_counter
        for i in range(1, filelimit):
            # filename = "Images/page_"+str(i)+".jpg"
            filename = f"{path}page_{str(i)}.jpg"
            os.remove(filename)
        print("Done")
