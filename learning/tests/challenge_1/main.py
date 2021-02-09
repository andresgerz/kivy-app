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

from kivymd.uix.label import MDLabel
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem, MDList, IconLeftWidget


from data import head, body, end
from expansion_panel_custom import ExpansionPanelCustom, MDExpansionPanelOneLine

Config.set('graphics','resizable',0)
Window.size = (360, 640)


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


class NavigationDrawer(MDApp):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

    def build(self):
        return Builder.load_file("myfile.kv")
            

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
        #print(new_doby)
        
        for new_obj in new_doby:

            self.root.ids.content_drawer.ids.md_list.add_widget(
                ExpansionPanelCustom(
                    icon=new_obj["icon"],
                    content=Content(new_obj),
                    panel_cls=MDExpansionPanelOneLine(
                        text="[color=6258B1]" + new_obj["text"] + "[/color]",
                    )
                )
            )  

NavigationDrawer().run()

"""  MDExpansionPanel(
                icon=new_obj["icon"],
                content=Content(new_obj),
                panel_cls=MDExpansionPanelOneLine(
                    text="[color=6258B1]" + new_obj["text"] + "[/color]",
                )
            ) 
"""