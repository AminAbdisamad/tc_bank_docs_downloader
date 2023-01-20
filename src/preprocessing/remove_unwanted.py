# Path: src/preprocessing/main.py
import re

un_wanted_words = [
    "abdullah",
    "day",
    "dq\003",
    "dqg\003",
    "dqn\003",
    "dqqxdo\003",
    "duh\003",
    "dv\003",
    "dw\003",
    "eh\003",
    "ehhq\003",
    "even",
    "five",
    "ghpdqg\003",
    "ghyhorsphqwv\003",
    "half",
    "hfkdqjh\003",
    "hfoxglqj\003",
    "hfrqrplf\003",
    "iii",
    "irrg\003",
    "iru\003",
    "iurp\003",
    "istanbul",
    "kdv\003",
    "kdyh\003",
    "kh\003",
    "lqfuhdvh\003",
    "lqfuhdvhv\003",
    "lqiodwlrq\003",
    "lqwhuhvw\003",
    "lv\003",
    "lw\003",
    "mehmet",
    "one",
    "four",
    "six",
    "three",
    "two",
    "seven",
    "oneweek",
    "pdqxidfwxulqj\003",
    "qrw\003",
    "revhuyhg\003",
    "ri\003",
    "rq\003",
    "rwkhu\003",
    "shufhqw\003",
    "shufhqw\021\003",
    "sulfh\003",
    "sulfhv\003",
    "sxeolf\003",
    "third",
    "fourth",
    "udwh\003",
    "udwhv\003",
    "ulus",
    "ulvh\003",
    "vhfwru\003",
    "wkdw\003",
    "wkh\003",
    "wkhvh\003",
    "wklv\003",
    "work",
    "wpi",
    "wr\003",
    "wuhqg\003",
    "wwwtcmbgovtr",
    "yavaş",
    "yazar",
    "year",
    "yearend",
    "yearonyear",
    "yörükoğlu",
    "ytl",
    "yücel",
    "zdv\003",
    "zklfk\003",
    "zloo\003",
    "zlwk\003",
    "zrxog\003",
    "thursday",
    "çetinkaya",
    "caddesi",
]


# print(un_wanted_words)


# contact for further information please contact press secretary tel no
# contact for further information please send an e mail to    türkiye cumhuriyet merkez bankası central bank of the republic of
# contact for further information please send an e mail to    türkiye cumhuriyet merkez bankası central bank of the republic of türkiye head office hacı bayram mahallesi istiklal caddesi ulus altındağ ankara

# Remove more than 2 spaces in a row
# Path: src/preprocessing/remove_unwanted.py
# Path: src/preprocessing/main.py


def remove_more_than_two_spaces(text):
    return re.sub(r"\s{2,}", " ", text)


remove_more_than_two_spaces(
    "contact for further information please send an e mail to    türkiye cumhuriyet merkez bankası central bank of the republic of türkiye head office hacı bayram mahallesi istiklal caddesi ulus altındağ ankara"
)

# remove anything that starts with a word until you reach another word
# Path: src/preprocessing/remove_unwanted.py
# Path: src/preprocessing/main.py
text = """
inflation outlook displays a significant improvement please click to access governor 
çetinkayas presentation in tur kish contact for further information you may send an 
email to     türkiye cumhuriyet merkez bankası central bank of the republic of turkey 
idare merkezi head office hacı bayram mahallesi istiklal caddesi ulus altındağ ankara   
briefing on inflation report i will be given on january in ankara january no the 
central bank of the republic of turkey cbrt will 

"""


def remove_until_next_word(start_word: str, end_word: str, text: str):
    return re.sub(rf"{start_word}.*?{end_word}", "", text)


sentence = remove_until_next_word(
    "contact",
    "please",
)

print(sentence)
