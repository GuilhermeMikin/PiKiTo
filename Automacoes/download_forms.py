import pyautogui
from time import sleep

pyautogui.PAUSE = 3
pyautogui.hotkey('alt','tab')
i = 0
for i in range(100):
    print(f'Baixando foto {i}...')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    sleep(6)
    pyautogui.write(f'foto-{i}')
    pyautogui.press('enter')
    sleep(10)
    i += 1