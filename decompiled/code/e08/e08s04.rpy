image e08s04-a85-1 = Movie(play = "images/E-08/s04/anim/e08s04-a85-1-2x-50fps.webm", start_image = "e08s04-a85-1 mc-fucks-arj-anim-01")
image e08s04-a85-1-f = Movie(play = "images/E-08/s04/anim/e08s04-a85-1-2x-60fps.webm", start_image = "e08s04-a85-1 mc-fucks-arj-anim-01")
image e08s04-a85-2 = Movie(play = "images/E-08/s04/anim/e08s04-a85-2-2x-50fps.webm", start_image = "e08s04-a85-2 mc-fucks-arj-anim-01")
image e08s04-a85-2-f = Movie(play = "images/E-08/s04/anim/e08s04-a85-2-2x-60fps.webm", start_image = "e08s04-a85-2 mc-fucks-arj-anim-01")
image e08s04-a85-3 = Movie(play = "images/E-08/s04/anim/e08s04-a85-3-2x-50fps.webm", start_image = "e08s04-a85-3 mc-fucks-arj-anim-01")
image e08s04-a85-3-f = Movie(play = "images/E-08/s04/anim/e08s04-a85-3-2x-60fps.webm", start_image = "e08s04-a85-3 mc-fucks-arj-anim-01")

image e08s04-a90-1 = Movie(play = "images/E-08/s04/anim/e08s04-a90-1-2x-50fps.webm", start_image = "e08s04-a90-1 mc-dunks-arj-fucking-anim-01")
image e08s04-a90-1-f = Movie(play = "images/E-08/s04/anim/e08s04-a90-1-2x-60fps.webm", start_image = "e08s04-a90-1 mc-dunks-arj-fucking-anim-01")
image e08s04-a90-2 = Movie(play = "images/E-08/s04/anim/e08s04-a90-2-2x-50fps.webm", start_image = "e08s04-a90-2 mc-dunks-arj-fucking-anim-01")
image e08s04-a90-2-f = Movie(play = "images/E-08/s04/anim/e08s04-a90-2-2x-60fps.webm", start_image = "e08s04-a90-2 mc-dunks-arj-fucking-anim-01")

image e08s04-a93-1 = Movie(play = "images/E-08/s04/anim/e08s04-a93-1-2x-50fps.webm", start_image = "e08s04-a93-1 mc-arj-dunk-harder-fuck-anim-01")
image e08s04-a93-1-f = Movie(play = "images/E-08/s04/anim/e08s04-a93-1-2x-60fps.webm", start_image = "e08s04-a93-1 mc-arj-dunk-harder-fuck-anim-01")
image e08s04-a93-2 = Movie(play = "images/E-08/s04/anim/e08s04-a93-2-2x-50fps.webm", start_image = "e08s04-a93-2 mc-arj-dunk-harder-fuck-anim-01")
image e08s04-a93-2-f = Movie(play = "images/E-08/s04/anim/e08s04-a93-2-2x-60fps.webm", start_image = "e08s04-a93-2 mc-arj-dunk-harder-fuck-anim-01")
image e08s04-a93-3 = Movie(play = "images/E-08/s04/anim/e08s04-a93-3-2x-50fps.webm", start_image = "e08s04-a93-3 mc-arj-dunk-harder-fuck-anim-01")
image e08s04-a93-3-f = Movie(play = "images/E-08/s04/anim/e08s04-a93-3-2x-60fps.webm", start_image = "e08s04-a93-3 mc-arj-dunk-harder-fuck-anim-01")

image e08s04-a97-1 = Movie(play = "images/E-08/s04/anim/e08s04-a97-1-2x-50fps.webm", start_image = "e08s04-a97-1 arj-fuck-mc-floor-anim-01")
image e08s04-a97-1-f = Movie(play = "images/E-08/s04/anim/e08s04-a97-1-2x-60fps.webm", start_image = "e08s04-a97-1 arj-fuck-mc-floor-anim-01")
image e08s04-a97-2 = Movie(play = "images/E-08/s04/anim/e08s04-a97-2-2x-50fps.webm", start_image = "e08s04-a97-2 arj-fuck-mc-floor-anim-01")
image e08s04-a97-2-f = Movie(play = "images/E-08/s04/anim/e08s04-a97-2-2x-60fps.webm", start_image = "e08s04-a97-2 arj-fuck-mc-floor-anim-01")
image e08s04-a97-3 = Movie(play = "images/E-08/s04/anim/e08s04-a97-3-2x-50fps.webm", start_image = "e08s04-a97-3 arj-fuck-mc-floor-anim-01")
image e08s04-a97-3-f = Movie(play = "images/E-08/s04/anim/e08s04-a97-3-2x-60fps.webm", start_image = "e08s04-a97-3 arj-fuck-mc-floor-anim-01")

image e08s04-a97-glambot-1 = Movie(play = "images/E-08/s04/anim/e08s04-97-04-2x-50fps.webm", start_image = "e08s04-97-04 arj-mc-fuck-bathroom-floor-anim-97-04-01_i", image = "e08s04-97-04 arj-mc-fuck-bathroom-floor-anim-97-04-79_i", loop = False)

