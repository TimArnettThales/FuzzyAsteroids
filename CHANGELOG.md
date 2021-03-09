# Changelog

## [1.1.3] - 09 - March 2021

- Enabled specification of starting position/angle/lives of the ShipSprite
- Enabled the tracking of lives within the ShipSprite, rather than in the Game environment
- Crash printouts now state crash time and position

## [1.1.2] - 08 - March 2021

- Resolved error where the final ship crash is not printed
- Resolved crash in completion of game mode, where the StoppingCondition enum
  could not be converted to an int

## [1.1.1] - 10 - February 2021

- Resolved error in AsteroidGame where game would end immediately due to while loop conditional
  not being properly updated for new StoppingCondition enum
- Added Exceptions for incorrect user Score/Scenario inputs to run()/start_new_game()

## [1.1.0] - 08 - February 2021

- Added StopCondition enum to highlight the game completion reason
- Added "time_limit" setting to the environment settings dictionary
- Time limit stop condition included, added time tracking to the graphics window
- Score now tracks time and stopping condition
- Fixed error where the ship was given an extra life. 
- Added computational cost tracking (evaluation time) to FuzzyAsteroidsGame via ``track_compute_cost`` kwarg, off by default

## [1.0.0] - 15 January 2021

- First official release of the Fuzzy Asteroids Simulation Environment

