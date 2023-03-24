#Import required modules
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.graphics import Color, Line

#Class "MyButton" which inhherits from "ToggleButton"
class MyButton(ToggleButton):
    def _do_press(self):
        #We can only press the button if the state is normal
        if self.state == "normal":
            ToggleButtonBehavior._do_press(self)


#Class "PaintApp" which inherits from "App"
class PaintApp(App):
    def build(self):
        self.canvas_widget = CanvasWidget()
        self.canvas_widget.set_color(get_color_from_hex("#2980b9"))
        return self.canvas_widget

#Class "CanvasWidget" which inherits from "Widget"
class CanvasWidget(Widget):
    line_width = 2
    def set_color(self, new_color):
        self.last_color = new_color
        self.canvas.add(Color(*new_color))
    def on_touch_down(self, touch):
        if Widget.on_touch_down(self, touch):
            return
        with self.canvas:
            #Line(circle = (touch.x, touch.y, 25 ), width = 4)
            touch.ud["current_line"] = Line(points = (touch.x, touch.y), width = self.line_width)
    def on_touch_move(self, touch):
        if "current_line" in touch.ud:
            touch.ud["current_line"].points += (touch.x, touch.y)
    def clear_canvas(self):
        saved = self.children[:]
        self.clear_widgets()
        self.canvas.clear()
        for widget in saved:
            self.add_widget(widget)
        self.set_color(self.last_color)
    def set_line_width(self, line_width = "normal"):
        self.line_width = {"Thin":1, "Normal":2, "Thick":4}[line_width]

#Main
if __name__ == "__main__":
    Window.size = (200, 600)
    Window.clearcolor = get_color_from_hex('#ffffff')
    PaintApp().run()