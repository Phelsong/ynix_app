"""SplashScreen"""
# libs
import os
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen

# local imports
from custom_widgets.attacker_settings_form import AttackerInput

# =============================================================================


class SimSettingsScreen(Screen):
    """Sim Settings Page"""

    Builder.load_file(f"{os.getcwd()}/kv/sim_settings_screen.kv")
    layout = GridLayout(rows=3, cols=3)
    title = Label(
        text="Sim Settings",
        size_hint=(0.8, 0.5),
        pos_hint={"center_x": 0.5, "center_y": 0.9},
    )
    submit_button = Button(
        text="Submit",
        size_hint=(0.2, 0.1),
        pos_hint={"center_x": 0.5, "center_y": 0.2},
    )

    def __init__(self, **kwargs) -> None:
        super(SimSettingsScreen, self).__init__(**kwargs)

        self.form = AttackerInput(
            cols=1,
            rows=24,
            padding="5sp",
            size_hint=(0.8, 0.5),
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            spacing=["30sp", "30sp"],
        )

        # ---------------]
        self.add_widget(self.layout)
        self.add_widget(self.title)
        self.add_widget(self.form)
        self.add_widget(self.submit_button)
        # ---------------]


# ------------------
