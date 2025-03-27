from sokoban import SokobanBoard

#----------------------------------------------------------------
# BOARD 1

with open("boards/board1.txt", "r") as f:
    content = f.read()
board1 = SokobanBoard.board_builder(content)

#----------------------------------------------------------------
# BOARD 2

with open("boards/board2.txt", "r") as f:
    content2 = f.read()
board2 = SokobanBoard.board_builder(content2)

#----------------------------------------------------------------
# BOARD 3

with open("boards/board3.txt", "r") as f:
    content3 = f.read()
board3 = SokobanBoard.board_builder(content3)


#----------------------------------------------------------------
# BOARD 4

with open("boards/board4.txt", "r") as f:
    content4 = f.read()
board4 = SokobanBoard.board_builder(content4)

#----------------------------------------------------------------
# BOARD 5

