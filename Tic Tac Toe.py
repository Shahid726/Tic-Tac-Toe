import time
print('Welcome to the Tic Tac Toe😁✌️')
time.sleep(2)
print('Getting everything ready for you😉')
time.sleep(2)
# print('\n')
print('Here you go😎')
time.sleep(2)
print('\n')
# take the name inputs from the players
player1 = input('Give a name as the 1st player:\n')
player2 = input('Give a name as the 2nd player:\n')
buffer_player = player1
board_list=[' ']*10

def display(board_list):
    '''Displays the game board to the players '''
    print(board_list[7]+'|'+board_list[8]+'|'+board_list[9])
    print(board_list[4]+'|'+board_list[5]+'|'+board_list[6])
    print(board_list[1]+'|'+board_list[2]+'|'+board_list[3])
display(board_list)


def player_input():
    '''Takes the input from the first player and accordingly assigns the coins to the players'''
    global b
    player1_marker='wrong'
    a=['x','o']
    while player1_marker not in a:
         player1_marker=input(f'{player1},choose your marker x or o: ')
         if player1_marker not in a:
            print('sorry i do not understand please choose x or o')
         if player1_marker == 'x':
            player2_marker = 'o'
         else:
            player2_marker = 'x'
    b = ((player1_marker,player2_marker)) 
    return b      
player_input()


def position_index1():
    '''Takes the index number from player1 and returns it'''
    position1='wrong'
    position_range=[0,1,2,3,4,5,6,7,8,9]
    index_vacancy = 'Yes'
    while position1.isdigit() == False or int(position1) not in position_range or index_vacancy == 'No':
        position1 = input(f'{player1},enter a position to place your marker: ')
        if position1.isdigit() == False:
            print('sorry your position is not a digit')
        elif position1.isdigit():
            if int(position1) not in position_range:
                print('sorry you are out of range') 
        elif board_list[int(position1)] != ' ':
            print('sorry the place is already taken') 
            position1 = input(f'{player1},enter a position to place your marker: ')


    return int(position1)


def position_index2(): 
    '''Takes the index number from player2 and returs it'''
    position2='wrong'
    position_range=[0,1,2,3,4,5,6,7,8,9]
    index_vacancy = 'Yes'
    while position2.isdigit()==False or int(position2) not in position_range or index_vacancy == 'No':
        position2=input(f'{player2},enter a position to place your marker: ')
        if position2.isdigit()==False:
            print('sorry your position is not a digit')
        elif position2.isdigit():
            if int(position2) not in position_range:
                print('sorry you are out of range') 
        elif board_list[int(position2)]!=' ':
            print('sorry the place is already taken')
            index_vacancy = 'No'
        else:
            index_vacancy = True              
    return int(position2)                  


def position_replacement(board_list,position,ex_or_o):
    '''Takes board_list,position and integer type parameter and reassigns the values from the inputs
      to the game board'''
    if board_list[position]!=' ':
            print('sorry the place is already taken') 
    while board_list[position] == ' ':
        board_list[position] = b[ex_or_o]
        display(board_list)
        return board_list   
        

def result_checker(board_list):
         '''takes the updated board list as the parameter and checks the result and returns the winner'''
         winner = 'no one still'
         if board_list[1]==board_list[2]==board_list[3]==b[0] or board_list[4]==board_list[5]==board_list[6]==b[0] or board_list[7]==board_list[8]==board_list[9]==b[0]:
            print(f'congratulations {player1}, you are the winner')
            winner = f'{player1}'

         elif board_list[1]==board_list[2]==board_list[3]==b[1] or board_list[4]==board_list[5]==board_list[6]==b[1] or board_list[7]==board_list[8]==board_list[9]==b[1]:
            print(f'congratulations {player2}, you are the winner')  
            winner = f'{player2}'

         elif  board_list[1]==board_list[4]==board_list[7]==b[0] or board_list[2]==board_list[5]==board_list[8]==b[0] or board_list[3]==board_list[6]==board_list[9]==b[0]:  
            print(f'congratulations {player1}, you are the winner')
            winner = f'{player1}' 

         elif board_list[1]==board_list[4]==board_list[7]==b[1] or board_list[2]==board_list[5]==board_list[8]==b[1] or board_list[3]==board_list[6]==board_list[9]==b[1]:
             print(f'congratulations {player2}, you are the winner')  
             winner = f'{player2}'  

         elif  board_list[1]==board_list[5]==board_list[9]==b[0] or board_list[3]==board_list[5]==board_list[7]==b[0]:  
            print(f'congratulations {player1}, you are the winner')
            winner = f'{player1}'  

         elif  board_list[1]==board_list[5]==board_list[9]==b[0] or board_list[3]==board_list[5]==board_list[7]==b[0]:  
            print(f'congratulations {player1}, you are the winner')
            winner = f'{player1}'  

         elif  board_list[1]==board_list[5]==board_list[9]==b[0] or board_list[3]==board_list[5]==board_list[7]==b[0]:  
            print(f'congratulations {player1}, you are the winner')
            winner = f'{player1}'  

         elif  board_list[1]==board_list[5]==board_list[9]==b[1] or board_list[3]==board_list[5]==board_list[7]==[1]:  
             print(f'congratulations {player2}, you are the winner')
              
         elif board_list.count(' ')<=2:
            print('oops it is a tie')

         return winner   


def continue_game(board_list):
    '''Takes board list as the parameter and continues the game flow'''
    game = True
    while game:
        position1 = position_index1()
        position_replacement(board_list,position1,0)  
        if(result_checker(board_list)) in [f'{player1}',f'{player2}']:
            game = False
            break

        position2 = position_index2()
        position_replacement(board_list,position2,1)   
        if(result_checker(board_list)) in [f'{player1}',f'{player2}']:
            game = False
            break
       
continue_game(board_list) 


def game_again():
    '''Takes input whether to play again or not and builds the game again everything from the start'''
    global player1
    global player2
    buffer_player = player1
    range_choice=['Y','N']
    n='wrong'
    while n not in range_choice:
        n=input('do you want to play again Y or N?  ')
        if n.upper()=='Y':
            board_list2=[' ']*10
            display(board_list2)
            player1 = player2
            player2 = buffer_player
            player_input()
            continue_game(board_list2)
            
        elif n.upper() == 'N':
            print('Thanks for playing Tik Tak Toe🙂')
            break    
        elif n not in range_choice:
            print("sorry! please select in 'Y' or 'N'")    
game_again()