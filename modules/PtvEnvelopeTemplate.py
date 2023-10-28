import sys
import pyautogui as pag
import pygetwindow as pgw

#---------------------------------------
def piano(x,y):
  pos_xy_zero()
  ptv = pgw.getWindowsWithTitle('ピストンボイス')[0]
  ptv.activate()

  #最初の点
  pag.PAUSE = 1/60
  pag.move(xOffset=0, yOffset=128)
  pag.drag(0, -256, 8/60, button='left')
  pag.PAUSE = 1/60

  pos_xy_zero()

  while y > 1:
    pag.PAUSE = 1/60
    pag.move(xOffset=x, yOffset=y)
    pag.PAUSE = 1/60
    pag.click()
    y = y/2

  pos_xy_zero()

#---------------------------------------
def flute(x,y):
  pos_xy_zero()
  ptv = pgw.getWindowsWithTitle('ピストンボイス')[0]
  ptv.activate()

  #最初の点
  pag.PAUSE = 1/60
  pag.move(xOffset=0, yOffset=128)
  pag.drag(0, 256, 8/60, button='left')
  pag.PAUSE = 1/60

  i=128
  pos_xy_zero()
  pag.move(xOffset=0, yOffset=256)

  while i > 1:
    pag.PAUSE = 1/60
    pag.move(xOffset=x, yOffset=-i)
    pag.PAUSE = 1/60
    pag.click()
    i = i/2

  pos_xy_zero()

#---------------------------------------
def follin_organ(frame):
  follin_envelope_attack_init(frame)

#---------------------------------------
def follin_piano(frame, x, y):
  follin_envelope_attack_init(frame)

  while y > 1:
    pag.PAUSE = 1/60
    pag.move(xOffset=x, yOffset=y)
    pag.PAUSE = 1/60
    pag.click()
    y = y/2

#---------------------------------------
def follin_envelope_attack_init(frame):
  ptv = pgw.getWindowsWithTitle('ピストンボイス')[0]
  ptv.activate()

  pause_buffer = 1/4
  yRange = 256
  yRange_half = 256
  move_time = 8/60

  pag.PAUSE = pause_buffer

  #エディタのトップ画面へ遷移
  gamen_move(300,160)
  #エディタ1のEnvelope画面へ遷移
  gamen_move(282,140)
  #x1.0ボタン押下
  pag.moveTo(ptv.topleft)
  pag.move(xOffset=150, yOffset=164)
  pag.click()
  #エディタ1のEnvelope編集
  pos_xy_zero()

  #1-0
  pag.move(xOffset=0, yOffset=128)
  pag.drag(0, -yRange_half, move_time, button='left')
  pag.PAUSE = pause_buffer
  #1-1
  pag.move(xOffset=frame, yOffset=yRange_half)
  pag.drag(0, -yRange_half, move_time, button='left')
  pag.PAUSE = pause_buffer
  #1-2
  pag.move(xOffset=1, yOffset=yRange_half)
  pag.drag(0, yRange_half, move_time, button='left')
  pag.PAUSE = pause_buffer
  #1-3
  pag.move(xOffset=frame, yOffset=-yRange_half)
  pag.drag(0, yRange_half, move_time, button='left')
  pag.PAUSE = pause_buffer
  #1-4
  pag.move(xOffset=1, yOffset=-yRange_half)
  pag.drag(0, -yRange_half, move_time, button='left')
  pag.PAUSE = pause_buffer

  #エディタのトップ画面へ遷移
  gamen_move(300,160)
  #エディタ2のEnvelope画面へ遷移
  gamen_move(282,284)
  #x1.0ボタン押下
  pag.moveTo(ptv.topleft)
  pag.move(xOffset=150, yOffset=164)
  pag.click()
  #エディタ2のEnvelope編集
  pos_xy_zero()

  #2-0
  pag.move(xOffset=0, yOffset=128)
  pag.drag(0, yRange_half, move_time, button='left')
  pag.PAUSE = pause_buffer
  #2-1
  pag.move(xOffset=frame, yOffset=-yRange_half)
  pag.drag(0, yRange_half, move_time, button='left')
  pag.PAUSE = pause_buffer
  #2-2
  pag.move(xOffset=1, yOffset=-yRange_half)
  pag.drag(0, -yRange_half, move_time, button='left')
  pag.PAUSE = pause_buffer
  #2-3
  pag.move(xOffset=frame, yOffset=yRange_half)
  pag.drag(0, -yRange_half, move_time, button='left')
  pag.PAUSE = pause_buffer
  #2-4
  pag.move(xOffset=1, yOffset=yRange_half)
  pag.drag(0, yRange_half, move_time, button='left')
  pag.PAUSE = pause_buffer
  #2-5(消音)
  pag.move(xOffset=1, yOffset=yRange_half)
  pag.drag(0, yRange_half, move_time, button='left')
  pag.PAUSE = pause_buffer




  # #2-1
  # pag.move(xOffset=frame, yOffset=yRange)
  # pag.PAUSE = pause_buffer
  # pag.click()
  # pag.PAUSE = pause_buffer
  # #2-2
  # pag.move(xOffset=0, yOffset=-yRange)
  # pag.move(xOffset=1, yOffset=0)
  # pag.PAUSE = pause_buffer
  # pag.click()
  # pag.PAUSE = pause_buffer
  # #2-3
  # pag.move(xOffset=frame, yOffset=0)
  # pag.PAUSE = pause_buffer
  # pag.click()
  # pag.PAUSE = pause_buffer
  # #2-4
  # pag.move(xOffset=0, yOffset=yRange)
  # pag.move(xOffset=1, yOffset=0)
  # pag.PAUSE = pause_buffer
  # pag.click()
  # pag.PAUSE = pause_buffer
  # #2-5(完全消音用の点配置)
  # pag.move(xOffset=16, yOffset=0)
  # pag.PAUSE = pause_buffer
  # pag.click()
  # pag.PAUSE = pause_buffer


#---------------------------------------
def gamen_move(x,y):
  ptv = pgw.getWindowsWithTitle('ピストンボイス')[0]
  ptv.activate()

  pag.moveTo(ptv.topleft)
  pag.move(xOffset=x, yOffset=y)
  pag.PAUSE = 1/60
  pag.click()
  pag.PAUSE = 1/60
  pag.moveTo(ptv.topleft)
#---------------------------------------
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
