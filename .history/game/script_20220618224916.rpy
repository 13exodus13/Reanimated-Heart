# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    define crux = Character("Crux", color='#000000')

    default show_quick_menu = True


    default inventory = []
    default selected_item = None
    default inven_key = KeyItem("Grete's House Key","key",'Home is where the badly cooked stew is.')

    define cen = Character(None, what_xalign=0.5, what_text_align=0.5)

# The game starts here.

label start:
    stop music
    scene bg day_clearskies

    play music "audio/bird_chirps.mp3" volume 3

    "{cps=20}The vicious frost of this year's winter took its toll on you.{w} You used to enjoy the holidays."
    
    "{cps=20}Even thinking about it drew up nostalgic festive scents.{w} Peppermint, cinnamon, and pine."
    
    "{cps=20}When you were young, you'd bounce around the white blankets of snow in central park.{w} Your cheeks flushed and laughter ringing for hours and hours until it got dark." 
    
    "{cps=20}You liked coming home after playing, too.{w} It meant cozy fires and hot cocoa, two marshmallows on top."

    "{cps=20}It was different now, as an adult."
    
    "{cps=20}The cold was no longer an opportunity to bundle up indoors and wear comfortable coats,{w=0.5} but instead a heartless agent of death."
    
    "{cps=20}In her carnage, she brought forth another bill,{w=0.5} another leak in the ceiling,{w=0.5} another stipulation in a contract you never bothered to read,{w=0.25} and the heater."
    
    "{cps=20}The goddamn heater, hummed away all day all night like a growling beast, bleeding out your paychecks month after month."

    "{cps=20}You thought you had it handled.{w} You did, for a while, until the lucrative opportunity that sent you across the country fell through."

    "{cps=20}By the time the new year's spring came into full bloom, there was nothing left in your bank account."

    "{cps=20}You decided to be honest with yourself."

    "{cps=20}You couldn't do this anymore."

    "{cps=20}You finalized your plans to move back to your hometown."

    "{cps=20}It was humiliating to return with your tail between your legs, but it'd be nice to be home, at least."

    "{cps=20}Or not."

    "{cps=20}During those months of planning, the city had completely changed."
    
    "{cps=20}All the news stations on cable TV exploded with reports prophesying the end of days."
    
    "{cps=20}There was,{w=0.5} get this, {w=0.5}a fucking pandemic, like this was Biblical Scripture or something!"

    "{cps=20}To make matters worse, the government proved itself ill-equipped to handle it."
    
    "{cps=20}You'd think with their posturing, they could at least formulate a sensible response, but no."
    
    "{cps=20}The orders were simple{w=0.5} stay at home, and don't ask any goddamn questions."

    "{cps=20}It was quickly followed by uproarious protests."

    "{cps=20}You didn't blame them. Anybody would be fucking angry."

    "{cps=20}Whatever your stance on the issue, it wouldn't matter."

    "{cps=20}You still had a flight."
    
    "{cps=20}Yours was one of the last tickets available before they started enforcing airport restrictions and regulations."
    
    "{cps=20}There was zero possibility of slipping through them if you delayed any longer."

    "{cps=20}Traveling was going to be very dangerous.{w} You just had to be extra careful." 
    
    jump car_crash

