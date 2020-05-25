class GameStates():
    def __init__(self,ai_settings):
        self.ai_settings=ai_settings
        self.game_active=False
        self.rest_states()

        self.high_score=0
        self.level=1

    def rest_states(self):
        self.ships_left=self.ai_settings.ship_limit
        self.score=0
