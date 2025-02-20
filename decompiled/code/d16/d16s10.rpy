image d16s10_mc_spin_arj_1 = Movie(play = "images/Day-16/Scene-10/anim/d16s10-a1-2x-50fps.webm", start_image = "d16s10-00-a1 arj-spin-anim-1-00")
image d16s10_mc_spin_arj_1_slow = Movie(play = "images/Day-16/Scene-10/anim/d16s10-a1-4x-60fps.webm", start_image = "d16s10-00-a1 arj-spin-anim-1-00")
image d16s10_mc_spin_arj_2 = Movie(play = "images/Day-16/Scene-10/anim/d16s10-a2-2x-50fps.webm", start_image = "d16s10-00-a2 arj-spin-anim-2-00_i")
image d16s10_mc_spin_arj_2_slow = Movie(play = "images/Day-16/Scene-10/anim/d16s10-a2-4x-60fps.webm", start_image = "d16s10-00-a2 arj-spin-anim-2-00_i")
image d16s10_mc_spin_arj_3 = Movie(play = "images/Day-16/Scene-10/anim/d16s10-a3-2x-50fps.webm", start_image = "d16s10-00-a3 arj-spin-anim-3-00_i")
image d16s10_mc_spin_arj_3_slow = Movie(play = "images/Day-16/Scene-10/anim/d16s10-a3-4x-60fps.webm", start_image = "d16s10-00-a3 arj-spin-anim-3-00_i")
image d16s10_arj_spin_mc_1 = Movie(play = "images/Day-16/Scene-10/anim/d16s10-a5-2x-50fps.webm", start_image = "d16s10-00-a5 mc-spin-anim-5-00_i")
image d16s10_arj_spin_mc_1_slow = Movie(play = "images/Day-16/Scene-10/anim/d16s10-a5-4x-60fps.webm", start_image = "d16s10-00-a5 mc-spin-anim-5-00_i")
image d16s10_arj_spin_mc_2 = Movie(play = "images/Day-16/Scene-10/anim/d16s10-a6-2x-50fps.webm", start_image = "d16s10-00-a6 mc-spin-anim-6-00_i")
image d16s10_arj_spin_mc_2_slow = Movie(play = "images/Day-16/Scene-10/anim/d16s10-a6-4x-60fps.webm", start_image = "d16s10-00-a6 mc-spin-anim-6-00_i")
image d16s10_arj_spin_mc_3 = Movie(play = "images/Day-16/Scene-10/anim/d16s10-a7-2x-50fps.webm", start_image = "d16s10-00-a7 mc-spin-anim-7-00_i")
image d16s10_arj_spin_mc_3_slow = Movie(play = "images/Day-16/Scene-10/anim/d16s10-a7-4x-60fps.webm", start_image = "d16s10-00-a7 mc-spin-anim-7-00_i")
image d16s10_arj_squirting_1 = Movie(play = "images/Day-16/Scene-10/anim/d16s10-a1-2-2x-50fps.webm", start_image = "d16s10-00-a1 arj-spin-anim-1-00")
image d16s10_arj_squirting_2 = Movie(play = "images/Day-16/Scene-10/anim/d16s10-a4-o-2x-50fps.webm", start_image = "d16s10-00-a4 arj-spin-anim-4-000")
image d16s10_mc_cumming_1 = Movie(play = "images/Day-16/Scene-10/anim/d16s10-a5-o-2x-50fps.webm", start_image = "d16s10-00-a6 mc-spin-anim-6-00_i")
image d16s10_mc_cumming_2 = Movie(play = "images/Day-16/Scene-10/anim/d16s10-a8-o-2x-50fps.webm", start_image = "d16s10-00-a8 mc-spin-anim-8-000")

