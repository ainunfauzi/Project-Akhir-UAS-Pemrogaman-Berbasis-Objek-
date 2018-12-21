#https://kivy.org/doc/stable/api-kivy.uix.colorpicker.html
#https://stackoverflow.com/questions/47389711/get-value-of-selected-checkbox-in-kivy
from kivy.uix.screenmanager import Screen,ScreenManager,WipeTransition
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty

Window.size = (300,300)
#Load Data from txt

class UserGroup(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    email = ObjectProperty(None)

    def insert_data(self):
        print('username:\t\t:',self.username.text,'\npassword:\t\t:',self.password.text,'\nemail:\t\t\t:',self.email.text)

kv_str = Builder.load_string('''
#:import os os
''')

class Login(App):

    def build(self):
        self.root = Builder.load_file('test1.kv')
        return self.root


if __name__ == '__main__':
    Login().run()
