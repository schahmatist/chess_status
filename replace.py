file='Season2_League_ALL_New.pgn'
#file='Season2_League_ALL.at'
new='Season2_League_all_replaced.pgn'

lookup={
'Alexandria-3.5-x86-64-bmi2':'Alexandria 3.5',
'Allie_v0.8-dev New Net':'Allie_v0.8-dev New Net',
'Andscacsnnue01':'Andscacs nnue 0.1',
'Arasanx-23.4-64-avx2':'Arasan 23.4',
'AsmFishWCP_2019-10-16_bmi2':'asmFishWCP_2019-10-16_bmi2',
'Berserk-11-x64-avx2-pext':'Berserk 11.1',
'BlackCore-bmi2-win-6.0':'Black Marlin 7.0',
'Blackmarlin-7.0-avx2':'BlackCore v6.0',
'Booot7_avx2_pext':'Booot 7.1_AVX2_PEXT',
'Caissa_1.7_AVX2_BMI2':'Caissa 1.7',
'Clover.3.3-avx2':'Clover 3.3.1',
'Coiled_1.1_x64':'Coiled 1.1 x64',
'Combusken_windows_amd64':'Combusken 2.0.0',
'Devre_4.0-avx2':'Devre 4.0',
'DON 230416.64 sse':'DON 230416.64',
'Dragon-3-64bit-avx2':'Dragon 3.2 by Komodo Chess 64-bit',
'Ethereal 14.00 pext-avx2':'Ethereal 14.00 (NNUE)',
'Expositor_2BR17':'Expositor 2BR17',
'FatFritz3':'Fat Fritz 3',
'Fire_8.NN.MC.3 updated':'Fire 8.NN.MC.3 x64 bmi2',
'Frozenight-6.0.0-windows-x86-64-v2':'Frozenight 6.0.0 1b89891',
'Gogobello_win_avx2':'gogobello 3.0',
'Halogen 11.4 avx2':'Halogen 11.4',
'Houdini 6.03 Pro pext':'Houdini 6.03 Pro x64-pext',
'Igel-x64_bmi2_avx2_3_4_0':'Igel 3.4.0 64 BMI2 AVX2',
'Koivisto_9.2-windows-avx2-pgo-pext':'Koivisto 9.2',
'Lc0_30':'Lc0_30',
'Marvin_x86_64_avx2':'Marvin 6.1.0',
'Minic_mingw_x64_skylake':'Minic 3.33',
'Nemorino_6.00_win64_avx2':'Nemorino 6.00 Patch 1 (AVX2/PEXT)',
'Pawn_1.0_win_haswell':'pawn 1.0',
'PowerFritz 18 AVX2':'PowerFritz 18',
'Rebel-16.2':'Rebel-16.2',
'Revenge_3_(Pedone)_avx2':'Revenge 3.0',
'Rick48':'Rick48',
'RofChade 3.0':'rofChade 3.0 BMI2 AVX2',
'RubiChess-20221203_x86-64-bmi2':'RubiChess 20221203 (bmi2)',
'RukChess.3.0.15.NNUE':'RukChess 3.0.15 NNUE',
'Schooner2.2-generic':'Schooner 2.2 NON-POPCNT',
'Scorpio':'Scorpio',
'Seer_v2.6_x64_avx2_popcnt':'Seer 2.6.0',
'Slow64-avx2':'SlowChess Blitz 2.9 avx2',
'Smallbrain7.0-x86-64-bmi2':'Smallbrain 7',
'Stash-34.0-windows-x86_64-bmi2':'Stash v34.0',
'Stockfish_23012306_x64_bmi2':'Stockfish dev-20230123-596a528c',
'Toga411-avx2':'Toga IV 1.1',
'Tucano 10.0':'Tucano 10.00',
'Uralochka3.39d-avx2':'Uralochka v3.39d',
'Velvet-v5.1.0-x86_64-avx2':'Velvet v5.1.0',
'Viridithas8.0.0-avx2':'Viridithas 8.0.0',
'Wasp650-windows-avx':'Wasp 6.50',
'Weiss-pext2.1':'Weiss 2.1-dev',
'Xiphos-0.6.1-w64-bmi2':'Xiphos 0.6.1 BMI2',
'Zahak-10.0-avx':'Zahak 10.0'
}

def handle_file(file,new):
    n=open(new, 'w') 
    i=0
    with open(file, 'r') as f:
        for line in f:
            delim='------'
            line=line.rstrip()

            if line.startswith('[White ') or line.startswith('[Black '): 
                new_engine = line.split('"')[1]
                line = line.split('"')[0]+'"'+ lookup.get(new_engine, new_engine)+'"]'

            elif delim in line:
                white = line.split(delim)[0].rstrip()
                black = line.split(delim)[1].lstrip().split('=')[0]
                line = lookup.get(white,white)+' '+delim+' '+lookup.get(black,black)
            
            elif line.startswith('Engine') and delim not in line:
                player = line.split('=')[1]
                part_num = line.split('=')[0]
                line = part_num + '=' + lookup.get(player, player)

#                i+=1
#                if i == 200:
#                    n.close()
#                    return
            n.write(line+'\n')
    n.close()
    return

handle_file(file, new)