label e08s04:

    $ e08s04_head_dunk = False

    scene black
    show screen scene_transistion(_("Next morning"))
    with Fade(0.9, 0.5, 0.5)
    pause
    $ renpy.music.set_volume(0.08, 3.0, "sound2")
    play sound2 park fadein 5.0
    hide screen scene_transistion
    play voice2 d7s6_snoring fadein 3.0
    play voice3 kanya_disappointed_snoring fadein 3.0
    scene e08s04-01 mc-arj-rj-sleep-morning-after-storm_c1
    with Fade(0.5, 0.5, 0.9)
    pause
    scene e08s04-02 mc-wakes-up_c1 with dissolve
    play voice2 mc_angry_hm2 noloop
    pause
    scene e08s04-03 mc-quietly-walks-up-to-door-looking-roof-damage_c1 with dissolve
    pause
    play sound sfx_door_slide2
    scene e08s04-04 mc-opens-barn-door_c1 with dissolve
    pause
    stop voice3 fadeout 1.5
    $ renpy.music.set_volume(0.2, 1.5, "sound2")
    $ renpy.music.set_volume(1.0, 1.5, "music")
    play music music_afterstorm_consequences fadein 3.0
    scene e08s04-05 mc-ruprised-looking-storm-damages_c1 with dissolve
    play voice2 mc_scared_huuuh3 noloop
    pause
    scene e08s04-06 farm-is-trashed_c1 with dissolve
    pause
    play sound sfx_footsteps_grass1 volume 0.6
    scene e08s04-07 mc-startled-by-woman-with-clock_c1 with dissolve
    pause
    stop sound fadeout 1.5
    scene e08s04-08 mc-approaches-woman-says-hello_c1 with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "Hello."
    scene e08s04-09 hh-informs-mc-there-was-a-storm_c1 with dissolve
    play voice4 dahlia_thinking_hmm1 noloop
    hh "Havisham."
    scene e08s04-10 mc-asks-hh-if-she-needs-help_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "Are you okay?"
    play voice4 dahlia_angry_hm1 noloop
    hh "There was a storm."
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah. I'm guessing you're from around here, but I had never seen you around in any of the town hall meetings."
    play voice4 dahlia_old_upset noloop
    hh "I am alone."
    mc "Do you need help? You shouldn't be alone right now."
    hh "When there is smoke, there is fire. When there is fire, there is rain."
    scene e08s04-11 mc-offers-water-from-barn_c1 with dissolve
    play voice2 d2s9_mchey noloop volume 1.6
    mc "Speaking of water, I'm going to grab some for you, stay here."
    mc "Or maybe you can come with me to the barn. It's right over there."
    scene e08s04-12 hh-has-no-time-water_c1 with dissolve
    play voice4 dahlia_no_serious noloop
    hh "No time."
    play voice2 d1s2_hmm noloop volume 1.5
    mc "What do you mean?"
    hh "I must be somewhere."
    scene e08s04-13 hh-tells-she-must-go-at-eight-horseflies-die_c1 with dissolve
    play voice4 dahlia_thinking_hmm3 noloop
    hh "When the clock hits eight, I'll be on my way."
    play voice2 d2s9_confused noloop
    mc "The clock isn't moving."
    hh "Did you know around this time of the month, all the horseflies die?"
    mc "Listen, Miss..."
    hh "Havisham."
    scene e08s04-14 mc-tells-hh-is-shaken-introduces-himself-by-name_c1 with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "Right. I'm [mcname]. You're a bit shaken, I can tell."
    mc "Can you tell me what happened?"
    play voice4 dahlia_thinking_mmm1 noloop
    hh "My home is gone. I have nothing left."
    hh "However, helping when I don't have anything is the most loving thing one can do."
    scene e08s04-15 mc-tells-it-will-be-a-minute-hh-should-wait-for-him_c1 with dissolve
    play voice2 mc_yes_okay2 noloop volume 1.4
    mc "Okay, you're in shock."
    mc "I'll only be a minute, one minute, and I'll be back."
    mc "So stay right here."
    play sound sfx_sand_run1
    scene e08s04-16 mc-runs-towards-barn_c1 with dissolve
    pause
    play sound sfx_paper_bag_1
    scene e08s04-17 mc-rummages-through-kit-arj-still-sleeping_c1 with dissolve
    pause
    scene e08s04-18 arj-wakes-up-asking-if-morning-already_c1 with dissolve
    play voice3 amrose_happy_mmm noloop
    arj "Mmm..."
    arj "Is it morning?"
    stop sound fadeout 1.0
    scene e08s04-19 mc-sorry-waking-arj-up-arj-asking-what-hes-doing_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "I'm sorry if I woke you."
    mc "I was just looking for something..."
    play voice3 amrose_no_nah noloop
    arj "It's okay. I was going to wake up anyway."
    arj "What are you looking for?"
    scene e08s04-20 mc-points-lady-outside-was-gonna-give-her-water_c1 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "There's a woman out there, she looks pretty beat up."
    mc "She probably needs some stuff. She says she's leaving soon."
    play voice3 amrose_arrogant_huh1 noloop
    arj "There are some eggs, we can give her a basketful."
    play sound sfx_paper_slide1
    scene e08s04-21 arj-ask-whats-the-hurry-mc-doesnt-know_c1 with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.7
    mc "Maybe we can convince her to stay."
    play voice3 amrose_arrogant_huh4 noloop
    arj "Why?"
    mc "I don't know."
    mc "I don't imagine her getting very far with that clock."
    scene e08s04-22 mc-arj-walk-out-barn-carry-bottled-water-eggs_c1 with dissolve
    pause
    scene e08s04-23 mc-arj-bring-water-eggs-to-hh_c1 with dissolve
    pause
    scene e08s04-24 mc-hands-hh-water_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Here."
    mc "Drink."
    play sound sfx_drink_loop1 volume 3.5
    scene e08s04-25 hh-drinks-whole-bottle-one-gulp_c1 with dissolve
    pause
    stop sound fadeout 1.0
    scene e08s04-26 hh-must-be-thirsty-mc-introduces-arj_c1 with dissolve
    play voice2 mc_surprised_wow2 noloop
    mc "You must have really been thirsty."
    mc "This is Amber-Rose. We're together."
    scene e08s04-27 hh-introduces-herself-arj-asking-first-or-lst-name_c1 with dissolve
    play voice3 amrose_hey_whisper noloop
    arj "Hello."
    play voice4 aaleyah_disappointed_eh1 noloop
    hh "Havisham."
    play voice2 mc_arrogant_hm2 noloop
    mc "That's her name."
    arj "Is that your first name or your surname?"
    hh "My mother's name."
    hh "She was a watchmaker."
    scene e08s04-28 its-mothers-name-arj-offers-eggs_c1 with dissolve
    play voice3 amrose_thinking_hmm1 noloop
    arj "I heard you were leaving. So before you did..."
    arj "Here."
    arj "Here's some eggs. If you need to take it home, we have enough food to tide us over."
    play voice4 aaleyah_thinking_hmm2 noloop
    hh "Eggs?"
    scene e08s04-29 arj-hands-eggs-hh_c1 with dissolve
    play voice3 amrose_arrogant_yeah1 noloop
    arj "Do you need anything else?"
    arj "What's wrong?"
    scene e08s04-30 hh-holds-eggs-in-awe_c1 with dissolve
    play voice4 aaleyah_thinking_hmm3 noloop
    hh "You would give a complete stranger your last remaining food?"
    hh "That is a kind gesture, reserved for only the happiest of occasions."
    scene e08s04-31 arj-reminds-hh-they-live-on-farm-invites-her-in_c1 with dissolve
    play voice2 d9s3_no noloop volume 1.4
    mc "Don't worry, we have more where that came from."
    play voice3 amrose_happy_laugh1 noloop
    arj "You're on a farm, after all."
    arj "It may not look like it, after last night."
    arj "Do you want to come in? You look pretty shaken up."
    play voice2 mc_angry_huh2 noloop
    mct "Why else is she talking in old-timey language?"
    play voice4 aaleyah_no_uhuh noloop
    hh "No, I must be going."
    scene e08s04-32 hh-runs-womens-shelter-mc-surprised_c1 with dissolve
    hh "I'm on my way to the women's shelter. They're waiting for me."
    hh "I'm the mother hen."
    play voice2 mc_surprised_what1 noloop
    mc "Really, you?"
    play voice3 amrose_old_chmchm noloop
    arj "[mcname]."
    scene e08s04-33 arj-shoots-angry-stare-mc_c1 with dissolve
    pause
    scene e08s04-34 hh-explains-women-waiting-to-tell-them-what-do-to_c1 with dissolve
    play voice2 d1s5b_emmm noloop volume 1.3
    mc "I mean... that's great."
    play voice4 dahlia_disappointed_hmm1 noloop
    hh "They're waiting for me to tell them what to do."
    play voice3 amrose_arrogant_huh2 noloop
    arj "What to do?"
    scene e08s04-35 hh-continues-explaining-shelter-is-destroyed-only-clock-remains_c1 with dissolve
    play voice4 dahlia_disappointed_hmm2 noloop
    hh "Everything is destroyed. There is nothing left back home."
    hh "No home."
    hh "All I managed to salvage was my clock, which is broken now."
    hh "I'll have to fix it. It's the only thing that remains now of hers."
    hh "It's a talisman."
    scene e08s04-36 mc-explains-their-phone-is-clock-asks-where-is-shelter_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "What's a talisman?"
    play voice4 aaleyah_thinking_hmm1 noloop
    hh "What helps us survive."
    play voice3 amrose_disappointed_oh3 noloop
    arj "If it's any consolation, Miss Havisham, our clock is broken too."
    play voice2 mc_arrogant_huh3 noloop
    mc "You mean our phone? It's out of charge."
    play voice3 amrose_no_simple2 noloop
    arj "No, all our clocks are broken in the house. Probably an electrical problem."
    hh "I'll bring these eggs back to the shelter."
    mc "Where is it located?"
    hh "It's a couple of miles from here. By the town library."
    scene e08s04-37 hh-answers-arj-offers-drive-there-hh-gets-car-sick_c1 with dissolve
    play voice3 amrose_thinking_hmm2 noloop
    arj "Do you want us to drive you?"
    play voice4 aaleyah_no_no1 noloop
    hh "No."
    hh "Thank you."
    hh "I get carsick."
    scene e08s04-38 hh-thanks-both-mc-and-arj_c1 with dissolve
    play voice4 aaleyah_happy_mmm1 noloop
    hh "Thank you for the eggs."
    hh "When you see me again, I hope it will be under better circumstances."
    play sound sfx_footsteps_grass1
    scene e08s04-39 hh-leaves-mc-arj-farm_c1 with dissolve
    stop sound fadeout 4.5
    pause
    scene e08s04-40 mc-asking-arj-hh-be-okay-she-doesnt-know_c1 with dissolve
    play voice2 mc_angry_huh1 noloop
    mc "That was weird."
    play voice3 amrose_yes_yeah2 noloop
    arj "Uh, yeah."
    mc "Is she going to be okay?"
    arj "I really don't know."
    play voice2 mc_arrogant_heh2 noloop
    mct "What a weird interaction that was."
    mct "She was like a ghost."
    scene e08s04-41 arj-doesnt-know-either_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "I didn't know there was a shelter around here."
    play voice3 amrose_yes_yap noloop
    arj "Me neither."
    arj "They must have been around for a while. It's weird how we've been here for more than a year and we don't know what all the buildings are."
    scene e08s04-42 mc-tells-they-dont-know-anyone-arj-suggest-they-meet-ppl_c1 with dissolve
    play voice2 mc_no_nah2 noloop
    mc "That's not that weird."
    mc "We don't really go anywhere."
    play voice3 amrose_thinking_hmm5 noloop
    arj "We should get to know our neighbors better. Not just our immediate neighbors like Ashley and Frank. Other ones outside our immediate vicinity."
    mc "We might have to."
    play sound sfx_bed_slide3 volume 0.5
    scene e08s04-43 mc-says-house-took-no-damage-arj-hopes-same-inside_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Our house looks okay, somehow."
    play voice3 amrose_yes_confident1 noloop
    arj "I hope it's the same story inside."
    mc "Yeah."
    scene e08s04-44 arj-asks-chance-of-electricity-mc-says-none_c1 with dissolve
    play voice3 amrose_disappointed_ehh2 noloop
    arj "What are the chances the electricity is on?"
    play voice2 mc_disappointed_ehh4 noloop
    mc "About zero. Same with the water, and the internet."
    mc "It'll probably take a couple of days for it to be restored."
    scene e08s04-45 arj-asks-what-they-do-in-meantime_c1 with dissolve
    play voice3 amrose_arrogant_huh3 noloop
    arj "What do we do in the meantime?"
    play voice2 mc_thinking_mmm5 noloop
    mc "Let's check how much food we have."
    scene e08s04-46 mc-suggest-boiling-water-arj-agrees-will-get-rj_c1 with dissolve
    mc "Then we can start boiling some water, so we can take a bath together, because I really need one."
    mc "We'll clean around the house. There's not much we can do out here that we haven't taken care of yesterday."
    play voice3 amrose_yes_okay1 noloop
    arj "Alright."
    arj "I'll get Remy."
    stop sound2 fadeout 2.0
    play sound sfx_water_pouring1 fadein 1.5
    scene e08s04-47 arj-mc-fill-tub-with-pots_c1 with dissolve
    stop sound fadeout 3.0
    pause
    scene e08s04-48 mc-doesnt-think-its-enought-arj-agrees_c1 with dissolve
    play voice2 mc_no_uhuh1 noloop
    mc "I don't think we have enough."
    play voice3 amrose_yes_ugu noloop
    arj "Definitely not."
    mc "How much do we need?"
    arj "I'm not sure."
    scene e08s04-49 arj-not-sure-asking-if-they-use-pot-measurements_c1 with dissolve
    play voice3 amrose_thinking_hmm4 noloop
    arj "Are we using pots as the measurement?"
    play voice2 mc_yes_yeah2 noloop
    mc "I suppose so."
    arj "We need like two more runs."
    $ renpy.music.set_volume(1.0, 0.0, "sound4")
    $ renpy.music.set_volume(1.0, 0.0, "sound5")
    $ renpy.music.set_volume(1.0, 0.0, "sound3")
    $ renpy.music.set_volume(0.5, 0.0, "sound2")
    scene e08s04-50 mc-arj-hear-knocking-on-door_c1 with dissolve
    call knock from _call_knock_13
    play voice2 mc_arrogant_heh1 noloop
    mc "I'll get it."
    play sound sfx_door_open1
    scene e08s04-51 mc-opens-door-worried-face_c1 with Fade(0.3, 0.3, 0.3)
    play voice2 mc_surprised_huh5 noloop
    mc "Oh my God."
    mc "What's wrong?"
    play voice5 claudie_sex_closedmoan4 noloop
    scene e08s04-52 fc-ac-need-help_c1 with dissolve
    play voice4 boy5_pain_ehh2 noloop
    fc "We need some help."
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, come in."
    mct "Thankfully we stocked the first aid kit before the storm."
    play sound sfx_door_closed2
    scene e08s04-53 fc-puts-ac-on-couch_c1 with dissolve
    pause
    play sound sfx_bed_fall1
    scene e08s04-54 mc-asking-what-happened_c1 with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "What happened?"
    play voice4 boy5_disappointed_oh2 noloop
    fc "Don't worry, we're fine."
    fc "Will you know it, our barn exploded."
    play voice2 mc_pain_ou1 noloop
    mc "Exploded?"
    scene e08s04-55 fc-tells-barn-exploaded-in-rain-ac-passed-out_c1 with dissolve
    play voice4 boy5_arrogant_pff noloop
    fc "Boom. During the storm, no less."
    fc "We weren't inside, thankfully."
    fc "Ashley passed out though, the destruction of our farm, the stress just put her over the edge."
    play voice2 d2s12_emmm noloop volume 1.4
    mc "Do you have a place to go?"
    scene e08s04-56 fc-asks-to-stay-over-mc-tells-him-ofcourse_c1 with dissolve
    play voice4 boy5_no_simple noloop
    fc "I was hoping you could do us a favor."
    play voice2 mc_yes_sure1 noloop
    mc "Of course, you guys can stay here."
    mc "The basement is flooded, so you'll have to stay in the living room. Is that okay?"
    play sound sfx_cloth_rustling2
    scene e08s04-57 fc-accepts-staying-in-living-room-mc-will-let-arj-know_c1 with dissolve
    play voice4 boy5_yes_simple noloop
    fc "That's perfectly acceptable."
    fc "Any place with a couch and working kitchen is more than enough."
    play voice2 mc_yes_aga2 noloop
    mc "Alright, because it can get a little chilly here."
    mc "I'll let AmRose know."
    scene e08s04-58 fc-thanks-mc-again-mc-tells-no-worries_c1 with dissolve
    play voice4 boy5_hey_calm noloop
    fc "Hey, [mcname]. Thanks again."
    play voice2 mc_no_nah1 noloop
    mc "Don't worry about it."
    play sound sfx_heels_steps2
    scene e08s04-59 arj-walks-down-stairs_c1 with dissolve
    stop sound fadeout 2.0
    pause
    scene e08s04-60 arj-sees-ac-on-couch_c1 with dissolve
    pause
    scene e08s04-61 arj-scared-for-ac-fc-tells-shes-fine_c1 with dissolve
    play voice3 amrose_surprised_ohmy noloop
    arj "Oh my God, is she okay?"
    play voice2 mc_hey_hey2 noloop
    mc "Hey, AmRose, these two are staying here."
    play voice4 boy5_yes_questioning noloop
    fc "She's fine, AmRose. Just needs a bit of rest, if you don't mind our imposition."
    arj "No, of course not."
    scene e08s04-62 arj-offers-fc-ac-take-bath-first_c1 with dissolve
    play voice3 amrose_thinking_emm noloop
    arj "We were just going to take a bath."
    arj "You guys can go first if you want."
    scene e08s04-63 fc-insist-arj-mc-go-first_c1 with dissolve
    play voice4 boy5_no_nonono noloop
    fc "No, no, you've done enough by letting us stay."
    fc "You guys go ahead."
    play voice3 amrose_thinking_hmm3 noloop
    arj "Are you sure?"
    play voice4 boy5_yes_active noloop
    fc "Sure, sure. Go on."
    fc "We'll be okay here."
    scene e08s04-64 mc-explains-where-suplies-are_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "If you need anything else, let us know."
    mc "Medical supplies should be all in the pantry. Water's unaffected, it's still running."
    play voice4 boy5_yes_ugu noloop
    fc "Got it."
    play sound sfx_cloth_rustling3

    jump e08s04_bathtub

