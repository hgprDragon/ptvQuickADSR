import sys
sys.dont_write_bytecode = True

import pyautogui as pag
import pygetwindow as pgw

import PtvEnvelopeTemplate as env

try:
  ptv = pgw.getWindowsWithTitle('ピストンボイス')[0]
except Exception:
  print('Pxtone voice is not started')
  sys.exit(1)

inType = pag.prompt(text='"ps"=piano-short\n"fs"=flute-short', title='envtype select', default='')

# s=short, m=middle, l=long
if inType == 'ps': env.piano(12,120)
if inType == 'pm': env.piano(25,120)
if inType == 'pl': env.piano(50,120)

if inType == 'fs': env.flute(12,128)
if inType == 'fm': env.flute(25,128)
if inType == 'fl': env.flute(50,128)
