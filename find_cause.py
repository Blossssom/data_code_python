from konlpy.tag import Twitter, Kkma, Mecab
import pandas as pd
import re
word_km = Kkma()
word_mecab = Mecab()
word_twitter = Twitter()
condition = ['면', '거든', '던들', '진대']
purpose = ['러', '려고', '고자']
causation = ['아서', '니까', '므로', '느라고']

word_head = ['date', 'title', 'newsID', 'organization', 'provider_code', 'provider', 'content', 'seedcontent']
word_list = []
tw_list = []
mecab_list = []
nlp_list = []
me_nlplist = []
tw_nlplist = []
kkma_text = open('/Users/blossom/kkma_text.csv', 'w')
mecab_text = open('/User/blossom/mecab_text.csv', 'w')
twitter_text = open('User/blossom/twitter_text.csv', 'w')
with open('/Users/blossom/fin_test.csv') as f:
    for i in range(100):
        data = f.readline()
        sol = re.sub('"', '', data)
        sol = re.sub('[-=.#/?:$}]', '', sol)
        print(sol)
        word_list.append(sol)
        if not sol:
            break
with open('/User/blossom/fin_test.csv') as f_me:
    for j in range(100):
        me_data = f.readline()
        sol1 = re.sub('"', '', data)
        sol1 = re.sub('[-=.#/?:$}]', '', sol)
        print(sol1)
        mecab_list.append(sol1)
        if not sol1:
            break

with open('/User/blossom/fin_test.csv') as f_tw:
    for j in range(100):
        tw_data = f_tw.readline()
        sol2 = re.sub('"', '', data)
        sol2 = re.sub('[-=.#/?:$}]', '', sol)
        print(sol2)
        tw_list.append(sol2)
        if not sol2:
            break

for word in word_list:
    text_w = word_km.pos(word)
    kkma_text.write(str(text_w) + '\n')
    nlp_list.append(text_w)
#print(nlp_list)

for me_word in mecab_list:
    text_me = word_mecab.pos(me_word)
    mecab_text.write(str(text_me) + '\n')
    mecab_list.append(text_me)

for tw_word in tw_list:
    text_tw = word_twitter.pos(tw_word)
    twitter_text.write(str(text_tw) + '\n')
    tw_list.append(text_tw)


f_me.close()
f_tw.close()
f.close()

kkma_text.close()
twitter_text.close()
mecab_text.close()