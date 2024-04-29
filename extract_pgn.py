#file='Weak_League_041623_replaced.pgn'
#file="Banksia_Weak_League_070823a_replaced.pgn"
file='Season4_Top_combined.pgn'
#file='Banksia_Top_v3c_replaced.pgn'
#new = 'partial_older_versions.pgn'
filtered = 'filtered_versions.pgn'
extract = 'extracted_versions2.pgn'


#save_engines=[ "Stockfish_23061416_x64_bmi2", "Marvin_x86_64_avx2"]
# save_engines=["Stockfish_16_released_x64_bmi2"]
#save_engines = ["Fire_8.NN.MC.3 updated", "Velvet-v7.1.0-x86_64-avx2", "Velvet-v7.2.0-x86_64-avx2",
#              "Arasan 24.1", "Clarity_5.1.0_x86-64-v3_BMI2"]

save_engines = ['Tenax 0.95']

def handle_file(file,filtered, extract):
    found=False
    current_game = ''
    filt=open( filtered, 'w') 
    ext=open( extract, 'w') 
    i=0
    j=0
    with open(file, 'r') as f:
        print('Starting')
        for line in f:
            line=line.rstrip()
            current_game=current_game+line+'\n'
                
            if line.startswith('[White ') or line.startswith('[Black '): 
                engine = line.split('"')[1]

                if engine in save_engines:
                    found=True

            if line.endswith('1-0') or line.endswith('0-1') or line.endswith('1/2-1/2'):
                save_game = current_game.split('\n')

                if not found:
                    i += 1

                    if i%100 == 0:
                        print(f'Filtered {i} games!')
                    
                    for save_line in save_game:
                        filt.write(save_line+'\n' )
                else:
                    j += 1

                    if j%100 == 0:
                        print(f'Extracted {j} games!')

                    for save_line in save_game:
                        ext.write(save_line+'\n' )

                current_game=''
                found = False

            elif line.endswith('*'):
                current_game=''
                
    filt.close()
    ext.close()
    print(f'Saved {j} games in {extract} and {i} games in {filtered}!')
    return

handle_file(file, filtered, extract)
