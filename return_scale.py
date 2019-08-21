import music21
import random
import argparse

# Define cmd-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", type=int, default=1,
                    help="number of scales to return")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity (i.e. print scale pitches)")
args = parser.parse_args()


# Return a random music21.key.Key
def randomKey():
    # Limit keys to those with < 7 accidentals
    sharps = random.randint(-7, 7)
    mode = random.choice(('major', 'minor'))
    key_signature = music21.key.KeySignature(sharps)
    key = key_signature.asKey(mode)

    return key


def main():
    # Print the name of a random major or minor key to std-out
    for n in range(args.number):
        key = randomKey()
        print(key.name.replace('-', 'b'))

        if args.verbose:
            # Print the pitches of the chosen key
            print(' '.join([p.name for p in key.pitches]).replace('-', 'b'))

        print()


if __name__ == "__main__":
    main()
