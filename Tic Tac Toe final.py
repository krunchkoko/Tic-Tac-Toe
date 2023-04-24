#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output

def display_board(board):
    
    
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])
    
    #Displaying of the board


# In[2]:


def player_input():
    
    marker = 'wrong'
    
    while marker not in ['X','O']:
        
        marker = input('Player 1 : Do you want to be X or O? ').upper()
        
    if marker == 'X':
        return('X','O')
    else:
        return('O','X')
    
    
#Asking for the prefered X or O and assigning them to each player
    


# In[3]:


def place_marker(board, marker, position):
    
    
    
    board[position] = marker
    
    #Place the X or O on the board based on the position they want


# In[5]:


def win_check(board, mark):
    
    if (board[1] == mark and board[2] == mark and board[3] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark) or(board[7] == mark and board[8] == mark and board[9] == mark) or(board[1] == mark and board[4] == mark and board[7] == mark) or(board[2] == mark and board[5] == mark and board[8] == mark) or(board[3] == mark and board[6] == mark and board[9] == mark) or(board[1] == mark and board[5] == mark and board[9] == mark) or(board[3] == mark and board[5] == mark and board[7] == mark):
        return True
    else:
        return False
    
#Check all the possible winning types


# In[6]:


import random
def choose_first():
    
    x = random.randint(1,2)

    if x == 1:
        print ('Player 1 will go first.')
    else:
        print ('Player 2 will go first.')
    

#Shuffle between player 1 and player 2, so as to see who will start the game first


# In[7]:


def space_check(board, position):
    
    if board[position] == ' ':
        return True
    else:
        return False
    
#To check if there is a space in the position, if there is that means next player cannot put marker there


# In[8]:


def full_board_check(board):
    
    if (board[1] and board[2] and board[3] and board[4] and board[5] and board[6] and board[7] and board[8] and board[9]) == ('X' or 'O'):
        return True
    else:
        return False
#Check if board is full, if it is that means it is a draw and game ends


# In[11]:


def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        
        position = int(input('Pick a position (1-9): '))
        
        
    return int(position)

#Asks the player to pick a position on the board
                


# In[14]:


def replay():
    
    play_again = ' '
    
    while play_again not in ['Y','N']:
        
        play_again = input('Another round (Y OR N)?: ').upper()
        
        if play_again not in  ['Y','N']:
            print('Sorry invalid choice! ')
            
    if play_again == 'Y':
        return True
    else:
        return False
    
#Ask if they want to play again


# In[ ]:


print('Welcome to Tic Tac Toe!')

while True:
    
    #To pick the player marker and assign to the 1 and 2 then decide who starts first
    turn = choose_first()
    player1_marker , player2_marker = player_input()
    
    #Display the board and start the game
    test_board = [' '] * 10
    display_board(test_board)
    
    #While loop to make sure the game does not end unless game won or full board
    game_on = True
    
    while game_on:
        if turn == 'Player 1 will go first.':
            #Ask player 1 to go place marker
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board, player1_marker, position)
            #Check if he wins based on win check
            if win_check(test_board, player1_marker):
                display_board(test_board)
                print('Congratulations, player 1 has won the game.')
                game_on = False
            #If he did not win, check if board is full
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print('It is a draw.')
                    game_on = False
                    #If no win and not full board, give the turn to player 2
                else:
                    turn = 'Player 2 will go first.'
                    #Will repeat till winner or full board then break out of the gameon loop
        
            
        else:
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board, player2_marker, position)
            if win_check(test_board, player2_marker):
                display_board(test_board)
                print('Congratulations, player 2 has won the game. ')
                game_on = False
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print('It is a draw.')
                    game_on = False
                else:
                    turn = 'Player 1 will go first.'
                    
    #Check  for play again?       
    if not replay():
        print('Thank you for playing.')
        break


# In[ ]:




