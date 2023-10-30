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
  #Follin Bros Tone
  if inType == 'fo-o': env.follin_organ(8)
  if inType == 'fo-ps': env.follin_piano(8,12,120)
  if inType == 'fo-pm': env.follin_piano(8,25,120)
  if inType == 'fo-pl': env.follin_piano(8,50,120)
  if inType == 'fo-bs': env.follin_piano(8,12,128)
  if inType == 'fo-bm': env.follin_piano(8,25,128)
  if inType == 'fo-bl': env.follin_piano(8,50,128)
  #Follin Bros Tone(NES Frame)
  if inType == 'ofo-o': env.follin_organ(16)
  if inType == 'ofo-ps': env.follin_piano(16,12,120)
  if inType == 'ofo-pm': env.follin_piano(16,25,120)
  if inType == 'ofo-pl': env.follin_piano(16,50,120)
  if inType == 'ofo-bs': env.follin_piano(16,12,128)
  if inType == 'ofo-bm': env.follin_piano(16,25,128)
  if inType == 'ofo-bl': env.follin_piano(16,50,128)
  #tremolo tone(square)
  if inType == 'tres8': env.tremolo_piano(8,120,'square')
  if inType == 'tres16': env.tremolo_piano(16,120,'square')
  if inType == 'tres32': env.tremolo_piano(32,120,'square')
  #tremolo tone(saw)
  if inType == 'trew8': env.tremolo_piano(8,120,'saw')
  if inType == 'trew16': env.tremolo_piano(16,120,'saw')
  if inType == 'trew32': env.tremolo_piano(32,120,'saw')
  #stripe tone
  if inType == 'stps8': env.stripe_piano(8,128,'square')
  if inType == 'stps16': env.stripe_piano(16,128,'square')
  if inType == 'stps32': env.stripe_piano(32,128,'square')
  #stripe tone(saw)
  if inType == 'stpw8': env.stripe_piano(8,128,'saw')
  if inType == 'stpw16': env.stripe_piano(16,128,'saw')
  if inType == 'stpw32': env.stripe_piano(32,128,'saw')

msgText = ('(◇Example: "pm" = Piano-Middle)\n\n'
           '■Envelope Time:\n'
           '"s" = short, "m" = middle, "l" = long\n\n'

           '■Envelope Type:\n'
           '"p[s,m,l]"=piano, "b[s,m,l]"=bell(0 Sustain piano), "f[s,m,l]"=flute, \n\n'

           '★Special:(used: ch1,2)\n'
           '◆Follin Tone([o]-> 1frame = 1/60sec, []none = 1/120sec)\n'
           '"[o]fo-o" = Follin-Organ, "[o]fo-p[s,m,l]" = Follin-piano, \n'

           '◆Tremolo Piano([int i] == msec)\n'
           '"tres[8,16,32]"=Echo Piano(square Envelope)\n'
           '"trew[8,16,32]"=Echo Piano(saw Envelope)\n'

           '◆Stripe Piano([o]=)\n'
           '"stps[8,16,32]"=Stripe Piano(square Note)\n'
           '"stpw[8,16,32]"=Stripe Piano(saw Note)\n'
           )

inType = pag.prompt(text=msgText, title='envtype select', default='')

request(inType)
