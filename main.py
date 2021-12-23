from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.tabbedpanel import TabbedPanel

Builder.load_file("tab.kv")

class Tabs(TabbedPanel):
    pass

class MyApp(App):
    def build(self):
        return Tabs()


if __name__ == "__main__":
    MyApp().run()
