import random
import time
import sys
import os
from typing import Optional

from util import HashableCoordinates, hidden_cursor, raw, nonblocking,\
    clear_terminal
from snake import Snake
from coordinates import Coordinates

class Game:
    _STEP_INTERVAL = 0.2
    _GAME_WIDTH = 10
    _GAME_HEIGHT = 10
    _snake: Snake
    _move_direction: str
    _mouse_location: Coordinates
    _game_over: bool

    def __init__(self) -> None:
        self._snake = Snake()
        self._move_direction = 'RIGHT'
        self._mouse_location = Coordinates(4, 4)
        self._game_over = False

    def _move_snake(self) -> None:
        if self._move_direction == 'LEFT':
            # TODO Move self._snake to the left. You may NOT directly access
            # the snake's private attributes here to accomplish this. You must
            # instead call one of the snake's methods (which you'll need to
            # design and implement)
            self._snake.set_direction('left')
            self._snake.move()




        if self._move_direction == 'RIGHT':
            # TODO Move self._snake to the right. You may NOT directly access
            # the snake's private attributes here to accomplish this. You must
            # instead call one of the snake's methods (which you'll need to
            # design and implement)
            self._snake.set_direction('right')
            self._snake.move()


        if self._move_direction == 'UP':
            # TODO Move self._snake up. You may NOT directly access the
            # the snake's private attributes here to accomplish this. You must
            # instead call one of the snake's methods (which you'll need to
            # design and implement)
            self._snake.set_direction('up')
            self._snake.move()




        if self._move_direction == 'DOWN':
            # TODO Move self._snake down. You may NOT directly access the
            # the snake's private attributes here to accomplish this. You must
            # instead call one of the snake's methods (which you'll need to
            # design and implement)
            self._snake.set_direction('down')
            self._snake.move()
            




    def _print(self, hashable_coordinates: set[HashableCoordinates]) -> None:
        print("\033[%d;%dH" % (0, 0))
        chars = [
            [' ' for _ in range(Game._GAME_WIDTH)]\
                for _ in range(Game._GAME_HEIGHT)
        ]
        for i in range(Game._GAME_HEIGHT):
            for j in range(Game._GAME_WIDTH):
                if HashableCoordinates(Coordinates(i, j)) in\
                        hashable_coordinates:
                    chars[i][j] = '*'
        chars[self._mouse_location.row][self._mouse_location.column] = '-'
        lines = [''.join(line) for line in chars]
        board = '\n'.join(lines)
        sys.stdout.write(f'{board}\n')
        sys.stdout.flush()

    def _step(self) -> None:
        self._move_snake()

        # TODO Replace `if False:` with a proper Python if statement condition
        # that correctly determines whether self._snake has run into itself. You
        # may NOT directly access the the snake's private attributes here to
        # accomplish this. You must instead call one of the snake's methods
        # (which you'll need to design and implement)
        if self._snake.check_self_collision():
            self._game_over = True

        coordinates_list = self._snake.get_coordinates_list()
        hashable_coordinates_set = set([
            HashableCoordinates(c) for c in coordinates_list
        ])
        if HashableCoordinates(self._mouse_location) in\
                hashable_coordinates_set:
            self._snake.grow() # grow the snakle
                    # respawn the mouse at a random empty cell
            empty_cells: list[Coordinates] = []

            for r in range(Game._GAME_HEIGHT):
                for c in range(Game._GAME_WIDTH):
                    candidate = Coordinates(r, c)
                    if (HashableCoordinates(candidate)
                            not in hashable_coordinates_set):
                        empty_cells.append(candidate)

            if empty_cells:
                self._mouse_location = random.choice(empty_cells)
            else:
                # no empty cells mean snake filled the borad aka the end
                 self._game_over = True



            # TODO Make self._snake grow. This should add one segment to the
            # snake. Its location should be where the snake's tail USED to be
            # just before the most recent movement. You may NOT directly access
            # the the snake's private attributes here to accomplish this. You
            # must instead call one of the snake's methods (which you'll need
            # to design and implement)
                                 

            




            # Don't modify this code here. It generates a new mouse at a random
            # empty location.
            coordinates_list = self._snake.get_coordinates_list()
            hashable_coordinates_set = set([
                HashableCoordinates(c) for c in coordinates_list
            ])
            empty_coordinates_tuples = [
                    (i, j) for i in range(Game._GAME_HEIGHT)\
                        for j in range(Game._GAME_WIDTH)\
                            if HashableCoordinates(Coordinates(i, j)) not in\
                                hashable_coordinates_set
            ]
            random_coordinates_tuple = empty_coordinates_tuples[
                random.randint(0, len(empty_coordinates_tuples) - 1)
            ]
            self._mouse_location = Coordinates(
                random_coordinates_tuple[0],
                random_coordinates_tuple[1]
            )

        self._print(hashable_coordinates_set)

    def _update_move_direction(self, user_input: str) -> None:
        if (user_input == 'a' or user_input == 'A') and \
                self._move_direction != 'RIGHT':
            self._move_direction = 'LEFT'
        elif (user_input == 's' or user_input == 'S') and \
                self._move_direction != 'UP':
            self._move_direction = 'DOWN'
        elif (user_input == 'd' or user_input == 'D') and \
                self._move_direction != 'LEFT':
            self._move_direction = 'RIGHT'
        elif (user_input == 'w' or user_input == 'W') and \
                self._move_direction != 'DOWN':
            self._move_direction = 'UP'

    def play(self) -> None:
        clear_terminal()
        time_of_last_step = None
        with hidden_cursor():
            with raw(sys.stdin):
                with nonblocking(sys.stdin):
                    while not self._game_over:
                        start = time.time()
                        last_input = ''
                        user_input = sys.stdin.read(1)
                        while user_input:
                            last_input = user_input
                            user_input = sys.stdin.read(1)
                        if last_input:
                            self._update_move_direction(last_input)
                        time_now = time.time()
                        if time_of_last_step is None or\
                                time_now - time_of_last_step >=\
                                    Game._STEP_INTERVAL:
                            time_of_last_step = time.time()
                            self._step()
                        time.sleep(0.01)
        clear_terminal()
        print('''
 ▗▄▄▖▗▞▀▜▌▄▄▄▄  ▗▞▀▚▖     ▗▄▖ ▄   ▄ ▗▞▀▚▖ ▄▄▄ 
▐▌   ▝▚▄▟▌█ █ █ ▐▛▀▀▘    ▐▌ ▐▌█   █ ▐▛▀▀▘█    
▐▌▝▜▌     █   █ ▝▚▄▄▖    ▐▌ ▐▌ ▀▄▀  ▝▚▄▄▖█    
▝▚▄▞▘                    ▝▚▄▞▘                ''')
