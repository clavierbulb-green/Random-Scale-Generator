import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", type=int, default=1,
                    help="number of scales to return")
args = parser.parse_args()


# Prints the name of a random major or minor scale to std-out

KEYS = ('C', 'C#-Db', 'D', 'D#-Eb', 'E', 'F', 'F#-Gb', 'G', 'G#-Ab', 'A',
        'A#-Bb', 'B')
MODES = ('major', 'minor')

for n in range(args.number):
    random_scale = random.choice(KEYS) + ' ' + random.choice(MODES)
    print(random_scale)
