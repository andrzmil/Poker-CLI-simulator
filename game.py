import numpy as np


def repl_figs_and_colors(list_to_rplc: list):
    """replace numbers to real figures used in the game (J, Q, K, A)
    replace color abbreviations with emoji
    """
    figs = {11:'J', 12:'Q', 13:'K', 14:'A'}
    cols = {'H': '♥️', 'S': '♠️', 'D': '♦️', 'C': '♣️'}
    replaced = []
    for lst in list_to_rplc:
        for el in lst:
            
            if el in figs.keys():
                replaced.append(figs[el])
            elif el in cols.keys():
                replaced.append(cols[el])
            else:
                replaced.append(el)
                           
    replaced = list(map(str, replaced))
    return "".join(replaced)
   
class Game():
    def __init__(self, no_players: int):
        self.no_players = no_players
        self.isEnded = False
        self.initial_order = [*range(self.no_players)]
        self.minimum_raise = 2
        
        self.hand_no = 1
        
        self.D_SB_pos = None
        self.D_pos = None
        self.sb_pos = None
        self.bb_pos = None



class Player():
    def __init__(self, name: str, seat_no: int):
        self.name = name
        self.deck = []
        self.money = 100
        self.isInAction = False
        self.seat_no = seat_no
        self.curr_bet = 0
        self.isPlayingNow = False
        self.isDSB = False
        self.isD = False
        self.isSB = False
        self.isBB = False
        
def get_player_seat_no(player):
    return player.seat_no
        
        
class SingleHand():
    def __init__(self):
        self.deck = {2:['H','C','S','D'], 3:['H','C','S','D'], 4:['H','C','S','D'],
        5:['H','C','S','D'], 6:['H','C','S','D'], 7:['H','C','S','D'],
        8:['H','C','S','D'], 9:['H','C','S','D'], 10:['H','C','S','D'],
        11:['H','C','S','D'], 12:['H','C','S','D'], 13:['H','C','S','D'],
        14:['H','C','S','D']}
        self.pot = 0
        self.no_active_players = 0
        
        
    def choose_cards(self):
        # chooses random combination of cards from deck and removes
        chosen_figure = np.random.choice(list(self.deck.keys()))
        chosen_color_no = np.random.randint(0, len(self.deck.get(chosen_figure)))
        chosen_color = self.deck.get(chosen_figure)[chosen_color_no] 
        
        # remove value or key
        if len(self.deck.get(chosen_figure)) > 1:
            self.deck[chosen_figure].remove(chosen_color)
        else:
            self.deck[chosen_figure].remove(chosen_color)
            self.deck.pop(chosen_figure, None)
        return [chosen_figure, chosen_color]                 