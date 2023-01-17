import re
import os
from itertools import islice


def clean_text(text):
    file = []
    with open(f"corpus/text/{text}", "r") as f:
        for i in range(10):

            # text =
            print(f.readline())
            # remove punctuation
            text = re.sub(r"[^\w\s]", "", text)

            # remove commas
            text = re.sub(r"\,", "", text)
            # remove newlines
            text = re.sub(r"\n", "", text)
            # remove tabs
            text = re.sub(r"\t", "", text)
            # remove extra spaces
            text = re.sub(r"\s+", " ", text)
            # remove leading and trailing spaces
            text = text.strip()
            return text


# text = "This is an example text with punctuation, commas, newlines, and tabs.\n\n\nIt also has extra spaces.    "
# print(clean_text(text))

# with open("corpus/text/2002-21.txt", "r") as f:
#     text = f.read()
#     print(clean_text(text))


# Count number of text files in corpus/text directory
# that has a word `Press Release` in it


def get_date(text):

    """
    Write a function that a text from corpus/text directory
    and the first date it finds in the text and returns it
    as a string in the format `DD MMM YYYY` or `MM DD YYYY`
    @examples
    31 October  2022
    21 October  2022
    21 July 2022
    20 August  2022
    23 September 2021
    5 April  2019
    22 April 2016
    January 31 , 2012
    """
    # get first occurence of date
    date_format_one = re.search(r"\d{1,2} \w+ \d{4}", text)
    date_format_two = re.search(r"\w+ \d{1,2} \d{4}", text)

    if date_format_one:
        return date_format_one.group()
    if date_format_two:
        return date_format_two.group()
    return "No date found"


# for file in os.listdir("corpus/text/2011-52.txt"):
clean = clean_text("2011-52.txt")
print(clean)
# print(get_date(clean))
