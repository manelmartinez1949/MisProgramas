import kivy
##kivy.require('2.3.0')

from kivy.config import Config


Config.set('graphics', 'width', '375')
Config.set('graphics', 'height', '665')
from kivymd.app import MDApp

from MDApp.screens.menuscreen.menuscreen import MenuScreen 
from MDapp.screens.gamecreen.gamescreen import MenuScreen 

    
class MainApp(MDApp):
        def build(self):
            title = 'Hola, tíos'

            def on_start(self):
                self.current = 'menu_screen'
        

  
if __name__=='_main_':
          MainApp().run() 

