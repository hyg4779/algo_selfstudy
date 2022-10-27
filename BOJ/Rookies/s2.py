import spacy
from spacy.lang.en.examples import sentences


nlp = spacy.load("en_core_web_sm")

# def anonymize_text(setences):
#     result = []
#     for doc in sentences:
#
#         text = nlp(doc)
#         print(text)
#
#         line = []
#         for token in text:
#             word = token.text
#             # print(token.text, token.pos_, token.pos)
#             # token.pos 96 == 주어
#             if token.pos == 96 or token.pos == 95:
#                 word = 'X'*len(word)
#
#             line.append(word)
#
#         result.append(' '.join(line))
#         print()
#     return result
#
# result = anonymize_text(sentences)
# for res in result:
#     print(res)



def anonymize_text(setences):
    result = []


    text = nlp(setences)


    line = []
    for token in text:
        word = token.text
        # print(token.text, token.pos_, token.pos)
        # token.pos 96 == 주어
        if token.pos == 96 or token.pos == 95:
            word = 'X'*len(word)

        line.append(word)

    result.append(' '.join(line))

    return ' '.join(result)

res = anonymize_text('john is old')
print(res)
'''
sentences[0]

Apple PROPN nsubj
is AUX aux
looking VERB ROOT
at ADP prep
buying VERB pcomp
U.K. PROPN dobj
startup NOUN dobj
for ADP prep
$ SYM quantmod
1 NUM compound
billion NUM pobj
'''

