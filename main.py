from nltk.corpus import stopwords


def main():
    text = 'Este é um bom livro'

    # nor_text = normalize_text(text)


if __name__ == '__main__':
    # main()

    with open('lex/oplexicon_v3.0/lexico_v3.0.txt') as file:
        lines = file.readlines()

    data = {}
    types = {}
    for line in lines:
        line = line.strip()
        parts = line.split(',')
        word = parts[1]
        type = word
        data[parts[0]] = {
            'type': type,
            'score': parts[2]
        }

        if type not in types:
            types[type] = []

        tdata = types[type]
        tdata.append(word)


