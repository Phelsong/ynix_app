"""SplashScreen"""
# libs
import os
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

# local imports

# =============================================================================
Builder.load_file(f"{os.getcwd()}\\pages\\sim_settings\\sim_settings_style.kv")


class SimSettingsScreen(Screen):
    """Sim Settings Page"""
