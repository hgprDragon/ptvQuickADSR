import sys
import pyautogui as pag
import pygetwindow as pgw

def xy_zero():
  try:
    ptv = pgw.getWindowsWithTitle('ピストンボイス')[0]
  except Exception:
    print('Pxtone voice is not started')
    sys.exit(1)

  ptv.activate()
  pag.moveTo(ptv.topleft)
  pag.move(xOffset=32, yOffset=179)
  pag.PAUSE = 0.1
