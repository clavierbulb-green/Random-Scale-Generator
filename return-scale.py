#!/usr/bin/env python3

keys = ('C', 'C#-Db', 'D', 'D#-Eb', 'E', 'F', 'F#-Gb', 'G', 'G#-Ab', 'A',
        'A#-Bb', 'B')
modes = ('major', 'minor')

NUM_KEYS = len(keys)
NUM_MODES = len(modes)

import random;

print("A program that returns a random major or minor scale.\n" + 
      "Press <Enter> to print a new scale. Press <Control-C> to quit.")

while True:
    try:
        input()
    except KeyboardInterrupt:
        print('\n')
        break
    print(keys[random.randint(0, NUM_KEYS - 1)], 
      modes[random.randint(0, NUM_MODES - 1)]);

