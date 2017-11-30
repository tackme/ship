from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
  print "Turn", turn + 1
  guess_row = (raw_input("row: "))
  guess_col = (raw_input("col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print "Succeed" 
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Wrong Number..."
      if turn == 3:
        print "game over..."
    elif board[guess_row][guess_col] == "X":
      print( "Already" )
      if turn == 3:
        print "game over..."
    else:
      print "Failed..."
      board[guess_row][guess_col] = "X"
      if turn == 3:
        print "gameover..."
      
    print_board(board)
