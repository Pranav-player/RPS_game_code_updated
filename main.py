#ROCK,PAPER & SCISSORS
print("EPIC BATTLE ")
print("Select your move (R, P OR S)")

player1score = 0
player2score = 0

while True:
  player1move = str(input( "Player 1 > "))
  print()
  player2move = str(input( "Player 2 >"))
  print()

  if player1move == "R":
    if player2move == "R":
      print("Draw")
    elif player2move == "S":
      print("Player 1 wins")
      player1score += 1
    elif player2move == "P":
      print("Player 2 wins")
      player2score +=1
  elif player1move == "P":
    if player2move == "R":
       print("Player 1 wins")
       player1score += 1
    elif player2move == "S":
       print("Player 2 wins")
       player2score +=1
    elif player2move == "P":
      print("Draw")
  elif player1move == "S":
    if player2move == "R":
      print("Player 2 wins")
      player2score +=1
    elif player2move == "S":
      print("Draw")
    elif player2move == "P":
      print("Player 1 wins")
      player1score +=1

  if player1score == 3 or player2score == 3:
    print("GAME OVER")
    exit()
  else:
    continue
        