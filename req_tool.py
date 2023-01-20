import enum
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file("ReqToolApp.kv")

Window.size = (520, 700)


class CertificatePurposes(enum.IntEnum):
    none = 0x0
    client_only = 0x1
    server_only = 0x2
    both = client_only ^ server_only
    pass


# test


class MainLayout(Widget):
    purposes = CertificatePurposes.both.value

    # def purposes_checkbox_clicked(self, instance, value, is_server):
    #     self.purposes ^= 1 << is_server
    #     self.ids.purposes_value.text = hex(self.purposes)
    #     # print(purposes, value)
    #     return

    def qualified_checkbox_clicked(self, instance, value):
        qualified_text = "O=\nC="
        not_qualified_text = ""
        self.ids.qualified_text_input.text = qualified_text if value \
            else not_qualified_text
        return

    def doit_clicked(self):
        print(self.ids.server_checkbox.active, self.ids.client_checkbox.active)
        if self.ids.server_checkbox.active:
            pass
        if self.ids.client_checkbox.active:
            pass
        return


class RequestTool(App):

    def build(self):
        return MainLayout()


if __name__ == "__main__":
    RequestTool().run()
