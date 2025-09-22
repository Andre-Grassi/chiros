from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

kv_string = '''
<Paint>:
    Button:
        text: 'clear'
        on_release: 
            # root.cleaner()
            app.root.erase()

<MyWidget>:
    canvas:
        Color:
            rgb: 0.1, 0.6, 0.3
        Ellipse:
            size: self.size     
            pos: self.pos

        Color:
            rgb: 0.6, 0.2, 0.1
        Ellipse:
            size: self.size     
            pos: self.center

<Background>:
    MyWidget:
        id: mywidget

    Paint:
        id: btn
'''

Builder.load_string(kv_string)


class Paint(Widget):

    def cleaner(self, *args):
        self.canvas.clear()
        print('Cleared')


class MyWidget(Widget):
    pass


class Background(BoxLayout):

    def erase(self):
        self.ids.mywidget.canvas.clear()


class TestApp(App):
    title = "Kivy Widget's canvas.clear() Demo"

    def build(self):
        return Background()


if __name__ == '__main__':
    TestApp().run()