import pyautogui
import time
import Quartz.CoreGraphics as CG
from pynput import keyboard

origin_x, origin_y = 323, 693  # 手写栏的起始坐标
size = 5
pause = False  # 初始化暂停状态


# 键盘事件处理函数
def on_press(key):
    global pause
    try:
        # 检查按下的键是否是等号键
        if key.char == '=':
            pause = not pause
            if pause:
                print("Paused")
            else:
                print("Resumed")
    except AttributeError:
        pass


# 启动键盘监听
listener = keyboard.Listener(on_press=on_press)
listener.start()


def repeat_function():
    One(origin_x, origin_y, size)


def main_loop():
    total_time = 13  # 每个循环的持续时间，单位为秒
    start_time = time.time()

    while time.time() - start_time < total_time:
        if not pause:  # 只有当不暂停时才执行
            repeat_function()
            time.sleep(0.01)  # 每0.1秒执行一次
        else:
            time.sleep(0.2)  # 如果暂停，也保持一定的间隔

    # 点击一系列按钮
    pyautogui.click(333, 483)  # “开心收下”按钮
    time.sleep(0.3)
    pyautogui.click(433, 945)  # “继续”按钮
    time.sleep(1.0)
    pyautogui.click(326, 818)  # “继续PK”按钮
    time.sleep(11)  # 等待下一轮的开始


def mouse_event(type, posx, posy):
    event = CG.CGEventCreateMouseEvent(None, type, (posx, posy), CG.kCGMouseButtonLeft)
    CG.CGEventPost(CG.kCGHIDEventTap, event)


def mouse_click_down(posx, posy):
    mouse_event(CG.kCGEventLeftMouseDown, posx, posy)


def mouse_click_up(posx, posy):
    mouse_event(CG.kCGEventLeftMouseUp, posx, posy)


def mouse_drag(posx, posy):
    mouse_event(CG.kCGEventLeftMouseDragged, posx, posy)


def One(origin_x, origin_y, size):
    # 按下鼠标
    mouse_click_down(origin_x, origin_y)
    time.sleep(0.02)
    mouse_drag(origin_x, origin_y + size)
    time.sleep(0.02)
    mouse_click_up(origin_x, origin_y + size)


# 主程序无限循环
while True:
    main_loop()  # 执行一个循环