label car_crash:

    stop music fadeout 1.5

    scene black with dissolve

    cen "{cps=10}{size=+15}LATE MARCH.{/size}"

    play music "audio/busy_street.mp3" volume 0.5

    scene bg afternooncloudcar with dissolve

    "{cps=20}The protests haven't died down."
    
    "{cps=20}In fact, they've gotten worse over the weeks."
    
    "{cps=20}The airport was empty upon your arrival, but the roads were packed with cars."

    "{cps=20}You have been stuck in traffic for the last two hours."
    
    "{cps=20}You check your phone.{w} Your social media feed is nothing but news and discourse."
    
    "{cps=20}You can feel yourself getting worked up, your trembling hand balled into a fist in your lap."

    "{cps=20}You find out one of these big events is happening in your city."

    "???""{cps=20}Great."

    "{cps=20}You feel a bit embarrassed by the fact that you said that aloud, however the driver's lack of reaction reassures you."

    "{cps=20}The light turns green. For a moment, you feel relief, but it's short-lived.{w} The cab moves an inch."

    "{cps=20}In the distance, you spot a traffic controller gesturing for everyone to make a turn onto the highway at the next left."

    "{cps=20}That's not even remotely near your destination!"

    play sound "audio/thump.mp3"

    "{cps=20}The driver smacks the steering wheel in frustration." 

    "Cab Driver" "{cps=20}Road's blocked 'cause o' the fuckin' protest.{w} Sorry, pal."

    "???" "{cps=20}You're kidding me."

    "Cab Driver" "{cps=20}Hey, maybe you can get past the crowd and pick up a cab there."

    "Cab Driver" "{cps=20}I'm telling you now, there ain't no way we're getting to the other side o' this street."

    "???" "{cps=20}This is just great."

    scene bg afternooncloud with Fade(0.5,0.5,0.5)

    play sound "audio/door_close.mp3"

    "{cps=20}You exit the cab in the middle of the road."

    play sound "audio/honking_car.mp3"
    
    "{cps=20}The surrounding cars honk at you in protest, but you don't care."
    
    "{cps=20}You grab your suitcase from the trunk and start weaving through the traffic, then the crowd."
    
    "{cps=20}You've never seen the city filled with this many people."
     
    "{cps=20}You're sure that, if you squinted, you could make out who belonged to what protest, but right now, you're just focusing on getting to the other side."
    
    "{cps=20}You've had enough delays."

    "{cps=20}Even with all the chaos, you can't help feeling nostalgic toward your old haunts." 
    
    "{cps=20}You remember that pizza parlor."
    
    "{cps=20}You used to hang out there during High School."
    
    "{cps=20}Your name etched on the corner booth with a sweetheart's. (Young love. Everyone thinks it'll last forever.)"
     
    "{cps=20}You got your prom outfit at the clothing store next to it, and you remember it was on sale."
    
    "{cps=20}You stop in front of its boarded up storefront."

    "{cps=20}'Closed.' The sign read.{w} You sigh."

    "{cps=20}You snap out of your reverie when you hear it."

    play sound "audio/pistol_shot.mp3" 

    "{cps=20}Several gunshots fire off in the distance."
    
    stop music fadeout 1.5

    play sound "audio/panic.mp3" volume 0.5 fadein 2.5
    
    "{cps=20}It sends everybody running like a pack of lemmings, and the crowd quickly transforms into a stampede." 
    
    "{cps=20}No rhyme or reason, just the feral instinct to survive reigning over everything else."
    
    "{cps=20}Your vision melts into a haze."
    
    "{cps=20}You follow the stream of people, taking off running with no destination, hoping to high heavens they lead you to safety as your heart pounds deafeningly in your chest."

    "{cps=20}Where did it come from? Did someone get hurt?"

    "{cps=20}Oh god, are you gonna die?"

    "{cps=20}The people in front of you veer into the alleyways, and you notice too late."

    "{cps=20}You stare down two blinding lights and —"

    "Stranger""{cps=20}Watch out!"

    "{cps=20}You brace for dear life."

    play sound "audio/car_accident.mp3"

    scene black with MultipleTransition([False, dissolve,'lensflaretransition.png',dissolve,"#51644b", dissolve, True])

    scene black with vpunch
    
    pause 0.25

    "{cps=20}Nothing."

    play music "audio/Redlight.mp3" fadein 1.5

    "{cps=20}You drop the arms shielding your face."

    scene bg tree with fade:
        xpos 0.5 ypos 1.0 xanchor 0.51 yanchor 0.93 zoom 1.25
        
    pause 0.5

    "{cps=20}You find yourself standing in the middle of an asphalt street."
    
    "{cps=20}Unlike your hometown, everything here is unfamiliar."
    
    "{cps=20}The first thing you notice is the color green."
    
    "{cps=20}It's not a serene green."
    
    "{cps=20}It's eerie, foreign, unsettling."
    
    "{cps=20}Everything is tinted with it — no, suffocating in it — like a radioactive nuclear wasteland or a swamp dominated by moss and algae."

    "{cps=20}That's not even the weirdest sight."
    
    $ show_quick_menu = False
    scene bg tree:
        xpos 0.5 ypos 1.0 xanchor 0.51 yanchor 0.93 zoom 1.25
        linear 4 yanchor 0.65
    $renpy.pause(4, hard=True)
    $ show_quick_menu = True

    "{cps=20}At the very center of this town, there's a hulking white tree with a trunk thicker than several mountaintops."
    
    "{cps=20}It extends far into the sky, far beyond what your eyes can see."
    
    "{cps=20}You're unsure if the branches are those of a regular tree, or if they're something similarly foreign, like tendrils stabbing into the void of space."
    
    "{cps=20}Surrounding it is the purest night sky you've ever seen, the kind of sky only your ancestors knew intimately." 
    
    "{cps=20}The stars above are clumped together like a thick coat of glitter on pitch black paper."

    "{cps=20}Just looking at this tree evokes a powerful feeling in the innermost part of your chest, but you're not sure what it is."

    "{cps=20}This must be what it was like to witness a god in its enormity."

    "{cps=20}You relax, for a split second, before you hear the fast thumping of heavy boots sprinting from a nearby alley."
    
    "{cps=20}Your consciousness slams back down on earth." 

    scene bg tree with move:
        xpos 0.5 ypos 1.0 xanchor 0.51 yanchor 0.93 zoom 1.25
    scene bg tree with dissolve:
        xpos 0.5 ypos 1.0 xanchor 0.51 yanchor 0.93 zoom 1.25
        matrixcolor BrightnessMatrix(0.1)
    
    "{cps=20}As you turn to check it out, a familiar bright light shines behind you."

    "{cps=20}Another incoming car —"

    play sound "audio/car_accident.mp3"

    scene black with MultipleTransition(['#000', dissolve,'lensflaretransition.png',dissolve,"#ffffff", dissolve, True])

    scene black with vpunch:
        xpos 0.5 ypos 1.0 xanchor 0.51 yanchor 0.93 zoom 1.25
    "{cps=20}You're knocked off your feet."

    "{cps=20}Your world spins."

    "{cps=20}You roll onto the cold, hard sidewalk, and as you come to your senses, you realize a kind stranger has pulled you into his arms and dragged you out of harm's way."
    
    "???""{cps=20}Thank —"

    "{cps=20}You open your eyes."

    scene blackcg1 with dissolve

    "{cps=20}That can't be real."

    window hide

    pause 1

    window show
    
    "{cps=20}You notice his eyes first."
    
    "{cps=20}They're bright red and dilated, as piercing as the end of a sniper's scope."
    
    "{cps=20}Icy dread fills up your lungs."
    
    "{cps=20}You can't breathe."
    
    "{cps=20}You're frozen in place, thighs trembling, head begging you to make a decision between kick and run."
    
    "{cps=20}You imagine it's the same type of shock a prey animal would experience when face to face with the gaping maw of a predator, knowing full well it was about to become its next meal."    
    
    scene streetlampbg with Dissolve(2, alpha=True,time_warp=None)

    play music "audio/Redlight.mp3" fadein 1.5

    "{cps=20}Just as quickly as he arrived, he extracts himself from you and sprints into the alleyway on this side of the street."
    
    "{cps=20}You barely have time to compose yourself."

    "{cps=20}The owner of the car parks on the side of the road."

    "Car Owner""{cps=20}What the hell, kid? You just appeared in the middle of the street! What was that, like some kinda magic trick or something!?"
    
    "???""{cps=20}I…"

    "{cps=20}Out of nowhere, another person pops out of the same alleyway your terrifying hero came from. A tall guy, made taller by his lanky build, sprints up to the road and looks visibly out of breath."
    
    "{cps=20}You two make eye contact."

    show crux closeup surprise with dissolve

    "{cps=20}Behind his glasses, you notice there's a hint of surprise and… recognition."
    
    "{cps=20}His gaze lingers on you, but he doesn't explain himself. He follows after shark teeth."

    hide crux with dissolve
    
    "{cps=20}If you can give me your info, I'll get you in contact with my insurance guy —"
    
    "{cps=20}You take off after them in a rush."

    stop music fadeout 1.5

    scene black with dissolve

    "{cps=20}You don't know what happened, where you are, or how you got here. If you lose the one thread you have to this entire mystery, you'll have nothing."

    "{cps=20}As you hunt down the two strangers, you start to register what sort of place this is." 
    
    "{cps=20}It's one of those small towns, likely with a population of a couple thousands… the sort of place where everybody has history with everyone else." 
    
    "{cps=20}It's a touch rural, but the kind that's fallen in love with the technological advances of the city and taking its first steps to urbanization."

    "{cps=20}You pass by a generic 24/7 gas station and a rundown playground in your chase." 
    
    "{cps=20}You can't help but cast your eyes over the locals." 
    
    "{cps=20}Some don't seem all that different from humans, but others have odd features, like multiple eyeballs and horns." 
    
    "{cps=20}You're starting to get freaked out, but you keep pursuing your white rabbit's silhouette in the distance." 
    
    "{cps=20}Luckily, he's not that fast of a runner."

    scene construction_site with dissolve

    "{cps=20}You end up at an abandoned construction site." 

    show black facecover teethout angry with dissolve
    
    "{cps=20}Your savior is crouched in front of an iron beam, covering his face with his hands." 

    show black facecover teethout angry at left with move

    show crux slouching blank at right with dissolve 
    
    "{cps=20}The green-eyed man clutches the beam next to him, trying to catch his breath."

    show crux slouching concerned talking

    "Lanky""{cps=20}Thank fucking god you stopped. My heart was gonna burst."

    show black facecover teethout angrytalk

    "Shark Teeth""{cps=20}Why the fuck were you following me?"

    show crux slouching blank talking

    show black facecover teethout angry

    "Lanky""{cps=20}If you'd just stayed put and let me talk, you wouldn't be freaking out. Look, I can explain all of this —"
    
    show crux slouching blank 

    show black facecover teethout angrytalk

    "Shark Teeth""{cps=20}You can explain this —"

    "{cps=20}He whips around to snarl, baring his monstrous fangs at his companion.{w} At that moment, he notices you standing in the entryway and stops."

    show black facehand teethout surprised

    "Shark Teeth""{cps=20}It's you…"

    "{cps=20}The lanky man gives you a gentle smile, and beckons you closer."

    show crux default smiling with move

    "Lanky""{cps=20}Please, don't be shy…"

    "Lanky""{cps=20}Can you introduce yourself"

    jump dressup

