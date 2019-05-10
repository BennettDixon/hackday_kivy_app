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


class GetFilename(BoxLayout, Screen):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    filename_write = StringProperty('')
    
    def store_filename_write(self, *args):
        filename = self.ids['filename_text'].text
        # TODO call backend here
        results = 'insert backend results here'
        self.manager.get_screen('results').api_results = results
        return True
        
class Results(Screen):
    api_results = StringProperty('')

    def get_info(self):
        print(self.api_results)

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('imageocr.kv')

class ImageOCRApp(App):
    """Defines the ImageOCR Application Class"""
    def build(self):
        """This method is called when run() method is called"""
        return kv

if __name__ == '__main__':
    ImageOCRApp().run()
