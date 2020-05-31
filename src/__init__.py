from src.utils import Game, StateManager
from src.states import Simulator


game = Game()

state_manager = StateManager()
state_manager.init(game)
state_manager.set_initial_state(Simulator())
