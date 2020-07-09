from konlpy.tag import Mecab

mc = Mecab()
the_list = []
mc_list = []
file_name = str(input('file_name : '))
with open(file_name, 'r') as f:
    while True:
        data = f.readline()
        if not data: break
        the_list.append(eval(data))

for make_mecab in the_list:
    temp = []
    for k in make_mecab:
        sol = mc.pos(k)
        mc_list.append(sol)
save_file_name = file_name + '_mecab.csv'
with open(save_file_name, 'a') as sf:
    for sv in mc_list:
        sf.write(str(sv) + '\n')