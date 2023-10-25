import sys
import pyautogui as pag
import pygetwindow as pgw

import PtvEditorPosZero as xy0

def piano(x,y):
  xy0.xy_zero()
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
  xy0.xy_zero()
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
