import numpy as np

from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy_garden.graph import Graph, LinePlot
from kivy.clock import Clock
from plyer import accelerometer
from plyer import gravity

from kivy.lang import Builder
Builder.load_file("app2.kv")

class app2(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.numbers = []
        self.time_list = []
        self.time_counter = 0
        self.time_step = 0.01
        self.max_plot = 5
        self.min_plot = 0
        self.ymax_plot = 2
        self.ymin_plot = -2
        self.graph = None
        self.plot = None
        self.start_function = None
        self.sensorEnabled= False
        self.acc= np.array([0, 0, 0])
        self.grav= np.array([0, 0, 0])
        self.lineal= np.array([0, 0, 0])

        self.start_plot()

    def start_plot(self):
        self.graph = Graph(xmin = self.min_plot, xmax = self.max_plot, ymin = self.ymin_plot, ymax = self.ymax_plot, border_color = [1,1,1,1], x_grid = True,
                            y_grid = True, draw_border = True, x_grid_label = True, y_grid_label = True,)
        self.graph.background_color = 0,0,0,1
        self.ids.box.add_widget(self.graph)
        self.plot = LinePlot(line_width = 1, color = [1,1,1,1])
        self.graph.add_plot(self.plot)
    
    def start(self):
        self.ids.start_button.state = 'down'
        self.ids.start_button.disabled = True
        self.start_function = Clock.schedule_interval(self.update_label, self.time_step)

    def stop(self):
        if(self.start_function):
            self.start_function.cancel()
            self.ids.start_button.state = 'normal'
            self.ids.start_button.disabled = False

    def update_label(self, *args):
        self.numbers.append(self.read_accelerometer)
        self.time_list.append(self.time_counter)
        self.time_counter += self.time_step

        if(len(self.numbers)*self.time_step > self.max_plot):
            self.reset_plot()

        self.plot.points = [(self.time_list[i], self.numbers[i]) for i in range(len(self.numbers))]

    def clear_plot(self):
        self.ids.box.clear_widgets()
        self.start_plot()
        self.reset_plot()

    def reset_plot(self):
        self.numbers = []
        self.time_counter = 0
        self.time_list = []

    def read_accelerometer(self, dt):
        self.acc= np.asarray(accelerometer.acceleration)
        self.grav= np.asarray(gravity.gravity)
        test= self.acc[0]- self.grav[0] #THIS LINE CRASHES THE APP!!
        self.root.ids['a_x'].text= f"{str(self.acc)}"
        self.root.ids['a_y'].text= f"{str(type(self.acc))}"
        self.root.ids['a_z'].text= " "
        #self.root.ids['g_x'].text= " "
        #self.root.ids['g_y'].text= " "
        self.root.ids['g_z'].text=f"{self.acc- self.grav}"
        # return np.random.uniform(self.ymin_plot, self.ymax_plot)

    def begin_read(self):
        if not self.sensorEnabled:
            accelerometer.enable()
            gravity.enable()
            Clock.schedule_interval(self.leer_accel, 1/100)
            self.sensorEnabled= True
        else:
            accelerometer.disable()
            Clock.unschedule(self.leer_accel)
            self.sensorEnabled= False              
    
class MainApp(App):
    def build(self):
        return app2()
    
if __name__ == '__main__':
    MainApp().run()


        