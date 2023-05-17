import os
import time
import random


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class LifeGame:
    def __init__(self, ocean: list):
        self.ocean = ocean

    def get_next_generation(self):
        new_ocean = []
        for y in range(len(self.ocean)):
            new_ocean.append([])

            for x in range(len(self.ocean[y])):
                cell = self.ocean[y][x]
                count = 0
                # для соседей
                for new_y in [y - 1, y, y + 1]:
                    for new_x in [x - 1, x, x + 1]:
                        if (new_x >= 0 and new_x < len(self.ocean[y])) and (new_y >= 0 and new_y < len(self.ocean)):
                            if not (new_x == x and new_y == y):
                                if (self.ocean[new_y][new_x] == 1):
                                    count += 1
                if cell == 0:
                    if count == 3:
                        new_cell = 1
                    else:
                        new_cell = 0
                elif cell == 1:
                    if count == 2 or count == 3:
                        new_cell = 1
                    else:
                        new_cell = 0
                new_ocean[y].append(new_cell)

        self.ocean = new_ocean
        return self

    def __str__(self) -> str:
        new_str = ''
        for lst in self.ocean:
            for x in lst:
                if x == 0:
                    new_str += '•'
                elif x == 1:
                    new_str += '■'
                new_str += ' '
            new_str += '\n'
        return new_str

    def __repr__(self) -> str:
        pass


# my_ocean = [
#     [0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0]
# ]

my_ocean = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0]
]


def create_ocean(size: int):
    answer = []
    for i in range(size):
        # zero_count = random.randint(0, size // 2)
        zero_count = size // 2
        one_count = size - zero_count
        my_list = [0]*zero_count + [1]*one_count
        random.shuffle(my_list)
        answer.append(my_list)
    return answer


my_ocean = create_ocean(20)
life_game = LifeGame(my_ocean)
print(life_game)

GameOn = True
prev_ocean = []
while GameOn:
    prev_ocean.append(life_game.ocean)
    time.sleep(0.2)
    clear()
    print(life_game.get_next_generation())
    count = 0
    for y in range(len(life_game.ocean)):
        for x in range(len(life_game.ocean[y])):
            if x != 0:
                count += 1
    if count == 0:
        GameOn = False
    for ocean in prev_ocean:
        if life_game.ocean == ocean:
            GameOn = False
