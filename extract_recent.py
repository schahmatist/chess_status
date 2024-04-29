#file='Weak_League_041623_replaced.pgn'
#file="Banksia_Weak_League_070923b_replaced.pgn"
#file='Banksia_Top_v3c_replaced.pgn'
#file="Banksia_Weak_060923_replaced.pgn"
file='Season4 Top.pgn'
#file='older_versions.pgn'
#new = 'older_versions_temp.pgn'
#new = 'season3q_recent.pgn'
new = file.split(' ')[0]+'_extract_top20.pgn'

save_engines=[]

with open('t1', 'r') as f:
    for line in f:
        line=line.rstrip()
        save_engines.append(line)

#save_engines.extend(['Stockfish HCE 16',"Stockfish HCE 200731"]) 

def handle_file(file,new):
    found=False
    white=''
    black=''
    current_game = ''
    n=open(new, 'w') 
    num=0
    with open(file, 'r') as f:
        print('Starting')
        for line in f:
            line=line.rstrip()
            current_game=current_game+line+'\n'
                
            if line.startswith('[White '):
                white = line.split('"')[1]
            elif line.startswith('[Black '): 
                black = line.split('"')[1]

            if white in save_engines and black in save_engines:
                found=True

            if line.endswith('*'):
                white=''
                black=''
                current_game=''
                found =''
                continue

            if line.endswith('1-0') or line.endswith('0-1') or line.endswith('1/2-1/2'):
                if found:
                    num += 1

                    if num%500 == 0:
                        print(f'Found {num} games!')

                    save_game = current_game.split('\n')
                    
                    for save_line in save_game:
                        n.write(save_line+'\n' )
                current_game=''
                white=''
                black=''
                found=False
    n.close()
    print(f'Found {num} games!')
    return

handle_file(file, new)
