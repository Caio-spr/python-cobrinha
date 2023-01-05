"""
!Copyright - 2023 Caio_spr <spina.caioramos@gmail.com>
!COPYRIGHT NOTICE: As this is an iteration of a famous game, one may use this code elsewhere, as long as given permission
*THIS FILE HAS THE MAIN CODE TO RUN THE GAME, NO OBJECT OR FUNCTION
*WILL BE DEFINED HERE, YOU MAY FIND THEM INSIDE "game/assets/classes_and_functions.py"
"""

#*importing classes and tests

from assets.classes_and_functions import *

#*running tests*#
game = False
noERROR = run__all__tests()
if noERROR is True:
    game = True

#*running the game

while game: 
    

        #*generating the map
        game_map = generate_game_map(25,25,15)


        #*spawning the player
        #?player should spawn in the middle of the map
        player = Player(game_map[2],game_map[0][int(len(game_map[0])/2)] + game_map[3],game_map[0][int(len(game_map[1])/2)] + game_map[3],'black') 
        player.create_player()



        window.mainloop()




