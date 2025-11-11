import keyboard

enabled = True

def toggle():
    global enabled
    enabled = not enabled
    print("Режим:", "ON" if enabled else "OFF")

def copy_action():
    if enabled:
        keyboard.send("ctrl+c")

def paste_action():
    if enabled:
        keyboard.send("ctrl+v")

keyboard.add_hotkey("c", copy_action, suppress=True, trigger_on_release=True)
keyboard.add_hotkey("v", paste_action, suppress=True, trigger_on_release=True)
keyboard.add_hotkey("f12", toggle)

print("C/V → копирование/вставка (режим ON)")
print("F12 → включить/выключить")
print("ESC → выйти")

keyboard.wait("esc")
