from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Splitters example exercise 32


class SplittersEx(Widget):
    pass


class CustomLayout(Widget):
    pass


class ExampleApp(App):

    # def build(self):
    #     return CustomLayout()
    pass


if __name__ == '__main__':
    ExampleApp().run()
'''
# Spinner example exercise 32
# Builder.load_file("ExampleApp.kv")


class CustomLayout(Widget):

    def spinner_clicked(self, value):
        self.ids.click_label.text = f"Issuer: {value}"


class ExampleApp(App):

    def build(self):
        # main_widget = CustomLayout()
        # main_widget.ids.click_label.text = "Issuer: ???"
        # return main_widget
        return CustomLayout()


if __name__ == '__main__':
    ExampleApp().run()
'''
'''
# Screens
class MainWindow(Screen):
    pass


class RequestSatisfaction(Screen):
    pass


class CertificateConverter(Screen):
    pass


class WindowsManager(ScreenManager):
    pass


class ExampleApp(App):
    def build(self):
        return kv  # For screenmanager


if __name__ == '__main__':
    ExampleApp().run()
'''
# Какой то урок, не помню
'''
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
'''
