"""SplashScreen"""
# libs
import os

# kivy imports
# from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen

# local imports

# =============================================================================


class SplashScreen(Screen):
    """Splash Page"""

    # Builder.load_file(f"{os.getcwd()}/kv/splash_screen.kv")
    layout = GridLayout(cols=3, rows=5, padding="10sp")
    title1 = Label(
        text="Welcome to ~Project Ynix~",
        font_size="30sp",
        pos_hint={"center_x": 0.5, "center_y": 0.9},
    )

    def __init__(self, **kwargs):
        super(SplashScreen, self).__init__(**kwargs)
        self.add_widget(self.layout)
        self.layout.add_widget(self.title1)
