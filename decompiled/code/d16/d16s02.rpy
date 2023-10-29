image d16s02-a1 = Movie(play = "images/Day-16/Scene-02/anim/d16s02-a1-2x-50fps.webm", start_image = "d16s02-20-a1 mc-arj-entrance-lick1-anim-1-01_i")
image d16s02-a2 = Movie(play = "images/Day-16/Scene-02/anim/d16s02-a2-2x-50fps.webm", start_image = "d16s02-20-a2 mc-arj-entrance-lick1-anim-2-01_i")
image d16s02-a3 = Movie(play = "images/Day-16/Scene-02/anim/d16s02-a3-2x-50fps.webm", start_image = "d16s02-20-a3 mc-arj-entrance-lick1-anim-3-01_i")
image d16s02-a4 = Movie(play = "images/Day-16/Scene-02/anim/d16s02-a4-2x-50fps.webm", start_image = "d16s02-21-a4 mc-arj-entrance-lick2-anim-4-01_i")
image d16s02-a5 = Movie(play = "images/Day-16/Scene-02/anim/d16s02-a5-2x-50fps.webm", start_image = "d16s02-21-a5 mc-arj-entrance-lick2-anim-6-01_i")
image d16s02-a6 = Movie(play = "images/Day-16/Scene-02/anim/d16s02-a6-2x-50fps.webm", start_image = "d16s02-21-a6 mc-arj-entrance-lick2-anim-6-01_i")

image d16s02-a7 = Movie(play = "images/Day-16/Scene-02/anim/d16s02-a7-4x-60fps.webm", start_image = "d16s02-21-a7 mc-arj-entrance-lick3-anim-7-01_i")
image d16s02-a7-f = Movie(play = "images/Day-16/Scene-02/anim/d16s02-a7-2x-50fps.webm", start_image = "d16s02-21-a7 mc-arj-entrance-lick3-anim-7-01_i")
image d16s02-a8 = Movie(play = "images/Day-16/Scene-02/anim/d16s02-a8-4x-60fps.webm", start_image = "d16s02-21-a8 mc-arj-entrance-lick3-anim-8-01_i")
image d16s02-a8-f = Movie(play = "images/Day-16/Scene-02/anim/d16s02-a8-2x-50fps.webm", start_image = "d16s02-21-a8 mc-arj-entrance-lick3-anim-8-01_i")
image d16s02-a9 = Movie(play = "images/Day-16/Scene-02/anim/d16s02-a9-4x-60fps.webm", start_image = "d16s02-21-a9 mc-arj-entrance-lick3-anim-9-01_i")
image d16s02-a9-f = Movie(play = "images/Day-16/Scene-02/anim/d16s02-a9-2x-50fps.webm", start_image = "d16s02-21-a9 mc-arj-entrance-lick3-anim-9-01_i")

