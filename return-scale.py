#!/usr/bin/env python3

keys = ('C', 'C#-Db', 'D', 'D#-Eb', 'E', 'F', 'F#-Gb', 'G', 'G#-Ab', 'A',
        'A#-Bb', 'B')
modes = ('major', 'minor')

NUM_KEYS = len(keys)
NUM_MODES = len(modes)

import random;
print(keys[random.randint(0, NUM_KEYS - 1)], 
      modes[random.randint(0, NUM_MODES - 1)]);
