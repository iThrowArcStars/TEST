# main.py
from mana import ManaPool
from battlefield import Battlefield
from hand import PlayerHand
from abilities import Ability, DrawCard

from creature import Creature

draw_card_ability = DrawCard()

test_creature01 = Creature(
    name="Test Creature01",
    power=5,
    toughness=4,
    mana_cost={"Red": 2, "Colorless": 3},
    abilities=[draw_card_ability]
)
test_creature02 = Creature(
    name="Test Creature02",
    power=5,
    toughness=4,
    mana_cost={"Red": 2, "Colorless": 3},
    abilities=[draw_card_ability]
)

# Simulate performing abilities during the game
deck = [test_creature01, test_creature02]
game_state = {'player': 'Player 1'}
battlefield = Battlefield()
p1_mana_pool = ManaPool()
p1_hand = PlayerHand()

p1_hand.add(deck, 7)
print(p1_hand.player_hand)

p1_mana_pool.add_mana("Red", 4)
p1_mana_pool.add_mana("Colorless", 3)
print(p1_mana_pool.mana)
battlefield.add(test_creature01, p1_mana_pool)
draw_count = 7
test_creature01.perform_abilities(game_state, deck, p1_hand, draw_count)