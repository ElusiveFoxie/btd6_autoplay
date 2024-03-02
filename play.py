# pip3 install pyautogui
# pip3 install keyboard

import pyautogui
import time
import keyboard

def exit():
    pyautogui.click(452, 95)
    time.sleep(2)
    pyautogui.click(790, 65)
    time.sleep(2)
    pyautogui.click(356, 491)
    time.sleep(0.5)

def use_sword_charge():
    pyautogui.click(35, 384)
    time.sleep(0.5)

def buy_dart_monkey():
    pyautogui.click(250, 590)
    time.sleep(0.5)

def buy_sub_monkey():
    pyautogui.click(630, 600)
    time.sleep(0.5)

def buy_tack():
    pyautogui.click(412, 593)
    time.sleep(0.5)

def buy_glue():
    pyautogui.click(524, 597)
    time.sleep(0.5)

def buy_bomb():
    pyautogui.click(348, 597)
    time.sleep(0.5)

def first_sub():
    pyautogui.click(535, 385)
    time.sleep(0.5) 

def second_sub():
    pyautogui.click(573, 386)
    time.sleep(0.5) 

def first_monkey():
    pyautogui.click(288, 349)
    time.sleep(0.1)

def second_monkey():
    pyautogui.click(290, 286)
    time.sleep(0.1)

def druid():
    pyautogui.click(390, 371)
    time.sleep(0.5)

def spike():
    pyautogui.click(750, 320)
    time.sleep(0.5)

def alchemist():
    pyautogui.click(715, 308)

def village():
    pyautogui.click(484, 410)

def first_tack():
    pyautogui.click(498, 369)

def glue():
    pyautogui.click(361, 388)

def second_tack():
    pyautogui.click(465, 369)

def bomb():
    pyautogui.click(428, 404)
    time.sleep(0.5) 

def moab_eliminator():
    pyautogui.click(36, 343)
    time.sleep(0.5) 

def set_strong_left():
    pyautogui.click(41, 250)
    time.sleep(0.5)

def upgrade_010_right():
    pyautogui.click(768, 383)
    time.sleep(0.5)

def upgrade_010_right2():
    pyautogui.click(769, 384)
    time.sleep(0.5)

def upgrade_100_right():
    pyautogui.click(764, 307)
    time.sleep(0.5)

def upgrade_001_right():
    pyautogui.click(766, 454)
    time.sleep(0.5)

def upgrade_100_left():
    pyautogui.click(167, 306)

def upgrade_010_left():
    pyautogui.click(168, 382)

def upgrade_001_left():
    pyautogui.click(156, 442)
    time.sleep(0.5) 

# click 'active window' for keyboard (driud etc.)
pyautogui.click(440, 20)
time.sleep(1)

# click 'Play'
pyautogui.click(350, 570)
time.sleep(1)

# click to scroll to hardest maps
pyautogui.click(70, 290)
time.sleep(0.5)

# click to choose 'dark castle'
pyautogui.click(200, 365)
time.sleep(0.5)

# click to choose 'hard'
pyautogui.click(580, 280)
time.sleep(1)

# click to choose 'chimps'
pyautogui.click(742, 445)
time.sleep(1)

# click to overwritesave 
pyautogui.click(500, 437)
time.sleep(3)

# click to choose 'ok'
pyautogui.click(412, 454)
time.sleep(1.5)

buy_sub_monkey()
first_sub()

buy_dart_monkey()
first_monkey()
time.sleep(1)

# click start
pyautogui.click(771, 596)
# click 'fast forward'
pyautogui.click(771, 596)

# some delay
time.sleep(10)

#second dart 23
buy_dart_monkey()
second_monkey()
print("bought 2nd monkey")


# some delay
time.sleep(20)

#second sub 42
buy_sub_monkey()
pyautogui.click(573, 386)
print("bought 2nd sub")

time.sleep(31)

#buy and place sauda
pyautogui.click(200, 605)
time.sleep(0.5)
pyautogui.click(428, 371)
time.sleep(0.5)
print("bought sauda")

time.sleep(15)

#buy and place driud
druid()
keyboard.press_and_release('g')
#pyautogui.press('g') not working :(
time.sleep(1)
druid()
print("bought druid")
druid()
time.sleep(10)

# 010 druid
upgrade_010_right()
print("010 druid")
time.sleep(10)

# 110 druid
upgrade_100_right()
print("110 druid")
time.sleep(10)

# 120 driud 126
upgrade_010_right()
print("120 druid")
time.sleep(24)

# 130 druid
upgrade_010_right2()
print("130 druid")
time.sleep(19)

# buy and place spike factory
pyautogui.click(430, 210)
spike()
keyboard.press_and_release('j')
time.sleep(1)
spike()
print("spike")
time.sleep(10)


