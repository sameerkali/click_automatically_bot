import pyautogui
import time
import keyboard

while True:
    if keyboard.is_pressed('s'):
        x, y = pyautogui.position()
        print(f"Mouse Position: ({x}, {y})")
        break

button_x = x
button_y = y

while True:
    pyautogui.moveTo(button_x, button_y, duration=0.3)
    pyautogui.click()
    # print(f"Clicked at ({button_x}, {button_y})")
    time.sleep(3)