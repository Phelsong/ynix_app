"""Login Page"""
# libs

# from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen

# local imports


# =================================================================


class LoginScreen(Screen):
    """Login"""

    # Builder.load_file(f"{os.getcwd()}/kv/login_screen.kv")
    layout = GridLayout(
        cols=1,
        col_default_width="100sp",
        rows=6,
        row_default_height="100sp",
        padding=120,
        spacing=8,
    )
    user_name_label = Label(
        size_hint=(0.1, 0.1),
        text="User Name",
        pos_hint={"center_x": 0.5, "center_y": 0.7},
    )

    user_input = TextInput(
        multiline=False,
        size_hint=(0.3, 0.1),
        pos_hint={"center_x": 0.5, "center_y": 0.6},
    )

    password_label = Label(
        text="Password",
        size_hint=(0.1, 0.1),
        pos_hint={"center_x": 0.5, "center_y": 0.5},
    )

    password_input = TextInput(
        size_hint=(0.3, 0.1),
        multiline=False,
        pos_hint={"center_x": 0.5, "center_y": 0.4},
    )

    login_button = Button(
        size_hint=(0.2, 0.1),
        text="Login",
        pos_hint={"center_x": 0.5, "center_y": 0.2},
    )

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        print(self.children)
        self.add_widget(self.layout)
        self.add_widget(self.user_name_label)
        self.add_widget(self.user_input)
        self.add_widget(self.password_label)
        self.add_widget(self.password_input)
        self.add_widget(self.login_button)

        def handle_click(self) -> None:
            print(self.parent.user_input.text)
            print(self.parent.password_input.text)
            print(self.parent.children)

        self.login_button.bind(on_release=handle_click)
