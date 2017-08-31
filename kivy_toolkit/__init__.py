from . import colors
from kivy.graphics import Color, Rectangle
from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


def update_rect(instance, value):
    instance.rect.size = instance.size
    instance.rect.pos = instance.pos


def layout_background(layout, color):
    with layout.canvas:
        layout._col = Color(*color)
        layout.rect = Rectangle(size=layout.size, pos=layout.pos)
    layout.bind(size=update_rect, pos=update_rect)


class ImageButton(ButtonBehavior, Image):
    def __init__(self, *, source="", **kwargs):
        super(ImageButton, self).__init__(**kwargs)
        self.source = source


class Menu(Screen):
    def __init__(self, *, title="", buttons=[], background=(), **kwargs):
        """
        buttons: nested list, secondary lists consist of string for button text
                 and button function

        """
        
        super(Menu, self).__init__(**kwargs)

        # Use a float layout for menu screens
        self.layout = FloatLayout()
        self.add_widget(self.layout)

        # Create a background canvas
        if background:
             layout_background(self.layout, background)
    
        # Create the title
        self.title = Label(text=title, size_hint=(1, 0.4),
                           pos_hint={'x': 0, 'y': 0.6})
        self.layout.add_widget(self.title)

        # Create the buttons
        self.buttonlist = []
        for i in buttons:
            y_pos = 0.5 - buttons.index(i) * 0.075
            self.buttonlist.append(Button(text=i[0], size_hint=(0.3, 0.07),
                                          pos_hint={'x': 0.35, 'y': y_pos},
                                          on_press=i[1]))
            self.layout.add_widget(self.buttonlist[-1])


class TopController(App):
    def __init__(self, *, return_value=None, **kwargs):
        super(TopController, self).__init__(**kwargs)
        self.return_value = return_value

    def build(self):
        return self.return_value()
