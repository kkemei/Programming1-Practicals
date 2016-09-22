from kivy.app import App
from kivy.uix.button import Button
import sys


class CheckSetupApp(App):

    def build(self):
        return Button(text='hello world!')


if __name__ == '__main__':
    # In PyCharm, right-click here and choose 'Run check_setup'
    print("Python version information:", sys.version)
    CheckSetupApp().run()







BoxLayout:
    orientation: 'horizontal'
    TextInput:
        id: input_number
        text: '7'
        font_size: 48
        multiline: True
    Button:
        text: 'Square'
        # the following line specifies the function in the app class to call when the button is pressed
        on_press: app.handle_calculate(int(input_number.text))
    Label:
        id: output_label
        font_size: 48
        color: (1, 0, 1, 1)
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Enter a number and press "Square"'
            color: (1, 1, 0, 1)
            id: output2_label