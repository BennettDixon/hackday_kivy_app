"""Defines the ImageOCRApp class"""
from kivy.app import App

# Import widgets from kivy
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from .tools import verify_image, convert_image
from kivy.core.window import Window


class GetFilename(BoxLayout, Screen):
    """Defines the GetFileName class -> Screen for manually inputting image pathname"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_dropfile=self._on_file_drop)
    

    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    filename_write = StringProperty('')
    filepath = StringProperty('')
    
    def store_filename_write(self, *args):
        filename = self.ids['filename_text'].text
        if verify_image(filename) is False:
            return False
        json = convert_image(filename)
        results = 'insert backend results here'
        self.manager.get_screen('results').api_results = results
        self.manager.get_screen('results').source = filename
        return True
    
    def load(self, path, filename, *args):
        if len(filename) < 1:
            return False
        self.manager.get_screen('main').filepath = filename[0]
        if verify_image(filename[0]) is False:
            return False
        json = convert_image(filename[0])
        results = 'insert backend results here!'
        self.manager.get_screen('results').api_results = results
        self.manager.get_screen('results').source = filename[0]
        return True

    def _on_file_drop(self, window, filepath):
        image = filepath.decode('utf-8')
        self.manager.get_screen('main').filepath = image
        

class Results(Screen):
    api_results = StringProperty('')
    source = StringProperty('')

    def get_info(self):
        print(self.api_results)

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('frontend/imageocr.kv')

class ImageOCRApp(App):
    """Defines the ImageOCR Application Class"""
    def build(self):
        """This method is called when run() method is called"""
        return kv

if __name__ == '__main__':
    ImageOCRApp().run()