# 0-0-2 Spike
spike()
upgrade_001_left()
upgrade_001_left()
print("002_spike")
time.sleep(16)

# 2-0-2 Spike
upgrade_100_left()
print("102_spike")
time.sleep(4)
upgrade_100_left()
print("202_spike")
time.sleep(35)

# 2-0-3 Spike
upgrade_001_left()
print("203_spike")
time.sleep(41)

# 2-0-4 Spike
upgrade_001_left()
print("204_spike")
time.sleep(5)

alchemist()
keyboard.press_and_release('f')
time.sleep(0.5)
alchemist()
alchemist()
time.sleep(2)
upgrade_100_left()
time.sleep(2)
upgrade_100_left()
time.sleep(11)

#11s alch 300
upgrade_100_left()
print("300 alch")
time.sleep(5)

#x sec alch 320
upgrade_010_left()
print("310 alch")
time.sleep(2)
upgrade_010_left()
print("320 alch")

# 2 Tacks next to Sauda
buy_tack()
first_tack()
print("1st tack")
time.sleep(0.5)

buy_tack()
second_tack()
print("2nd tack")
time.sleep(0.5)

time.sleep(5) # to check

village()
keyboard.press_and_release('k')
time.sleep(0.5)
village()
print("village")
village()
time.sleep(3) 
upgrade_100_left()
print("100 village")
time.sleep(7) 
upgrade_100_left()
print("200 village")
time.sleep(6) 
upgrade_100_left()
print("300 village")
time.sleep(21)
upgrade_100_left()
print("400 village")
time.sleep(2) # to check
upgrade_010_left()
print("410 village")
time.sleep(12) # to check
upgrade_010_left()
print("420 village")

time.sleep(5) # to check
first_tack()
upgrade_100_left()
upgrade_100_left()
time.sleep(5) # to check
upgrade_010_left()
upgrade_010_left()
time.sleep(5) 
upgrade_100_left()
print("320 tack")

time.sleep(18) 
upgrade_100_left()
print("420 tack")

time.sleep(5) 

# second tack
second_tack()
upgrade_100_left()
time.sleep(2) 
upgrade_100_left()
time.sleep(2) 
upgrade_100_left()
time.sleep(3) 
upgrade_010_left()
upgrade_010_left()

time.sleep(5) 
upgrade_100_left()

time.sleep(5) # to adjust
druid()
upgrade_100_left()
print("druid 230")

time.sleep(35) # to adjust 39s
upgrade_010_left()
print("druid 240")
time.sleep(3)

time.sleep(1)
# 012 glue gunner
buy_glue()
time.sleep(1)
glue()
time.sleep(0.5)
print("glue")
glue()
time.sleep(1)
upgrade_010_right()
print("glue 010")
time.sleep(2)
upgrade_001_right()
print("glue 011")
time.sleep(2)
upgrade_001_right()
print("glue 012")

time.sleep(10) # to adjust
upgrade_001_right()
print("glue 013")

time.sleep(41)

#glue()
time.sleep(1)
upgrade_001_right()
time.sleep(1)
upgrade_010_right()
print("glue 024")
time.sleep(310)

#time.sleep(53) # to check important!
druid()
upgrade_010_right()
print("240 driud")


time.sleep(15)
buy_bomb()
time.sleep(1)
bomb()
time.sleep(1)
bomb()
time.sleep(1)
set_strong_left()
time.sleep(22)

upgrade_010_left()
upgrade_010_left()
upgrade_010_left()
upgrade_010_left()
time.sleep(3)
upgrade_001_left()
upgrade_001_left()
print("bomb 042")
# timer 361

time.sleep(146)
# timer: 507 
spike()
#time.sleep(180)
upgrade_001_left()
print("spike 205")

# timer 531 alch
time.sleep(24)

alchemist()
time.sleep(1)
upgrade_100_left()
print("alch 420")

# timer 635
time.sleep(104)
bomb()
time.sleep(1)
upgrade_010_left()
print("bomb 052")


# timer 670
time.sleep(35)
first_sub()
upgrade_001_left()
upgrade_001_left()
upgrade_001_left()
upgrade_001_left()

upgrade_100_left()
upgrade_100_left()

# timer 680
time.sleep(10)
second_sub()
upgrade_001_left()
upgrade_001_left()
upgrade_001_left()
upgrade_001_left()

upgrade_100_left()
upgrade_100_left()

#timer 690
# click anywhere for insta monkey
time.sleep(11)
pyautogui.click(301, 442)
 
# victory 'next' button
pyautogui.click(405, 525)
time.sleep(1)

# victory 'home' button
pyautogui.click(295, 500)
time.sleep(3)

#goto start

#exit()





