# btd6_autoplay
This repository contains a script to automatically win Dark Castle map in CHIMPS mode in Bloons Tower Defense 6

# Tutorial
1. Download the repository `git clone https://github.com/ElusiveFoxie/btd6_autoplay` and install the requirments `pip install -r requirements.txt`
2. Download AHK software in deprecated version 1.1.37.01 -> https://www.autohotkey.com/download/ahk-install.exe
3. Install it via running 'AutoHotkey_1.1.37.01_setup.exe' executable
4. Run the 'MoveWindow.ahk' script

```ahk
; This script moves the active window to the left-hand corner of the screen
; when you press Win+Alt+L+K

#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

; Hotkey: Win+Alt+L+K
#!l::
    WinGet, active_id, ID, A ; Get the active window ID
    WinMove, ahk_id %active_id%, , 0, 0 ; Move the window to the top-left corner
return
```

5. Run BTD6 game and setup the screen size 800 x 600
6. Press the top bar of the BTD6 window to make it active one
7. Press Win+Alt+L+K (The window should be placed in the left upper corner)
8. Before running script make sure you have unlocked and selected 'Sauda' as a hero and have CHIMPS mode unlocked for 'Dark Castle' map 
9. Run the script and enjoy rewards
