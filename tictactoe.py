# -*- coding: utf-8 -*-
"""
Created on Wed Jun  24 19:13:28 2020

@author: Wilson
@description: Simple script for tic-tac-toe playing

"""
cells = [' '] * 9

def print_board():
    line = '-' * 13
    print(line)
    print('|', cells[0], '|', cells[1], '|', cells[2], '|')
    print(line)
    print('|', cells[3], '|', cells[4], '|', cells[5], '|')
    print(line)
    print('|', cells[6], '|', cells[7], '|', cells[8], '|')
    print(line)


def print_board_of_indexes():
    line = '-' * 13
    print(line)
    print('|', '1', '|', '2', '|', '3', '|')
    print(line)
    print('|', '4', '|', '5', '|', '6', '|')
    print(line)
    print('|', '7', '|', '8', '|', '9', '|')
    print(line)
    
def ending_condition():
    #Horizontal
    if cells[0] == cells[1] == cells[2] and (cells[0] != ' '):
        return True
    elif cells[3] == cells[4] == cells[5] and (cells[3] != ' '):
        return True
    elif cells[6] == cells[7] == cells[8] and (cells[6] != ' '):
        return True
    
    #Vertical
    elif cells[0] == cells[3] == cells[6] and (cells[0] != ' '):
        return True
    elif cells[1] == cells[4] == cells[7] and (cells[1] != ' '):
        return True
    elif cells[2] == cells[5] == cells[8] and (cells[2] != ' '):
        return True
    
    # Diagonal
    elif cells[0] == cells[4] == cells[8] and (cells[0] != ' '):
        return True
    elif cells[2] == cells[4] == cells[6] and (cells[2] != ' '):
        return True

def player_move(num):
    label = 'player' + str(num)
    while True:
        try:
            label = input("Player {}'s turn. Key in a number from 1 to 9: ".format(str(num)))
            label = int(label)
            if label > 9:
                label = ''
                label = int(label)
        except ValueError:
            print('')
            print("Sorry, I did not understand that.")
            print("Please key in Digits only, and between 1 to 9.")
            continue
        else:
            break
    return label
        
def checker(grid, indx):
    ''' Checks if index is taken '''
    if grid[indx - 1] != ' ':
        return False
    return True

def retrieve_correct_index(playernum, indx):
    ''' If the cell that user selects is occupied, ask for another one '''
    while True:
        if checker(cells, indx) is False:
            print("Oops! Cell is already taken!") 
            print("Please select another index.")
            indx = player_move(playernum)
            continue
        else:
            break
        
    return (indx)
            
def start_tic_tac_toe():
    for index in range(9):
        print('Current board:')
        print_board()  
        
        # Player 1
        if index % 2 == 0: 
            player_one_index = player_move(1)
            player_one_index = retrieve_correct_index(1, player_one_index)
            cells[int(player_one_index) - 1] = 'X'
        
        # Player 2
        else:
            player_two_index = player_move(2)
            player_two_index = retrieve_correct_index(2, player_two_index)
            cells[int(player_two_index) - 1] = 'O'
        
        # When game is won
        if ending_condition() == True:
            print ('Game ended!')
            print_board()
            
            if index % 2 == 0: 
                print ('Player 1 won!')
            else: 
                print ('Player 2 won!')
            
            break
                 

if __name__ == "__main__":
    print('')
    print('These are the indexes on the board:')
    print_board_of_indexes()
    print('e.g. "1" is the top leftmost grid')
    print('')
    print('Player 1: X | Player 2: O')
    print('')
    start_tic_tac_toe()  
