import os
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

# local imports

# =============================================================================
Builder.load_file(f"{os.getcwd()}\\pages\\wiki\\wiki.kv")


class WikiScreen(Screen):
    """Splash Page"""
