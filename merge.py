import string

with open("test.at", "r") as f:
    tourn=f.readlines()

games_dic={}
for line in tourn:
    parts=line.split("=")
    pair=parts[0]
    result=parts[1]
    if pair not in games_dic.keys():
        games_dic[pair]=result
    else:
        if len(games_dic[pair]) < len(result):
            games_dic[pair]=result

for pair,result in games_dic.items():
    with open ('new.at','a') as w:
        w.write('='.join([pair,result]))


# Allie 0.5 ------ Andscacs=111+
# Allie 0.5 ------ Andscacs=111+

