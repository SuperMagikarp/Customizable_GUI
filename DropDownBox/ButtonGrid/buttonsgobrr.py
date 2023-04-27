from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.app import App


class MyApp(App):

    def build(self):
        list_of_environments = ["Tavern", "Dungeon", "Swamp"]
        layout = GridLayout()
        for i in list_of_environments:
            layout.add_widget(Button(text=i))
        return layout


if __name__ == "__main__":
    MyApp().run()
