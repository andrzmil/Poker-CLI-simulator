from game import *
import re
import os

def draw_table(initial=False,*args):
    empty_list = []
    for arg in args:
        empty_list.append(arg)
    
    for p in player_pool:
        print("Seat {}: {} - {}".format(p.seat_no, p.name, p.money))

def play_single_hand():
    # initiate single hand object
    sh = SingleHand()
    
    # set number of active players
    sh.no_active_players = len(player_pool)
    
    #assign dealer button, sb, bb or dsb to particular players as well
    if game.hand_no == 1 and game.no_players == 2:
        game.D_SB_pos, game.bb_pos = 0, 1
        player_pool[0].isDSB = True
        player_pool[1].isBB = True
    elif game.hand_no == 1 and game.no_players > 2:
        game.D_pos, game.sb_pos, game.bb_pos = 0, 1, 2
        player_pool[0].isD = True
        player_pool[1].isSB = True
        player_pool[2].isSB = True
    elif game.D_pos == game.no_players - 1:
        game.D_pos, game.sb_pos, game.bb_pos = 0, 1, 2
    elif game.D_pos == game.no_players - 2:
        game.D_pos, game.sb_pos, game.bb_pos = game.no_players - 1, 0, 1
    elif game.D_pos == game.no_players - 3:
        game.D_pos, game.sb_pos, game.bb_pos = game.no_players - 2, game.no_players - 1, 0
    
    


        
    
    
              
    
    # draw cards for all players and set each player as active
    for pl in player_pool:
        pl.deck = [sh.choose_cards(), sh.choose_cards()]
        pl.isInAction = True

    isPreflopFinished = False
    
    """ preflop - each player can choose fold, call (limp) or raise or check
    all possible scenarios:

    
    
    """
    
       
    while sh.no_active_players > 1:
        
        
        for pr_pl in list(range(len(player_pool))) * 100:
            if not player_pool[pr_pl].isInAction == False:
                draw_table()
                print("Player {} turn.\nYour cards: {}".format(player_pool[pr_pl].name, repl_figs_and_colors(player_pool[pr_pl].deck)))
                curr_pf_pl_action = input("Choose (F)old, (C)all or place value no greater than your stack: ")
            elif sh.no_active_players == 1:
                break
            else:
                continue
                
            """three scenarios:
            if player chooses fold, his action is ended and he is no longer eligible to participate in hand
            

            """
            
            if curr_pf_pl_action.upper() == "F":
                print("{} folds\n".format(player_pool[pr_pl].name))
                player_pool[pr_pl].isInAction = False
                sh.no_active_players = sh.no_active_players-1
                #os.system('cls||clear')
            elif curr_pf_pl_action.upper() == "C":
                print("CALL")
            elif int(curr_pf_pl_action) > 2 and int(curr_pf_pl_action) <= player_pool[pr_pl].money:
                print("RAISE") 
            else:
                print("Incorrect submission!")

def define_players(no_players: int):
    # players stored in list as object
    global player_pool
    player_pool = []
    
    seats = [*range(no_players)]
    
    for p in range(no_players):
        temp_player = input("Player {} name: ".format(p+1))
        
        # assign random seat number to player and remove from seat list
        rnd_seat = np.random.choice(seats)
        seats.remove(rnd_seat)
        
        # append players to the list
        player_pool.append(Player(temp_player, rnd_seat))
        print("Welcome {}! Your seat number is {}\n".format(temp_player, rnd_seat))
        
    # final player pool compliant with seat number and print
    player_pool.sort(key=get_player_seat_no) 
    draw_table()
    
    print("-------------------------------------------------------------------\n")
    

def play_game():
    # initiate game with desired name of players
    
    global game
    game = Game(5)
    
    define_players(game.no_players)
    
    
    # initiate the game object
    
    play_single_hand()


