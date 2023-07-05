from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button


class CustomTabbedPanelHeader(TabbedPanelHeader):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            screen_manager = self.parent.parent.parent.parent
            screen_name = self.text
            screen = screen_manager.get_screen(screen_name)
            screen_manager.current = screen_name
        return super().on_touch_down(touch)


class TabbedPanelApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        screen_manager = ScreenManager()

        screen1 = Screen(name='Aba 1')
        layout1 = BoxLayout(orientation='vertical')
        button1 = Button(text='Botão 1')
        layout1.add_widget(button1)
        screen1.add_widget(layout1)
        screen_manager.add_widget(screen1)

        screen2 = Screen(name='Aba 2')
        layout2 = BoxLayout(orientation='vertical')
        button2 = Button(text='Botão 2')
        button3 = Button(text='Botão 3')
        layout2.add_widget(button2)
        layout2.add_widget(button3)
        screen2.add_widget(layout2)
        screen_manager.add_widget(screen2)

        screen3 = Screen(name='Aba 3')
        layout3 = BoxLayout(orientation='vertical')
        button4 = Button(text='Botão 4')
        button5 = Button(text='Botão 5')
        button6 = Button(text='Botão 6')
        layout3.add_widget(button4)
        layout3.add_widget(button5)
        layout3.add_widget(button6)
        screen3.add_widget(layout3)
        screen_manager.add_widget(screen3)

        tab_panel = TabbedPanel(do_default_tab=False)
        tab_panel.header_cls = CustomTabbedPanelHeader
        tab_panel.add_widget(TabbedPanelHeader(text='Aba 1', content=layout1))
        tab_panel.add_widget(TabbedPanelHeader(text='Aba 2', content=layout2))
        tab_panel.add_widget(TabbedPanelHeader(text='Aba 3', content=layout3))

        layout.add_widget(tab_panel)
        layout.add_widget(screen_manager)

        return layout


if __name__ == '__main__':
    TabbedPanelApp().run()
