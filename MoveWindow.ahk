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