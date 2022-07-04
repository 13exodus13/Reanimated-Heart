init python:
    class Player_Notes:
        def __init__(self, name = '???', first_impression = '???', image_name='questionmark'):
            self.name = name
            self.first_impression = first_impression
            self.image_name = "images/character_icons/"+ image_name + ".png"

default York_Crux = Player_Notes()
default Black_Lumaban = Player_Notes()
default Grete_Braun = Player_Notes()