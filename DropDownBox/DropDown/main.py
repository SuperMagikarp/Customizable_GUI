import kivy
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp


"""creating a dropdown object"""
dropdown = DropDown()
list_of_environments = ["Tavern", "Dungeon", "Swamp"]
for i in list_of_environments:

    """makes a button widget with a height of 44 and 
    sets it text to current iterator.size_hint-y set to None so dropdown can choose its own height"""
    btn = Button(text=i, size_hint_y=None, height=44)

    """binds what the button does IE. on release it sets the
     dropdown boxes text to whatever button was pressed"""
    btn.bind(on_release=lambda button: dropdown.select(btn.text))

    """adding each button to the dropdown"""
    dropdown.add_widget(btn)

main_button = Button(text=" Environments ", size_hint=(None, None))

"""when the mainbutton is pressed it will open the dropdown"""
main_button.bind(on_select=dropdown.open)

"""Changes the mainbutton's text to whatever button in the dropdown was pressed"""
dropdown.bind(on_select=lambda instance, x: setattr(main_button, 'text', x))

runTouchApp(main_button)




