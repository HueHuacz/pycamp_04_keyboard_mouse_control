from pynput import keyboard

controller = keyboard.Controller()
controller.press(keyboard.Key.cmd_l)
controller.release(keyboard.Key.cmd_l)
