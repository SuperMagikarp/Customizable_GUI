import random

from discordwebhook import Discord
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class DiceButton:
    """Describes a dimension of dice (for e.g. a Dimension 20 dice [D20])
    whose number can be increased or decreased,
    and that can be rolled through calls to its inner, methods which are
    triggered by with the Object's respective buttons members.
    """

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
        """Changes the label on the main Dice button."""
        self.roll_button.text = f"{self.dice_to_roll}d{self.dice_size}"

    def do_increase(self):
        """Increase the number of dice to be rolled."""
        self.dice_to_roll += 1
        self.update_label()

    def do_decrease(self):
        """Decrease the number of dice to be rolled."""
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
        discord.post(content=f"Result : {roll_result_sum} = {self.dice_to_roll}d{self.dice_size} {dice_rolled_results}")


class DiceRoller(App):
    def build(self):
        """
        Initialises the GUI for the App.

        :return: (GridLayout) GUI of the Dice Roller App.
        """

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

        """
            [0: Button for Subtracting Dice | 1: Button for Rolling Dice | 2: Button for Adding Dice]
        """
        grid = GridLayout(cols=3)  # [-][dX][+]

        for dice in dice_buttons:
            grid.add_widget(dice.decrease_button)
            grid.add_widget(dice.roll_button)
            grid.add_widget(dice.increase_button)

        return grid


def get_webhook(web_hook_file):
    """Open the file containing the webhook and read the URL,
    which should be on a single line."""

    try:
        with open(web_hook_file) as f:
            return f.read()
    except FileNotFoundError:
        print(f"WARNING: The specified webhook file '{web_hook_file}' was not found.")


if __name__ == "__main__":

    web_hook_url = get_webhook("config/web_hook_url.txt")
    if not web_hook_url:
        print("""
            A web hook URL is needed to start this program.
            See README.md
            """
              )
        exit()

    discord = Discord(url=web_hook_url)  # Create the Webhook

    DiceRoller().run()  # Start the GUI
