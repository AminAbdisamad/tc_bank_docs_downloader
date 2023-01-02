import os, re
from pprint import pprint

# Get date example (03 January 2002) from the text files in the corpus folder
# and save it in a dictionary with context as value and date as key
def get_date_from_text_files():
    """Get date example (03 January 2002 ) from the text files in the corpus folder and save it in a dictionary with context as value and date as key."""
    dates = {}
    for file in os.listdir("./corpus/text"):
        if file.endswith(".txt"):
            with open(f"./corpus/text/{file}", "r") as text_file:
                text = text_file.read()
                date = re.search(r"\d{2} \w+ \d{4}", text)
                if date:
                    dates[date.group()] = text
    return dates


dates = get_date_from_text_files()
pprint(dates)
