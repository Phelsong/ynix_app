""" Application File """
# libs
import os
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, ShaderTransition
from kivy.lang import Builder
from pages.sim_settings.sim_settings_screen import SimSettingsScreen

# local imports
from pages.splash.splash_screen import SplashScreen
from pages.login.login_screen import LoginScreen
from pages.sim_settings.sim_settings_screen import SimSettingsScreen

# =============================================================================

Builder.load_file(f"{os.getcwd()}\\app_shell.kv")


class ProjectYnix(App):
    """Application"""

    def build(self):
        screen_man = ScreenManager()
        screen_man.add_widget(SplashScreen(name="SplashScreen"))
        screen_man.add_widget(LoginScreen(name="LoginScreen"))
        screen_man.add_widget(SimSettingsScreen(name="SimSettingsScreen"))
        return screen_man


if __name__ == "__main__":
    ProjectYnix().run()
