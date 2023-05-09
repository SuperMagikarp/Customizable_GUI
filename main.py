from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.app import App

import random


class DiceButton:

    def __init__(self, dice_size):
        self.dice_to_roll = 1
        self.dice_size = dice_size

        self.increase_button = Button(text="+", size_hint_x=0.25)
        self.decrease_button = Button(text="-", size_hint_x=0.25)
        self.roll_button = Button(text=f"{self.dice_to_roll}d{self.dice_size}", size_hint_x=0.5)

        self.increase_button.bind(on_release=lambda x: self.do_increase())
        self.decrease_button.bind(on_release=lambda x: self.do_decrease())
        self.roll_button.bind(on_release=lambda x: self.do_roll())

    def update_label(self):
        self.roll_button.text = f"{self.dice_to_roll}d{self.dice_size}"

    def do_increase(self):
        self.dice_to_roll += 1
        self.update_label()

    def do_decrease(self):
        if self.dice_to_roll > 1:
            self.dice_to_roll -= 1
            self.update_label()

    def do_roll(self):
        roll_result_sum = 0
        dice_rolled_results = []

        for i in range(self.dice_to_roll):
            rolled_dice = (random.randrange(self.dice_size)) + 1
            dice_rolled_results.append(rolled_dice)
            roll_result_sum += rolled_dice

        # Send to Webhook
        print(f"Result : {roll_result_sum} = {self.dice_to_roll}d{self.dice_size} {dice_rolled_results}")


class MyApp(App):
    def build(self):
        dice_buttons = [
            DiceButton(2),
            DiceButton(4),
            DiceButton(6),
            DiceButton(8),
            DiceButton(10),
            DiceButton(12),
            DiceButton(20),
            DiceButton(100),
        ]

        grid = GridLayout(cols=3)  # [-] [dX] [+]

        for dice in dice_buttons:
            grid.add_widget(dice.decrease_button)
            grid.add_widget(dice.roll_button)
            grid.add_widget(dice.increase_button)

        return grid


if __name__ == "__main__":
    MyApp().run()
