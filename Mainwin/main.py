from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager

Builder.load_string("""
<Main>
    FloatLayout:
        Image:
            source:"bg.jpg"
            
        Button:
            text:"Login"                 
            size_hint: .1,.1
            pos: root.width /2 - 50, root.height / 2  
            on_press: root.manager.current = "login"
                
        
        Button:
            text:"Register"                 
            size_hint: .1,.1   
            pos: 350,200
            on_press: root.manager.current = "register"
        
        Button:
            text:"Settings"                 
            size_hint: .1,.1   
            pos: 350,100
            on_press: root.manager.current = "settings"     
""")

class Main(Screen):
    pass

class Login(Screen):
    pass

class Register(Screen):
    pass

class Settings(Screen):
    pass

class LoginApp(App):
    def build(self):
        sm = ScreenManager()
        
        sm.add_widget(Main(name="main"))
        sm.add_widget(Login(name="login"))
        sm.add_widget(Register(name="register"))
        sm.add_widget(Settings(name="settings"))
        return sm


LoginApp().run()