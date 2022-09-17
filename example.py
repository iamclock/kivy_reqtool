from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


# Screens
class MainWindow(Screen):
    pass


class RequestSatisfaction(Screen):
    pass


class CertificateConverter(Screen):
    pass


class WindowsManager(ScreenManager):
    pass


kv = Builder.load_file("ExampleApp.kv")


class CustomLayout(Widget):
    pass


class MyGridLayout(Widget):

    name = ObjectProperty(None)
    surname = ObjectProperty(None)
    color = ObjectProperty(None)

    def submit(self, instance):
        name = self.name.text
        surname = self.surname.text
        color = self.color.text
        # self.add_widget(Label(text=f"{name} {surname} {color}"))
        print(f"{name} {surname} {color}")
        # self.name.text = ""
        # self.surname.text = ""
        # self.color.text = ""
        return


class ExampleApp(App):
    # pass
    def build(self):
        # return MyGridLayout()
        # return CustomLayout()
        return kv  # For screenmanager


if __name__ == '__main__':
    ExampleApp().run()
