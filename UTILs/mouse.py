# 마우스를 클릭한 좌표를 저장
# 저장하한 좌표를 마우스로 100번 클릭하는 프로그램

import pyautogui
import time
from pynput import mouse
AAA = "AAA"

# 마우스 좌표를 저장할 리스트

mouse_list = []
count = 5

# 마우스 좌표를 저장하는 함수

def on_click(x, y, button, pressed):
    if pressed:
        print("마우스 클릭 좌표를 저장합니다.")
        print('Button: %s, Position: (%s, %s), Pressed: %s ' %(button, x, y, pressed))
        mouse_list.append((x, y))
    if len(mouse_list) == 1:
        return False


with mouse.Listener(
    on_click=on_click) as listener:
    listener.join()

print(mouse_list)

# 마우스 좌표를 저장한 리스트를 이용하여 마우스를 클릭하는 함수

def click_mouse():
    global count
    while True:
        pyautogui.click(mouse_list[0][0], mouse_list[0][1])
        count = count - 1
        print(count)
        time.sleep(10)
        if count == 0:
            print("끝!!!!")
            break

click_mouse()






      
