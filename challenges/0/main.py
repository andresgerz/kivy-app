from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.list import TwoLineAvatarListItem
from kivymd.uix.list import ImageLeftWidget

from data import data_arr

Builder.load_string(
    '''
#:import images_path kivymd.images_path


<CustomTwoLineAvatarListItem>:

    ImageLeftWidget:
        source: root.source


<PreviousMDIcons>:

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(50)
        padding: dp(60)

        MDBoxLayout:
            adaptive_height: True

            MDIconButton:
                icon: 'magnify'

            MDTextField:
                id: search_field
                hint_text: 'Search Pizza'
                on_text: root.set_list_md_icons(self.text, True)

        RecycleView:
            id: rv
            key_viewclass: 'viewclass'
            key_size: 'height'

            RecycleBoxLayout:
                padding: dp(10)
                default_size: None, dp(82)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
'''
)

class CustomTwoLineAvatarListItem(TwoLineAvatarListItem):
    source = StringProperty()

class PreviousMDIcons(Screen):

    def set_list_md_icons(self, text="", search=False):
        '''Builds a list of icons for the screen MDIcons.'''

        def add_icon_item(image_obj):
            self.ids.rv.data.append(
                {
                    "viewclass": "CustomTwoLineAvatarListItem",
                    "text": image_obj["Pizza"],
                    "source": image_obj["Image"],
                    "secondary_text": "Ingredientes: " + image_obj["Ingredientes"],
                    "callback": lambda x: x,
                }
            )

        self.ids.rv.data = []
        for image_obj in data_arr:
            if search:
                if text in image_obj["Pizza"]:
                    add_icon_item(image_obj)
            else:
                add_icon_item(image_obj)

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = PreviousMDIcons()

    def build(self):
        return self.screen

    def on_start(self):
        self.screen.set_list_md_icons()

MainApp().run()