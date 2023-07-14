from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class AttackerInput(GridLayout):
    def __init__(self, **kwargs):
        super(AttackerInput, self).__init__(**kwargs)
        # --
        self.class_id = TextInput(
            text="class",
            size_hint=(0.1, 0.05),
        )
        self.add_widget(self.class_id, index=1)
        # --
        self.ap = TextInput(
            text="ap",
            size_hint=(0.1, 0.05),
        )
        self.add_widget(self.ap, index=2)
        # --
        self.aap = TextInput(
            text="aap",
            size_hint=(0.1, 0.05),
        )
        self.add_widget(self.aap, index=3)
        # --
        self.acc = TextInput()
        self.add_widget(self.acc, index=4)
        # --
        self.acc_rate = TextInput()
        self.add_widget(self.acc_rate, index=5)
        # --
        self.crit_rate = TextInput()
        self.add_widget(self.crit_rate, index=6)
        # --
        self.monster_ap = TextInput()
        self.add_widget(self.monster_ap, index=7)
        # --
        self.kama_damage = TextInput()
        self.add_widget(self.kama_damage, index=8)
        # --
        self.demi_damage = TextInput()
        self.add_widget(self.demi_damage, index=9)
        # --
        self.human_damage = TextInput()
        self.add_widget(self.human_damage, index=10)
        # --
        self.other_damage = TextInput()
        self.add_widget(self.other_damage, index=11)
        # --
        self.crit_damage = TextInput()
        self.add_widget(self.crit_damage, index=12)
        # --
        self.back_damage = TextInput()
        self.add_widget(self.back_damage, index=13)
        # --
        self.down_damage = TextInput()
        self.add_widget(self.down_damage, index=14)
        # --
        self.air_damage = TextInput()
        self.add_widget(self.air_damage, index=15)
        # --
        self.ap_combat_buffs = TextInput()
        self.add_widget(self.ap_combat_buffs, index=16)
        # --
        self.crit_combat_buffs = TextInput()
        self.add_widget(self.crit_combat_buffs, index=17)
        # --
        self.ap_debuffs = TextInput()
        self.add_widget(self.ap_debuffs, index=18)
        # --
        self.acc_combat_buffs = TextInput()
        self.add_widget(self.acc_combat_buffs, index=19)
        # --
        self.acc_debuffs = TextInput()
        self.add_widget(self.acc_debuffs, index=20)
        # --
        self.human_damage_debuffs = TextInput()
        self.add_widget(self.human_damage_debuffs, index=21)
        # --