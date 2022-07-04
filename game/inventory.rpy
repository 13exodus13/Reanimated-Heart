image wallet:
    "images/inventory/wallet.png"
    size(100,100)
image map:
    "images/inventory/map.png"
    size(100,100)
image key:
    "images/inventory/key.png"
    size(100,100)

image white = "#ffffff"
image bg keyitem = "#0ac0ff"

init python:
    class InventoryItem:
        def __init__(self, name, img, description,value):
            self.name = name
            self.img = img
            self.description = description
            self.value = value

    
    class Equipabble(InventoryItem):
        def __init__(self, name, img, description, value):
            InventoryItem.__init__(self, name, img, description, value)
            self.isequipped = False
            self.equipped_to = None
            
        def equip(self,target):
            self.isequipped = True
            self.equipped_to = target

        def unequip(self):
            self.isequipped = False
            self.equipped_to = None

    class KeyItem(InventoryItem):
        def __init__(self, name, img, description):
            InventoryItem.__init__(self, name, img, description,0)

screen inventory_tab():
    tag menu

    use game_menu(_(""))
    frame:
        offset(365, 85)
        background "gui/inventoryasset.png"

        hbox:
            #equipped items (add later)
            #inventory grid
            grid 4 7:
                spacing 5
                offset(75,110)
                for item in inventory:
                    frame:
                        style "slot"
                        imagebutton idle item.img action SetScreenVariable("selected_item", item)
                for i in range(len(inventory),28):
                    frame:
                        style "slot"
                        
            #item details
            vbox:
                offset(175,-55)

                if selected_item != None:
                    add selected_item.img:
                        size(600,600)
                    
                    viewport id "vp":
                        draggable True
                        mousewheel True
                        area(110,10,410,700)
                        vbox:
                            label "{b}[selected_item.name]{/b}" text_size 30
                            label "[selected_item.description]" text_size 25    
                            # if not isinstance(selected_item, KeyItem):
                                #     textbutton "Discard" action SetScreenVariable(inventory, selected_item), SetVariable("selected_item", None)

