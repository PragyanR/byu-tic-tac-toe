#This is the game controller that orchestrates the gae

from tic_tac_toe import Game, Player, Score

player1 = None
player2 = None
game = None
player_marker=None
player_name=None
score = None
#this function runs after one game is done. 
def game_prompt():
    while(True):
        print('Do you want to play a new game?(yes or no)')
        y_or_n=input()
        if y_or_n.lower().startswith('y'):
            print('new game starting')
            print()
            break
        else:
            print("ok, game ending")
            exit()
        

#While true loop, pools the game until they say stop
while True:
  #get players
  if player1 == None or player2 == None:
    print("Welcome to Pragyan's Tic Tok Toe!!!")
    print()
    print("what is the first person's name?")
    person1= input()
    print("what is the second person's name?")
    person2= input()
    player1 = Player(person1,"X")
    player2 = Player(person2,"O")
    score = Score(player1, player2)

  if game == None:
    game = Game()
  
  if len(game.board_index) > 0: 
    if(len(game.board_index)%2==0):
      player_marker=player2.marker
      player_name=player2.name
    else:
      player_marker=player1.marker
      player_name=player1.name

  game.printboard()
  print(player_name+', where would you like to put '+player_marker+'? For example, 0,0')
  placement = input()
  game.update_board(placement, player_marker)
  print()
  
  if len(game.board_index) < 5:
    winning_marker = game.check()
    if winning_marker != None:
      winner_name = ""
      if winning_marker == player1.marker:
        winner_name = player1.name  
      else:
        winner_name = player2.name
      print ("The winner is: {}".format(winner_name))
      score.update_score(winner_name)
      score.print_score()
      
      game= Game()
      game_prompt()
      continue
        
  if len(game.board_index) == 0:
    print('It is a Draw!')
    game = Game()
    game_prompt()

