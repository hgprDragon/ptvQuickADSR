import sys
import pyautogui as pag
import pygetwindow as pgw

def piano(x,y):
  pos_xy_zero()
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
  pos_xy_zero()
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

def follin_organ():
  x=1

  while y > 1:
    pag.PAUSE = 1/60
    pag.move(xOffset=x, yOffset=y)
    pag.PAUSE = 1/60
    pag.click()
    y = y/2

def follin_envelope_attack_init(editor_num):
  pos_xy_zero()
  ptv = pgw.getWindowsWithTitle('ピストンボイス')[0]
  ptv.activate()

  #エディタのトップ画面へ遷移
  pag.move(xOffset=2000, yOffset=-32)
  pag.click()
  pag.PAUSE = 1/60

  #エディタ1のEnvelope画面へ遷移
  pag.move(xOffset=0, yOffset=-32)
  pag.click()
  pag.PAUSE = 1/60

  #座標リセット
  pos_xy_zero()

def pos_xy_zero():
  try:
    ptv = pgw.getWindowsWithTitle('ピストンボイス')[0]
  except Exception:
    print('Pxtone voice is not started')
    sys.exit(1)

  ptv.activate()
  pag.moveTo(ptv.topleft)
  pag.move(xOffset=32, yOffset=179)
  pag.PAUSE = 1/60
