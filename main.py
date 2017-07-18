#from nltk.corpus import stopwords
import codecs
from functools import partial

lex = {}
stopwords = []

def load_lex():
    with codecs.open('lex/oplexicon_v3.0/lexico_v3.0.txt', encoding='utf8') as file:
        lines = file.readlines()

    global lex
    for line in lines:
        line = line.strip()
        parts = line.split(',')
        type = parts[1]
        lex[parts[0]] = {
            'type': type,
            'score': parts[2]
        }


def load_stopwords():
    with codecs.open('lex/stopwords.txt', encoding='utf8') as file:
        lines = file.readlines()

    global stopwords
    for line in lines:
        word = line.strip()
        stopwords.append(word)


def normalize_text(text):
    text = text.lower()

    return text


def ngram(text, n):
    parts = text.split(' ')
    grams = []
    for i in range(0, len(parts)):
        gram = []
        for j in range(0, n):
            if i+j >= len(parts):
                continue
            gram.append(parts[i+j])
        if len(gram) < n:
            break
        grams.append(' '.join(gram))

    return grams


def main():
    load_lex()
    load_stopwords()

    original_text = 'Este é um bom livro'

    text = normalize_text(original_text)
    #uni_text = unigram(text)
    grams = ngram(text, 1)
    #for g in grams:


if __name__ == '__main__':
    main()
