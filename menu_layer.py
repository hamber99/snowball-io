from cocos.director import director
from cocos.scene import Scene
from cocos.menu import *
from pyglet.app import exit
from cocos.layer import MultiplexLayer

try:
    aa = open(".name", "r")
    f = aa.read()
except:
    f = "DATA MISSING"
    # h()


class MM(Menu):
    def __init__(self):
        super().__init__("snowball.io")
        self.font_title["font_size"] = 64
        self.font_title["color"] = (255, 255, 255, 255)
        self.font_title["bold"] = True
        self.font_item["color"] = (155, 155, 255, 255)
        self.font_item["font_size"] = 38
        self.font_item_selected["color"] = (195, 195, 255, 255)
        self.font_item_selected["font_size"] = 46
        self.menu_valign = CENTER
        self.menu_halign = CENTER
        items = [MenuItem("Play", self.p), MenuItem("Option", self.o), MenuItem("Skin", self.s),
                 MenuItem("Quit", self.q)]
        self.create_menu(items, shake(), shake_back())

    def p(self):
        pass

    def o(self):
        self.parent.switch_to(1)
        # pass

    def q(self):
        exit()

    def s(self):
        pass


class OM(Menu):
    def __init__(self):
        global f
        super().__init__("snowball.io")
        self.font_title["font_size"] = 64
        self.font_title["color"] = (255, 255, 255, 255)
        self.font_title["bold"] = True
        self.font_item["color"] = (155, 155, 255, 255)
        self.font_item["font_size"] = 38
        self.font_item_selected["color"] = (195, 195, 255, 255)
        self.font_item_selected["font_size"] = 46
        self.menu_valign = BOTTOM
        self.menu_halign = RIGHT
        try:
            sss = open(".music")
            fgg = sss.read()
        except:
            fgg = 1
        items = [EntryMenuItem("Name: ", self.p, f), ToggleMenuItem("Music: ", self.o, fgg),
                 MenuItem("Back", self.q)]
        self.create_menu(items, shake(), shake_back())

    def p(self, qq):
        print(qq)
        z = open(".name", "w")
        z.write(qq)

    def o(self, l):
        print(l)

    def q(self):
        self.parent.switch_to(0)


def a():
    director.init(caption="snowball.io", width=500, height=400)
    director.run(Scene(MultiplexLayer(MM(), OM())))
