from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from plyer import accelerometer
import matplotlib.pyplot as plt


class CustomTabbedPanelHeader(TabbedPanelHeader):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            screen_manager = self.parent.parent.parent.parent
            screen_name = self.text
            screen = screen_manager.get_screen(screen_name)
            screen_manager.current = screen_name
        return super().on_touch_down(touch)


class Screen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.button_start = Button(text='Iniciar', on_press=self.start_accelerometer)
        self.button_stop = Button(text='Parar', on_press=self.stop_accelerometer, disabled=True)
        self.layout.add_widget(self.button_start)
        self.layout.add_widget(self.button_stop)
        self.add_widget(self.layout)

        self.x_data = []
        self.y_data = []
        self.z_data = []

    def start_accelerometer(self, *args):
        self.button_start.disabled = True
        self.button_stop.disabled = False
        accelerometer.enable()
        accelerometer.set_update_interval(1 / 30)  # Taxa de atualização de 30 vezes por segundo
        accelerometer.bind(on_acceleration=self.on_acceleration)

    def stop_accelerometer(self, *args):
        self.button_start.disabled = False
        self.button_stop.disabled = True
        accelerometer.disable()

    def on_acceleration(self, instance, acceleration):
        x, y, z = acceleration
        self.x_data.append(x)
        self.y_data.append(y)
        self.z_data.append(z)
        self.plot_graph()

    def plot_graph(self):
        plt.figure(figsize=(8, 6))
        plt.plot(self.x_data, label='Força X')
        plt.plot(self.y_data, label='Força Y')
        plt.plot(self.z_data, label='Força Z')
        plt.xlabel('Tempo (amostras)')
        plt.ylabel('Força')
        plt.legend()
        plt.title('Gráfico de Forças do Acelerômetro')
        plt.show()


class Screen2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.button = Button(text='Aba 2')
        self.layout.add_widget(self.button)
        self.add_widget(self.layout)


class Screen3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.button = Button(text='Aba 3')
        self.layout.add_widget(self.button)
        self.add_widget(self.layout)


class TabbedPanelApp(App):
    def build(self):
        tab_panel = TabbedPanel(do_default_tab=False)
        tab_panel.header_cls = CustomTabbedPanelHeader
        tab_panel.add_widget(TabbedPanelHeader(text='Aba 1', content=Screen1()))
        tab_panel.add_widget(TabbedPanelHeader(text='Aba 2', content=Screen2()))
        tab_panel.add_widget(TabbedPanelHeader(text='Aba 3', content=Screen3()))

        return tab_panel