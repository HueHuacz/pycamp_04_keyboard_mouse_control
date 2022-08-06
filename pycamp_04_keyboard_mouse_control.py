""" Skrypt przejmujący kontrole nad myszką i klawiaturą """

from pynput import mouse, keyboard
from json import load
from time import sleep

class Config:
    pass

class Klikacz:
    def __init__(self):
        self.mouse = mouse.Controller()
        self.key = keyboard.Controller()
        # with open(config_file) as config:
        #     self.config = load(config)

    def _open_app(self):
        self.key.tap(keyboard.Key.cmd_l)
        sleep(0.5)
        self.key.type('chrome')
        sleep(0.5)
        self.key.tap(keyboard.Key.enter)
        sleep(0.5)
        with self.key.pressed(keyboard.Key.ctrl_l):
            self.key.tap('t')
        sleep(0.5)

    def _open_yt_site(self):
        self.key.type('youtube.pl')
        sleep(0.5)
        self.key.tap(keyboard.Key.enter)

    def _insert_text(self):
        pass

    def _press_enter(self):
        pass

    def _open_yt_site(self):
        pass

    def _open_recent_video(self):
        pass

    def open_recent_yt_video(self):
        self._open_app()
        sleep(1)
        self._open_yt_site()


if __name__ == '__main__':
    controller = Klikacz()
    controller.open_recent_yt_video()
