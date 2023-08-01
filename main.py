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
from pages.splash.splash_screen import SplashScreen
from pages.login.login_screen import LoginScreen
from pages.sim_settings.sim_settings_screen import SimSettingsScreen
from pages.wiki.wiki import WikiScreen

# =============================================================================
CATALOG_ROOT = os.path.dirname(__file__)

class AppShell(GridLayout):
    """Root Widget"""

    columns = 2
    rows = 1
    screen_manager = ScreenManager()
    screen_manager.add_widget(SplashScreen(name="SplashScreen"))
    screen_manager.add_widget(LoginScreen(name="LoginScreen"))
    screen_manager.add_widget(SimSettingsScreen(name="SimSettingsScreen"))
    screen_manager.add_widget(WikiScreen(name="WikiScreen"))
    # -----------
    Builder.load_file(f"{os.getcwd()}/app_shell.kv")

    def __init__(self, **kwargs) -> None:
        super(AppShell, self).__init__(**kwargs)
        #
        self.add_widget(self.screen_manager)
        self.ids.selector.values = [
            screen.name for screen in self.screen_manager.screens
        ]
        self.ids.selector.bind(text=self.change_screen)

    def change_screen(self, instance, value):
        self.screen_manager.current = value


class ProjectYnix(App):
    def build(self):
        self.config = Config
        return AppShell()

    def on_pause(self):
        return True


if __name__ == "__main__":
    run(ProjectYnix().async_run())
