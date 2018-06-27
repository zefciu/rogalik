from readchar import readkey

from rogalik.board import Board, OutOfBounds
from rogalik.player import Player
from rogalik.monster import Orc
from random import randint

CLEAR_SCREEN = '\x1b[3;J\x1b[H\x1b[2J'
CTRL_C = '\x03'

DIRECTIONS = {
    '\x1b[D': (-1, 0),
    '\x1b[C': (1, 0),
    '\x1b[A': (0, -1),
    '\x1b[B': (0, 1),
}


def play():
    board = Board(20, 20)
    player = Player()
    monster=Orc()
    board.add_mob(monster,randint(0,20),randint(0,20))
    board.add_mob(player, 10, 10)
    while True:
        print(CLEAR_SCREEN)
        print(board.render())
        key = readkey()
        if key==' ':
            continue
        if key==CTRL_C:
            print('quit')
            break
             
        vector = DIRECTIONS.get(key)
        if vector is not None:
            try:
                board.move(player.position, vector)
            except OutOfBounds:
                pass
        vector=monster.move_to_player(player.position)
        board.move(monster.position, vector)        


if __name__ == '__main__':
    play()
