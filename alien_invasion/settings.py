class Settings():
    def __init__(self):
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)

        self.ship_limit=3
        self.fleet_drop_speed=20

        self.speed_scale=1.1

        self.bullet_width=6
        self.bullet_height=30
        self.bullet_color=(200,20,20)
        self.bullet_allowed=3

        self.score_scale=1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 1.2
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_point=50

    def increase_speed(self):
        self.ship_speed_factor *=self.speed_scale
        self.bullet_speed_factor *=self.speed_scale
        self.alien_speed_factor *=self.speed_scale
        self.alien_point=int(self.alien_point*self.score_scale)
        print(self.alien_point )



