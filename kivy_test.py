import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require('2.0.0')

class GameView(BoxLayout):

    def __init__(self):
        super(GameView, self).__init__()
class DavidApp(App):
    def build(self):
        return GameView()
    
davidApp = DavidApp()
davidApp.run()
    
