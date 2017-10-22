"""Default tester for morselate"""
from morselate.morselate import demorse, emorse

CODED = '- .... . / --.- ..- .. -.-. -.- / -... .-. --- .-- -. / ..-. --- -..- / .--- ..- -- .--. ... / --- ...- . .-. / - .... . / .-.. .- --.. -.-- / -.. --- --.'
DECODED = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'

def test_decoding():
    assert demorse(CODED.split(' ')) == DECODED

def test_encoding():
    assert emorse(DECODED.split(' ')) == CODED