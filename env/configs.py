"""
Define the configuration for the Texas Hold'em Poker game.
"""

class PlayerConfig:
    """Configuration for the player."""
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips

class TableConfig:
    """Configuration for the table."""
    def __init__(self, num_players, starting_chips, small_blind, big_blind):
        self.num_players = num_players
        self.starting_chips = starting_chips
        self.small_blind = small_blind
        self.big_blind = big_blind

class GameConfig:
    """Configuration for the game."""
    def __init__(self, num_rounds, mode)
        self.num_rounds = num_rounds
        self.mode = mode # 't' for tournament, 'c' for cash game
