from konlpy.tag import Kkma, Twitter
import pandas as pd
import re
import gensim
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

kkm = Kkma()
twitter = Twitter()
word_list = []
nlp_list = []
w2v_data = []
noun_list = []
######################
num_features = 300
min_word_count = 10
num_works = 2
context = 5
downsampling = 1e-3
dust_list = []

def dust():
    with open('/Users/blossom/Downloads/ndsl미세먼지초록.csv') as duf:
        while True:
            data = duf.readline()
            if not data: break
            sol = re.sub('"', '', data)
            #sol = re.sub('[-=.#/?:$}]', '', sol)
            if len(sol) > 5:
                print(data)
                dust_list.append(sol)

def dic_word():
    with open('/Users/blossom/Downloads/dicword_file.csv') as dif:
        while True:
            data = dif.readline()
            if not data:
                break
            data = re.sub(',', '', data)
            nlp_list.append(data)
        dif.close()
def read_csv():
    with open('/Users/blossom/Documents/fin_test.csv') as f:
        while True:
            data = f.readline()
            if not data:
                print('브레잌!!!')
                break
            sol = re.sub('"', '', data)
            sol = re.sub('[-=.#/?:$}]', '', sol)
            word_list.append(sol)
            #print(len(word_list))
        print(*word_list, sep='\n')
        f.close()
def nlp_word(word_list):
    for word in word_list:
        text = twitter.pos(word)
        noun_text = twitter.nouns(word)
       # print(text)
        n_token = []
        noun_token = []
        for token in text:
            nn_token = token[0] + '/' + token[1]
            n_token.append(nn_token)
        nlp_list.append(n_token)

        #for noun in noun_text:
            #noun_to = noun[0] + '/' + noun[1]
            #noun_token.append(noun_to)
        noun_list.append(noun_text)
    print(nlp_list)
    print(noun_list)
def word_2_vec(nlplist):
    global model
    model = gensim.models.Word2Vec(nlplist, workers=num_works,
                                   size=num_features, min_count=min_word_count,
                                   window=context, sample=downsampling)
    model_name = 'feature100_context2'
    model.save(model_name)
    print(*model.most_similar("대기오염", topn=30), sep='\n')


def word_2_vec_second(nounli):
    model = gensim.models.Word2Vec(nounli,  workers=num_works,
                                   size=num_features, min_count=min_word_count,
                                   window=context, sample=downsampling)
    model.init_sims(replace=True)
    print(model)
    #print('====================== others =========================')
    #print(*model.most_similar("대기오염", topn=200), sep='\n')
    #print('====================== 미세먼지 ======================')
    #print(*model.most_similar("미세먼지", topn=30), sep='\n')
    sol = model.most_similar("대기오염")
    print(sol)
    replace_sol = str(sol).replace("'", '\n')
    for sol_word in sol:
        with open('/Users/blossom/word2_vec2.csv', 'a') as fd:
            fd.write(str(sol_word) + '\n')
            print('save!')
def noun_2_vec(nounlist):
    noun_model = gensim.models.Word2Vec(nounlist, workers=num_works,
                                        size= num_features, min_count=min_word_count,
                                        window=context, sample=downsampling)
    noun_model_name = 'noun100_context2'
    noun_model.save(noun_model_name)
    print('====================== noun =========================')
    print(*noun_model.most_similar("대기오염", topn=30), sep='\n')




def plot_word(model):
    path = '/Library/Fonts/Webdings.ttf'
    fontprop = fm.FontProperties(fname=path, size=15)
    labels = []
    tokens = []

    for word in model.wv.vocab:
        tokens.append(model[word])
        labels.append(word)
    tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=2500, random_state=23)
    new_value = tsne_model.fit_transform(tokens)

    x = []
    y = []
    for value in new_value:
        x.append(value[0])
        y.append(value[1])
    plt.figure(figsize=(8, 8))
    for i in range(len(x)):
        plt.scatter(x[i], y[i])
        plt.annotate(labels[i], xy=(x[i], y[i]), xytext=(5, 2), ha='right', va='bottom')
    plt.show()

#dust()
#dic_word()
read_csv()
#nlp_word(dust_list)
word_2_vec(nlp_list)
#noun_2_vec(noun_list)
#word_2_vec_second(word_list)
#plot_word(model)