import re
from konlpy.tag import Kkma
import pandas as pd
import numpy as np

asdf =[]
kkm = Kkma()
keyword = '대기오염'
cause_list = '(\D*)(인해)( %s)(\D*)|(\D*)(의해)( %s)|(\D*)(의한)( %s)|(\D*)(인한)( %s)|(\D*)(때문에)( %s)|(\D*)(부터)( %s)|(\D*)(따른)( %s)|(\D*)(따라)( %s)|(\D*)(결과)( %s)'
result = re.compile('대기오염')
ko_list = ['의해', '인해', '의한', '인한', '때문에', '로 부터', '따른', '에 따라', '의 결과']
def blossom():
    cause = re.compile(cause_list %(keyword, keyword, keyword, keyword, keyword, keyword, keyword, keyword, keyword))
    word_list = []
    num = 0
    clean_list = []
    dd_list = []
    km_list = []
    kmword_list = []
    blossom_list = []
    soa_list = []
    on_list = []
    fin_list = []
    with open('/Users/blossom/Documents/flower/ndsl"대기오염"초록문.csv') as bf:
        while True:
            data = bf.readline()
            if not data: break
            data = re.sub('"', '', data)
            data = re.sub("'", '', data)
            data = re.sub('\n', '', data)
            if keyword in data:
                for i in ko_list:
                    if i in data:
                        #print(data)
                        word_list.append(data)
    word_list = list(set(word_list))
    for k in word_list:
        clean_text = cause.match(k)
        if str(clean_text) != 'None':
            num += 1
            print(num,clean_text.string)

        #if len(clean_text) == 1:
        #    clean_list.append(clean_text)
    #print(*clean_list, sep='\n')
    '''for de in clean_list:
        for dde in de:
            temp = []
            for dd_word in dde:
                if len(dd_word) > 0:
                    temp.append(dd_word)
            dd_list.append(temp) # full list!!!'''
    #print(*dd_list, sep='\n')
    '''for ddl in dd_list:
        sol = kkm.pos(ddl[0])
        km_list.append(sol)
    print(*km_list, sep='\n')
    for kmkm in km_list:
        #print(kmkm)
        kkma = []
        try:
            for kw in range(-2, -5, -1):
                if kmkm[kw][1] == 'NNG':
                    kkma.append(kmkm[kw])
        except IndexError:
            continue
        kmword_list.append(kkma)
    #print(*kmword_list, sep='\n')
    #print(*dd_list, sep='\n')
    #print(len(kmword_list))
    #print(len(dd_list))
    for rkm in kmword_list:
        nono = []
        for rkm2 in reversed(rkm):
            nono.append(rkm2[0])
        blossom_list.append(nono)
    for soso in blossom_list:
        soso_str = ''
        for soa in soso:
            soso_str += soa + ' '
        soa_list.append(soso_str)
    for nn in range(len(soa_list)):
        nn_sol = [soa_list[nn], keyword]
        fin_list.append(nn_sol)'''
    #df = pd.DataFrame(dd_list)
    #df.to_csv('/Users/blossom/Documents/flower/제발_fin.csv', sep=',',header=False)



def blossom_rev():
    word_list = []
    clean_list = []
    dd_list = []
    km_list = []
    kmword_list = []
    the_list = []
    soa_list = []
    sso_list = []
    fin_list = []
    cc_list = []
    cause_list2 = '(%s..{0,5})(인해)(\D*)|(%s..{0,5})(의해)(\D*)|(%s..{0,5})(의한)(\D*)|(%s..{0,5})(인한)(\D*)|(%s..{0,5})(때문에)(\D*)|(%s..{0,5})(부터)(\D*)|(%s..{0,5})(따른)(\D*)|(%s..{0,5})(따라)(\D*)|(%s..{0,5})(결과)(\D*)'
    cause = re.compile(cause_list2 %(keyword, keyword, keyword, keyword, keyword, keyword, keyword, keyword, keyword))
    with open('/Users/blossom/Documents/flower/fin_test2.csv') as bf:
        for af in range(1000):
            data = bf.readline()
            if not data: break
            data = re.sub('"', '', data)
            data = re.sub("'", '', data)
            data = re.sub('\n', '', data)
            data = re.sub(',', '', data)
            if keyword in data:
                for i in ko_list:
                    if i in data:
                        #print(data)
                        word_list.append(data)
    word_list = list(set(word_list))
    for k in word_list:
        clean_text = cause.findall(k)
        if len(clean_text) == 1:
            clean_list.append(clean_text)
    #print(*clean_list, sep='\n')
    for de in clean_list:
        for dde in de:
            temp = []
            for dd_word in dde:
                if len(dd_word) > 0:
                    temp.append(dd_word)
            dd_list.append(temp) # full list!!!
    for clear in dd_list:
        if len(clear[2]) > 1:
            cc_list.append(clear)
    #print(*dd_list, sep='\n')
    '''for ddl in cc_list:
        sol = kkm.pos(ddl[2])
    #    print(sol)
        km_list.append(sol)
    #print(*km_list, sep='\n')
    for kmkm in km_list:
        ttemp = []
        check = False
        for lkm in kmkm:
            if lkm[1] != 'NNG':
                break
            else:
                ttemp.append(lkm)
        kmword_list.append(ttemp)
    for ww in kmword_list:
        #print(ww, len(ww))
        if len(ww) >= 1:
            the_list.append(ww)
    #print(*the_list, sep='\n')
    for rkm in the_list:
        nono = []
        for ono in rkm:
            nono.append(ono[0])
        soa_list.append(nono)
    for soso in soa_list:
        soso_str = ''
        for soa in soso:
            soso_str += soa + ' '
        sso_list.append(soso_str)
    for nn in range(len(sso_list)):
        nn_sol = [keyword,sso_list[nn]]
        fin_list.append(nn_sol)
    print(*fin_list, sep='\n')'''
    df = pd.DataFrame(np.array(cc_list))
    df.to_csv('/Users/blossom/Documents/flower/sla_fin.csv', sep=',', line_terminator='\n', header=False)
    #print(*fin_list, sep='\n')


blossom()
#blossom_rev()