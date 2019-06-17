#!/usr/bin/env python3

import random;
import PySimpleGUI as sg

keys = ('C', 'C#-Db', 'D', 'D#-Eb', 'E', 'F', 'F#-Gb', 'G', 'G#-Ab', 'A',
        'A#-Bb', 'B')
modes = ('major', 'minor')

NUM_KEYS = len(keys)
NUM_MODES = len(modes)

layout = [[sg.Text('Your random scale: '), 
    sg.Text('', key='_OUTPUT_', size=(10,1))],
          [sg.Button('New Scale')]]

window = sg.Window('Random Scale Generator', layout, return_keyboard_events=True)

while True:
    event, values = window.Read()
    if event is None or event == 'q':
        break
    
    if event == 'New Scale':
        scale = keys[random.randint(0, NUM_KEYS - 1)] + ' ' + modes[
                random.randint(0, NUM_MODES - 1)]
        window.Element('_OUTPUT_').Update(scale)

window.Close()
