import sys
import pyautogui as pag
import pygetwindow as pgw

#common utils
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
#---------------------------------------

#envelope types
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
  pos_xy_zero()
#---------------------------------------
def follin_piano(frame, x, y):
  follin_envelope_attack_init(frame)

  pag.PAUSE = 1/60
  #エディタのトップ画面へ遷移
  gamen_move(300,160)
  #エディタ1のEnvelope画面へ遷移
  gamen_move(282,140)

  #envエディタ1の続きの位置にカーソルを合わせる
  pos_xy_zero()
  setup = (frame+1) * 2
  pag.move(xOffset=setup, yOffset=0)

  while y > 1:
    pag.PAUSE = 1/60
    pag.move(xOffset=x, yOffset=y)
    pag.PAUSE = 1/60
    pag.click()
    y = y/2

  pos_xy_zero()
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


#tremolo
#---------------------------------------
def tremolo_piano(x, y, type):
  ptv = pgw.getWindowsWithTitle('ピストンボイス')[0]
  ptv.activate()

  #エディタのトップ画面へ遷移
  gamen_move(300,160)
  #エディタ1のEnvelope画面へ遷移
  gamen_move(282,140)

  pag.PAUSE = 1/4
  tremolo_piano_parts(x, type, 1)

def stripe_piano(x, y, type):
  x=x

#---------------------------------------
def tremolo_piano_parts(x, type, mode):
  ptv = pgw.getWindowsWithTitle('ピストンボイス')[0]
  pause_buffer = 1/4
  click_buffer = 1/60
  yRange_half = 240
  move_time = 12/60

  frame = x
  y_top = 256  #エディタ最大高さ

  pos_xy_zero()
  #相方の編集の場合、消音状態かつx分ずらしてから開始
  if mode == 2:
    pag.move(xOffset=0, yOffset=y_top/2)
    pag.click(interval=pause_buffer)
    pag.rightClick(interval=pause_buffer)
    pag.PAUSE = pause_buffer

    pag.move(xOffset=frame, yOffset=-yRange_half)
    pag.drag(0, yRange_half, move_time, button='left')
    pag.PAUSE = pause_buffer

    pag.move(xOffset=1, yOffset=-yRange_half)
    pag.drag(0, -yRange_half, move_time, button='left')
    pag.PAUSE = pause_buffer
    #TODO 開始点(本当に最大値から始めて良いのかは要考慮)
    pag.move(xOffset=0, yOffset=-yRange_half-y_top/2)

  else: #mode == 1 (一番最初の点)
    pag.move(xOffset=0, yOffset=y_top/2)
    pag.drag(0, -yRange_half, move_time, button='left')
    pag.PAUSE = pause_buffer
    pos_xy_zero()

  start_value = 6 #何回処理するか
  i = start_value #何回残っているか
  y_target = 256  #点を打つ高さの基準

  pag.PAUSE = 1 #debug

  while i >= 1:
    if i != start_value: #1回目だった場合、セットアップで値を決定しているのでスキップ
      #1(必ずy256に居るはず)
      pag.PAUSE = click_buffer
      pag.move(xOffset=1, yOffset=y_top-y_target)
      pag.PAUSE = click_buffer
      pag.click()
      pag.PAUSE = click_buffer

    # pag.PAUSE = 2 #debug
    #2(#1と同じyに点を打つ。最後はy_topに戻る)
    pag.PAUSE = click_buffer
    pag.move(xOffset=frame, yOffset=0)
    pag.click()
    pag.PAUSE = click_buffer
    if i!=start_value:
      pag.move(xOffset=0, yOffset=-(y_top-y_target))

    y_target = y_target/2

    # pag.PAUSE = 2 #debug
    #3
    if type=="saw":
      pag.move(xOffset=x/2, yOffset=(y_target/4*3))
      pag.PAUSE = click_buffer
      pag.click()
      pag.PAUSE = click_buffer
      pag.move(xOffset=-x/2, yOffset=-(y_target/4*3))
    else : #type=="square"
      pag.move(xOffset=1, yOffset=(y_top/2)-16)
      pag.drag(0, yRange_half, move_time, button='left')
      pag.PAUSE = pause_buffer
      pag.move(xOffset=0, yOffset=-yRange_half)
      pag.move(xOffset=-1, yOffset=-(y_top/2)+16)
      pag.PAUSE = click_buffer

    # pag.PAUSE = 2 #debug
    #4
    pag.move(xOffset=x+1, yOffset=y_top/2)
    pag.drag(0, yRange_half, move_time, button='left')
    pag.PAUSE = pause_buffer
    pag.move(xOffset=0, yOffset=-yRange_half)
    pag.move(xOffset=0, yOffset=-(y_top/2))
    pag.PAUSE = click_buffer

    # pag.PAUSE = 2 #debug

    #loop last
    i-=1




