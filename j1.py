def show_game_board():
    for i in range (3):
        for j in range (3):
            print ( game [i][j], end = ' ')
        print( )

def check():
    if game [0][0]=='x'and game [0][1]=='x'and game [0][2]=='x':
        print ('player1 wins ')
    else :
        if game [0][0]=='o' and game [0][1]=='o' and game [0][2] == 'o':
            print ('player2 wins ')
            exit()
        

game = [['_','_','_'],
       ['_','_','_'],
       ['_','_','_']]

show_game_board()
while True:

    #player1
    while True:
       print ('player1')
       row= int (input('row: '))
       col = int (input('col : '))
       if 0<= row <= 2 and 0 <= col <= 2 :
          if game [row][col]=='_':
             game[row][col]='x'
             break
          else:
             print ('this is not empty')
       else:
          print('invalid inputs,row and col must be between 0 and 2')
    show_game_board()
    check()

    #player2
    while True:
        print ('player2')
        row = int(input ('row: ')) 
        col = int(input ('col: '))
        if 0<= row <= 2 and 0<= col <=2 :
            if game [row][col]=='_':
               game = [row][col]= 'o'
               break
            else:
               print ('this is not empty')
        else:
            print ('invalid inputs , row and col must be between 0 and 2')
    show_game_board()
    check()

    
    
    
        