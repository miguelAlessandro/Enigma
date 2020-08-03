from dotenv import load_dotenv
import os
load_dotenv()

n = int(os.getenv('N_ROTORS'))
order = list(map(int, os.getenv('WHO_ROTORS').split(',')))
rotor = os.getenv('ROTORS_CONFIG').split(',')
pairs = os.getenv('CONNECTIONS').split(',')
initial_position = os.getenv('INITIAL_POSITION').split(',')