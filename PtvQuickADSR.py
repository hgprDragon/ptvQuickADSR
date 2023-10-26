import sys
sys.dont_write_bytecode = True

import pyautogui as pag
import pygetwindow as pgw

import modules.PtvEnvelopeTemplate as env

try:
  ptv = pgw.getWindowsWithTitle('ピストンボイス')[0]
except Exception:
  print('Pxtone voice is not started')
  sys.exit(1)

msgText = ('■Envelope Type:\n'
           '"p" = piano, "f" = flute, \n\n'
           '■Envelope Time:\n'
           '"s" = short, "m" = middle, "l" = long\n\n'
           '(◇Example: "pm" = Piano-Middle)')

inType = pag.prompt(text=msgText, title='envtype select', default='')

# s=short, m=middle, l=long
if inType == 'ps': env.piano(12,128)
if inType == 'pm': env.piano(25,128)
if inType == 'pl': env.piano(50,128)

if inType == 'fs': env.flute(12,128)
if inType == 'fm': env.flute(25,128)
if inType == 'fl': env.flute(50,128)