label d16s02:

    $ d16s02_points = 0
    $ d16s02_arj_eatout = False

    $ renpy.music.set_volume(0.3, 4.0, "music")
    scene black
    show screen scene_transistion(_("15 minutes later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    play sound sfx_door_closed1
    play sound3 buzz noloop
    hide screen scene_transistion
    scene d16s02-01-1 mc-arj-stacy-exit1_c1
    with Fade(0.5, 0.5, 0.9)
    play voice2 mc_arrogant_heh1 noloop
    mc "It's always fun to feel like the talk of the town when you step out of there."
    scene d16s02-01-1 mc-arj-stacy-exit1_c3 with dissolve
    play voice3 amrose_arrogant_huh1 noloop
    arj "Really? It kinda gives me anxiety, to be honest. I disabled all my notifications."
    scene d16s02-01-1 mc-arj-stacy-exit1_c2 with dissolve
    play voice2 mc_pain_ou1 noloop
    mc "Shit..."
    scene d16s02-01-2 mc-arj-stacy-exit2_c3 with dissolve
    play voice3 amrose_surprised_uh3 noloop
    arj "Everything alright?"
    scene d16s02-01-1 mc-arj-stacy-exit1_c1 with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "I missed a ton of calls and messages from Lydia last night 'cause of the cage."
    scene d16s02-01-3 mc-arj-stacy-exit3_c3 with dissolve
    play voice3 amrose_disappointed_oh5 noloop
    arj "Oh boy..."
    scene d16s02-01-5 mc-arj-stacy-exit5_c3 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeeep. She seems...concerned."
    mc "I think I better go back to her place and make sure everything's alright.{w} Wanna come with?"
    scene d16s02-01-5 mc-arj-stacy-exit5_c1 with dissolve
    play voice3 amrose_yes_yeah2 noloop
    arj "Sure. It's not too far away anyway."
    arj "Maybe I can be your bodyguard and protect you from her wrath."
    stop music fadeout 8.0

label replay_d16s02 hide:

    $ renpy.music.set_volume(0.05, 2.0, "sound2")
    play sound2 park fadein 2.5
    play sound ["<silence 0.3>", sfx_door_open5]
    scene d16s02-02 mc-arj-entrance2_c2 with fade
    pause
    scene d16s02-02 mc-arj-entrance2_c1 with dissolve
    play voice2 mc_hey_hey4 noloop
    mc "Lydia?{w} Lydia!?"
    scene d16s02-02 mc-arj-entrance2_c2 with dissolve
    play voice3 amrose_arrogant_hmm1 noloop
    arj "Did you text her—?"
    scene d16s02-03 mc-arj-entrance3_c2 with dissolve
    $ renpy.music.set_volume(0.5, 0.0, "voice4")
    play voice4 amrose_old_hey2 noloop
    lc "I'm in the shower! I'll be out in a minute!"
    play voice2 mc_thinking_oh1 noloop
    mc "Oh. Looks like we'll have to wait a bit."
    scene d16s02-06-2 mc-arj-entrance-phone2_c3 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mct "Wonder if I missed anything else—"
    call buzz from _call_buzz_15
    $ renpy.music.set_volume(1.0, 0.0, "voice4")
    scene d16s02-06-2 mc-arj-entrance-phone2_c2 with dissolve
    fl "Ensnare and enrapture. Some are far better at it than others."
    fl "{i}Cunnilingus{/i} is our Fetish of the Day."
    fl "How will {i}you{/i} fare?"
    $ renpy.music.set_volume(0.8, 3.0, "music")
    play voice3 amrose_hey_happy4 noloop
    scene d16s02-06-2 mc-arj-entrance-phone2_c1 with dissolve
    arj "Hey! That's an easy one."
    play music saxophone_sexy2_stereo
    arj "We can do it right here even."
    play voice2 mc_surprised_what2 noloop
    mc "What do you mean?"
    scene d16s02-07 mc-arj-entrance-talk1_c2 with dissolve
    play voice3 amrose_surprised_huh3 noloop
    arj "What do you mean \"What do you mean?\"?"
    arj "Y'know, you, me, on this..."
    scene d16s02-07-02 mc-arj-entrance-talk2_c2 with dissolve
    play voice3 amrose_happy_mmm noloop
    arj "Sturdy table."
    play voice2 mc_scared_oh4 noloop
    mc "Oh, oh! Christ. Sorry. Slow on the uptake today."
    scene d16s02-07-03 mc-arj-entrance-talk3_c2 with dissolve
    play voice3 amrose_happy_laugh1 noloop
    arj "*Giggles* So what do you say?"

    menu:
        "Rock her world"(hint="d16s02m01c01") if True:

            $ d16s02_arj_eatout = True
            $ d16s02_points = 12

            $ renpy.music.set_volume(1.0, 3.0, "music")
            scene d16s02-05 mc-arj-entrance-talk1_c1 with dissolve
            play voice2 mc_arrogant_heh1 noloop
            mc "What do you think?"
            play voice3 dahlia_thinking_hmm3 noloop


            $ Lovense.stop()

            scene d16s02-08 mc-arj-entrance-kiss_c1 with dissolve
            $ Lovense.vibrate(1)
            play sound maria_kiss2
            pause
            play voice2 d1s1_mmm noloop
            scene d16s02-08 mc-arj-entrance-kiss_c2 with dissolve
            play sound maria_kiss1
            pause
            scene d16s02-08 mc-arj-entrance-kiss_c3 with dissolve
            play sound maria_kiss3
            pause
            play voice3 amrose_surprised_uh2 noloop
            play voice2 mc_angry_hm2 noloop
            scene d16s02-09 mc-arj-entrance-hug_c2 with dissolve
            arj "Woah—!"
            play voice3 dahlia_sex_closedmoan2 noloop
            play sound sfx_bed_fall1
            scene d16s02-17 mc-arj-entrance-tease3_c1 with dissolve
            pause
            play voice2 mc_angry_huh2 noloop
            $ Lovense.vibrate(2)
            scene d16s02-17 mc-arj-entrance-tease3_c2 with dissolve
            pause
            play voice3 dahlia_sex_closedmoan1 noloop
            play voice2 maria_kiss1 noloop
            scene d16s02-15 mc-arj-entrance-tease_c2 with dissolve
            pause
            play voice2 d3s8_licking1 noloop
            $ Lovense.vibrate(3)
            scene d16s02-15 mc-arj-entrance-tease_c3 with dissolve
            pause

            if d14s03_arj_kiss is True:
                scene d16s02-15 mc-arj-entrance-tease_c1 with dissolve
                play voice2 mc_thinking_mmm2 noloop
                mc "Already wet? Well someone's an eager beaver."

            play voice3 dahlia_sex_closedmoan4 noloop
            scene d16s02-20-a1 mc-arj-entrance-lick1-anim-1-01_i with dissolve
            pause
            play voice2 d14s19_lc_licking
            play voice3 amrose_old_moaning
            $ Lovense.vibrate(4)
            scene d16s02-a1
            pause
            scene d16s02-a2 with dissolve
            arj "*Breaths get heavier* Yes..."
            pause
            scene d16s02-a3 with dissolve
            play voice3 dahlia_pain_ah2 noloop
            queue voice3 amrose_old_moaning
            arj "*Yelps*"
            pause




























            $ renpy.music.set_volume(0.2, 0.0, "sound3")
            play sound3 ["<silence 1.0>", sfx_fisting_fist1, "<silence 2.0>", sfx_fisting_fist2, "<silence 1.0>"]
            scene d16s02-a7 with dissolve
            pause

            scene d16s02-a8 with dissolve
            pause

            play voice4 d1s1_mmm noloop
            scene d16s02-a9 with dissolve
            pause

            play sound3 sfx_fisting_fast1
            scene d16s02-a7-f with dissolve
            pause

            scene d16s02-a8-f with dissolve
            pause

            scene d16s02-a9-f with dissolve
            pause

            stop voice3 fadeout 1.0
            stop sound3 fadeout 1.0
            scene d16s02-16 mc-arj-entrance-tease2_c1 with dissolve
            play voice2 mc_thinking_mmm1 noloop
            if date_arj_romance is False:
                mc "Spread yourself for me."
            elif True:
                mc "Can you spread yourself for me?"

            play voice3 dahlia_sex_closedmoan3 noloop
            scene d16s02-21-a4 mc-arj-entrance-lick2-anim-4-01_i with dissolve
            pause
            queue voice3 amrose_old_moaning
            play voice2 d14s19_lc_licking noloop
            $ Lovense.vibrate(5)
            scene d16s02-a4
            pause
            scene d16s02-a5 with dissolve
            pause
            play voice3 dahlia_sex_closedmoan1 noloop
            scene d16s02-21 mc-arj-entrance-lick2_c2 with dissolve
            play voice2 mc_angry_huh2 noloop
            mc "You're close aren't you? I can feel it."
            mc "Cum for me."
            play voice2 d14s19_lc_licking noloop
            play voice3 amrose_old_orgasming
            scene d16s02-a6 with dissolve
            pause

            $ Lovense.vibrate(8)
            scene d16s02-21 mc-arj-entrance-lick2_c1 with vpunch
            pause
            arj "*Sputtered moans* [mcname]..."

            stop voice2 fadeout 1.0
            $ Lovense.vibrate(1)
            scene d16s02-16 mc-arj-entrance-tease2_c2 with dissolve
            play voice3 amrose_disappointed_ehh2 noloop
            arj "I...uhm, that was nice."
            $ renpy.music.set_volume(0.4, 4.0, "music")
            scene d16s02-16 mc-arj-entrance-tease2_c1 with dissolve
            play voice2 mc_arrogant_huh2 noloop
            mc "Just \"nice?\"?"


            $ renpy.end_replay()
            $ unlock_gallery_slot("cg", "d16s02")
            $ unlock_gallery_slot("scene", "d16s02")
            $ renpy.music.set_volume(1.0, 0.0, "sound3")
            play sound3 sfx_cloth_rustling1 noloop


            $ Lovense.stop()

            scene d16s02-18 mc-arj-entrance-end-message_c2 with dissolve
            call buzz from _call_buzz_16
            play sound3 sfx_heels_steps1 noloop
            scene d16s02-18 mc-arj-entrance-end-message_c1 with dissolve
            stop sound3 fadeout 3.0
            call add_points (d16s02_points) from _call_add_points_8
            flr "You have earned [d16s02_points] points."
        "Not right now"(hint="d16s02m01c02") if True:


            $ renpy.music.set_volume(0.4, 4.0, "music")
            if date_arj_romance is False:
                play voice2 mc_no_no5 noloop
                mc "No. We can't. Lydia might come out any second."
            elif True:
                play voice2 mc_arrogant_hm3 noloop
                mc "Uh... I'm not sure. I don't think we have the time. Lydia might come out any second."
            scene d16s02-07 mc-arj-entrance-talk1_c2 with dissolve
            play voice3 amrose_disappointed_oh3 noloop
            arj "Oh, right. Uhm, okay. We don't have to do it here then."
            $ renpy.end_replay()

    stop sound2 fadeout 2.5
    $ renpy.music.set_volume(1.0, 2.0, "sound3")
    jump d16s03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
