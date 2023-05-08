from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
import random


class MyApp(App):
    dice_to_buttons = {}

    amount_of_dice = {
        "d2": [1, ""],
        "d4": [1, ""],
        "d6": [1, ""],
        "d8": [1, ""],
        "d10": [1, ""],
        "d12": [1, ""],
        "d20": [1, ""],
        "d100": [1, ""],
    }

    def increase_dice(self, button):
        self.amount_of_dice[self.dice_to_buttons[button]][0] += 1

    def decrease_dice(self, button):
        self.amount_of_dice[self.dice_to_buttons[button]][0] -= 1

    def roll_the_dice(self, dice_type):
        d = int(dice_type.split("d")[1])
        print(str(self.amount_of_dice[dice_type]) + dice_type + "'s have been rolled")
        total = 0
        for i in range(self.amount_of_dice[dice_type]):
            result = random.randint(1, d)
            total += result
        print("Result: " + str(total))

    def build(self):
        cols = 3
        grid = GridLayout(cols=cols)
        for j in self.amount_of_dice:
            for i in range(cols):
                if i == 0:
                    button = Button(text="-", size_hint_x=0.25)
                    button.bind(on_release=lambda x: self.decrease_dice(x))
                    self.dice_to_buttons[button] = j
                elif i == cols - 1:
                    button = Button(text="+", size_hint_x=0.25)
                    button.bind(on_release=lambda x: self.increase_dice(x))
                    self.dice_to_buttons[button] = j
                else:
                    button = Button(text=j, size_hint_x=0.5)
                    button.bind(on_release=lambda x: self.roll_the_dice(x.text))
                    self.amount_of_dice[j][1] = button
                grid.add_widget(button)
        return grid


if __name__ == "__main__":
    MyApp().run()
