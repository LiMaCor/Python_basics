def draw_game():
    print("The game is drawed.")
    clear_screen(main_screen)

def clear_screen(screen):
    print("Screen cleared!")

class Screen():
    def __init__(self, screen_name):
        self.screen_name = screen_name

# This will initialize main_screen as a Singleton
main_screen = Screen("MainScreen1")