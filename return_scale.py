import music21
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", type=int, default=1,
                    help="number of scales to return")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity (i.e. print scale pitches)")
args = parser.parse_args()


KEYS = ('C', 'D-', 'D', 'E-', 'E', 'F', 'G-', 'G', 'A-', 'A',
        'B-', 'B')
MODES = ('major', 'minor')


# Print the name of a random major or minor scale to std-out

for n in range(args.number):
    tonic = random.choice(KEYS)
    mode = random.choice(MODES)
    if mode == 'major':
        random_scale = music21.scale.MajorScale(tonic)
    else:
        random_scale = music21.scale.HarmonicMinorScale(tonic)

    print(random_scale.name.replace('-', 'b'))

    if args.verbose:
        # Print the pitches of the chosen scale
        print(' '.join([p.name for p in random_scale.pitches]).replace('-', 'b'))
        print('\n')
