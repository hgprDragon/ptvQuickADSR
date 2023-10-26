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

def pos_test(posName,x,y):
  pag.moveTo(ptv.topleft)
  pag.move(xOffset=x, yOffset=y)
  pag.prompt(posName + ": x=" + str(x) + ", y=" + str(y))

posName = "原点"
pos_test(posName,0,0)

# posName = "エディタ基準点_OK"
# pos_test(posName,32,179)

# posName = "エディタ > 戻るボタン_OK"
# pos_test(posName,300,160)

# posName = "wavエディタ > [32,16]"
# pos_test(posName,64,195) # x = 32+32, y = 179+ 16

# posName = "top > wavエディタ1ボタン"
# pos_test(posName,100,140)
# posName = "top > wavエディタ2ボタン"
# pos_test(posName,100,284)

# posName = "top > envエディタ1ボタン"
# pos_test(posName,282,140)
# posName = "top > envエディタ2ボタン"
# pos_test(posName,282,284)
