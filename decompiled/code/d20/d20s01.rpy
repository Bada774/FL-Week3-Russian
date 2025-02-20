image d20s01-a1 = Movie(play = "images/Day-20/s01/anim/d20s1-a16-4-1-2x-50fps.webm", start_image = "d20s1-a16-4-1 mc-sy-arj-pee2-anim-16-4-1-00")
image d20s01-a2 = Movie(play = "images/Day-20/s01/anim/d20s1-a16-4-2-2x-50fps.webm", start_image = "d20s1-a16-4-2 mc-sy-arj-pee2-anim-16-4-2-00")

label d20s01:

    $ d20s01_let_sy_pee = False
    $ d20s01_judges_pursued = 0

    scene black
    show screen scene_transistion(_("Saturday\nDay-20"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.1, 0.0, "sound2")
    play sound2 park fadein 1.5
    play voice2 d7s6_snoring fadein 1.5
    $ renpy.music.set_volume(0.1, 0.0, "voice4")
    play voice4 amrose_disappointed_snoring
    play sound sfx_cloth_rustling2
    scene d20s1-01 mc-arj-sy-room-walkup1_c1_i
    with Fade(0.5, 0.5, 2.0)
    pause
    scene d20s1-01 mc-arj-sy-room-walkup1_c3_i with dissolve
    pause
    play voice2 d7s6_awake noloop
    scene d20s1-01 mc-arj-sy-room-walkup1_c2_i with dissolve
    mc "Stacy...?"
    scene d20s1-02 mc-arj-sy-room-walkup2_c1_i with dissolve
    pause
    scene d20s1-02 mc-arj-sy-room-walkup2_c2_i with dissolve
    play voice3 stacy_laugh4 noloop
    sy "*Ghostly sounds, for some reason* WOoOo, go back to sleEeeEp. This is a dreaAaaAm."
    scene d20s1-02 mc-arj-sy-room-walkup2_c3_i with dissolve
    play voice2 mc_disgust_pfe1 noloop
    mc "C'mon, stop."
    play sound sfx_cloth_rustling1
    scene d20s1-03 mc-arj-sy-room-walkup3_c2_i with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "Why would I go back to sleep if I'm already dreaming?"
    scene d20s1-03 mc-arj-sy-room-walkup3_c1_i with dissolve
    play voice3 stacy_yeahno noloop
    sy "Yeah, alright. That's not my best work. But I didn't have much time to come up with anything."
    scene d20s1-03 mc-arj-sy-room-walkup3_c3_i with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What? Why—?"
    scene d20s1-04 mc-arj-sy-room-sit_c1_i with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Don't tell me this is some half-baked ploy to get the shower before us."
    scene d20s1-04 mc-arj-sy-room-sit_c3_i with dissolve
    play voice3 stacy_no2 noloop
    sy "...Nope."
    scene d20s1-04 mc-arj-sy-room-sit_c2_i with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Very convincing."
    queue voice2 d7s6_moan2 noloop
    scene d20s1-05 mc-arj-sy-room-yawn_c2_i with dissolve
    pause
    scene d20s1-05 mc-arj-sy-room-yawn_c1_i with dissolve
    mc "But you're shit outta luck 'cause I need it first today."
    stop voice4 fadeout 1.0
    scene d20s1-05 mc-arj-sy-room-yawn_c3_i with dissolve
    play voice3 stacy_angry noloop
    sy "You assho--"
    $ renpy.music.set_volume(1.0, 1.0, "music")
    play music foolish_tune
    play sound sfx_barefoot_run1 loop
    play voice2 mc_happy_wooh3 noloop
    $ renpy.music.set_volume(1.0, 1.0, "voice4")
    scene d20s1-06 mc-arj-sy-room-run_c1_i with vpunch
    pause
    play voice3 polly_pollyangry noloop
    play sound4 sfx_barefoot_run1
    scene d20s1-06 mc-arj-sy-room-run_c2_i with dissolve
    pause
    scene d20s1-06 mc-arj-sy-room-run_c3_i with dissolve
    play voice4 amrose_disappointed_ehh1 noloop
    arj "Ugh, what are you two doing?"
    play voice3 stacy_impressed noloop
    sy "Fighting for the bathroom!"
    stop sound4 fadeout 1.0
    stop sound2 fadeout 3.5
    play sound sfx_door_closed4
    scene d20s1-07 sy-bathroom1_c1_i with dissolve
    "*Loud door slamming sound*"
    $ renpy.music.set_volume(0.6, 3.0, "music")
    play sound knockknock
    scene d20s1-09 sy-bathroom3_c1_i with dissolve
    play voice3 stacy_hey noloop
    sy "[mcname]! Damn it, open this door right now! I have an interview today, asshole!"
    scene d20s1-08 sy-bathroom2_c1_i with dissolve
    play voice2 mc_yes_yeah7_muffled noloop
    mc "And I got an exam that'll determine my socioeconomic status for the rest of my life, so I think I got you beat on this one."
    play voice3 polly_angry noloop
    sy "I swear to God, [mcname], I'm gonna break in there and strangle you if you don't open this door right now!"
    scene d20s1-10 sy-arj-bathroom4_c2_i with dissolve
    play voice4 amrose_disappointed_ehh2 noloop
    arj "My God, it's too early for this."
    arj "Can you two knuckleheads keep it down a bit before the neighbors call in a domestic situation?"
    scene d20s1-10 sy-arj-bathroom4_c1_i with dissolve
    $ renpy.music.set_volume(1.0, 0.0, "sound2")
    play voice3 stacy_angryhuh noloop
    sy "It'll become a damn domestic situation if he doesn't let me in."
    scene d20s1-10 sy-arj-bathroom4_c2_i with dissolve
    play voice4 amrose_arrogant_huh1 noloop
    arj "Just let him take a shower in peace, what's the rush?"
    scene d20s1-10 sy-arj-bathroom4_c1_i with dissolve
    play voice3 stacy_mmm1 noloop
    sy "My interview? You promised you'd take me there."
    play voice4 amrose_disappointed_oh3 noloop
    arj "Oh shit."
    play sound sfx_door_open3 volume 1.5
    scene d20s1-12 mc-sy-arj-bathroom-entry_c1_i with dissolve
    play voice4 amrose_hey_active1 noloop
    arj "[mcname], open up. We really need to take a shower as well."
    scene d20s1-12 mc-sy-arj-bathroom-entry_c2_i with dissolve
    play voice2 d1s5b_ehhh noloop
    mc "Just give me—"
    scene d20s1-12 mc-sy-arj-bathroom-entry_c3_i with dissolve
    play voice4 amrose_thinking_emm noloop
    arj "We can shower together."
    if date_sy is False:
        scene d20s1-13 mc-sy-arj-bathroom-entry2_c1_i with dissolve
        play voice2 mc_surprised_what2 noloop
        mc "What!?"
    arj "We don't have time."
    scene d20s1-13 mc-sy-arj-bathroom-entry2_c2_i with dissolve
    play voice4 amrose_thinking_hmm2 noloop
    arj "You have an exam to go to and Stacy has an interview that I need to take her to."
    scene d20s1-13 mc-sy-arj-bathroom-entry2_c3_i with dissolve
    play voice3 polly_aga noloop
    sy "We'll just have to squeeze in together and make it work."

    $ Lovense.stop()

    if date_sy is False:
        sy "We showered all the time as kids. What's the point of being embarrassed?"
    play voice4 amrose_happy_laugh3 noloop
    arj "See? She's a team player."
    $ Lovense.vibrate(1)
    play sound sfx_skirt_off2
    scene d20s1-13 mc-sy-arj-bathroom-entry2_c4_i with dissolve
    pause
    $ renpy.music.set_volume(0.4, 0.0, "sound4")
    $ renpy.music.set_volume(0.4, 3.0, "music")
    play sound4 shower fadein 1.5
    scene d20s1-15-2 mc-sy-arj-bathroom-shower1_c3_i with fade
    play voice2 mc_arrogant_heh1 noloop
    mc "Where are you two going anyway?"
    scene d20s1-15-2 mc-sy-arj-bathroom-shower1_c1_i with dissolve
    play voice3 stacy_oh2 noloop
    if d17s05_mh_sy is True:
        sy "Lyssa pulled some strings and got me an interview with CPD again."
    else:
        sy "I got a call back from CPD."
    scene d20s1-16 mc-sy-arj-bathroom-shower2_c3_i with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Didn't you hate the gig they offered you?"
    scene d20s1-16 mc-sy-arj-bathroom-shower2_c1_i with dissolve
    play voice3 stacy_yeahno noloop
    sy "Yes, but this is different."
    sy "They didn't give me any details, but they said it was a dev job this time.{w} So I'm excited about that."
    scene d20s1-15-2 mc-sy-arj-bathroom-shower1_c3_i with fade
    play voice2 mc_arrogant_huh1 noloop
    mc "Huh, that's cool. Hope you land it then."
    scene d20s1-15-2 mc-sy-arj-bathroom-shower1_c1_i with dissolve
    play voice3 stacy_hmm noloop
    sy "Of course I will. They'd be lucky to have me."

label replay_d20s01 hide:

    if _in_replay:
        $ renpy.music.set_volume(0.4, 0.0, "sound4")
        $ renpy.music.set_volume(0.4, 3.0, "music")
        play sound4 shower fadein 1.5
        play music foolish_tune
    if date_sy is True and fl_watersports is True:
        scene d20s1-16-3 mc-sy-arj-pee1_c3_i with dissolve
        play voice3 stacy_upset1 noloop volume 1.5
        sy "Ugh, I didn't even get to piss 'cause of your bullshit."
        play voice2 mc_arrogant_hm1 noloop
        mc "Just piss. Everybody does it."
        play sound sfx_piss_loop1 loop fadein 1.5
        $ unlock_gallery_slot("cg", "d20s01")
        $ Lovense.vibrate(3)
        scene d20s1-16-4 mc-sy-arj-pee2-1 with dissolve
        pause
        play voice4 amrose_disgust_eww noloop
        scene d20s1-16-4 mc-sy-arj-pee2_c2_i with dissolve
        arj "Ew, just get— Annnd, you're peeing already."
        scene d20s1-16-4 mc-sy-arj-pee2_c1_i with dissolve
        menu:
            "Do you want Stacy to pee on you?"
            "Yes"(hint="d20s01m01c01"):
                $ d20s01_let_sy_pee = True

                scene d20s1-16-4 mc-sy-arj-pee2_c3_i with dissolve
                play voice3 stacy_oh noloop
                sy "Oh? Looks like he's feeling lonely."
                scene d20s1-16-4 mc-sy-arj-pee2_c2_i with dissolve
                play voice4 amrose_surprised_uh4 noloop
                arj "What are you two doin—?"
                $ Lovense.vibrate(7)
                play sound sfx_piss_loop2 loop volume 1.5
                scene d20s01-a1 with dissolve
                pause
                scene d20s1-16-4 mc-sy-arj-pee2_c2_i with dissolve
                play voice4 amrose_surprised_uh5 noloop
                arj "When did you two develop a piss fetish?"
                scene d20s01-a2 with dissolve
                play voice2 d2s12_emmm noloop
                mc "It's a...uh, recent development."
                pause
                stop sound fadeout 1.0
                $ Lovense.vibrate(3)
                scene d20s1-17 mc-sy-arj-shower3_c1_i with dissolve
                play voice3 stacy_suckmoan1 noloop
                sy "Annnd she's done. Much better."
                scene d20s1-18 mc-sy-arj-shower4_c2_i with dissolve
                play voice4 amrose_disgust_yak noloop
                arj "You two are unbelievable. I wonder what else you're keeping from me?"
                scene d20s1-18 mc-sy-arj-shower4_c1_i with dissolve
                play voice3 stacy_huh2 noloop
                sy "Oh c'mon, you can't judge. I'm sure you've done kinkier things."
                $ unlock_gallery_slot("scene", "d20s01")
            "No"(hint="d20s01m01c02"):

                scene d20s1-16-4 mc-sy-arj-pee2_c2_i with dissolve
                play voice4 amrose_disgust_argh noloop
                arj "My God, Stacy."
                scene d20s1-16-4 mc-sy-arj-pee2-1 with dissolve
                pause
                stop sound fadeout 1.0
                $ Lovense.vibrate(1)
                scene d20s1-17 mc-sy-arj-shower3_c1_i with dissolve
                play voice3 stacy_suckmoan1 noloop
                sy "Annnd she's done. Much better."
                scene d20s1-18 mc-sy-arj-shower4_c2_i with dissolve
                play voice4 amrose_disgust_yak noloop
                arj "You're unbelievable."
                scene d20s1-18 mc-sy-arj-shower4_c1_i with dissolve
                play voice3 stacy_huh2 noloop
                sy "Oh c'mon, you can't judge. I'm sure you've done worse things."

        scene d20s1-16-4 mc-sy-arj-pee2_c2_i with dissolve
        play voice4 amrose_surprised_uh2 noloop
        arj "Moving on!"
        $ renpy.end_replay()

        jump d20s01_judges

label d20s01_judges:

    $ Lovense.vibrate(1)
    arj "Did you figure out the situation with the judges, by the way?"
    if d19s06_call_tl is True:
        $ d20s01_judges_pursued += 1
        scene d20s1-18 mc-sy-arj-shower4_c3_i with dissolve
        play voice2 mc_yes_yeah4 noloop
        mc "I managed to contact Lewald and get her to meet me."
        scene d20s1-19 mc-sy-arj-shower5_c1_i with dissolve
        play voice3 stacy_huh noloop
        sy "How'd you do that?"
        scene d20s1-17 mc-sy-arj-shower3_c3_i with dissolve
        play voice2 d4s4_mclaugh noloop
        mc "My insane charm and a promise of teaching her how to better discipline her daughter."
        mc "Somehow, she took the bait. Now I just gotta reel her in."
    else:
        scene d20s1-18 mc-sy-arj-shower4_c3_i with dissolve
        play voice2 mc_disappointed_ehh3 noloop
        mc "I couldn't do anything about Lewald."
        mc "Hopefully she gives me a pass."
        scene d20s1-19 mc-sy-arj-shower5_c1_i with dissolve
        play voice3 stacy_huh noloop
        sy "Maybe you should wear a big cross to the exam? Appeal to her religious side a bit."
        scene d20s1-17 mc-sy-arj-shower3_c3_i with dissolve
        play voice2 d2s9_confused noloop volume 1.4
        mc "At this point, that's not a bad idea, actually."

    if d19s08_mh_help is True or d19s03_go_to_mh is True:
        $ d20s01_judges_pursued += 1
        scene d20s1-19 mc-sy-arj-shower5_c3_i with dissolve
        play voice2 mc_thinking_mmm4 noloop
        if d20s01_judges_pursued  > 0:
            mc "And with Zara, the best I could come up with was to talk with her."
        else:
            mc "I couldn't come up with anything to get Zara. The only thing I can really do is talk with her."
        scene d20s1-21 mc-sy-arj-shower7_c1_i with dissolve
        play voice2 d3s11b_mcheh noloop
        mc "I called Lyssa to get her help as well."
        mc "Not sure there's much that she could do here, but having a lawyer with you never hurts."
        scene d20s1-21 mc-sy-arj-shower7_c3_i with dissolve
        play voice3 polly_impressed noloop
        sy "Zarah won't stand a chance with Lyssa there."
    else:
        scene d20s1-19 mc-sy-arj-shower5_c3_i with dissolve
        play voice2 mc_arrogant_nah1 noloop
        mc "I tried to see if there's anything I could do about Zara, but nope."
        mc "At this point, I'm just hoping for a miracle. Nothing else would change her vote."

    if d19s07_mk_nordin is True:
        $ d20s01_judges_pursued  += 1
        scene d20s1-18 mc-sy-arj-shower4_c4_i with dissolve
        play voice2 mc_scared_oh3 noloop
        if d20s01_judges_pursued  > 0:
            mc "And I managed to convince Maria to fuck Nordin."
        else:
            mc "I managed to convince Maria to fuck Nordin."
        scene d20s1-20 mc-sy-arj-shower6_c3_i with dissolve
        play voice4 amrose_surprised_what noloop
        arj "Wait, what?"
        play voice2 d9s2_yeah noloop volume 2.0
        mc "Yep. It was...surprisingly easy."
        scene d20s1-20 mc-sy-arj-shower6_c2_i with dissolve
        play voice3 stacy_mmm2 noloop
        sy "Who's Maria again?"
        scene d20s1-20 mc-sy-arj-shower6_c1_i with dissolve
        play voice4 amrose_arrogant_hmm2 noloop
        arj "Some lesbian. Though that's becoming more and more of a lie everyday it seems."
    else:
        scene d20s1-18 mc-sy-arj-shower4_c4_i with dissolve
        play voice2 mc_disappointed_ehh2 noloop
        mc "There wasn't much I could do for Nordin."
        mc "I just have to hope that I studied hard enough I guess."

    if d20s01_judges_pursued  == 0:
        scene d20s1-25 mc-sy-arj-end2_c2_i with dissolve
        play voice2 mc_disappointed_ah2 noloop
        mc "So I'm pretty much screwed basically."
        if study_points >= 4:
            scene d20s1-21 mc-sy-arj-shower7_c1_i with dissolve
            play voice2 d1s5_mchappy noloop volume 1.6
            mc "I'm confident about acing the actual exam. I've studied hard."
            mc "I just gotta hope and pray that the judges take it easy on me, I guess..."

    play sound sfx_hands_clap3
    $ Lovense.vibrate(5)
    scene d20s1-19 mc-sy-arj-shower5_c2_i with dissolve
    pause
    play voice2 d1s1_mmm noloop
    play sound sfx_bath_out1
    scene d20s1-23 mc-sy-arj-hug_c1_i with dissolve
    pause
    scene d20s1-23 mc-sy-arj-hug_c2_i with dissolve
    play voice4 amrose_happy_mmm noloop
    arj "Hey, you're gonna pull through. I know it. Regardless of what happens today."
    scene d20s1-23 mc-sy-arj-hug_c3_i with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "I hope so."
    scene d20s1-24 mc-sy-arj-end1_c3_i with dissolve
    play voice3 stacy_hmm noloop
    sy "And if you don't, you can become my pantry rat. I don't mind."
    sy "Just keep the place clean when I'm gone."
    $ Lovense.vibrate(2)
    scene d20s1-24 mc-sy-arj-end1_c2_i with dissolve
    play voice2 mc_surprised_wow3 noloop
    mc "Wow, what a generous offer. I would take it 'cept you barely even have a pantry for me to be a rat in."
    scene d20s1-25 mc-sy-arj-end2_c3_i with dissolve
    play voice3 stacy_angryhuh noloop
    sy "Considering you picked this place for me, whose fault is that exactly?"
    sy "Oh yeah, when are we going to the server room, by the way?"
    scene d20s1-25 mc-sy-arj-end2_c1_i with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Definitely after the exam. Probably around sunset."
    mc "I'll need some time to settle after the exam. And it's best we go when there aren't a lot of people around."
    scene d20s1-26 mc-sy-arj-end3_c2_i with dissolve
    play voice4 amrose_yes_yeah1 noloop
    arj "That sounds good to me."
    scene d20s1-26 mc-sy-arj-end3_c3_i with dissolve
    play voice3 stacy_yay noloop
    sy "Nice. I can't wait."
    stop music fadeout 3.0
    stop sound4 fadeout 2.0
    $ renpy.music.set_volume(1.0, 7.0, "sound4")
    $ renpy.music.set_volume(1.0, 7.0, "music")

    $ Lovense.stop()

    jump d20s02tl
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
