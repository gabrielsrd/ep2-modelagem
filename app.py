from kivy.app import App
from kivy.uix.widget import Widget

grupo = [
    "Fernando Henrique Junqueira Muniz Barbi Silva (11795888)",
    "Integrante 1",
    "Integrante 2",
    "Integrante 3"
]

class Example(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def show_button(self):
        self.set_group()

    def set_group(self):
        texto = ""
        for i in grupo:
            texto += i + "\n"
        self.ids.label.text = texto

class MyApp(App):
    def build(self):
        return Example()

if __name__ == '__main__':
    MyApp().run()