label replay_d16s10:
label d16s10:

    $ d16s10_talk_future = False
    $ d16s10_points = 12

    if not _in_replay:
        scene black
        show screen scene_transistion(_("Later that evening"))
        with Fade(0.9, 0.5, 0.5)
        pause
        play sound sfx_door_closed9
        hide screen scene_transistion
        scene d16s10-01 mc-arj-room-talk1_c2
        with Fade(0.5, 0.5, 0.9)
        $ renpy.music.set_volume(0.5, 3.0, "music")
        play music lofi_evening fadein 1.8
        pause
        play voice2 mc_thinking_hmm4 noloop
        mc "I should probably call Lydia in a little while."
    else:
        $ renpy.music.set_volume(0.5, 3.0, "music")
        play music lofi_evening fadein 1.8
    scene d16s10-01 mc-arj-room-talk1_c1 with dissolve
    play voice3 amrose_arrogant_hmm2 noloop
    arj "You really talk to her every night?"
    scene d16s10-01 mc-arj-room-talk1_c2 with dissolve
    play voice2 d9s2_yeah volume 1.5 noloop
    mc "Pretty much."
    scene d16s10-02 mc-arj-room-talk2_c1 with dissolve
    arj "What do you talk about?"
    mc "Usually? Whatever I fucked that day."
    scene d16s10-03 mc-arj-room-talk3_c1 with dissolve
    play voice3 amrose_surprised_huh2 noloop
    arj "What? Not who?"
    play voice2 d2s12_emmm noloop
    mc "Sorry, I misspoke. Whomever I fucked."
    scene d16s10-04 mc-arj-room-talk4_c1 with dissolve
    play voice3 amrose_happy_laugh2 noloop
    arj "I mean, if you're into-"
    play voice2 mc_no_no4 noloop
    mc "NO."
    play voice3 amrose_yes_okay1 noloop
    arj "Okay."
    scene d16s10-42 mc-arj-room-chair_c1 with dissolve
    play voice2 d1s2_hmm volume 1.5 noloop
    mc "Did you get a new chair?"
    scene d16s10-42 mc-arj-room-chair_c2 with dissolve
    play voice3 amrose_yes_yeah1 noloop
    arj "Yeah, it arrived the other day. Those hard wooden chairs were killing me."
    play sound sfx_bed_slide3 volume 0.4
    scene d16s10-05 mc-arj-room-talk5_c1 with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "That's a nice office chair... are you starting a business or something?"
    scene d16s10-06 mc-arj-room-talk6_c1 with dissolve
    play voice3 amrose_arrogant_hmm1 noloop
    arj "It's comfortable.{w}.. and I wanted something for when I play games on my laptop."
    mc "Really? What kind of games?"
    scene d16s10-07 mc-arj-room-talk7_c1 with dissolve
    arj "4X strategy games mostly. Stellaris, Civilization, that kinda thing."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh."
    scene d16s10-08 mc-arj-room-talk8_c1 with dissolve
    play voice3 amrose_yes_ugu noloop
    arj "I also like factory games. They're a lot like working with computer hardware."
    play voice2 mc_yes_okay2 noloop
    mc "Oh, okay. I should've guessed that we don't play the same stuff."
    scene d16s10-09 mc-arj-room-talk9_c1 with dissolve
    play voice3 amrose_happy_mmm noloop
    arj "I'm guessing you just play first person shooters."
    play voice2 mc_thinking_emm1 noloop
    mc "Some. Mostly stuff like GTA, Ass's Creed, that sort of thing."
    scene d16s10-10 mc-arj-room-talk10_c1 with dissolve
    play voice3 amrose_old_haha2 noloop
    arj "I absolutely loved Vice City when I was a kid. Didn't really get into the ones after that."
    play voice2 mc_thinking_hmm3 noloop
    mc "Really? I keep meaning to go back and try that, but it was before my time."
    scene d16s10-11 mc-arj-room-talk11_c1 with dissolve
    play voice3 amrose_hey_happy1 noloop
    arj "We're the same age."
    play voice2 mc_yes_yeah6 noloop
    mc "Yeah, but, ya'know. My parents thought I was too young."
    scene d16s10-12 mc-arj-room-talk12_c1 with dissolve
    play voice3 amrose_arrogant_huh3 noloop
    arj "Huh. I suppose-"
    call buzz from _call_buzz_17
    scene d16s10-14 mc-arj-room-talk14_c1 with dissolve
    play voice3 amrose_disappointed_oh3 noloop
    arj "That's your phone."
    scene d16s10-15 mc-arj-room-talk15_c1 with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "It's Fetish Locator. It said, \"Surprise Me\". Then told me to invent a brand new fetish."
    scene d16s10-15 mc-arj-room-talk15_c2 with dissolve
    play voice3 amrose_surprised_uh3 noloop
    arj "Well, that's different. {w}How are you supposed to do that?"
    if cockcage_released is False:
        scene d16s10-15-2 mc-arj-room-talk16_c1 with dissolve
        play voice2 mc_yes_yeah5 noloop
        mc "Yeah, especially with my dick caged."
        scene d16s10-15-2 mc-arj-room-talk16_c2 with dissolve
    play voice3 amrose_thinking_emm noloop
    arj "Does it have a time limit?"
    scene d16s10-15-2 mc-arj-room-talk16_c1 with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "Thankfully, no. I doubt I could-"
    scene d16s10-15 mc-arj-room-talk15_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Wait a second."
    arj "What's up?"
    mc "I've got an idea. {w}I'll need your help."
    scene d16s10-15 mc-arj-room-talk15_c2 with dissolve
    play voice3 amrose_old_hey1 volume 1.3 noloop
    arj "You never even need to ask. You know you've got it."
    scene d16s10-15-2 mc-arj-room-talk16_c1 with dissolve
    play voice2 mc_yes_okay3 noloop
    mc "Okay... let's take your new chair for a ride."
    play voice3 amrose_arrogant_huh4 noloop
    arj "... huh?"

    $ Lovense.stop()

    scene d16s10-16-2 mc-arj-room-talk17_c1 with fade
    $ Lovense.vibrate(1)
    play voice3 amrose_thinking_hmm3 noloop
    arj "Okay, now what?"
    scene d16s10-16-2 mc-arj-room-talk17_c2 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Put your legs up on the arm rests-"
    play voice3 amrose_yes_yap noloop
    arj "Sounds good."
    scene d16s10-16-2 mc-arj-room-talk17_c3 with dissolve
    mc "So, you're going to masturbate-"
    play sound sfx_bandage_off1
    scene d16s10-16-3 mc-arj-room-talk18_c2 with dissolve
    play voice3 amrose_thinking_oh1 noloop
    arj "I like this plan so far."
    scene d16s10-16-3 mc-arj-room-talk18_c3 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "And I am going to spin the chair while you play with yourself."
    scene d16s10-16-4 mc-arj-room-talk19_c2 with dissolve
    play voice3 amrose_surprised_what noloop
    arj "... what?"
    scene d16s10-16-4 mc-arj-room-talk19_c3 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Hear me out. {w}So, this will accomplish two things."
    scene d16s10-17-3 mc-arj-room-talk23_c2 with dissolve
    play voice3 amrose_yes_ugu noloop
    arj "I'm listening."
    mc "On the one hand, it should provide a lightheadedness that accentuates the experience."
    scene d16s10-17 mc-arj-room-talk20_c2 with dissolve
    play voice3 amrose_old_huh noloop
    arj "Like scarfing or auto-erotic aphyxiation?"
    play voice2 mc_yes_yeah1 noloop
    mc "Only safer, yeah."
    scene d16s10-17-1 mc-arj-room-talk21_c2 with dissolve
    play voice3 amrose_thinking_hmm1 noloop
    arj "Go on."
    play voice2 d1s5_mchappy volume 1.5 noloop
    if fl_watersports is True:
        mc "On the other hand, when you squirt it should give a fountain effect."
        scene d16s10-17-7 mc-arj-room-talk27_c2 with dissolve
        play voice3 amrose_arrogant_huh1 noloop
        arj "Fair enough. {w}I doubt anyone else has tried anything like this."
    else:
        mc "On the other hand, the app did say, \"Surprise me.\""
        scene d16s10-17-2 mc-arj-room-talk22_c2 with dissolve
        play voice3 amrose_arrogant_huh1 noloop
        arj "Fair enough. {w}It is surprising."
    scene d16s10-17-5 mc-arj-room-talk25_c2 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "All set?"
    scene d16s10-17-8 mc-arj-room-talk28_c2 with dissolve
    play voice3 amrose_old_upset volume 1.5 noloop
    arj "Let me get myself going a bit before you start spinning me."
    play voice2 mc_yes_okay2 noloop
    mc "Okay."
    scene d16s10-17-9 mc-arj-room-talk29_c2 with dissolve
    play voice3 daisy_thinking noloop
    arj "Mmmm..."
    arj "Tell me something."
    play voice2 mc_arrogant_huh3 noloop
    mc "What's that?"
    scene d16s10-18 mc-arj-room-move1_c1 with dissolve
    play voice3 amrose_thinking_hmm2 noloop
    arj "Anything sexy. {w}Tell me something sexy to get me going."
    scene d16s10-18 mc-arj-room-move1_c2 with dissolve
    menu:
        "Tell her how you would fuck her"(hint="d16s10m01c01"):

            $ d16s10_talk_future = True

            scene d16s10-18 mc-arj-room-move1_c3 with dissolve
            play voice2 d1s1_mmm noloop
            mc "I have this fantasy about us. I don't remember when I first had it."
            mc "I thought about it sometimes even when we were just friends and I had no idea how you felt about me."
            scene d16s10-18-2 mc-arj-room-move2_c1 with dissolve
            play voice3 dahlia_thinking_hmm3 noloop
            arj "Really? {w}You thought about me back then?"
            scene d16s10-18-2 mc-arj-room-move2_c2 with dissolve
            play voice2 mc_happy_yay2 noloop
            mc "Of course. I'm a guy, and you're fucking gorgeous."
            scene d16s10-18-2 mc-arj-room-move2_c3 with dissolve
            play voice2 mc_thinking_mmm2 noloop
            mc "So, it starts with the two of us on a camping trip. We're cosy and warm in our tent."
            mc "It's deep winter. There's at least a foot of snow on the ground outside."
            scene d16s10-18-3 mc-arj-room-move3_c3 with dissolve
            mc "You're relaxing on top of your sleeping bag and talking to me while I look through the camp supplies we packed."
            if cage_ntr is True:
                mc "I find a bunch of lengths of rope in the bag, and that gives me an idea."
                play voice2 mc_angry_huh2 noloop
                mc "This gets kinda dark and rough. You okay with that?"
                scene d16s10-18-3 mc-arj-room-move3_c2 with dissolve
                play voice3 amrose_yes_happy1 noloop
                arj "Fuck yes. What happens next?"
                scene d16s10-18-2 mc-arj-room-move2_c3 with dissolve
                play voice2 mc_thinking_mmm4 noloop
                mc "Sometimes I convince you to walk outside with me. Sometimes I just grab you by the hair and drag you out of the tent."
                mc "Either way I press you against a tree and start tying you up."
                scene d16s10-18-2 mc-arj-room-move2_c1 with dissolve
                mc "You struggle a little, but I can easily overpower you."
                mc "Pretty soon I've got your wrists bound to a thick limb above your head."
                play voice2 d1s5_orgasm noloop
                scene d16s10-18-3 mc-arj-room-move3_c3 with dissolve
                mc "Then I start stripping you of your clothes."
                mc "Exposing your bare skin to the freezing cold..."
            else:
                play voice2 mc_thinking_mmm4 noloop
                mc "Suddenly you start complaining that it is too hot in our tent."
                mc "You pull off your sweater and reveal that you aren't wearing anything underneath."
                scene d16s10-18-3 mc-arj-room-move3_c2 with dissolve
                mc "I lunge towards you and kiss you passionately."
                mc "Pretty soon both of us are tearing off our clothes."
                scene d16s10-18-2 mc-arj-room-move2_c3 with dissolve
                play voice2 mc_angry_huh2 noloop
                mc "You tell me something, but I'm too focused on what I'm doing to listen."
                mc "What I'm doing is shoving my hard cock deep into your cunt."
                scene d16s10-18-3 mc-arj-room-move3_c1 with dissolve
                play voice3 dahlia_sex_closedmoan1 noloop
                mc "You shout out in pleasure and tell me again that you're on the pill so I can cum inside you as much as I want."
                mc "I want it. I ride you without any hesitation or concern."
                scene d16s10-18-3 mc-arj-room-move3_c3 with dissolve
                play voice2 d1s5_orgasm noloop
                mc "I fuck you as passionately as humanly possible."
        "Tell her how you came while she was under the table"(hint="d16s10m01c02"):


            scene d16s10-18 mc-arj-room-move1_c3 with dissolve
            play voice2 mc_happy_yay2 noloop
            mc "Do you remember when you crashed that lunch date I had with Lydia?"
            mc "She wanted me to tell her some story. She was incredibly drunk at the time."
            scene d16s10-18-2 mc-arj-room-move2_c1 with dissolve
            play voice2 mc_thinking_mmm4 noloop
            mc "Meanwhile, all my attention was on you - under the table sucking my cock."
            mc "I made up some story. I don't even remember what I said."
            scene d16s10-18-2 mc-arj-room-move2_c3 with dissolve
            play voice2 mc_angry_huh2 noloop
            mc "It might have been real or complete fiction. It didn't matter. She could barely hear me."
            mc "There we were, Lydia and myself in a fancy restaurant."
            scene d16s10-18-3 mc-arj-room-move3_c1 with dissolve
            play voice3 dahlia_sex_closedmoan1 noloop
            mc "I completely forgot about her. I forgot about what I was saying. I forgot about the other people enjoying their meals."
            mc "All that mattered in the world at that moment were your lips, your tongue, your mouth, and my dick."
            scene d16s10-18-3 mc-arj-room-move3_c3 with dissolve
            play voice2 d1s5_orgasm noloop
            mc "If I had drunk a little bit more I would have dragged you out of hiding and fucked you right there on that table."
            mc "I dream about that sometimes. Lydia, the maî·tre d', and everyone else just watching me fuck you on that table."

    stop music fadeout 5.0
    scene d16s10-18-3 mc-arj-room-move3_c2 with dissolve
    play voice3 dahlia_sex_closedmoan2 noloop
    arj "That's so fucking hot."
    play voice2 mc_arrogant_huh3 noloop
    mc "You ready?"
    scene d16s10-20 mc-arj-room-rotation1_c1 with dissolve
    play voice3 amrose_yes_okay2 noloop
    arj "Okay - let's try this thing."
    scene d16s10-00-a1 arj-spin-anim-1-00 with dissolve
    play voice2 d9s2_ugu volume 1.5 noloop
    mc "Alright. I'm going to spin you."
    $ renpy.music.set_volume(0.8, 3.0, "music")
    if is_extended_edition is True:
        play music "<from 0 to 31.860>audio/loudlout/extended/music_youspinmeround_intro.ogg"
    queue music music_youspinmeround
    play sound [sfx_chair_spin_slow1, "<silence 6.3>"] loop
    play sound2 ["<silence 6.3>", sfx_chair_spin_slow2]
    $ Lovense.vibrate(3)
    scene d16s10_mc_spin_arj_1_slow with hpunch
    play voice3 amrose_happy_woo noloop
    arj "Weeeee"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    play sound [sfx_chair_spin_slow1, "<silence 6.3>"] loop
    play sound2 ["<silence 6.3>", sfx_chair_spin_slow2]
    scene d16s10_mc_spin_arj_2_slow with dissolve
    queue voice3 daisy_moaning
    play voice2 mc_thinking_hmm2 noloop
    mc "How's that?"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    play sound [sfx_chair_spin_slow1, "<silence 6.3>"] loop
    play sound2 ["<silence 6.3>", sfx_chair_spin_slow2]
    scene d16s10_mc_spin_arj_1_slow with dissolve
    pause
    play sound [sfx_chair_spin_slow1, "<silence 6.3>"] loop
    play sound2 ["<silence 6.3>", sfx_chair_spin_slow2]
    scene d16s10_mc_spin_arj_2_slow with dissolve
    pause
    play sound [sfx_chair_spin_slow1, "<silence 6.3>"] loop
    play sound2 ["<silence 6.3>", sfx_chair_spin_slow2]
    scene d16s10_mc_spin_arj_3_slow with dissolve
    pause
    play voice3 amrose_happy_laugh1 noloop
    queue voice3 ["<silence 0.6>", daisy_moaning]
    arj "I think I can go a little faster!"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    play sound [sfx_chair_spin_fast1, "<silence 2.6>", sfx_chair_spin_fast1, "<silence 2.7>"] loop
    play sound2 ["<silence 4.0>", sfx_chair_spin_fast2, "<silence 0.2>"]
    scene d16s10_mc_spin_arj_1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Alright."
    play voice3 amrose_happy_woohoo noloop
    queue voice3 ["<silence 0.6>", daisy_moaning]
    arj "Wooohoooo!!!"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    play sound [sfx_chair_spin_fast1, "<silence 2.6>", sfx_chair_spin_fast1, "<silence 2.7>"] loop
    play sound2 ["<silence 4.0>", sfx_chair_spin_fast2, "<silence 0.2>"]
    $ Lovense.vibrate(4)
    scene d16s10_mc_spin_arj_2 with dissolve
    if cage_ntr is True:
        arj "Spin! Spin! {w}Spin the black circle!!"
    else:
        arj "You spin me right-round baby right-round! {w}Like a record!!!"
    mct "Clearly she's enjoying this..."
    play voice3 amrose_happy_yay2 noloop
    queue voice3 ["<silence 0.6>", daisy_moaning]
    arj "Wooot!! Faster, baby, faster!!!"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    play sound [sfx_chair_spin_fast1, "<silence 2.6>", sfx_chair_spin_fast1, "<silence 2.7>"] loop
    play sound2 ["<silence 4.0>", sfx_chair_spin_fast2, "<silence 0.2>"]
    scene d16s10_mc_spin_arj_3 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay..."
    play voice3 jessie_oh noloop
    arj "OOoooooohhhhh-"
    queue voice3 jessie_yes2 noloop
    arj "-yyeeeeeessssss..."
    play sound [sfx_chair_spin_fast1, "<silence 2.6>", sfx_chair_spin_fast1, "<silence 2.7>"] loop
    play sound2 ["<silence 4.0>", sfx_chair_spin_fast2, "<silence 0.2>"]
    scene d16s10_mc_spin_arj_1 with dissolve
    pause
    play sound [sfx_chair_spin_fast1, "<silence 2.6>", sfx_chair_spin_fast1, "<silence 2.7>"] loop
    play sound2 ["<silence 4.0>", sfx_chair_spin_fast2, "<silence 0.2>"]
    scene d16s10_mc_spin_arj_2 with dissolve
    pause
    play sound [sfx_chair_spin_fast1, "<silence 2.6>", sfx_chair_spin_fast1, "<silence 2.7>"] loop
    play sound2 ["<silence 4.0>", sfx_chair_spin_fast2, "<silence 0.2>"]
    scene d16s10_mc_spin_arj_3 with dissolve
    pause
    queue voice3 amrose_old_orgasming
    if fl_watersports is True:
        stop sound fadeout 1.0
        stop sound2 fadeout 1.0
        play sound [sfx_chair_spin_fast1, "<silence 2.6>", sfx_chair_spin_fast1, "<silence 2.7>"] loop
        play sound2 ["<silence 4.0>", sfx_chair_spin_fast2, "<silence 0.2>"]
        play sound4 sfx_piss_loop1 fadein 1.0
        play sound6 sfx_piss_loop2 fadein 1.0
        scene d16s10_arj_squirting_1 with dissolve
        pause
        stop sound fadeout 1.0
        stop sound2 fadeout 1.0
        play sound [sfx_chair_spin_fast1, "<silence 2.6>", sfx_chair_spin_fast1, "<silence 2.7>"] loop
        play sound2 ["<silence 4.0>", sfx_chair_spin_fast2, "<silence 0.2>"]
        scene d16s10_arj_squirting_2 with dissolve
        play voice2 mc_happy_yay1 noloop
        mc "That's a fucking fountain alright!"
        stop sound4 fadeout 1.0
        stop sound6 fadeout 1.0
    else:
        play voice2 mc_happy_yay1 noloop
        mc "That's what I'm talking about!"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    $ renpy.music.set_volume(0.4, 3.0, "music")
    $ Lovense.vibrate(1)
    scene d16s10-21 mc-arj-room-unwell1_c1 with dissolve
    play voice3 amrose_disgust_argh noloop
    arj "Ohhhh fuckkkk!! {w}STOP!!!"
    scene d16s10-21 mc-arj-room-unwell1_c2 with dissolve
    play voice3 amrose_pain_ahh1 noloop
    arj "Fuck fuckfuck too fast...."
    $ renpy.music.set_volume(0.3, 3.0, "music")
    scene d16s10-21 mc-arj-room-unwell1_c3 with dissolve
    play voice3 min_disgust_boeah noloop
    arj "BLARGH."
    play voice2 d1s5b_emmm volume 1.5 noloop
    mc "Let me help-"
    scene d16s10-22 mc-arj-room-unwell2_c1 with dissolve
    play voice3 amrose_surprised_oh3 noloop
    arj "BATHROOM! {w}NEED!!!"
    scene d16s10-22 mc-arj-room-unwell2_c2 with dissolve
    arj "NOWWW!!!!"
    $ renpy.music.set_volume(0.2, 3.0, "music")
    $ renpy.music.set_pan(-0.7, 0.0, "voice3")
    play voice3 sfx_cough_female1 noloop
    scene d16s10-22 mc-arj-room-unwell2_c3 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh."
    scene d16s10-22-2 mc-arj-room-unwell3_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "Hmm. Not entirely successful as far as tests go."
    mc "Maybe I shouldn't have spun her so fast."
    call buzz from _call_buzz_18
    $ Lovense.stop()
    scene d16s10-23 mc-arj-room-phone_c1 with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Oh, fuck."
    $ renpy.music.set_volume(0.1, 3.0, "music")
    scene d16s10-24 mc-arj-room-phone2_c1 with dissolve
    $ renpy.music.set_pan(0.0, 0.0, "voice3")
    play voice3 amrose_happy_phew2 noloop
    arj "That was {w}fun?"
    play voice2 mc_arrogant_huh1 noloop
    mc "Are you alright?"
    scene d16s10-24 mc-arj-room-phone2_c2 with dissolve
    play voice3 amrose_yes_yeah3 noloop
    arj "Yeah. Got dizzy, lightheaded, climaxed, then suddenly felt very very ill."
    mc "Do you need a moment?"
    arj "I'm all good now. {w}You keep looking at your phone. What's wrong?"
    play sound sfx_jeans_fly1
    scene d16s10-25 mc-arj-room-talk1_c1 with dissolve
    play voice2 mc_no_nah2 noloop
    mc "Nothing wrong... it's just my turn now."
    if cockcage_released is False:
        scene d16s10-25 mc-arj-room-talk1_c2 with dissolve
        play voice3 amrose_arrogant_huh4 noloop
        arj "How is that supposed to work?"
        scene d16s10-25 mc-arj-room-talk1_c3 with dissolve
        play voice2 d1s5b_ehhh volume 1.5 noloop
        mc "I don't know, but I guess I better get undressed and find out."
        play sound sfx_skirt_off1
        scene d16s10-26 mc-arj-room-talk2_c2 with fade
        play voice3 amrose_thinking_hmm4 noloop
        arj "Well, we're both naked. What does the app expect us to do now?"
        scene d16s10-26 mc-arj-room-talk2_c1 with dissolve
        play voice2 mc_arrogant_hm3 noloop
        mc "Maybe I should sit down and you can start spinning me?"
        scene d16s10-26 mc-arj-room-talk2_c3 with dissolve
        play voice3 amrose_surprised_uh4 noloop
        arj "And then what, your cage just flies off and breaks something in my house?!"
        play voice2 mc_thinking_emm1 noloop
        mc "I suppose-"
        arj "Well-"
        play sound cockcage_lock_off
        $ Lovense.vibrate(10)
        pause
        $ Lovense.stop()
        scene d16s10-27 mc-arj-room-talk3_c3
        if cage_ntr is False:
            show d16s10-27-mc-arj-room-talk3-lc_c3
        with dissolve
        play voice2 d9s5_auch2 noloop
        mc "FREEDOM!!!"

        $ fl_achievement_unlock("d16s10n01")
        $ unlock_gallery_slot("extra", "d16s10n01")

        scene d16s10-27 mc-arj-room-talk3_c2 with dissolve
        play voice3 amrose_happy_laugh2 noloop
        arj "Oh, thank goodness."
        play voice2 mc_scared_huuuh3 noloop
        mc "FREEDOM!!!"
        scene d16s10-28 mc-arj-room-talk4_c1 with dissolve
        play voice3 amrose_happy_laugh3 noloop
        arj "Congratulations on getting your cock back."
        scene d16s10-28 mc-arj-room-talk4_c2
        if cage_ntr is False:
            show d16s10-28-mc-arj-room-talk4-lc_c2
        with dissolve
        play voice2 d4s8_scared volume 1.5 noloop
        mc "WHOOOOAAA FRREEEEEDOOOMMMM!!!!"
        if persistent.is_special is True:
            scene d16s10-28 mc-arj-room-talk4_c1 with dissolve
            play voice3 amrose_hey_active1 noloop
            arj "Ready to go?"
            play voice2 mc_angry_errr4 noloop
            mc "Ready! {w}I'm so horny I could fuck a horse."
        if fl_goldstars >= 3:
            $ fl_achievement_unlock("d16s04n01")
            $ unlock_gallery_slot("extra", "d16s04n01")
    else:
        mc "I suppose I'll join you in getting buck naked."
        scene d16s10-25 mc-arj-room-talk1_c2 with dissolve
        play voice3 amrose_thinking_hmm4 noloop
        arj "Maybe we could start a nudist club."
        play voice2 mc_yes_sure1 noloop
        mc "They could meet at your house."
        scene d16s10-25 mc-arj-room-talk1_c3 with dissolve
        play voice3 amrose_no_nah noloop
        arj "Although, from what I understand nudists don't watch each other masturbate."
        play voice2 mc_happy_a1 noloop
        mc "I guess it depends on which kind of nudist club we start."
    scene d16s10-28 mc-arj-room-talk4_c3 with dissolve
    play voice3 amrose_disappointed_ehh2 noloop
    arj "Alright, get in the chair."
    play voice2 mc_happy_hah1 noloop
    mc "You sound like my dentist."
    play sound sfx_cloth_rustling2
    $ Lovense.vibrate(2)
    scene d16s10-30 mc-arj-room-rotation2_c1 with dissolve
    play voice3 amrose_arrogant_yeah2 noloop
    arj "Have you done this sort of thing with your dentist?"
    play voice2 mc_no_no5 noloop
    mc "He's like a century old and... No.{w} Just, no."
    play voice3 amrose_thinking_hmm2 noloop
    arj "Think of something sexy and leave the rest to me."
    scene d16s10-30 mc-arj-room-rotation2_c2 with dissolve
    play voice2 d2s12_emmm noloop
    mc "Maybe a little slower than I spun you?"
    scene d16s10-30 mc-arj-room-rotation2_c1 with dissolve
    play voice3 amrose_old_haha2 noloop
    arj "If you yell, \"Faster\" then you live with the consequences."
    play voice2 d9s2_yeah volume 1.5 noloop
    mc "Fair enough."
    scene d16s10-30 mc-arj-room-rotation2_c3
    if cage_ntr is False:
        show d16s10-30-mc-arj-room-rotation2-lc_c3
    with dissolve
    play voice3 amrose_thinking_hmm3 noloop
    arj "Got you happy, sexy, fun time thought?"
    play voice2 mc_yes_yeah1 noloop
    mc "Definitely."
    if d16s03_love_lc is True:
        scene d16s03-00_mc-lc-amr-cuddle-post-climax
        show memory-cloud
        with dissolve
    else:
        scene d16s02-23 mc-arj-entrance-lick3_c2
        show memory-cloud
        with dissolve
    pause
    scene d16s10-00-a5 mc-spin-anim-5-00_i with dissolve
    mc "Most definitely."
    play voice3 amrose_happy_yay1 noloop
    arj "Let's do this!"
    $ Lovense.vibrate(4)
    $ renpy.music.set_volume(0.8, 3.0, "music")
    play voice2 d7s4_mcbreathing fadein 1.5
    play sound [sfx_chair_spin_slow1, "<silence 6.3>"] loop
    play sound2 ["<silence 6.3>", sfx_chair_spin_slow2]
    scene d16s10_arj_spin_mc_1_slow
    pause
    scene d16s10_arj_spin_mc_2_slow with dissolve
    pause
    scene d16s10_arj_spin_mc_3_slow with dissolve
    pause
    arj "How's that?"
    mc "Faster!"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    play sound [sfx_chair_spin_fast1, "<silence 2.6>", sfx_chair_spin_fast1, "<silence 2.7>"] loop
    play sound2 ["<silence 4.0>", sfx_chair_spin_fast2, "<silence 0.2>"]
    scene d16s10_arj_spin_mc_2 with dissolve
    play voice3 amrose_arrogant_huh2 noloop
    arj "Is that better?"
    mc "Perfect!"
    $ Lovense.vibrate(6)
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    play sound [sfx_chair_spin_fast1, "<silence 2.6>", sfx_chair_spin_fast1, "<silence 2.7>"] loop
    play sound2 ["<silence 4.0>", sfx_chair_spin_fast2, "<silence 0.2>"]
    scene d16s10_arj_spin_mc_3 with dissolve
    mc "Just like that!"
    play voice2 mc_happy_wooh1 noloop
    queue voice2 d7s4_mcbreathing
    mc "Woooohoooo!!!"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    play sound [sfx_chair_spin_fast1, "<silence 2.6>", sfx_chair_spin_fast1, "<silence 2.7>"] loop
    play sound2 ["<silence 4.0>", sfx_chair_spin_fast2, "<silence 0.2>"]
    play voice2 [d1s5_orgasm2, "<silence 1.0>", d1s5_orgasm, "<silence 1.0>", mc_pain_mff4, "<silence 1.0>", mc_angry_errr4, "<silence 1.0>", mc_pain_mff1, "<silence 1.0>"]
    scene d16s10_mc_cumming_1 with dissolve
    mc "FUCK YES!!!"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    play sound [sfx_chair_spin_fast1, "<silence 2.6>", sfx_chair_spin_fast1, "<silence 2.7>"] loop
    play sound2 ["<silence 4.0>", sfx_chair_spin_fast2, "<silence 0.2>"]
    $ Lovense.vibrate(13)
    scene d16s10_mc_cumming_2 with dissolve
    pause
    play voice2 d4s8_scared noloop
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    $ renpy.music.set_volume(0.2, 10.0, "music")
    $ Lovense.vibrate(1)
    scene d16s10-31 mc-arj-room-rest1_c1 with dissolve
    play voice3 amrose_hey_whisper noloop
    arj "How do you feel?"
    scene d16s10-31 mc-arj-room-rest1_c2 with dissolve
    play voice2 mc_surprised_wow2 noloop
    mc "Fucking amazing."
    play voice3 amrose_old_huh noloop
    arj "Any lightheadedness? Nausea?"
    scene d16s10-31 mc-arj-room-rest1_c3 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Lightheaded as fuck. {w}I'm about to fall over, but I feel fantastic."
    scene d16s10-32 mc-arj-room-rest2_c3 with dissolve
    play voice3 amrose_thinking_hmm5 noloop
    arj "I bet we could figure out what the correct RPM is."
    arj "Maybe something like the G-forces experienced by pilots."
    arj "Then we could patent the-"
    scene d16s10-33 mc-arj-room-rest3_c3 with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "AmRose?"
    play voice3 amrose_yes_yeah2 noloop
    arj "Yeah?"
    play voice2 mc_disappointed_ah2 noloop
    mc "Not now."
    scene d16s10-34 mc-arj-room-hug_c1 with dissolve
    pause
    scene d16s10-34 mc-arj-room-hug_c3 with dissolve
    play voice3 amrose_happy_mmm noloop
    arj "How's this?"
    scene d16s10-34 mc-arj-room-hug_c2 with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "This I like."
    stop music fadeout 3.0
    scene d16s10-35 mc-arj-room-lick_c1 with Fade(0.7, 1.5, 0.7)
    $ renpy.music.set_volume(0.5, 3.0, "music")
    queue music lofi_evening
    play voice2 mc_disgust_ooh1 noloop
    $ Lovense.vibrate(3)
    mc "Why not leave it for now? It'll be easier to clean when it dries."
    play voice3 amrose_no_uhuh noloop
    arj "That's not how cleaning works. {w}That's not how anything works."
    play voice3 daisy_licking2 noloop
    scene d16s10-35 mc-arj-room-lick_c2 with dissolve
    pause
    scene d16s10-35 mc-arj-room-lick_c3 with dissolve
    $ Lovense.vibrate(5)
    play voice2 d1s1_mmm volume 1.5 noloop
    mct "Damn. {w}I wonder when I'll get to fuck that ass."
    $ renpy.end_replay()
    scene d16s10-36 mc-arj-room-lick2_c1 with dissolve
    queue voice3 daisy_dlick noloop
    mct "Maybe I should try right now."
    scene d16s10-36 mc-arj-room-lick2_c2 with dissolve
    pause
    $ Lovense.vibrate(2)
    play voice2 mc_angry_huh2 noloop
    scene d16s10-36 mc-arj-room-lick2_c3 with dissolve
    pause
    scene d16s10-37 mc-arj-room-floor_c1 with dissolve

    $ Lovense.stop()

    play voice2 d1s5_mchappy volume 1.5 noloop
    mc "I've been meaning to ask you something."
    play voice3 amrose_yes_ugu noloop
    arj "Me too. {w}You ever think about how much Fetish Locator knows about us."
    scene d16s10-37 mc-arj-room-floor_c2 with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Well, yeah. {w}I don't even need to take pics or anything anymore. {w}It just knows."
    scene d16s10-37 mc-arj-room-floor_c3 with dissolve
    play voice3 amrose_yes_confident2 noloop
    arj "Exactly. It knows a lot about everyone with the app installed, but it..."
    if is_antagonist_mode is False:
        arj "It seems to know more about those of us in the VIP-"
    else:
        arj "It seems to know more about those of us in the reten-"
    play voice3 amrose_surprised_uh2 noloop
    arj "Fuck. We're not supposed to talk about that."
    scene d16s10-37 mc-arj-room-floor_c1 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    if is_antagonist_mode is False:
        mc "The VIP Program?"
    else:
        mc "Retention?"
    play voice3 amrose_yes_confident1 noloop
    arj "Yes, that. {w}It seems to know more about us than anyone should."
    call buzz from _call_buzz_19
    scene d16s10-38 mc-arj-room-talk1_c2 with dissolve
    flr "Nice work."
    scene d16s10-38 mc-arj-room-talk1_c1 with dissolve
    call add_points (d16s10_points) from _call_add_points_9
    flr "You have earned [d16s10_points] points."
    scene d16s10-39 mc-arj-room-talk2_c2 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "You never did tell me."
    scene d16s10-38 mc-arj-room-talk1_c3 with dissolve
    play voice3 amrose_surprised_huh3 noloop
    arj "Huh? I'm sorry. I'm really sleepy."
    scene d16s10-39 mc-arj-room-talk2_c2 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    if is_antagonist_mode is False:
        mc "What did you do to get in the VIP Program? Did you send them pics or what?"
    else:
        mc "What does retention have on you? What pics did you send them?"
    scene d16s10-39 mc-arj-room-talk2_c3 with dissolve
    play voice3 amrose_disappointed_oh3 noloop
    arj "Well, I guess that's enough cleaning for tonight."
    play voice2 mc_hey_hey3 noloop
    mc "You didn't answer my question."
    play voice3 amrose_disappointed_ehh1 noloop
    arj "I'm suddenly very sleepy. Let's go to bed."
    scene d16s10-40 mc-arj-room-talk3_c1 with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "Fine. I can take a hint."
    scene d16s10-40 mc-arj-room-talk3_c2 with dissolve
    play voice3 amrose_happy_laugh3 noloop
    arj "Let me put it this way...{w} Lydia is a music major, right?"
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah."
    arj "If you really want to know, then you can ask her-"
    scene d16s10-41 mc-arj-room-talk4_c1 with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "Why would she know?"
    play voice3 amrose_old_chmchm noloop
    arj "Let me finish. You can ask her..."
    mc "... yes?"
    scene d16s10-41 mc-arj-room-talk4_c2 with dissolve
    play voice3 amrose_arrogant_huh3 noloop
    arj "Just ask her about Mozart."
    play voice2 d2s12_emmm volume 1.3 noloop
    mc "Mozart?"
    play voice3 amrose_yes_yap noloop
    arj "Yep."
    scene d16s10-40 mc-arj-room-talk3_c1 with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What about Mozart?"
    play voice3 amrose_no_nah noloop
    arj "That's as much as I'm going to say."
    scene d16s10-40 mc-arj-room-talk3_c2 with dissolve
    play voice2 mc_surprised_what3 noloop
    mc "Really? That's it? {w}I should ask Lydia about Mozart."
    play voice3 amrose_yes_ugu noloop
    arj "Yup."
    arj "Enough about that. Let's go to bed."
    scene d16s10-41 mc-arj-room-talk4_c1 with dissolve
    play voice2 mc_yes_okay3 noloop
    mc "Okay. I'll be with you in a few minutes."
    play voice3 amrose_arrogant_huh2 noloop
    arj "You going to call Lydia?"
    play voice2 mc_arrogant_heh3 noloop
    mc "Not about Mozart. {w}We just usually talk-"
    scene d16s10-41 mc-arj-room-talk4_c2 with dissolve
    play voice3 amrose_thinking_hmm1 noloop
    arj "Invite her over here for breakfast."
    play voice2 mc_arrogant_huh2 noloop
    mc "Really?"
    arj "Sure. We can get together, eat, and study together."
    scene d16s10-41 mc-arj-room-talk4_c1 with dissolve
    play voice2 mc_happy_thatsgood noloop
    mc "That's... {w}very mature of you. I'll do that."
    scene d16s10-40 mc-arj-room-talk3_c2 with dissolve
    play voice3 amrose_yes_yeah2 noloop
    arj "Cool. {w}G'night!"
    play voice2 mc_yes_ugu1 noloop
    mc "Good night. I'll join you soon."
    $ unlock_gallery_slot("scene", "d16s10")
    stop music fadeout 3.0

    jump d17s01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
