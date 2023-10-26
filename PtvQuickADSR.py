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

msgText = ('(◇Example: "pm" = Piano-Middle)\n\n'
           '■Envelope Type:\n'
           '"p" = piano, "f" = flute, \n\n'
           '■Envelope Time:\n'
           '"s" = short, "m" = middle, "l" = long\n\n'
           '■Special:(used: ch1,2)\n'
           '"fo-o" = Follin-Organ, "fo-p[s,m,l]" = Follin-piano'
           )

inType = pag.prompt(text=msgText, title='envtype select', default='')

if inType == 'ps': env.piano(12,128)
if inType == 'pm': env.piano(25,128)
if inType == 'pl': env.piano(50,128)

if inType == 'fs': env.flute(12,128)
if inType == 'fm': env.flute(25,128)
if inType == 'fl': env.flute(50,128)

if inType == 'fo-o': env.follin_organ()
if inType == 'fo-ps': env.follin_piano(12,128)
if inType == 'fo-pm': env.follin_piano(25,128)
if inType == 'fo-pl': env.follin_piano(50,128)
