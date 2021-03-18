from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label


def error(flag):
    content = BoxLayout(orientation='vertical')
    if flag == 1:
        message_label = Label(text="Connection couldn't be established")
    if flag == 2:
        message_label = Label(text="Subject is empty")
    if flag == 3:
        message_label = Label(text="Body is empty")
    dismiss_button = Button(text='OK')
    content.add_widget(message_label)
    content.add_widget(dismiss_button)
    popup = Popup(title='Error', content=content, size_hint=(0.3, 0.25))
    dismiss_button.bind(on_press=popup.dismiss)
    popup.open()


class UI(FloatLayout):
    def process_input(self):
        self.ids['output'].text = "User does not exist"


class ConversionApp(App):
    def build(self):
        return UI()


if __name__ == '__main__':
    ConversionApp().run()
