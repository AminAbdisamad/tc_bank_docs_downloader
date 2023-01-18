import os

# import pandas as pd
import re

# specify the directory where the text files are located
corpus_dir = "corpus/text/"

# create an empty list to store the cleaned text
corpus_text = []
MESSAGE = "Türkiye Cumhuriyet Merkez Bankası Central Bank of the Republic of Turkey Head Office Hacı Bayram Mah İstiklal Cad No Ulus Altındağ Ankara"
HEADER_MESSAGE = " türkiye cumhuriyet merkez bankası central bank of the republic of turkey head office hacı bayram mah istiklal cad no ulus altındağ ankara"
# iterate through the files in the corpus directory
for file in os.listdir(corpus_dir):
    if file.endswith(".txt"):
        # read the text file
        with open(os.path.join(corpus_dir, file), "r") as f:
            text = f.read()

            # clean the text by removing punctuation, numbers, spaces, and commas
            text = re.sub(r"“", "", text)
            text = re.sub(
                r"""Detailed tables related to Balance of Payments Developments can be found at the internet address: 
    http://www.tcmb.gov.tr  under the heading: “Publications/Periodical Publications/Balance of Payments 
    Statistics""",
                "",
                text,
            )
            text = re.sub(
                r"""Contact:  For further information, please contact CBRT Press  Secretary  Yücel Yazar 
    Tel. No: 312 507 5656. """,
                "",
                text,
            )
            # Lowercase
            text = text.lower()
            text = re.sub(r"[^\w\s]", "", text)
            text = re.sub(r"\d+", "", text)
            text = re.sub(r"\s+", " ", text)
            # remove web links
            text = re.sub(r"http\S+", "", text)
            # remove email addresses
            text = re.sub(r"\S+@\S+", "", text)
            # street addresses with cadde
            text = re.sub(r"\S+cadde\S+", "", text)
            # street addresses with sokak
            text = re.sub(r"\S+sokak\S+", "", text)
            text = re.sub(
                MESSAGE,
                "",
                text,
            )
            text = re.sub(r"wwwtcmbgovtr", " ", text)
            text = re.sub(r"basintcmbgovtr", " ", text)
            text = re.sub(r"press release", " ", text)
            text = re.sub(HEADER_MESSAGE, " ", text)
            text = re.sub(r"          ", " ", text)
            # add the cleaned text to the corpus list
            corpus_text.append(text)

# join all cleaned text into a single string
corpus_text = " ".join(corpus_text)

# create a new text file and write the corpus text to it
with open("corpus/clean_corpus.txt", "w") as f:
    f.write(corpus_text)
