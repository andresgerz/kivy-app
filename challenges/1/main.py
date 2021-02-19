from kivy.config import Config
from kivy.core.window import Window
from kivy.graphics import Color
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty, ListProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.recycleview import RecycleView
from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.label import MDLabel
from kivymd.uix.list import ILeftBodyTouch, IRightBodyTouch, OneLineAvatarIconListItem, MDList, IconLeftWidget

from data import head, body, end

# Dimensiones de pantalla portrait
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

        # si no son cadenas vacias '', agrego a la data al recycleview
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

""" Clase para cuando no hay ninguna imagen, está clase en vez de heredar del widget IRightBodyTouch hereda de ILeftBody Touch.

"""

class MDExpansionChevronRight(ILeftBodyTouch, MDIconButton):
    """Chevron icon on the right panel."""

    _angle = NumericProperty(0)

class MDExpansionPanelCustom(MDExpansionPanel):
   
    def __init__(self, data, image, **kwargs):
        super(MDExpansionPanelCustom, self).__init__(**kwargs)
        self.at_least_an_image=image
        
        """ si no hay ninguna imagen, borra el widget ImageLeftWidget de la componente MDExpansionPanel y agrega el widget MDExpansionChevronRight() a la izquierda.
        
        """
        if not self.at_least_an_image:
            for child in self.panel_cls.children[0:1]:
                self.panel_cls.remove_widget(child)
            
            self.chevron = MDExpansionChevronRight()
            self.panel_cls.add_widget(self.chevron)
            
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
        at_least_an_image = False

        for obj in body:
            for key,val in obj.items():
                if val == None:
                    obj[key] = ''
            if obj['icon'] != '':           
                at_least_an_image = True

            new_doby.append(obj)        

        for new_obj in new_doby:
            self.root.ids.content_drawer.ids.md_list.add_widget(
                MDExpansionPanelCustom(
                    image=at_least_an_image,
                    data=new_obj,
                    icon=new_obj["icon"],
                    content=Content(new_obj),
                    panel_cls=MDExpansionPanelOneLine(
                        text="[color=6258B1]" + new_obj["text"] + "[/color]",
                    )
                )
            )  

NavigationDrawer().run()