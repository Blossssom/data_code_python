import re

file_name = '/content/drive/My Drive/data code/'
input_file_name = str(input('file_name : '))
file_name = file_name + input_file_name

data_list = [] # 형태소 분석을 마친 full data 입니다. tuple 로 구성되어 있습니다.

with open(file_name, 'r') as sf:
  while True:
    data = sf.readline()
    if not data:
      break
    else:
      if len(data) > 4:  # 비어있는 혹은 너무 짧아 의미없는 기사를 날리기위한 구간입니다.
        data_list.append(eval(data))

dict_list = {}
for aj in data_list:
  for ka in aj:
    if ka[1] == 'VV+EC':
      dict_list[ka[0]] = ka[1]

#patt_1 = re.compile("\(.*, 'NNG'\), .*, \('인해', 'VV\+EC'\), .*, \(.*, 'JKO'\)+")
#patt_1 = re.compile("\(.*, 'NNG'\), .*, \('따라', 'VV\+EC'\), .*, \(.*, 'JKO'\)+")
#patt_1 = re.compile("\(.*, 'NNG'\), .*, \('의해', 'VV\+EC'\), .*, \(.*, 'JKO'\)+")
#patt_1 = re.compile("\(.*, 'NNG'\), .*, \('일으켜', 'VV\+EC'\), .*, \(.*, 'JKO'\)+")
#patt_1 = re.compile("\(.*, 'NNG'\), .*, \('의해서', 'VV\+EC'\), .*, \(.*, 'JKO'\)+")
patt_1 = re.compile("\(.*, 'NNG'\), .*, \('의하여', 'VV\+EC'\), .*, \(.*, 'JKO'\)+")

pat_list = []
for f_data in data_list:
  find_patt = patt_1.findall(str(f_data))
  if len(find_patt) > 0:  # 패턴에 해당하지 않는 비어있는 리스트를 제외하기 위한 조건문 입니다.
      #print(find_patt)
      pat_list.append(find_patt)

tu_list = []    # 데이터를 다시 tuple 형태로 변환하고 명사(NNG)를 추출하기 전 조사(JKO)를 기준으로 범위를 정하는 구간입니다.
for k in pat_list:
  for tu_data in k:
    tu_list.append(list(eval(tu_data)))

clue_list = []
clue_fin = []
for find_a in tu_list:
  #print(find_a.index(('인해', 'VV+EC')))
  clue = find_a.index(('의하여', 'VV+EC'))
  while True:
    if find_a[clue][1] == 'JKO':
      clue_list.append(find_a[:clue+1])
      break
    clue+=1

for find_b in clue_list:
  clue2 = find_b.index(('의하여', 'VV+EC'))
  find_break = clue2 - 1
  while True:
    if find_b[find_break][1] == 'NNG' and find_b[find_break - 1][1] != 'NNG':
    #if find_b[find_break][1] == 'NNP' and find_b[find_break - 1][1] != 'NNP':
      print(find_b[find_break-1:])
      #print(find_b.index(find_b[find_break]))
      clue_fin.append(find_b[find_break:])
      break
    find_break -= 1

fin_list = []
for fin_data in clue_fin:
  te_list = []
  for clear_n in fin_data:
    if clear_n[1] == 'NNG' or clear_n[1] == 'VV+EC':
    #if clear_n[1] == 'NNP' or clear_n[1] == 'VV+EC':
      te_list.append(clear_n)
  fin_list.append(te_list)


with open('/content/drive/My Drive/data code/dust_pattern.csv', 'a') as pf:
  for k in fin_list:
    pf.write(str(k) + '\n')