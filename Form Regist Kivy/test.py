#https://kivy.org/doc/stable/api-kivy.uix.colorpicker.html
#https://stackoverflow.com/questions/47389711/get-value-of-selected-checkbox-in-kivy
from kivy.uix.screenmanager import Screen,ScreenManager,WipeTransition
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty

kv_str = Builder.load_string('''
#:import os os
''')
Window.size = (600,700)

class UserGroup(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    email = ObjectProperty(None)
    alamat = ObjectProperty(None)
    male = ObjectProperty(None)
    female = ObjectProperty(None)
    age = ObjectProperty(None)

    def insert_data(self):
        if self.male.active:
            print('Male')
        elif self.female.active:
            print('Female')
        else:
            print('No gender selected')
        print('username:\t\t:',self.username.text,'\npassword:\t\t:',self.password.text,'\nemail:\t\t\t:'
              ,self.email.text,'\nalamat:\t\t\t:',self.alamat.text,'\nage:\t\t\t:',self.age.text)



class Register(App):

    def build(self):
        self.root = Builder.load_file('test.kv')
        return self.root

if __name__ == '__main__':
    Register().run()
