#!/usr/bin/env python3

import os
import time

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.image import Image


class LandingPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Window.bind(on_dropfile=self._on_file_drop)

    def camera_button(self):
        test_app.screen_manager.current = "Camera"

    def _on_file_drop(self, window, file_path):
        image = file_path.decode("utf-8")
        test_app.image = image
        test_app.upload_page.add_image()
        test_app.screen_manager.current = "Upload"


class UploadPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_image(self):
        self.add_widget(Image(source=test_app.image, size=self.size, pos=self.pos))


class CameraPage(BoxLayout):
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        image = "IMG_{}.png".format(timestr)
        camera.export_to_png(image)
        test_app.image = image
        test_app.screen_manager.current = "Upload"
        print("Captured")

    def land(self):
        test_app.screen_manager.current = "Landing"


class TestApp(App):

    image = ""

    def build(self):
        self.screen_manager = ScreenManager()
        self.landing_page = LandingPage()
        screen = Screen(name="Landing")
        screen.add_widget(self.landing_page)
        self.screen_manager.add_widget(screen)

        self.camera_page = CameraPage()
        screen = Screen(name="Camera")
        screen.add_widget(self.camera_page)
        self.screen_manager.add_widget(screen)

        self.upload_page = UploadPage()
        screen = Screen(name="Upload")
        screen.add_widget(self.upload_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == '__main__':
    test_app = TestApp()
    test_app.run()
