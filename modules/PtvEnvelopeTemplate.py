import sys
import pyautogui as pag
import pygetwindow as pgw

def piano(x,y):
  xy_zero()
  ptv = pgw.getWindowsWithTitle('ピストンボイス')[0]
  ptv.activate()

  pag.click()

  while y > 1:
    pag.PAUSE = 1/60
    pag.move(xOffset=x, yOffset=y)
    pag.PAUSE = 1/60
    pag.click()
    y = y/2

def flute(x,y):
  xy_zero()
  ptv = pgw.getWindowsWithTitle('ピストンボイス')[0]
  ptv.activate()

  pag.move(xOffset=0, yOffset=256)
  pag.PAUSE = 1/60
  pag.click()

  i=128

  while i > 1:
    pag.PAUSE = 1/60
    pag.move(xOffset=x, yOffset=-i)
    pag.PAUSE = 1/60
    pag.click()
    i = i/2

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
