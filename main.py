""" Application File """
# libs
import os
from asyncio import run

# kivy imports
from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, ShaderTransition
from kivy.lang import Builder
from kivy.properties import ObjectProperty


# local imports
from pages.screen_manager import screen_manager, change_screen

# =============================================================================
CATALOG_ROOT: str = os.path.dirname(__file__)


class AppShell(GridLayout):
    """Root Widget"""

    columns: int = 2
    rows: int = 1

    # -----------
    Builder.load_file(f"{os.getcwd()}/kv/app_shell.kv")

    def __init__(self, **kwargs) -> None:
        super(AppShell, self).__init__(**kwargs)
        #
        self.add_widget(screen_manager)
        self.ids.selector.values = [screen.name for screen in screen_manager.screens]
        self.ids.selector.bind(text=change_screen)


# =============================================================================


class ProjectYnix(App):
    def build(self) -> AppShell:
        self.config = Config
        return AppShell()

    def on_pause(self) -> bool:
        return True


# =============================================================================

if __name__ == "__main__":
    run(ProjectYnix().async_run())
