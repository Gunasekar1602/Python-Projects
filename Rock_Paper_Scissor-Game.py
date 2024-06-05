import random
options=('rock','paper','scissor')  
playing=True

while playing:
    player=None
    computer=random.choice(options)
    while player not in options:
    
        player=input('Enter your Choice (Rock,Paper,Scissor) : ')

    print('Player : ',player)
    print('Computer : ',computer)

    if player==computer:
        print('Its Tie !')
    elif player.lower()=='rock'  and computer=='scissor':
        print('Congrats, You Win !!') 
    elif player.lower()=='scissor'  and computer=='paper':
        print('Congrats, You Win !!')
    elif player.lower()=='paper'  and computer=='rock':
        print('Congrats, You Win !!')
    else:
        print('You Loss')
    if not input('Play Again ? (Yes or No) : ').lower()=='yes':
        playing=False
print('Thank You for Playing')        


        