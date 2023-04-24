#this class contains all the functions required to run tic tac toe
class Game:
  
  def __init__(self):
    self.board = [["-", "-", "-"],
         ["-", "-", "-"], 
         ["-", "-", "-"]]
    self.board_index =['0,0','0,1','0,2','1,0','1,1','1,2','2,0','2,1','2,2']              
    self.placement = []

  #this funtion displays the board
  def printboard(self):
    for x in self.board:
      for y in x: 
        print(y,end = " ")
      print()
  #this board gets the coordinates and then puts them on the board.
  def update_board(self, input, player_marker):
    
    try :
      (row_num), (col_num) = input.split(',')
      self.board_index.remove(str(input))
      self.board[int(row_num)][int(col_num)]=player_marker
    except:
      print("Invalid coordinate. Please try again.")
  #this function checks the board to see if there are any winners
  def check(self):
    
    for x in self.board:
      value=""
      for y in x:
        value = value + y
      
      
      if value == 'XXX':
        
        return 'X'
        
      if value == 'OOO':
        
        return 'O'
            
    
    for x in range(3):
      value=""
      for y in range(3):
        value = value + self.board[y][x]
      
      if value == 'XXX':
        
        return 'X'      
      if value == 'OOO':
        
        return 'O'
  
    
    value = ""
    for x in range(3):
      value += self.board[x][x]
    if value == 'XXX':
      
      return 'X'      
    if value == 'OOO':
      
      return 'O'
    
    value = self.board[0][2]+self.board[1][1]+self.board[2][0]
    if value == 'XXX':
      
      return 'X'      
    if value == 'OOO':
      
      return 'O'
    return None

#This class is used for player details 
class Player:
  def __init__(self, name, marker):
    self.name = name
    self.marker = marker

#this class contains all functions required to keep track of the score.
class Score:
  score = {}
  
  def __init__(self, player1, player2):
    self.score.update({player1.name: 0})
    self.score.update({player2.name: 0})

  #this function prints the score
  def print_score(self):
    print("Score:"+str(self.score))

  #this function updates the score by getting it from the check function
  def update_score(self, winner_name):
    winnerscore= int(self.score.get(winner_name))+1
    self.score.update({winner_name:winnerscore})
