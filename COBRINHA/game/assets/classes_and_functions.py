"""
!Copyright - 2023 Caio_spr <spina.caioramos@gmail.com>
!COPYRIGHT NOTICE: As this is an iteration of a famous game, one may use this code elsewhere, as long as given permission
*THIS FILE HAS ALL THE OBJECTS, FUNCTIONS AND TESTS USED TO RUN THE GAME
*NO CODE WILL BE RUN DIRECTLY FROM HERE
"""


from tkinter import * #?creating a canvas
import keyboard #?detecting player input


##*canvas*##

window = Tk()
canvas = Canvas(window, width = 1280, height=720)
canvas.pack()


##*Classes*##

class Game:
    def __init__(self, player, game_map, food, game_over = False):
        self.player = player
        self.game_map = game_map
        self.food = food
        self.game_over = game_over
class Triangle: #!food
    def __init__(self, x1, y1, x2, y2, x3, y3, color = None):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.color = color
        self.id = None
    def create(self):
        if self.color is not None:
            canvas.create_polygon(self.x1,self.y1,self.x2,self.y2,self.x3,self.y3, fill=f"{self.color}")
        elif self.color is None:
            canvas.create_polygon(self.x1,self.y1,self.x2,self.y2,self.x3,self.y3) 
    def delete(self):
        canvas.delete(self.id) 
class Square: #!player and map
    def __init__(self, square_side, x, y, fill_color=None):
        self.square_side = square_side
        self.x = x
        self.y = y
        self.fill_color = fill_color
        self.id = None

    def square_create(self): #?takes the side and adds it to x and y to get the final coordinates
        if self.fill_color is not None:
            canvas.create_rectangle(self.x, self.y, (self.x + self.square_side), (self.y + self.square_side), fill=f"{self.fill_color}")
        elif self.fill_color is None:
            canvas.create_rectangle(self.x, self.y, (self.x + self.square_side), (self.y + self.square_side))

    def square_delete(self):
        canvas.delete(self.id)

    def square_move(self, dx, dy):
        self.square_delete()
        if self.fill_color is not None:
            self.x += dx
            self.y += dy
            self.x += (dx+self.square_side)
            self.y += (dy+self.square_side)
            self.create()
        elif self.fill_color is None:
            self.create(self.x+dx, self.y+dy, self.x+dx+self.square_side, self.y+dy+self.square_side)


#*player subclass*#


class Player(Square):
    def __init__(self, square_side, x, y, fill_color, player_direction = None, squares = None):
        super().__init__(square_side, x, y, fill_color)
        self.id = None
        self.player_location = [x,y]

        #! set default player_direction to 'up'
        if player_direction is not None: 
            self.player_direction = player_direction
        else:
            self.player_direction = 'up'
        
        #! define 'squares' as an empty list
        if squares is not None: 
            self.squares = squares
        else:
            self.squares = []
    

    #*create and delete self functions*#


    def create_player(self):
        self.squares.append(Square(self.square_side, self.player_location[0], self.player_location[1],self.fill_color))
        self.squares[0].square_create()

    def delete_player(self): #?delete all player squares and player_locations inside the respective lists
        for i in range(len(self.squares)):
            self.squares[i][0].square_delete()
        for j in range(len(self.squares)):
            del self.squares[-i]
        for k in range(len(self.player_location)):
            del self.player_location[-i]
        

    #*movement functions*#

    def get_player_direction(self):
        if keyboard:
            self.player_direction = 'up'
    
    def player_move_right(self):
        for i in range(len(self.player_location)):
            self.player_location[i][0] += self.square_side
            self.player_direction = 'right'
    def player_move_left(self):
        for i in range(len(self.player_location)):
            self.player_location[i][0] -= self.square_side
            self.player_direction = 'left'
    def player_move_down(self):
        for i in range(len(self.player_location)):
            self.player_location[i][1] += self.square_side
            self.player_direction = 'down'
    def player_move_up(self):
        for i in range(len(self.player_location)):
            self.player_location[i][1] -= self.square_side
            self.player_direction = 'up'



    #*growth function*#

    def player_grow(self):
        new_square = []
        if self.player_direction == 'up':
            newSquare = [self.player_location[len(self.player_location)][0], (self.player_location[len(self.player_location)][1]+self.square_side)] 
            self.player_location.append(new_square)
        elif self.player_direction == 'down':
            newSquare = [self.player_location[len(self.player_location)][0], (self.player_location[len(self.player_location)][1]-self.square_side)] 
            self.player_location.append(new_square)
        elif self.player_direction == 'left':
            newSquare = [(self.player_location[len(self.player_location)][0] + self.square_side), self.player_location[len(self.player_location)][1]] 
            self.player_location.append(new_square)
        elif self.player_direction == 'right':
            newSquare = [(self.player_location[len(self.player_location)][0] + self.square_side), self.player_location[len(self.player_location)][1]] 
            self.player_location.append(new_square)
        self.squares.append(Square(self.square_side, self.player_location[len(self.player_location)-1][0], self.player_location[len(self.player_location)-1][1]))
        self.squares[self.squares.length-1].create()