label after_dressup:

    scene construction_site with fade

    pause 0.1

    show crux default smiling with dissolve

    "Lanky" "{cps=20}[player_name], huh?"

    "Lanky" "{cps=20}Good to meet you. The name’s Crux."

    crux "{cps=20}I'm sure you can tell, but you walked in at a bit of an awkward time. But you probably have questions." 

    crux "{cps=20}I'll get to them after I address his little situation…"

    "{cps=20}Crux turns to his friend and frowns, expression severe."

    show crux slouching blank at left with move

    show black 

    "Shark Teeth""{cps=20}I know… I know I did. Damn it, I still remember, it’s so fresh…"
    
    "Shark Teeth""{cps=20}This bastard pulled out a gun, and he was about to fire on a girl for recording him…"

    "{cps=20}A gun?"

    "Shark Teeth""{cps=20}Was she okay?"

    crux "{cps=20}I don't know"

    crux "{cps=20}And frankly, I don't give a shit."

    crux "{cps=20}I just watched you die right in front of my eyes. She can get fucked for all I care"

    "{cps=20}Black glares at him in outrage."

    "{cps=20}Crux crouches down to look him directly in the eyes."

    crux "{cps=20}The important thing is that I anticipated you could die because of these dumb protests, so I planned in advance."

    "Shark Teeth""{cps=20}Meaning…?"

    crux "{cps=20}Remember my witch friend? I struck a deal with her for a spell to revive you."
    
    crux "{cps=20}Had it prepared and everything. Only, she's not capable of creating spells that heal or revive life." 
    
    crux "{cps=20}Call it the price of destructive magic, I suppose."

    crux "{cps=20}I'll get to my point. You're a zombie now"

    "{cps=20}None of this is making sense. Witches and magic? Zombies? Real, live, shambling walkers, the kind in TV shows?"

    "{cps=20}Black doesn't seem to be buying it either. He looks incredulous."

    "{cps=20}Shark Teeth""I'm a zombie?"

    crux "{cps=20}That would make as much sense as anything, wouldn't it?"

    "[player_name]""{cps=20}But wait… how do I fit into this picture? I think I know what protest you two are talking about, but I just got hit with a car, and I still ended up in this strange place…!"

    crux "{cps=20}I suppose it's your turn, isn't it? Unfortunately, I have to be the bearer of bad news…"

    crux "{cps=20}While I was doing the spell, I noticed there was a magical interference that interrupted it. It all happened fast."
    
    crux "{cps=20}bright, green light shone in the distance before Black disappeared from my arms." 
    
    crux "{cps=20}I'm certain whatever — or whoever — interrupted it, unintentionally opened a rift that sent you two to this dimension."

    crux "{cps=20}Magic's a finicky thing. Even one unexpected component can disrupt an entire spell and alter it completely."

    crux "{cps=20}I have reason to believe that the interference was you."

    crux "{cps=20}This is making your head hurt."

    "Shark Teeth""{cps=20}Jumped dimensions with… us…? But not you, Crux?"

    crux "{cps=20}No. I'm not the Crux you know. Well, I am, but it's complicated." 
    
    crux "{cps=20}Everyone has copies of themselves in multiple dimensions." 
    
    crux "{cps=20}I just happen to be aware of all of mine, including the one you knew. Feel free to treat me the same way. There's no difference."

    crux "{cps=20}Speaking of this dimension, neither of you can leave, I'm afraid."

    "Shark Teeth""{cps=20}What?"

    crux "{cps=20}I'm sorry. Nobody leaves this dimension. Do you understand? This is it." 
    
    crux "{cps=20}This is the end of the road. Past here, there's nothing but void."
    
    crux "{cps=20}I suggest you both start getting used to that. You don't have a choice."