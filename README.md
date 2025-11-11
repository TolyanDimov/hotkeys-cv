# HotKeysCV

A simple tool that intercepts **C** and **V** and replaces them with:
- C → Ctrl+C
- V → Ctrl+V

Normal typing of C and V is blocked:  
pressing them triggers copy/paste instead of printing characters.

## Installation (using .venv)
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run
```bash
python hotkeys-cv.py
```

## Build .exe
```bash
python -m PyInstaller --onefile --noconsole --name HotKeysCV hotkeys-cv.py
```

The compiled file will appear in `dist/`.

## Hotkeys
- C — copy (Ctrl+C)
- V — paste (Ctrl+V)
- F12 — toggle mode
- ESC — exit
