from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.app import App

import random

"""
{
    "d2" : DiceButton(2)
}

class DiceButton{
    
    Random rand_seed

    Button increase;
    Button decrease;
    Button dice;
    
    int dice_to_roll;
    int diceSize;
    
    
    void increase(){
        dice_to_roll++;
    }
    
    void decrease(){
        if(dice_to_roll>0){
            dice_to_roll--;
        }
    }
    
    String DoRoll(){
        
        roll_result = []
        sum = 0

        for(dice in range(dice_to_roll)){
            dice_result = random.rand(dice_size)
            roll_result.append(dice_result)
            sum += roll_result
        }
    
        f"Result : {sum} = {dice_to_roll}d{dice_size} {roll_result}
    
    }
}


"""


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
        print(str(self.amount_of_dice[dice_type][0]) + dice_type + "'s have been rolled")
        total = 0
        for i in range(self.amount_of_dice[dice_type][0]):
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
