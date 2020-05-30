import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
from star import random_stars
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
import game_functions as gf

def load_highscore(stats):
    filename = 'highscore.txt'
    with open(filename) as file_object:
        stats.high_score = int(file_object.readline())

def run_game():
   # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    
    pygame.display.set_caption("Alien Invasion")
    
    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    load_highscore(stats)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Create start
    stars = random_stars(50, ai_settings.screen_width, ai_settings.screen_height)

    # Start the main loop for the game.
    while(True):
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets) 
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, stars,
                         play_button)
    

run_game()