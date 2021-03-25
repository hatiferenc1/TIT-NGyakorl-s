'''Kő papir olló. Randommal. Listából. ha elgépeli a felhasználó figyelmeztesse. 10 pontig megy'''

import random 

player = 0 
bot = 0 

lst = ["kő","papír","olló"]

while player < 10 and bot < 10:
    player_input = input()
    bot_valasztas = lst[random.randint(0,2)]
    print(f'bot pontja  {bot}')
    print(f'player pontja  {player}')
#egyenlő
    if player_input.lower() == bot_valasztas:
        print('Döntetlen, senki nem kap pontot ')
       
        
#kő üti az ollót    
    elif player_input.lower() == "kő" and bot_valasztas == 'olló':
        print('Player nyert, kap egy pontot ')
        player += 1
       

#olló üti a papírt
    elif player_input.lower() == 'olló' and bot_valasztas == 'papír':
        print('Player nyert,kap egy pontot ') 
        player += 1
        

#papír üti a követ
    elif player_input.lower() == 'papír' and bot_valasztas == 'kő':
        print('Player nyert,kap egy pontot ')
        player += 1 
        

#ha ez a buzi nyer(bot)
    else:
        print('Bot nyert ,ez a buzi kap egy pontot ')   
        bot += 1 

    print(f'Te választásod:  {player_input}')
    print(f'Ez a buzi választása: {bot_valasztas}')

if player == 10:
    print('Nyertél fasz!!')
else:
    print('Nem nyertél fasz :(') 
    
    
                  


