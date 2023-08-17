import os
from kivy.uix.button import Button
from kivy.uix.label import Label

# from kivy.uix.
from kivy.uix.stacklayout import StackLayout
from typing import Self
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

# local imports

# =============================================================================


class WikiScreen(Screen):
    """Splash Page"""

    # Builder.load_file(f"{os.getcwd()}/kv/wiki.kv")
    layout = StackLayout(orientation="lr-tb", spacing=[10, 10])
    title = Label(text="Test Wiki Page", font_size="18sp")
    button = Button(
        text="Click Me",
        size_hint=[0.2, 0.1],
        pos_hint={"center_x": 0.5, "center_y": 0.3},
    )

    def __init__(self, **kwargs):
        super(WikiScreen, self).__init__(**kwargs)

        self.add_widget(self.layout)
        self.add_widget(widget=self.title)
        self.add_widget(widget=self.button)
