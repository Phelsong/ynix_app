""" Application File """
# libs
import os
import kivy
from kivy.app import App
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


class AppShell(GridLayout):
    """Root Widget"""
    Builder.load_file(f"{os.getcwd()}\\app_shell.kv")
    screen_manager = ObjectProperty(ScreenManager())

    columns = 1
    rows = 2
    #

    def __init__(self, **kwargs) -> None:
        super(AppShell, self).__init__(**kwargs)
        # self.screen_manager.add_widget(SplashScreen(name="SplashScreen"))
        self.screen_manager.add_widget(LoginScreen(name="LoginScreen"))
        self.screen_manager.add_widget(SimSettingsScreen(name="SimSettingsScreen"))
        self.screen_manager.add_widget(WikiScreen(name="WikiScreen"))
        #
        self.ids.selector.values = [
            screen.name for screen in self.screen_manager.screens
        ]
        self.ids.selector.bind(text=self.change_screen)

    def change_screen(self, instance, value):
        self.screen_manager.current = "SplashScreen"


class ProjectYnix(App):
    def build(self):
        return AppShell()


if __name__ == "__main__":
    ProjectYnix().run()
