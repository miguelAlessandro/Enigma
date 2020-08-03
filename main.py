from settings import *
from library.enigma import Enigma


def press_button(machine, key):
    #poner cosas de la gui
    machine.press(key)
    #poner cosas de la gui x2


if __name__ == '__main__':
    machine = Enigma(n, order, rotor, pairs, initial_position)
    print(machine.press('A'))