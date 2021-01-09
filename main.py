from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem


KV = '''

<MyTile@SmartTileWithLabel>
    size_hint_y: "1200"
    height: "500dp"

GridLayout:
    rows: 2
    adaptive_height: True

    MDBoxLayout:
        adaptive_height: True

        MDIconButton:
            icon: 'magnify'

        MDTextField:
            id: search_field
            hint_text: 'Search icon'
            on_text: root.set_list_md_icons(self.text, True)


    ScrollView:

        GridLayout:
            cols: 3
            adaptive_width: True
            padding: dp(4), dp(4)
            spacing: dp(4)

            MyTile:
                source: "./images/pizza.jpeg"
                text: "[size=26]Pizza 1[/size]"

            MyTile:
                source: "./images/pizza2.jpeg"
                text: "[size=26]Pizza 2[/size]"
                tile_text_color: app.theme_cls.accent_color

            MyTile:
                source: "./images/pizza3.jpeg"
                text: "[size=26]Pizza 3[/size]"
                tile_text_color: app.theme_cls.accent_color

            MyTile:
                source: "./images/pizza4.jpeg"
                text: "[size=26]Pizza 4[/size]"
                tile_text_color: app.theme_cls.accent_color

            MyTile:
                source: "./images/pizza5.jpeg"
                text: "[size=26]Pizza 5[/size]"
                tile_text_color: app.theme_cls.accent_color

            MyTile:
                source: "./images/pizza6.jpeg"
                text: "[size=26]Pizza 6[/size]"
                tile_text_color: app.theme_cls.accent_color

            MyTile:
                source: "./images/pizza7.jpeg"
                text: "[size=26]Pizza 7[/size]"
                tile_text_color: app.theme_cls.accent_color

            MyTile:
                source: "./images/pizza8.jpeg"
                text: "[size=26]Pizza 8[/size]"
                tile_text_color: app.theme_cls.accent_color                
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


MainApp().run()