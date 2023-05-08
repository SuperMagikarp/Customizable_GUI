from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.app import App


class MyApp(App):

    dictionary_of_envs = {"Forest": "Trees",
                          "River": "fish",
                          "Dungeon": "Skeleton",
                          "Market": "coins"}

    def use_the_stuff(self, environment):
        if environment == "Forest":
            print(f"there are {self.dictionary_of_envs[environment]} here")
        elif environment == "Dungeon":
            print(f"there are {self.dictionary_of_envs[environment]} here")
        elif environment == "Market":
            print(f"there are {self.dictionary_of_envs[environment]} here")
        elif environment == "River":
            print(f"there are {self.dictionary_of_envs[environment]} here")

    def build(self):
        layout = GridLayout(cols=1)
        for i in self.dictionary_of_envs:
            btn = Button(text=i)
            layout.add_widget(btn)
            btn.bind(on_release=lambda x: self.use_the_stuff(x.text))
        return layout


if __name__ == "__main__":
    MyApp().run()
