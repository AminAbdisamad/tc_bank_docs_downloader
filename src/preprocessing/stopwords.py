from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import nltk


# import word_tokenize from nltk library


# having a corpus text wrie a function that removes
# stop words using nltk library

# Path: src/preprocessing/stopwords.py
def remove_stop_words(text):
    text = text.lower()
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    return " ".join(filtered_sentence)


# lematize text using nltk library
# Path: src/preprocessing/stopwords.py


import nltk
from nltk import word_tokenize

text = "This is one simple example."


def lematize_text(text):
    tokens = word_tokenize(text)
    tags = nltk.pos_tag(tokens, tagset="universal")
    lemmatizer = WordNetLemmatizer()
    words = []
    for tag in tags:
        if tag[1] == "NOUN":
            words.append(lemmatizer.lemmatize(tag[0], pos="n"))
        elif tag[1] == "VERB":
            words.append(lemmatizer.lemmatize(tag[0], pos="v"))
        elif tag[1] == "ADJ":
            words.append(lemmatizer.lemmatize(tag[0], pos="a"))
        elif tag[1] == "ADV":
            words.append(lemmatizer.lemmatize(tag[0], pos="r"))
        else:
            words.append(lemmatizer.lemmatize(tag[0]))
    return " ".join(words)

    # print("token", tokens)
    # print("tags", tags)

    # words = []
    # for word in text.split():
    #     w = lemmatizer.lemmatize(word)
    #     print(w)
    # return " ".join(words)
    # print("rocks :", lemmatizer.lemmatize("rocks"))
    # print("corpora :", lemmatizer.lemmatize("corpora"))
    # print("better :", lemmatizer.lemmatize("better", pos="a"))


sentence = """ 
reinforcement in macroeconomic foundations must be sustained 
for this reason draft laws currently pending including those 
about social security financial institutions and revenue
 administration are highly significant recently a lot of 
 attention has been focused on the question regarding to 
 what extent the exchange rate movements can affect inflation 
 it has been occasionally emphasized in previous reports 
 that the relationship between exchange rate developments 
 and inflation has weakened undoubtedly the exchange rate 
 will continue to be an important determinant of inflation
in  a country on the path to becoming an increasingly
open economy however there is a crucial point about 
exchange rateinflation


"""
lemmatizer = WordNetLemmatizer()
print("undoubtedly ", lemmatizer.lemmatize("undoubtedly", "a"))
print("increasingly ", lemmatizer.lemmatize("increasingly", "a"))

text = remove_stop_words(sentence)
# print("Stop words removed", text)
# print("Lemmatized", lematize_text(text))
