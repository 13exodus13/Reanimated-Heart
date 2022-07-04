screen license():
    frame:
        xpos 1100
        ypos 210
        background "gui/driverselicense.png"
        
        input default "":
            xpos 235
            ypos 165
            pixel_width(460)
            value VariableInputValue("player_name")

        hbox:
            xpos 450
            ypos 215
            imagebutton auto "gui/uncertain/f_%s.png" action [SetVariable("gender", "female"), SelectedIf(gender == "female")]
            imagebutton auto "gui/uncertain/m_%s.png" action [SetVariable("gender", 'male'), SelectedIf(gender == 'male')]
        
        hbox:
            xpos 390
            ypos 280
            imagebutton auto "gui/uncertain/he_%s.png" action [SetVariable("pronoun", 0), SelectedIf(pronoun == 0)]
            imagebutton auto "gui/uncertain/she_%s.png" action [SetVariable("pronoun", 1), SelectedIf(pronoun == 1)]
            imagebutton auto "gui/uncertain/they_%s.png" action [SetVariable("pronoun", 2), SelectedIf(pronoun == 2)]
        

        

init python:
    base_styles_num, shirt_styles_num, eyes_styles_num, hair_styles_num = 4, 3, 4, 11
    base, shirt, eyes, hair= 3, 1, 1, 4
   
    def draw_char(st, at): 
        return LiveComposite(
            (361, 702),     
            (0, 0), "images/Default Character/base%d.png"%base,
            (0, 0), "images/Default Character/shirt%d.png"%shirt, 
            (0, 0), "images/Default Character/jacket.png",
            (0, 0), "images/Default Character/eyes%d.png"%eyes,
            (0, 0), "images/Default Character/hair%d.png"%hair,
            ),.1

    def draw_char_side(st, at):
        return LiveComposite(
            (361, 702),
            (10, 550), im.FactorScale("images/Default Character/base%d.png"%base, .45, .45),
            (10, 550), im.FactorScale("images/Default Character/shirt%d.png"%shirt, .45, .45),
            (10, 550), im.FactorScale("images/Default Character/jacket.png", .45, .45),
            (10, 550), im.FactorScale("images/Default Character/eyes%d.png"%eyes, .45, .45),
            (10, 550), im.FactorScale("images/Default Character/hair%d.png"%hair, .45, .45),            
            ),.1    

init:
    image char = DynamicDisplayable(draw_char) # using DynamicDisplayable ensures that any changes are visible immedietly
    # $ character = Character('Koma', color="#c8ffc8", window_left_padding=180, show_side_image=DynamicDisplayable(draw_char_side))
    $ player_name = ""
    $ gender = 'female'
    $ pronoun = 1
label dressup:
    stop music
    window hide
    scene bg character_selection
    show screen license
    show char:
        xpos 400
        ypos 180
    $ show_quick_menu = False
    $ _skipping = False #disable skip
    $ _preferences.afm_enable = False #turn off auto
    python:
        y = 50
        ui.imagebutton("gui/button/l_arrow.png", "gui/button/l_arrow_hover.png", clicked=ui.returns("baseL"), ypos=500, xpos=325)
        ui.imagebutton("gui/button/r_arrow.png", "gui/button/r_arrow_hover.png", clicked=ui.returns("baseR"), ypos=500, xpos=885)
        y += 80
        ui.imagebutton("gui/button/l_arrow.png", "gui/button/l_arrow_hover.png", clicked=ui.returns("shirtL"), ypos=750, xpos=325)
        ui.imagebutton("gui/button/r_arrow.png", "gui/button/r_arrow_hover.png", clicked=ui.returns("shirtR"), ypos=750, xpos=885)
        y += 80
        ui.imagebutton("gui/button/l_arrow.png", "gui/button/l_arrow_hover.png", clicked=ui.returns("eyesL"), ypos=325, xpos=325)
        ui.imagebutton("gui/button/r_arrow.png", "gui/button/r_arrow_hover.png", clicked=ui.returns("eyesR"), ypos=325, xpos=885)
        y += 80
        ui.imagebutton("gui/button/l_arrow.png", "gui/button/l_arrow_hover.png", clicked=ui.returns("hairL"), ypos=225, xpos=325)
        ui.imagebutton("gui/button/r_arrow.png", "gui/button/r_arrow_hover.png", clicked=ui.returns("hairR"), ypos=225, xpos=885)
        
        ui.imagebutton("gui/button/finishedbutton.png","gui/button/finishedbutton_hover.png", clicked=ui.returns("goback"), ypos=955, xpos=1400) 
        
    $ picked = ui.interact()
    if picked == "baseL":
        $ base -= 1 
    if picked == "baseR":
        $ base += 1 
    if base < 1: 
        $ base = base_styles_num
    if base > base_styles_num: 
        $ base = 1

    if picked == "shirtL":
        $ shirt -= 1
    if picked == "shirtR":
        $ shirt += 1
    if shirt < 1:
        $ shirt = shirt_styles_num
    if shirt > shirt_styles_num:
        $ shirt = 1

    if picked == "eyesL":
        $ eyes -= 1
    if picked == "eyesR":
        $ eyes += 1
    if eyes < 1:
        $ eyes = eyes_styles_num
    if eyes > eyes_styles_num:
        $ eyes = 1

    if picked == "hairL":
        $ hair -= 1
    if picked == "hairR":
        $ hair += 1
    if hair < 1:
        $ hair = hair_styles_num
    if hair > hair_styles_num:
        $ hair = 1
        
    if picked == "goback":
        show screen confirm(message=layout.ARE_YOU_SURE, yes_action=[Hide('confirm'),Jump('everything_returns')], no_action=[Hide('confirm'),Jump('dressup')])
    jump dressup 

label everything_returns:
    hide char
    hide screen license
    $ selectedpronouns = pronounlist[pronoun]

    # This calls the label for updating self-voicing text tags.

    call tts_tag_update

    # TODO: The following are used in this guide to set the pronoun variables to match the selected pronouns (as explained below). These would need to be changed if you need more/different variables (e.g., for translations).

    $ they = theylist[pronoun]
    $ them = themlist[pronoun]
    $ their = theirlist[pronoun]
    $ theirs = theirslist[pronoun]
    $ s = slist[pronoun] # TODO: If you want to use "s" for a character or a variable elsewhere, you will have to change the "s" here to something else (e.g., default ss = slist[pronoun]). You would also need to change it in pronounselection.
    $ es = eslist[pronoun]
    $ are = arelist[pronoun]
    if player_name == '':
        $ player_name = 'Player'
    $ show_quick_menu = True
    $ _skipping = True #disable skip

    jump after_dressup
    return
