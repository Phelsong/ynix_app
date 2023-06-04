"""SplashScreen"""
# libs
import os
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

# local imports
from .attacker_settings_form import AttackerInput

# =============================================================================
Builder.load_file(f"{os.getcwd()}\\pages\\sim_settings\\sim_settings_style.kv")


class SimSettingsScreen(Screen):
    """Sim Settings Page"""

    def __init__(self, **kwargs):
        super(SimSettingsScreen, self).__init__(**kwargs)
        # --
        self.form = AttackerInput(
            columns=1,
            rows=24,
            padding=20,
            size_hint=(0.8, 0.2),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            width=500,
            spacing=[30, 30],
        )
        self.add_widget(self.form)
        # --


# ------------------
