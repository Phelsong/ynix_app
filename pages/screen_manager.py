"""Screen Manager for Full Pages"""

# kivy
from kivy.uix.screenmanager import ScreenManager, ShaderTransition

# imports
from pages.splash_screen import SplashScreen
from pages.login_screen import LoginScreen
from pages.sim_settings_screen import SimSettingsScreen
from pages.wiki_screen import WikiScreen


# =================================================================

screen_manager = ScreenManager()
screen_manager.add_widget(SplashScreen(name="SplashScreen"))
screen_manager.add_widget(LoginScreen(name="LoginScreen"))
screen_manager.add_widget(SimSettingsScreen(name="SimSettingsScreen"))
screen_manager.add_widget(WikiScreen(name="WikiScreen"))


def change_screen(instance, value: str = "SplashScreen") -> None:
    screen_manager.current = value
