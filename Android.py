## kivy para Android

import kivy
from kivy.app import App
from kivy .uix.label import Label                                   
class MiApp(App):
    def build(self):
        return Label(text=" Python para el móvil")
if __name__ == "__main__":
    MiApp().run()
