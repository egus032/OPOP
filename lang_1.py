

from asyncore import read
import spacy

nlp = spacy.load('en_core_web_lg')
doc = nlp(u'Hello World, this is my first step in NLP')
print([w.text for w in doc])


#лемматизация - from current form to basis form, for example downloading -> download
doc_1 = nlp(u'this product integrates both libraries for downloading and applying patches')
for token in doc_1:
    # токен(набор букв?) и его лемма
    print(token.text, token.lemma_)


doc_2 = nlp(u'I am flying in Frisco')
print([w.text for w in doc_2])

# get_pipe function sets name for rule, then to add rules against word and lemm 
nlp.get_pipe("attribute_ruler").add([[{'TEXT': 'Frisco'}]], {'LEMMA' : 'San-Francisco'})
print([w.lemma_ for w in nlp(doc_2)])

doc_3 = nlp(u'I have flown to LA. Now I am flying to Frisco.')
# проверка, был ли токену присвоен один из атрибутов VB, VBD или VBG
# под проверку попадает только flying
print([w.text for w in doc_3 if w.tag_ == 'VBG' or w.tag_ == 'VB'])
# выводит, что является Именем собственным
print([w.text for w in doc_3 if w.pos_ == 'PROPN'])

# цикл по меткам и вывод
# for token in doc_3:
#     print(token.head.text, token.dep_, token.text, token.pos_)

# sents для прохода по тексту и разрезания его
for sent in doc_3.sents:
    print([w.text for w in sent if w.dep_ == 'ROOT' or w.dep_ == 'pobj'])

for token in doc_3:
    if token.ent_type_ != 0: # этот токен проверяет, если не 0, то именованная сущность
        print(token.text, token.ent_type_) 

# Taken - токен
# Span - фраза/предложение
# Doc - текст целиком
# Doc может содержать внутри себя другие контейнеры, тогда доступ по индексам с 0

from spacy.tokens.doc import Doc #без импорта давал ошибку TypeError: Doc() takes no arguments
from spacy.vocab import Vocab
doc_4 = Doc(Vocab(), words = [u'Hi', u'there'])
print(doc_4)


doc_5 = nlp(u'I wnat a green apple')
print([w for w in doc_5[4].lefts]) # return left or right element from desired
print([w for w in doc_5[1].rights])
print([w for w in doc_5[4].children]) # search children elements from desired


g_read_file = open(r'C:\Users\User\My Family.txt').read()
g_doc = nlp(g_read_file)

# divide the text to list of sentences, where every sentence is list
for sent in g_doc.sents:
    print([sent[i] for i in range(len(sent))])

# divide the text to list of words
print([g_doc[i] for i in range(len(g_doc))])

# selecting the noun chunk, where noun is main part and get list of nouns
print([noun for noun in g_doc.noun_chunks])

# detouring in loop all nouns in text and search syntax of children elements every noun, then we get noun chunks
for token in g_doc:
    if token.pos_ == 'NOUN':
        g_chunk = ''
        for w in token.children:
            if w.pos_ == 'DET' or w.pos_ == 'ADJ':
                g_chunk = g_chunk + ' ' + w.text + ''
        g_chunk = g_chunk + ' ' + token.text
        print(g_chunk)    

# loop selects text's tokens and last function returns description for token
for token in g_doc:
    print(token.text, token.pos_, spacy.explain(token.pos_), token.tag_, spacy.explain(token.tag_)) 

# loop selects tokens equal NUM and send their to list
g_list = []
for token in g_doc:
    if token.pos_ == 'NUM':
        g_list.append(token.text)
        print(g_list)    

# change statement form to question form with loop - MANY WAYS

# function for evaluate semantics similarity between different sentence or words, or intervals
doc_6 = nlp('I want a green apple.')
print(doc_6.similarity(doc_6[2:5])) #that function is not for use with 'en_core_web_sm'

