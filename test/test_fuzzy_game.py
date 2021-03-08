from src.fuzzy_asteroids.fuzzy_asteroids import *


class FuzzyController(ControllerBase):
    pass

    def actions(self, ship: SpaceShip, input_data: Dict[str, Tuple]) -> None:
        pass


if __name__ == "__main__":
    # Available settings
    settings = {
        "frequency": 60,
        "real_time_multiplier": 3,
        "lives": 3,
        "time_limit": None,
        "graphics_on": True,
        "sound_on": False,
        "prints": True,
        "allow_key_presses": False
    }

    # Instantiate an instance of FuzzyAsteroidGame
    game = FuzzyAsteroidGame(settings=settings)

    score = game.run(controller=FuzzyController())
