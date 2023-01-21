import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# example text text = 'What can I say about this place. The staff of these restaurants is nice and the eggplant is not bad'


class Splitter(object):
    """
    split the document into sentences and tokenize each sentence
    """

    def __init__(self):
        self.splitter = nltk.data.load("tokenizers/punkt/english.pickle")
        self.tokenizer = nltk.tokenize.TreebankWordTokenizer()

    def split(self, text):
        """
        out : ['What', 'can', 'I', 'say', 'about', 'this', 'place', '.']
        """
        # split into single sentence
        sentences = self.tokenizer.tokenize(text)
        # tokenization in each sentences
        tokens = [self.tokenizer.tokenize(sent) for sent in sentences]
        return tokens


class LemmatizationWithPOSTagger(object):
    def __init__(self):
        pass

    def get_wordnet_pos(self, treebank_tag):
        """
        return WORDNET POS compliance to WORDENT lemmatization (a,n,r,v)
        """
        if treebank_tag.startswith("J"):
            return wordnet.ADJ
        elif treebank_tag.startswith("V"):
            return wordnet.VERB
        elif treebank_tag.startswith("N"):
            return wordnet.NOUN
        elif treebank_tag.startswith("R"):
            return wordnet.ADV
        else:
            # As default pos in lemmatization is Noun
            return wordnet.NOUN

    def pos_tag(self, tokens):
        # find the pos tagginf for each tokens [('What', 'WP'), ('can', 'MD'), ('I', 'PRP') ....
        pos_tokens = [nltk.pos_tag(token) for token in tokens]

        # lemmatization using pos tagg
        # convert into feature set of [('What', 'What', ['WP']), ('can', 'can', ['MD']), ... ie [original WORD, Lemmatized word, POS tag]
        pos_tokens = [
            [
                (
                    word,
                    lemmatizer.lemmatize(word, self.get_wordnet_pos(pos_tag)),
                    [pos_tag],
                )
                for (word, pos_tag) in pos
            ]
            for pos in pos_tokens
        ]
        return pos_tokens


text = """ Hello Mr. Smith, how are you doing today?
The weather is great, and Python is awesome.
The sky is pinkish-blue. You should not eat cardboard. 
which is mainly used for the purpose of removing the
unwanted words from the text. """

lemmatizer = WordNetLemmatizer()
splitter = Splitter()
lemmatization_using_pos_tagger = LemmatizationWithPOSTagger()

# step 1 split document into sentence followed by tokenization
tokens = splitter.split(text)
# print(tokens)

# step 2 lemmatization using pos tagger
lemma_pos_token = lemmatization_using_pos_tagger.pos_tag(tokens)
get_wordnet_pos = lemmatization_using_pos_tagger.get_wordnet_pos("VBZ")
print(lemma_pos_token)
