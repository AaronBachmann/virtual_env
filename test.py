import random
import os
import json

rolls = {"NOTHING": "HERE"}


def main():
    load_rolls()
    show_header()
    show_leaderboard()
    player1, player2 = get_players()
    play_game(player1, player2)