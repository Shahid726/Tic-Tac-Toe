board_list=[' ']*10
def display(board_list):
    print(board_list[7]+'|'+board_list[8]+'|'+board_list[9])
    print(board_list[4]+'|'+board_list[5]+'|'+board_list[6])
    print(board_list[1]+'|'+board_list[2]+'|'+board_list[3])
display(board_list)

def player_input():
    global b
    player1_marker='wrong'
    a=['x','o']
    while player1_marker not in a:
         player1_marker=input('player1,choose your marker x or o: ')
         if player1_marker not in a:
            print('sorry i  do not understand please choose x or o')
         if player1_marker =='x':
            player2_marker='o'
         else:
            player2_marker='x'
    b = ((player1_marker,player2_marker)) 
    return b      
player_input()

def position_index():
    position1='wrong'
    position_range=[0,1,2,3,4,5,6,7,8,9]
    while position1.isdigit()==False or int(position1) not in position_range:
        position1=input('player1,enter a position to place your marker: ')
        if position1.isdigit()==False:
            print('sorry your position is not a digit')
        if position1.isdigit():
            if int(position1) not in position_range:
                print('sorry you are out of range')        
    position2='wrong'
    while position2.isdigit()==False or int(position2) not in position_range:
        position2=input('player2,enter a position to place your marker: ')
        if position2.isdigit()==False:
            print('sorry your position is not a digit')
        if position2.isdigit():
            if int(position2) not in position_range:
                print('sorry you are out of range')         
    return [(int(position1),int(position2))]


def position_replacement(board_list,position_tup):
    if board_list[position_tup[0][0]]!=' ' or board_list[position_tup[0][1]]!=' ':
            print('sorry the place is already taken') 
    while board_list[position_tup[0][0]] == ' ' and board_list[position_tup[0][1]] == ' ':
        
            for position1,position2 in position_tup:
                board_list[position1] = b[0]
                board_list[position2] = b[1]
                display(board_list)
            return board_list   
        
position_replacement(board_list,position_index())


def continue_game(board_list):
    game=True
    while game:
         position_replacement(board_list,position_index())
         if board_list[1]==board_list[2]==board_list[3]==b[0] or board_list[4]==board_list[5]==board_list[6]==b[0] or board_list[7]==board_list[8]==board_list[9]==b[0]:
            print('congratulations player1, you are the winner')
            game=False
         elif board_list[1]==board_list[2]==board_list[3]==b[1] or board_list[4]==board_list[5]==board_list[6]==b[1] or board_list[7]==board_list[8]==board_list[9]==b[1]:
            print('congratulations player2, you are the winner')  
            game=False
         elif  board_list[1]==board_list[4]==board_list[7]==b[0] or board_list[2]==board_list[5]==board_list[8]==b[0] or board_list[3]==board_list[6]==board_list[9]==b[0]:  
             print('congratulations player1, you are the winner')
             game=False
         elif board_list[1]==board_list[4]==board_list[7]==b[1] or board_list[2]==board_list[5]==board_list[8]==b[1] or board_list[3]==board_list[6]==board_list[9]==b[1]:
             print('congratulations player2, you are the winner')  
             game=False  
         elif  board_list[1]==board_list[5]==board_list[9]==b[0] or board_list[3]==board_list[5]==board_list[7]==b[0]:  
             print('congratulations player1, you are the winner')
             game=False     
         elif  board_list[1]==board_list[5]==board_list[9]==b[0] or board_list[3]==board_list[5]==board_list[7]==b[0]:  
             print('congratulations player1, you are the winner')
             game=False     
         elif  board_list[1]==board_list[5]==board_list[9]==b[0] or board_list[3]==board_list[5]==board_list[7]==b[0]:  
             print('congratulations player1, you are the winner')
             game=False     
         elif  board_list[1]==board_list[5]==board_list[9]==b[1] or board_list[3]==board_list[5]==board_list[7]==[1]:  
             print('congratulations player2, you are the winner')
             game=False 
         elif board_list.count(' ')<=2:
            print('oops it is a tie')
            game=False
                        
continue_game(board_list) 

def game_again():
    range_choice=['Y','N']
    n='wrong'
    while n not in range_choice:
        n=input('do you want to play again Y or N?  ')
        if n.upper()=='Y':
            board_list2=[' ']*10
            display(board_list2)
            player_input()
            position_index()
            position_replacement(board_list2,position_index())
            continue_game(board_list2)
        elif n.upper() == 'N':
            break    
        elif n not in range_choice:
            print("sorry! please select in 'Y' or 'N'")    
game_again()          
