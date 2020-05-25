import pygame
from settings import Settings
from ship     import Ship
from Alien    import Alien
import game_functions as gf
from pygame.sprite import Group
from game_states import GameStates
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("史大炮大战外星人")
    play_button=Button(ai_settings,screen,"Play")

    states=GameStates(ai_settings)
    sb=Scoreboard(ai_settings,screen,states)

    ship=Ship(ai_settings,screen)
    bullets=Group()

    alien=Alien(ai_settings,screen)
    aliens=Group()
    gf.creat_fleet(ai_settings,screen,ship,aliens)

    while 1:
        gf.check_events(ai_settings,screen,states,sb,play_button,ship,aliens,bullets)
        if states.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,states,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,states,sb,ship,aliens,bullets)

        gf.update_screen(ai_settings,screen,states,sb,ship,aliens,bullets,play_button)

run_game()
