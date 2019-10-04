import music21
import random
import argparse

# Define cmd-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", type=int, default=1,
                    help="number of scales to return")
parser.add_argument("-a", "--accidentals", type=int, default=7,
                    help="maximum number of accidentals")
parser.add_argument("-M", "--major", action="store_true",
                    help="return only major keys")
parser.add_argument("-m", "--minor", action="store_true",
                    help="return only minor keys")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity (i.e. print scale pitches)")
args = parser.parse_args()


# Return a random music21.key.Key
def randomKey(mode=None, num_accidentals=7):
    if mode is None:
        mode = random.choice(('major', 'minor'))
    # By default, limit keys to those with <= 7 accidentals
    sharps = random.randint(-num_accidentals, num_accidentals)
    key_signature = music21.key.KeySignature(sharps)
    key = key_signature.asKey(mode)

    return key


def main():
    # Print the name of a random major or minor key to std-out
    mode = None
    if args.major:
        mode = 'major'
    elif args.minor:
        mode = 'minor'

    for n in range(args.number):
        key = randomKey(mode, args.accidentals)
        print(key.tonic.unicodeName, key.mode)

        if args.verbose:
            # Print the pitches of the chosen key
            print(' '.join([p.unicodeName for p in key.pitches]))

        print()


if __name__ == "__main__":
    main()
