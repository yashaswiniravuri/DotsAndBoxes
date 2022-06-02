from PlayGame import *
from Box import *
from Chain import *
import numpy as np

class computer_game():
    def __init__(self,PlayGame):
        self.game=PlayGame
        self.make_move()

    def make_move(self):
        self.game.box.check_box()
        if self.game.box.found_box==False:
            self.select_next_edge()
            self.game.switch_player()

    def select_next_edge(self):
        if np.all((self.game.chain_list==0)):
            self.game.chain.make_chain()
        elif np.all((self.game.chain_list!=0)):
            self.game.chain.close_chain()
        else:
            self.game.chain.extend_chain()