from kivy.config import Config
from kivy.core.window import Window
from kivy.graphics import Color
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.recycleview import RecycleView
from kivy.uix.screenmanager import Screen
from kivymd import images_path
from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons
from kivymd.theming import ThemableBehavior
from kivymd.uix.button import MDIconButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.label import MDLabel
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem, MDList, IconLeftWidget


Config.set('graphics','resizable',0)
Window.size = (360, 640)

head = { 
    'profile_picture': 'resource/profile/image.png',
    'button_edit_pic': True,
    'person_name': 'Raúl Guiller',
    'account_name':'raul-guiller',
    'notifications': 3,
    'new_msg': 2
    }


body = [
    {'icon': None, 'text': 'Notifications', 'sub': None},
    {'icon': None, 'text': 'Subscriptions', 'sub': None},
    {'icon': './images/50x50.png', 'text': 'Entities', 
    'sub': [
        {'icon': 'language-python', 'text': '@Cyberlink', 'icon_button': 'pen'}
        ]
    },
    {'icon': None, 'text': 'Contact', 'sub': None},
    {'icon': None, 'text': 'Settings', 'sub': None}
    ]

end = {'light_mode': True}


class Container(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True


class ContentNavigationDrawer(BoxLayout):
    pass


class NavigationItem(OneLineAvatarIconListItem):
    icon = StringProperty() 
    icon2 = StringProperty()


class Content(MDBoxLayout):
    def __init__(self, item):
        super(Content, self).__init__() 
        self.ids.rv.data = []

        # si no son '', agrego a la data del recycleview,
      
        if item['sub'] != '':
            for sub_obj in item['sub']:  
                self.ids.rv.data.append(
                    {
                        "viewclass": "NavigationItem",
                        "icon": sub_obj['icon'],
                        "text": sub_obj['text'],
                        "icon2": sub_obj['icon_button'],
                        "callback": lambda x: x,
                    }
                )


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

class NavigationDrawer(MDApp):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

    def build(self):
        return Builder.load_file("main.kv")
            

    def on_start(self):
        new_doby = list()

        """ Cambia todos las claves None por '' porque
        None is not allowed for MDExpansionPanel.icon 

        """
        for obj in body:
            for key,val in obj.items():
                if val == None:
                    obj[key] = ''
                    
            new_doby.append(obj)        
        print(new_doby)
        
        for new_obj in new_doby:

            self.root.ids.content_drawer.ids.md_list.add_widget(
                MDExpansionPanel(
                    icon=new_obj["icon"],
                    content=Content(new_obj),
                    panel_cls=MDExpansionPanelOneLine(
                        text="[color=6258B1]" + new_obj["text"] + "[/color]",
                    )
                )
            )  


NavigationDrawer().run()