label replay_e08s04:
label e08s04_bathtub:

    scene e08s04-65 mc-arj-head-for-bathroom_c1 with dissolve
    pause
    scene e08s04-66 arj-bath-not-full-but-its-been-two-days_c1 with dissolve
    play voice3 amrose_arrogant_hmm2 noloop
    arj "I think we're still one pot short, and the water's not as hot as we'd like it."
    arj "But it has been two days."
    play voice2 mc_yes_yeah5 noloop volume 0.7
    mc "And we are filthy."
    play sound sfx_shoes_off1
    scene e08s04-67 arj-entering-bath-mc-to-follow_c1 with dissolve
    pause
    play sound sfx_bath_in1
    play sound3 sfx_bath_waterplay1 fadein 5.0
    scene e08s04-68 mc-arj-in-bathtub_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Ahh..."
    play voice3 amrose_angry_breath1 noloop
    arj "It's still warm."
    mc "We should wash Remy too."
    scene e08s04-69 arj-surprised-mc-wants-wash-dog-now_c1 with dissolve
    play voice3 amrose_old_wow noloop
    arj "What, now?"
    play voice2 mc_no_no2 noloop
    mc "No, after Frank and Ashley."
    arj "What happened to her?"
    scene e08s04-70 mc-explains-cooper-barn-exploaded_c1 with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "Their barn exploded."
    play voice3 amrose_surprised_uh5 noloop
    arj "Really?"
    mc "Yeah."
    scene e08s04-71 arj-tries-to-understand-barn-exploading_c1 with dissolve
    play voice3 amrose_surprised_oh4 noloop
    arj "Exploded? That's a lot to take in."
    arj "Did Ashley get hurt?"
    play voice2 mc_no_no1 noloop
    mc "No. She collapsed apparently, due to the burden of it all."
    mc "Sounds like an ulcer brought on by stress."
    scene e08s04-72 arj-feels-sorry-for-fc_c1 with dissolve
    play voice3 amrose_old_upset noloop volume 1.3
    arj "I feel so sorry for her, and Frank. They've been here a lot longer than us, but we came out relatively unscathed."
    arj "Were we just lucky?"
    play voice2 mc_disappointed_ehh2 noloop
    mc "At least everyone is okay."
    scene e08s04-73 mc-not-worried-for-neighbours-but-worried-about-hh_c1 with dissolve
    mc "But that Havisham lady has seen better days."
    play voice3 amrose_thinking_oh1 noloop
    arj "We can probably go for a visit downtown, and see if they have any supplies left. Maybe we can get something for the shelter."
    play voice2 mc_yes_sure1 noloop
    mc "Sure."
    $ renpy.music.set_volume(0.4, 5.5, "music")
    stop music fadeout 4.0
    scene e08s04-74 mc-sure-go-shelter-later-now-offers-arj-sex_c1 with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "In the meantime, how about we, you know..."
    play voice3 amrose_surprised_uh4 noloop
    queue music music_horny_upstairs
    arj "Really?"
    mc "Why not?"
    scene e08s04-75 mc-asking-why-not-arj-tells-mc-gets-horny-wierdest-moments_c1 with dissolve
    play voice3 amrose_angry_ehh noloop
    arj "You get aroused at the weirdest moments."
    play voice2 mc_surprised_huh6 noloop
    mc "Are you worried that they might hear us?"
    scene e08s04-76 arj-worried-ac-fc-will-hear_c1 with dissolve
    play voice3 amrose_yes_confident2 noloop
    arj "They {i}will{/i} hear us."
    play voice2 mc_thinking_mmm2 noloop
    mc "It's just that seeing you as such a caring and loving person makes me want to share in that love, is that so weird?"
    arj "A little bit."
    scene e08s04-77 arj-agrees-sex-but-quiet-mc-wants-try-new_c1 with dissolve
    play voice3 amrose_angry_ergh noloop
    arj "Alright. Let's do it, but let's not be too loud. We don't want to wake up Ashley."
    play voice2 mc_happy_a1 noloop
    mc "Why don't we try something new?"
    scene e08s04-78 arj-asking-what-does-mc-have-in-mind_c1 with dissolve
    play voice3 amrose_arrogant_huh1 noloop
    arj "What do you have in mind?"
    play voice2 mc_thinking_mmm1 noloop
    mc "Let me show you."
    play sound3 sfx_water_floatup1 noloop
    scene e08s04-79 arj-positions-hererself-wierd-way_c1 with dissolve
    pause
    scene e08s04-80 arj-worried-if-she-will-fall_c1 with dissolve
    play voice3 dahlia_sex_closedmoan1 noloop
    arj "I hope I don't fall."
    play voice2 mc_happy_yay2 noloop
    mc "Don't worry, just hold on to the bath."
    scene e08s04-81 arj-holds-bathtub-asking-if-mc-sure_c1 with dissolve
    play voice3 amrose_arrogant_huh4 noloop
    arj "Are you sure about this?"

    menu:
        "Dunk her head in the water"(hint="e08s04m01c01"):
            $ e08s04_head_dunk = True

            scene e08s04-82 mc-choice_c1 with dissolve
            play voice2 mc_thinking_hmm1 noloop
            mc "Before we do this, we should pick a safe word."
            play voice3 amrose_arrogant_hmm1 noloop
            arj "Well, it doesn't really make sense to have a safe word seeing as how my head will be underwater."
            mc "Okay, so how are you going to let me know?"
            scene e08s04-83 arj-safeword-will-be-middle-finger_c1 with dissolve
            play voice3 amrose_surprised_oh1 noloop
            arj "Fuck you!"
            play voice2 mc_surprised_what3 noloop
            mc "What?"
            play voice3 amrose_happy_laugh2 noloop
            arj "If I don't fall, or flail around, I guess a middle finger directed at you?"
            arj "Stick it."
            play voice2 mc_yes_okay3 noloop
            mc "Works for me."
        "Don't dunk her head in the water"(hint="e08s04m01c02"):

            pass

    $ Lovense.stop()

    $ Lovense.vibrate(1)
    scene e08s04-84 mc-ready-to-enter-arj_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Alright, hold on tight."
    play voice3 amrose_surprised_uh3 noloop
    arj "Wait, you're just going in?"
    play voice2 mc_yes_yeah4 noloop
    mc "It's a little late for foreplay, isn't it?"
    $ Lovense.vibrate(3)
    scene e08s04-85 mc-fucks-arj-anim_c1 with dissolve
    play voice3 amrose_surprised_uh2 noloop
    arj "Ahh! I don't know."
    arj "Are you sure?"
    $ Lovense.vibrate(5)
    scene e08s04-a85-1 mc-fucks-arj-anim-01 with dissolve
    play voice3 dahlia_sex_closedmoan2 noloop
    arj "Mmfph!"
    $ renpy.music.set_volume(0.6, 2.5, "music")
    play voice3 daisy_moaning
    play voice2 d7s4_mcbreathing fadein 1.5
    $ Lovense.pattern("6;10", 1700)
    scene e08s04-a85-1
    pause
    scene e08s04-a85-2 with dissolve
    pause
    scene e08s04-a85-3 with dissolve
    pause
    play voice3 amrose_old_moaning2
    $ Lovense.pattern("6;10", 900)
    scene e08s04-a85-1-f with dissolve
    pause
    scene e08s04-a85-2-f with dissolve
    pause
    scene e08s04-a85-3-f with dissolve
    pause
    stop voice3 fadeout 1.0
    $ Lovense.stop()
    $ Lovense.vibrate(3)
    scene e08s04-86 mc-asking-if-they-fucked-here-arj-tells-probably_c1 with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "Have we fucked in a bathroom before?"
    play voice3 amrose_angry_breath2 noloop
    arj "We must have."
    arj "Right?"
    play voice2 mc_arrogant_heh2 noloop
    mc "Not with guests."
    scene e08s04-87 arj-lists-locations-mc-asks-when-lst-time_c1 with dissolve
    play voice3 amrose_thinking_hmm1 noloop
    arj "At parties, near pools, in front of guests."
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "When's the last time we had one of those?"
    play voice3 amrose_old_moaning noloop
    scene e08s04-88 arj-being-loud-mc-want-to-be-quiet_c1 with dissolve
    stop voice3 fadeout 1.5
    arj "I don't remember. Ahh fuck."
    play voice2 mc_angry_cough1 noloop
    mc "You're being too loud."
    arj "I can't help you fucking me so good."
    if e08s04_head_dunk is True:
        scene e08s04-89 mc-asking-if-dunking-would-help_c1 with dissolve
        play voice2 mc_angry_hm1 noloop
        mc "If you have a dunk, will you settle down?"
        play voice3 amrose_thinking_hmm5 noloop
        arj "Let me give it a try."
        play sound sfx_water_dive1
        scene e08s04-a90-1 mc-dunks-arj-fucking-anim-01 with dissolve
        pause
        play voice2 d7s4_mcbreathing fadein 1.5
        play voice3 amrose_old_moaning_underwater
        $ Lovense.pattern("8;12", 1700)
        scene e08s04-a90-1
        pause
        scene e08s04-a90-2 with dissolve
        pause
        play voice3 amrose_old_moaning3_underwater
        $ Lovense.pattern("8;12", 900)
        scene e08s04-a90-1-f with dissolve
        pause
        scene e08s04-a90-2-f with dissolve
        pause
        play voice3 amrose_angry_breath2 noloop
        play sound sfx_water_dive1
        $ Lovense.stop()
        $ Lovense.vibrate(5)
        scene e08s04-91 mc-bring-arj-for-some-air-asking-how-is-it-she-jokes-he-fucks-soft_c1 with dissolve
        play voice2 mc_happy_oof3 noloop
        mc "How was that?"
        arj "Good."
        arj "Let me get another look down there. I think I almost found it."
        play voice2 mc_surprised_what1 noloop
        mc "What?"
        play voice3 amrose_arrogant_huh3 noloop
        arj "Your balls."
        play voice2 mc_angry_errr4 noloop
        play sound sfx_water_run2
        scene e08s04-90 mc-dunks-arj-head-in-tub-fucking-her-anim_c2 with vpunch
        stop sound fadeout 5.0
        pause
        play voice3 samiya_mfff noloop
        scene e08s04-92 mc-pushes-arj-back-under-water_c1 with dissolve
        pause
        scene e08s04-a93-1 mc-arj-dunk-harder-fuck-anim-01 with dissolve
        pause
        play voice2 d7s4_mcbreathing fadein 1.5
        play voice3 amrose_old_moaning4_underwater
        $ Lovense.pattern("9;14", 1700)
        scene e08s04-a93-1
        pause
        scene e08s04-a93-2 with dissolve
        pause
        scene e08s04-a93-3 with dissolve
        pause
        $ Lovense.pattern("9;14", 900)
        scene e08s04-a93-1-f with dissolve
        pause
        scene e08s04-a93-2-f with dissolve
        pause
        scene e08s04-a93-3-f with dissolve
        pause
        $ Lovense.stop()
        $ Lovense.vibrate(5)
        play voice3 amrose_pain_coughs noloop
        play voice2 d1s5_orgasm noloop
        play sound sfx_water_out1
        scene e08s04-94 mc-finally-lets-arj-take-another-breath_c1 with dissolve
        arj "Huff... huff..."
        arj "That was too rough."
        arj "I almost lost consciousness."
        scene e08s04-95 mc-asking-why-not-using-safeword_c1 with dissolve
        play voice2 mc_happy_hah1 noloop
        mc "You didn't use your safe word."
        play voice3 amrose_angry_ugh noloop
        arj "Because it felt so good and weird."
        play voice2 mc_thinking_hmm2 noloop
        mc "Do you want to do it again?"
        scene e08s04-96 arj-flips-mc-off_c1 with dissolve
        play voice3 amrose_happy_laugh3 noloop
        arj "I usually don't like new things."
        arj "But this is great."
        arj "I love trying out new things with you."
    play sound ["<silence 0.3>", sfx_fall_mud1]
    scene e08s04-97-04 arj-mc-fuck-bathroom-floor-anim-97-04-01_i with fade
    pause
    play sound sfx_camera_fly1 volume 2.0
    scene e08s04-a97-glambot-1
    pause
    scene e08s04-a97-1 arj-fuck-mc-floor-anim-01 with dissolve
    play voice2 d1s2_mchey noloop volume 1.5
    mc "It's like our honeymoon again."
    play voice3 amrose_arrogant_yeah2 noloop
    queue voice3 daisy_moaning
    play voice2 d7s4_mcbreathing fadein 1.5
    $ Lovense.pattern("9;14", 1700)
    scene e08s04-a97-1
    arj "Under the most fucked up situation imaginable, but yeah, just like our honeymoon."
    pause
    scene e08s04-a97-2 with dissolve
    pause
    scene e08s04-a97-3 with dissolve
    pause
    play voice3 amrose_old_moaning2
    $ Lovense.pattern("9;14", 900)
    scene e08s04-a97-1-f with dissolve
    pause
    scene e08s04-a97-2-f with dissolve
    mc "I love you."
    arj "I love you back."
    pause
    scene e08s04-a97-3-f with dissolve
    pause
    stop voice3 fadeout 1.0
    $ Lovense.stop()
    $ Lovense.vibrate(5)
    scene e08s04-98 arj-loves-this-more-than-rough_c1 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.6
    mc "I hope we don't get a cold from this."
    scene e08s04-99 mc-arj-both-say-love-you_c1 with dissolve
    play voice3 amrose_disappointed_pff noloop
    arj "That's what you're worried about?"
    play voice2 mc_hey_hey3 noloop
    mc "Having a cold is no joke."
    play sound sfx_door_creak4
    scene e08s04-100 fc-peeking-mc-arj-having-sex_c1 with dissolve
    pause
    play voice2 mc_pain_mff1 noloop
    scene e08s04-101 arj-startled-by-noise_c1 with dissolve
    play voice3 amrose_surprised_huh3 noloop
    arj "What was that?"
    play sound sfx_barefoot_steps1 volume 4.0
    $ Lovense.vibrate(1)
    scene e08s04-102 mc-goes-to-check-door_c1 with dissolve
    pause
    play sound sfx_door_creak1 volume 1.6
    scene e08s04-103 mc-checks-no-one-there_c1 with dissolve
    pause
    play sound sfx_door_closed1 volume 1.3
    scene e08s04-104 mc-says-must-been-dog-want-another-round_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Nothing. It was probably Remy."
    play voice3 amrose_thinking_oh2 noloop
    arj "Is she okay?"
    play voice2 d9s2_yeah noloop volume 1.6
    mc "She's fine. Let's go again."
    $ unlock_gallery_slot("scene", "e08s04")
    scene e08s04-105 arj-tells-mc-turn-tp-hold-bath_c1 with dissolve
    play voice3 amrose_happy_laugh6 noloop
    arj "Alright. This time, you're holding onto the bath."
    play voice2 d1s2_hmm noloop volume 1.7
    mc "What are you going to do?"
    arj "I got a few ideas."

    $ Lovense.stop()
    $ renpy.end_replay()

    jump e08s04_next_morning

