
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.gridlayout import GridLayout

"""creating a dropdown object"""
list_of_environments = ["Tavern", "Dungeon", "Swamp"]
list_of_dice = ["d2", "d4", "d6", "d8"]
layout = GridLayout(cols=2)


def dropdown_maker(listofbuttons):
    dropdown = DropDown()
    for i in range(len(listofbuttons)):
        """makes a button widget with a height of 44 and 
        sets it text to current iterator.size_hint-y set to None so dropdown can choose its own height"""
        btn = Button(text=listofbuttons[i], size_hint_y=None, height=44)

        """binds what the button does IE. on release it sets the
         dropdown boxes text to whatever button was pressed"""
        btn.bind(on_release=lambda button: dropdown.select(listofbuttons.index(button.text)))

        """adding each button to the dropdown"""
        dropdown.add_widget(btn)
    main_button = Button(text=" Environments ", size_hint=(None, None))

    """when the mainbutton is pressed it will open the dropdown"""
    main_button.bind(on_release=dropdown.open)

    """Changes the mainbutton's text to whatever button in the dropdown was pressed"""
    dropdown.bind(on_select=lambda instance, x: print(x))
    return main_button


main_button1 = dropdown_maker(list_of_environments)
main_button2 = dropdown_maker(list_of_dice)

layout.add_widget(main_button1)
layout.add_widget(main_button2)

runTouchApp(layout)