#-TODO----------------------------------
def tremolo_flute_parts(x, type, mode):
  ptv = pgw.getWindowsWithTitle('ピストンボイス')[0]
  pause_buffer = 1/4
  click_buffer = 1/60
  yRange_half = 240
  move_time = 12/60

  frame = x
  y_top = 256  #エディタ最大高さ

  pos_xy_zero()
  #相方の編集の場合、消音状態かつx分ずらしてから開始
  if mode == 2:
    pag.move(xOffset=0, yOffset=y_top/2)
    pag.click(interval=pause_buffer)
    pag.rightClick(interval=pause_buffer)
    pag.PAUSE = pause_buffer

    pag.move(xOffset=frame, yOffset=-yRange_half)
    pag.drag(0, yRange_half, move_time, button='left')
    pag.PAUSE = pause_buffer

    pag.move(xOffset=1, yOffset=-yRange_half)
    pag.drag(0, -yRange_half, move_time, button='left')
    pag.PAUSE = pause_buffer
    #TODO 開始点(本当に最大値から始めて良いのかは要考慮)
    pag.move(xOffset=0, yOffset=-yRange_half-y_top/2)

  else: #mode == 1 (一番最初の点)
    pag.move(xOffset=0, yOffset=y_top/2)
    pag.drag(0, -yRange_half, move_time, button='left')
    pag.PAUSE = pause_buffer
    pos_xy_zero()

  start_value = 8 #何回処理するか
  i = start_value #何回残っているか
  y_target = 256  #点を打つ高さの基準

  pag.PAUSE = 1 #debug

  while i >= 1:
    if i != start_value: #1回目だった場合、セットアップで値を決定しているのでスキップ
      #1
      pag.PAUSE = click_buffer
      pag.move(xOffset=1, yOffset=y_top-(y_top-y_target))
      pag.PAUSE = click_buffer
      pag.click()

    pag.PAUSE = 0.5 #debug
    #2
    pag.PAUSE = click_buffer
    pag.move(xOffset=frame, yOffset=0)
    pag.click()
    pag.PAUSE = click_buffer
    if i!=start_value: pag.move(xOffset=0, yOffset=-y_target)

    y_target = y_target/2

    pag.PAUSE = 0.5 #debug
    #3
    if type=="saw":
      pag.move(xOffset=x/2, yOffset=y_target/4*3)
      pag.PAUSE = click_buffer
      pag.click()
      pag.PAUSE = click_buffer
      pag.move(xOffset=-x/2, yOffset=-y_target/4*3)
    else : #type=="square"
      pag.move(xOffset=1, yOffset=(y_top/2)-16)
      pag.drag(0, yRange_half, move_time, button='left')
      pag.PAUSE = pause_buffer
      pag.move(xOffset=0, yOffset=-yRange_half)
      pag.move(xOffset=-1, yOffset=(-y_top/2)+16)
      pag.PAUSE = click_buffer

    pag.PAUSE = 0.5 #debug
    #4
    pag.move(xOffset=x+1, yOffset=y_top/2)
    pag.drag(0, yRange_half, move_time, button='left')
    pag.PAUSE = pause_buffer
    pag.move(xOffset=0, yOffset=-yRange_half)
    pag.move(xOffset=0, yOffset=-y_top/2)
    pag.PAUSE = click_buffer

    pag.PAUSE = 0.5 #debug

    #loop last
    i-=1
