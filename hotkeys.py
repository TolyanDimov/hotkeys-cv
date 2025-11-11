import time
import keyboard

def copy_action():
    keyboard.press('ctrl')
    keyboard.press('c')
    time.sleep(0.03)
    keyboard.release('c')
    keyboard.release('ctrl')

    time.sleep(0.02)
    keyboard.press_and_release('ctrl+insert')

def paste_action():
    keyboard.press('ctrl')
    keyboard.press('v')
    time.sleep(0.03)
    keyboard.release('v')
    keyboard.release('ctrl')

    time.sleep(0.02)
    keyboard.press_and_release('shift+insert')

keyboard.add_hotkey('c', copy_action, suppress=True, trigger_on_release=True)
keyboard.add_hotkey('v', paste_action, suppress=True, trigger_on_release=True)

print('C → Ctrl+C | V → Ctrl+V (символы не печатаются). ESC — выход.')
keyboard.wait('esc')