import kivy
import wolframalpha as wa

# base Class of your App inherits from the App class.
# app: always refers to the instance of your application
from kivy.app import App

# This restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require('2.0.0')

from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

# Setting size to resizable
Config.set('graphics', 'resizable', 1)
Config.set('graphics', 'minimum_height', '600')
# We don`t set minimum_width for additional bug

# WolframAlpha Client object
api_key = 'WY8PAY-HGU2JQHEXK'
client = wa.Client(api_key)
# Query parameters
params = (
    ('assumption', '*C.pi-_*NamedConstant-'),
    ('assumption', 'DateOrder_**Day.Month.Year--'),
)


# Creating Layout class
class CalcGridLayout(GridLayout):

    # Function called when equals is pressed
    def calculate(self, calculation):
        if calculation:
            try:
                # Solve formula and display it in entry
                # which is pointed at by display
                self.display.text = str(eval(calculation))
            except (SyntaxError, NameError, TypeError): # ZeroDivisionError - Another bug
                result = client.query(input=calculation, params=params)
                try:
                    self.display.text = next(result.results).text
                except StopIteration:
                    self.display.text = "Error"


# Building App class
class CalculatorApp(App):

    def build(self):
        return CalcGridLayout()

# Creating object and running it
calcApp = CalculatorApp()
calcApp.run()
