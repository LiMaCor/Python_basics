# When programming, errors happen. It's just a fact of life. Python's solution to errors are exceptions.
# Sometimes you don't want exceptions to completely stop the program. Here's when the "try/except" block enters the game
def do_something_with_number(n):
    print(n)

def catch_this():
    the_list = (1, 2, 3, 4, 5)
    
    for i in range(20):
        try:
            do_something_with_number(the_list[i])
        except IndexError:
            do_something_with_number(0)

catch_this()