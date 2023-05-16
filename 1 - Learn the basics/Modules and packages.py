# A module is a piece of software that has a specific functionality.
# Each module consists of a different file, which may be edited separately
# Modules inf Python are just Python files with a '.py' extension.
# The name of the module is the same as the file name.

# Try this uncommented, then comment it again
# import draw

# def main():
#     result = play_game()
#     draw.draw_game()

# Try this uncommented, then comment it again
# from draw import draw_game

# def main():
#     result = play_game()
#     draw_game()

# Try this uncommented, then comment it again
# from draw import *

# def main():
#     result = play_game()
#     draw_game()

# Modules may be loaded under any name you want.
# This is useful when importing a module conditionally to use the same name in the rest of code
# Try this uncommented, then comment it again
# if visual_mode:
#     import draw_visual as draw

# def main():
#     result = play_game()
#     draw.draw_game()

# The first time a module is loaded into a running Python script, it is initialized by
# executing the code in the module once.
# See this part in 'draw.py' file

# Functions used through the exercises
def play_game():
    print("Game's on!")

# This means that if  this script is executed, then
# main() will be executed
if __name__ == "__main__":
    main()