##**non-object functions**##


#*generate map function*#
    #takes the total rows, columns, the side of each square and the margin*
    #and
    #margin must be equal in all sides
    #!can't yet be used to change the size of the screen, will only do that
    #!after the menu is created

def generate_game_map(Trows, Tcollumns, square_side,margin = None, test = False):
    if margin is None:
        margin = 5
    game_map = []
    collumn = []
    row = []
    for xc in range(Tcollumns):
        collumn.append(xc*square_side)
    for yr in range(Trows):
        row.append(yr*square_side)
    game_map.append(collumn)
    game_map.append(row)

    if test is False:
        i = 0
        for j in range(len(game_map[i])):
            x = game_map[i][j] + margin
            for k in range(len(game_map[i+1])):
                y = game_map[i+1][k]+margin
                a = Square(square_side, x, y)
                a.square_create()
    
    game_map.append(square_side)
    game_map.append(margin)

    return game_map






                        #!!! TESTS !!!#




#*randomizers
import random

#* run all tests:


def run__all__tests():
    print(f"executing unit tests")
    noERROR = True
    total_tests = 1 #change after adding new tests
    current_test = 0
    failed_tests = []
    print(f"{current_test}/{total_tests}")
    
    while current_test < total_tests:
        noERROR = generate_game_map__TEST(noERROR)
        if noERROR is False:
            print(f"an error was found in test: {1}")
            failed_tests.append(current_test)
            current_test += 1
        else:
            current_test += 1
            print(f'{current_test}/{total_tests}')

        #put new tests here, in the same form as the first one


    print("all tests complete")
    if len(failed_tests) == 0:
        print("all tests were successful")
        print("executing the game")
        return noERROR
    else:
        print(f"failed tests:")
        print(f"{failed_tests}\n")
        print("correct the mistakes before continuing")
        return noERROR


#!test generate_game_map


def generate_game_map__TEST(noERROR):
    Trows = random.randint(1,100)
    Tcollumns = random.randint(1,100)
    square_side = random.randint(0,10)
    margin = random.randint(0,5)
    game_map = generate_game_map(Trows,Tcollumns,square_side,margin,True)

    #*testing if all coordinates and values are stored

    if len(game_map) != 4:
        print(f"ERROR: 'game_map' LENGTH IS NOT '4'\n")
        noERROR = False

    #*testing if number of x coordinates is equal to the amount of colummns

    if len(game_map[0]) > Tcollumns:
        print(f"ERROR: THERE ARE MORE 'x' COORDINATES THAN COLLUMNS\n")
        noERROR = False
    elif len(game_map[0]) < Tcollumns:
        print(f"ERROR: THERE ARE MORE COLLUMNS THAN 'x' COORDINATES\n")
        noERROR = False
    
    #*testing if number of x coordinates is equal to the amount of colummns

    if len(game_map[1]) > Trows:
        print(f"ERROR: THERE ARE MORE 'y' COORDINATES THAN ROWS\n")
        noERROR = False
    elif len(game_map[1]) < Trows:
        print(f"ERROR: THERE ARE MORE ROWS THAN 'y' COORDINATES\n")
        noERROR = False

    #*testing if the 'square_side' argument was interpreted correctly

    if game_map[2] != square_side:
        print(f"ERROR: 'square_side' ARGUMENT WAS MISINTERPRETED\n")
        noERROR = False
    
    #*testing if the 'margin' argument was interpreted correctly

    if game_map[3] != margin:
        print(f"ERROR: 'margin' ARGUMENT WAS MISINTERPRETED\n")
        noERROR = False

    #*testing if collumns are correctly spaced

    for i in range(len(game_map[0])):
        if i+1 < len(game_map[0]):
            fs = game_map[0][i]
            ss = game_map[0][i+1]
            res = ss - fs
            if res != square_side:
                print(f"ERROR: COLLUMNS ARE NOT CORRECTLY SPACED")
                noERROR = False
                break
        else:
            break    

    #*testing if rows are correctly spaced

    for i in range(len(game_map[1])):
        if i+1 < len(game_map[1]):
            fs = game_map[1][i]
            ss = game_map[1][i+1]
            res = ss - fs
            if res != square_side:
                print(f"ERROR: ROWS ARE NOT CORRECTLY SPACED")
                noERROR = False
                del fs, ss,res
                break
        else:
            del fs, ss,res
            break

    del game_map
    return noERROR