label e08s04_next_morning:

    stop music fadeout 4.5
    scene black
    show screen scene_transistion(_("The next morning"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play voice2 d7s6_snoring fadein 5.0
    scene e08s04-106 mc-wakes-up-bed-alone_c1
    with Fade(0.5, 0.5, 0.5)
    pause
    play voice2 d14s16_smell noloop
    scene e08s04-107 mc-opens-eyes-see-note_c1 with dissolve
    pause
    play sound sfx_paper_slide1
    scene e08s04-108 mc-reads-note-from-arj_c1 with dissolve
    pause
    play voice2 mc_happy_a1 noloop
    play sound sfx_jeans_on1
    scene e08s04-109 mc-dressed-check-mirror_c1 with dissolve
    play music relaxing_ballad
    pause
    $ renpy.music.set_volume(0.08, 3.0, "sound2")
    play sound2 park fadein 5.0
    play sound sfx_door_slide2 volume 2.0
    scene e08s04-110 mc-gets-inside-barn_c1 with dissolve
    pause
    scene e08s04-111 arj-greets-mc_c1 with dissolve
    play voice3 amrose_hey_attention noloop
    arj "Morning. Did you like your breakfast?"
    play voice2 mc_yes_yes2 noloop
    mc "I did. How come you didn't wake me?"
    scene e08s04-112 mc-had-breakfast-arj-not-wake-up-peaceful_c1 with dissolve
    play voice3 amrose_disappointed_oh1 noloop
    arj "You looked so peaceful."
    scene e08s04-113 mc-his-job-let-arj-sleep_c1 with dissolve
    play voice2 d2s9_mchey noloop volume 1.4
    mc "That's my job, I'm supposed to let you sleep in."
    play voice3 amrose_happy_laugh3 noloop
    arj "Maybe next time."
    scene e08s04-114 mc-asking-arj-why-holding-wheel_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Why are you holding a wheel?"
    play voice3 amrose_thinking_hmm3 noloop
    arj "It's actually a spoke."
    mc "Are you thinking about opening a garage or something?"
    arj "No, we need to clean this place up."
    scene e08s04-115 arj-stockpiling-supplies-wants-start-helping_c1 with dissolve
    play voice3 amrose_disappointed_ehh2 noloop
    arj "We'll need to stockpile supplies and clean up."
    arj "I think it's a good time to start thinking about helping out the community."
    play voice2 mc_yes_yeah4 noloop
    mc "I agree."
    arj "We need to start as soon as possible, and distribute what we have on the farm."
    scene e08s04-116 mc-wonder-all-of-sudden-arj-saw-fliers_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Where's this coming from all of a sudden?"
    mc "You're being really assertive. I think I like it."
    play voice3 amrose_arrogant_huh2 noloop
    arj "When I was picking up supplies, I saw some posted signs, there's some aid organizations in town."
    scene e08s04-117 arj-figured-red-cross-in-town-going-to-pick-supplies_c1 with dissolve
    arj "International Red Cross, Médecins Sans Frontières..."
    arj "I figured if they're in town, the storm must have affected our town quite substantially."
    play voice2 mc_yes_ugu1 noloop
    mc "That's true."
    mc "Stockpiling some supplies is probably a good idea anyway."
    mc "The helping out part is part of our duty now, isn't it?"
    scene e08s04-118 arj-hands-wheel-mc_c1 with dissolve
    play voice3 amrose_yes_okay2 noloop
    arj "I'm going to the shop to pick up some supplies."
    arj "You can get started with the refurnishing."
    arj "Here."
    play sound sfx_kick_leg1 volume 0.5
    scene e08s04-119 arj-leaving-mc-standing-behind-her_c1 with dissolve
    play voice2 d2s12_emmm noloop volume 1.3
    mc "Is this for the tractor? I mean, this is kinda old-fashioned."
    play voice3 amrose_no_nah noloop
    arj "Get rid of it."

    scene e08s04-120 transition-mc-calling-remy_c1 with Fade(0.5, 0.5, 0.5)
    play voice2 mc_hey_hey4 noloop
    mc "Remy!"
    mc "Where are you?"
    mct "Where is this dog? Sleeping again?"
    play sound dog_playing1
    scene e08s04-121 remy-running-towards-mc_c1 with dissolve
    stop sound fadeout 2.5
    pause
    play sound dog_licking1
    scene e08s04-122 remmy-licking-mc_c1 with dissolve
    play voice2 d4s4_mclaugh noloop
    mc "Can you stay here and give me moral support?"
    stop sound fadeout 1.5
    mct "Look at me, I'm talking to a dog."
    play sound dog_bark6
    scene e08s04-123 remy-barks-mc-agrees_c1 with dissolve
    pause
    play voice2 mc_arrogant_huh1 noloop
    mc "Atta, girl."
    mc "At least she understands me."
    mct "I think."
    play sound sfx_heels_steps1
    scene e08s04-124 mc-notices-fc-carrying-heavy-stuff_c1 with dissolve
    play voice2 mc_surprised_wow1 noloop
    mc "Hey, whoa, whoa whoa."
    play sound sfx_sand_jump1
    scene e08s04-125 mc-goes-help-fc_c1 with dissolve
    play voice2 d3s7_mcemm noloop volume 1.3
    mc "What are you doing?"
    play voice4 boy5_thinking_huh noloop
    fc "I'm helping."
    play voice2 mc_yes_yeah8 noloop
    mc "How come?"
    fc "Because the dog woke me up, and I need something to do."
    mc "You're pushing yourself too hard. You're taking care of Ashley, I mean you're barely sleeping."
    scene e08s04-126 fc-tells-mc-not-worry-about-him_c1 with dissolve
    play voice4 boy5_no_nah noloop
    fc "Don't worry about me."
    fc "I can't just sit by and not help."
    scene e08s04-128 mc-fc-carry-wood-talking-each-other_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Shouldn't you be taking care of your wife? You have your hands full."
    play voice4 boy5_thinking_hmm3 noloop
    fc "She's sleeping."
    scene e08s04-129 mc-fc-laugh_c1 with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "Alright, just don't burn yourself out. I can't afford to take care of both you and Ashley."
    play voice4 boy5_yes_yep noloop
    fc "Fair enough. Don't worry, I have a strong constitution."
    fc "So, whose idea was it, anyway? Setting up the shelter."
    play voice2 mc_thinking_hmm4 noloop
    mc "AmRose. She's been watching the news every night on my phone, and helping out at the women's shelter at the crack of dawn."
    play voice4 boy5_surprised_oh1 noloop
    fc "I'm guessing that's where she's at now."
    play sound dog_bark1
    scene e08s04-130 remy-barks-again_c1 with dissolve
    pause
    scene e08s04-131 mc-explains-place-flooded-other-shelters-full_c1 with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Apparently the whole place is flooded, according to her. She's helping with getting the water out and directing people here."
    play voice4 boy5_thinking_hmm2 noloop
    fc "What about the other shelters?"
    mc "They're all full."
    play sound sfx_bed_slide3
    scene e08s04-132 mc-asking-why-whould-farmer-know-about-floods_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "We need to help the others."
    mc "I wish I took a class on dealing with acts of God."
    play voice4 boy5_hey_calm noloop
    fc "You're a farmer."
    play voice2 mc_no_uhuh1 noloop
    mc "I wasn't always a farmer. I'm college-educated, you know?"
    play voice4 boy5_arrogant_hm noloop
    fc "Really? You didn't seem like the college-going type."
    fc "Anyway, don't worry too much. We're all figuring it out on our own time."
    play voice2 mc_yes_aga1 noloop
    mc "Thanks for the advice."
    scene e08s04-133 mc-jokes-not-even-owning-driveway_c1 with dissolve
    play voice2 d2s9_confused noloop
    mc "What are the chances of us needing a huge wheel spoke?"
    play sound sfx_bed_slide2
    scene e08s04-134 mc-thinks-odds-car-blown-by-storm_c1 with dissolve
    play voice4 boy5_arrogant_hah noloop
    fc "I would throw it out."
    scene e08s04-135 fc-knows-mc-doing-his-best_c1 with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.7
    mc "The others can pitch the tents we bought."
    play voice4 boy5_yes_aga noloop
    fc "Got it, chief."
    mct "The hard part's over, and now the real work begins."
    scene e08s04-136 mc-fc-leave-talking-campsites-shelter-ready_c1 with dissolve
    pause

    scene e08s04-137 crowd-gathered-mc-arj-front_c1 with Fade(0.5, 0.5, 0.5)
    pause
    play voice3 boy5_happy_mmm1 noloop
    play voice4 terrell_yay noloop
    play voice5 claudie_happy_mmm1 noloop
    scene e08s04-138 pov-crowd-happy_c1 with dissolve
    pause
    play sound dog_bark2
    scene e08s04-139 mc-smiles-back_c1 with dissolve
    pause
    play voice3 aaleyah_happy_mmm1 noloop
    scene e08s04-140 hh-watching-eerie-expression_c1 with dissolve
    pause
    scene e08s04-141 hh-leaves_c1 with dissolve
    pause

    stop sound2 fadeout 3.0
    jump e08s05

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
