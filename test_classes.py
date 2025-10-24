import pytest
from game import Block

def test_block_initial_health_for_non_white_color():
    block = Block(posx=10, posy=20, width=5, height=5, color="GREEN")
    # jeśli kolor różny od „WHITE”, health powinien być 100
    assert block.getHealth() == 100
