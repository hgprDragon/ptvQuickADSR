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

#Envelope
def request(inType):
  #piano
  if inType == 'ps': env.piano(12,120)
  if inType == 'pm': env.piano(25,120)
  if inType == 'pl': env.piano(50,120)
  #bell
  if inType == 'bs': env.piano(12,128)
  if inType == 'bm': env.piano(25,128)
  if inType == 'bl': env.piano(50,128)
  #flute
  if inType == 'fs': env.flute(12,128)
  if inType == 'fm': env.flute(25,128)
  if inType == 'fl': env.flute(50,128)
  #Follin Bros Tone()
  if inType == 'fo-o': env.follin_organ(8)
  if inType == 'fo-ps': env.follin_piano(8,12,128)
  if inType == 'fo-pm': env.follin_piano(8,25,128)
  if inType == 'fo-pl': env.follin_piano(8,50,128)
  #Follin Bros Tone(NES Frame)
  if inType == 'ofo-o': env.follin_organ(16)
  if inType == 'ofo-ps': env.follin_piano(16,12,128)
  if inType == 'ofo-pm': env.follin_piano(16,25,128)
  if inType == 'ofo-pl': env.follin_piano(16,50,128)

msgText = ('(◇Example: "pm" = Piano-Middle)\n\n'
           '■Envelope Time:\n'
           '"s" = short, "m" = middle, "l" = long\n\n'

           '■Envelope Type:\n'
           '"p[s,m,l]"=piano, "b[s,m,l]"=bell(0 Sustain piano), "f[s,m,l]"=flute, \n\n'

           '★Special:(used: ch1,2)\n'
           '◆Follin Tone([o]=)\n'
           '"[o]fo-o" = Follin-Organ, "[o]fo-p[s,m,l]" = Follin-piano'
           )

inType = pag.prompt(text=msgText, title='envtype select', default='')

request(inType)
