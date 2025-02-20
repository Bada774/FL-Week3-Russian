image d20s06-a1 = Movie(play = "images/Day-20/s06/anim/d20s06-a59-1-2x-50fps.webm", start_image = "d20s06-a59-1 mc-op-theater-jerking-01")
image d20s06-a1-f = Movie(play = "images/Day-20/s06/anim/d20s06-a59-1-2x-60fps.webm", start_image = "d20s06-a59-1 mc-op-theater-jerking-01")
image d20s06-a2 = Movie(play = "images/Day-20/s06/anim/d20s06-a59-2-2x-50fps.webm", start_image = "d20s06-a59-2 mc-op-theater-jerking-01")
image d20s06-a2-f = Movie(play = "images/Day-20/s06/anim/d20s06-a59-2-2x-60fps.webm", start_image = "d20s06-a59-2 mc-op-theater-jerking-01")
image d20s06-a3 = Movie(play = "images/Day-20/s06/anim/d20s06-a71-1-2x-50fps.webm", start_image = "d20s06-a71-1 mc-op-outside-bj-01")
image d20s06-a3-f = Movie(play = "images/Day-20/s06/anim/d20s06-a71-1-2x-60fps.webm", start_image = "d20s06-a71-1 mc-op-outside-bj-01")
image d20s06-a4 = Movie(play = "images/Day-20/s06/anim/d20s06-a71-2-2x-50fps.webm", start_image = "d20s06-a71-2 mc-op-outside-bj-01")
image d20s06-a4-f = Movie(play = "images/Day-20/s06/anim/d20s06-a71-2-2x-60fps.webm", start_image = "d20s06-a71-2 mc-op-outside-bj-01")
image d20s06-a5 = Movie(play = "images/Day-20/s06/anim/d20s06-a71-3-2x-50fps.webm", start_image = "d20s06-a71-3 mc-op-outside-bj-01")
image d20s06-a5-f = Movie(play = "images/Day-20/s06/anim/d20s06-a71-3-2x-60fps.webm", start_image = "d20s06-a71-3 mc-op-outside-bj-01")
image d20s06-a6 = Movie(play = "images/Day-20/s06/anim/d20s06-a91-1-2x-50fps.webm", start_image = "d20s06-a91-1 mc-op-blush-jerk-01")
image d20s06-a6-f = Movie(play = "images/Day-20/s06/anim/d20s06-a91-1-2x-60fps.webm", start_image = "d20s06-a91-1 mc-op-blush-jerk-01")
image d20s06-a7 = Movie(play = "images/Day-20/s06/anim/d20s06-a91-2-2x-50fps.webm", start_image = "d20s06-a91-2 mc-op-blush-jerk-01")
image d20s06-a7-f = Movie(play = "images/Day-20/s06/anim/d20s06-a91-2-2x-60fps.webm", start_image = "d20s06-a91-2 mc-op-blush-jerk-01")
image d20s06-a8 = Movie(play = "images/Day-20/s06/anim/d20s06-a91-3-2x-50fps.webm", start_image = "d20s06-a91-3 mc-op-blush-jerk-01")
image d20s06-a8-f = Movie(play = "images/Day-20/s06/anim/d20s06-a91-3-2x-60fps.webm", start_image = "d20s06-a91-3 mc-op-blush-jerk-01")

label d20s06:

    $ d20s06_kiss_op = False
    $ d20s06_eat_cum = False

    if date_op is False:
        stop music fadeout 3.0
        jump d20s07

    scene black
    show screen scene_transistion(_("Some time later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.3, 3.0, "music")
    queue music music_melancholy_forever
    $ renpy.music.set_volume(0.5, 1.0, "sound2")
    play sound2 distanttraffic fadein 2.0
    scene d20s06-00 mc_op_date
    with Fade(0.5, 0.5, 0.9)
    pause
    play sound sfx_car_approach1 fadein 1.0
    scene d20s06-01 mc_op_date_getsin with dissolve
    play voice2 d1s5_mcthinks noloop
    mct "Is that Lyssa's car?"
    play sound3 sfx_car_door_open1 noloop
    scene d20s06-02 mc_op_date_getsin with dissolve
    play voice3 oliver_hey_happy noloop
    op "Hey! It's great to see you!"
    $ renpy.music.set_volume(0.1, 1.5, "sound2")
    play sound3 sfx_car_door_closed1 noloop
    scene d20s06-03 mc_op_date with dissolve
    play voice2 d1s2_mchey noloop
    mc "Hey! Same here. For a sec I thought Lyssa was going to be joining in as well."
    scene d20s06-04 mc_op_date with dissolve
    play voice3 oliver_yeah2 noloop
    op "Oh, yeah. I told Miss Harris about the date, and she insisted that I use her car instead of renting one."
    scene d20s06-05 mc_op_date with dissolve
    play voice2 d3s11b_mcheh noloop
    mc "Yep. That sounds like her."
    scene d20s06-06 mc_op_date_box with dissolve
    play voice3 oliver_um1 noloop
    op "Here. It's, uhm, a gift..."
    play sound3 sfx_paper_slide1 noloop
    scene d20s06-07 mc_op_date_mcbox with dissolve
    play voice2 d1s2_hmm noloop
    mc "What is this?"
    scene d20s06-08 mc_op_date_openbox with dissolve
    play voice3 oliver_emm1 noloop
    op "Well, I thought it'd be nice, 'cause uhm..."
    scene d20s06-09 mc_op_date_pullsout with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Oliver, you didn't have to buy this."
    scene d20s06-10 mc_op_date with dissolve
    play voice3 oliver_oh1 noloop
    op "Oh, I didn't buy it! My landlady has a nice garden and I thought about you and..."
    scene d20s06-11 mc_op_date_words with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.5
    mc "Oliver... I— Thank you. I appreciate this. I've never been given flowers before."
    scene d20s06-12 mc_op_date_beaming with dissolve
    play voice3 oliver_huh6 noloop
    op "I'm glad you like it. I thought that it might've been too much."
    scene d20s06-13 mc_op_date with dissolve
    play voice2 d9s3_no noloop volume 2.0
    mc "No, it's great. Thank you."
    scene d20s06-14 mc_op_date_point with dissolve
    play voice3 oliver_huh4 noloop
    op "You look fantastic as well, by the way. I feel like I might've underdressed."
    scene d20s06-15 mc_op_date_point with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, this? Thanks, but don't worry about it. I'm coming straight from my finals, so I'm the one that's overdressed here."
    $ renpy.music.set_volume(0.5, 2.5, "sound2")
    play sound3 sfx_car_engine1 fadein 4.0 volume 1.6
    scene d20s06-16 mc_op_date_driving with dissolve
    play sound sfx_car_startmove fadein 1.5
    play voice3 oliver_oh2 noloop
    op "Oh? You had your finals today? How'd it go?"
    if d20s04_votes == 3:
        scene d20s06-17 mc_op_date_tally with dissolve
        play voice2 mc_happy_oof1 noloop
        mc "Pretty damn well, actually."
        mc "There was a lot of bullshit I had to deal with, but I somehow pulled through in the end."
        scene d20s06-18 mc_op_date_tally with dissolve
        play voice3 oliver_yeah2 noloop
        op "Fuck yeah! That's great to hear."
        scene d20s06-21 mc_op_date_nods with dissolve
    elif d20s04_votes == 2:
        scene d20s06-19 mc_op_date_tally with dissolve
        play voice2 mc_happy_oof3 noloop
        mc "I pulled through."
        mc "Honestly, I wasn't expecting to pass. But I guess Lady Luck was looking out for me today."
        scene d20s06-20 mc_op_date_tally with dissolve
        play voice3 oliver_hey_confident noloop
        op "Hey, a win is a win, right?"
        scene d20s06-21 mc_op_date_nods with dissolve
        play voice2 mc_yes_yes1 noloop
        mc "Right."
    else:
        scene d20s06-23 mc_op_date with dissolve
        play voice2 mc_arrogant_nah1 noloop
        mc "I'd prefer to not talk about it right now, Oliver."
        scene d20s06-22 mc_op_date with dissolve
        play voice3 oliver_ah2 noloop
        op "Oh, I, uh, I'm sorry, I didn't—"
        scene d20s06-25 mc_op_date with dissolve
        play voice2 mc_no_no5 noloop
        mc "It's okay. You didn't do anything wrong. I'm just tuckered out from all the exam stuff. So I'd prefer to talk about something else."
        scene d20s06-24 mc_op_date with dissolve
        play voice3 oliver_okay1 noloop
        op "I understand."
        scene d20s06-21 mc_op_date_nods with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "What about you?"
    scene d20s06-22 mc_op_date with dissolve
    play voice3 oliver_hmm1 noloop volume 1.6
    op "Hm? What about me?"
    scene d20s06-19 mc_op_date_tally with dissolve
    play voice2 d2s9_confused noloop
    mc "Do you not have any exams or whatever?"
    scene d20s06-20 mc_op_date_tally with dissolve
    play voice3 oliver_no2 noloop
    op "Oh, no. I don't go to college, and I'm done with school."
    op "I'm an apprentice under Miss Harris."
    scene d20s06-17 mc_op_date_tally with dissolve
    play voice2 mc_arrogant_huh1 noloop volume 0.85
    mc "Really? Huh, that's interesting. I've been meaning to ask what you did for ages now."
    scene d20s06-26 mc_op_date_smiles with dissolve
    play voice3 oliver_huh3 noloop volume 1.4
    op "You didn't know? What did you think I was doing?"
    scene d20s06-27 mc_op_date with dissolve
    play voice2 mc_no_no2 noloop
    mc "No. And I have no clue. I guess I thought you were some sort of assistant to Lyssa."
    scene d20s06-28 mc_op_date with dissolve
    play voice3 oliver_mmm1 noloop
    op "Well, that's not entirely incorrect. I do assist Miss Harris with a lot of stuff."
    op "But yeah. I basically study under her and hope that one day I will become as great as her."
    scene d20s06-29 mc_op_date with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "That's certainly a tall order, but if anyone can, I'm sure it'd be you."
    scene d20s06-30 mc_op_date_blush with dissolve
    play voice3 oliver_heh2 noloop volume 1.25
    op "Thank you."
    $ renpy.music.set_volume(0.2, 2.0, "sound2")
    stop sound3 fadeout 1.0
    play sound sfx_car_approach1 fadein 1.0
    scene d20s06-31 mc_op_date_parked_movie with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "What are we gonna be watching, by the way? Did you have anything planned?"
    scene d20s06-32 mc_op_date_parked with dissolve
    play voice3 oliver_yes1 noloop
    op "Oh, yes. I found a nice French movie that I thought might be nice. It's called \"Amélie.\" Have you heard of it?"
    scene d20s06-33 mc_op_date_parked with dissolve
    play voice2 mc_no_nope1 noloop
    mc "I haven't. Sounds nice though."
    scene d20s06-34 mc_op_date_parked with dissolve
    play voice3 oliver_mmm2 noloop
    op "I've heard good things about it, but it's not too popular over here."
    op "So I thought that it'd be the perfect movie to watch without it being too crowded."
    scene d20s06-35 mc_op_date_parked with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Smart. Hopefully we can have the theater to ourselves."
    scene d20s06-36 mc_op_date_parked with dissolve
    play voice3 oliver_yep1 noloop
    op "Yep!"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.5

label replay_d20s06 hide:

    if _in_replay:
        $ renpy.music.set_volume(0.3, 3.0, "music")
        play music music_melancholy_forever fadein 2.0
    play sound3 sfx_tv_film1 fadein 3.0
    scene d20s06-37 mc_op_date with Fade(0.4, 0.4, 0.4)
    pause
    scene d20s06-38 mc_op_date with dissolve
    play voice3 oliver_hey_unsure noloop
    op "Hey... Would you mind if I put my head on your shoulder?"
    scene d20s06-39 mc_op_date_surprised with dissolve
    play voice2 d9s3_no noloop volume 2.0
    mc "No. I don't mind. Go ahead."
    scene d20s06-40 mc_op_date_shoulder with dissolve
    pause
    scene d20s06-41 mc_op_date_montage_surprised with dissolve
    pause
    scene d20s06-42 mc_op_date_montage_humored with dissolve
    pause
    scene d20s06-43 mc_op_date_montage_focused with dissolve
    pause
    scene d20s06-44 mc_op_date_montage_satisfy with dissolve
    pause
    scene d20s06-45 mc_op_date_montage with dissolve
    pause
    scene d20s06-46 mc_op_date_montage with dissolve
    pause

    $ Lovense.stop()

    scene d20s06-47 mc_op_date_look with dissolve
    pause
    $ renpy.music.set_volume(0.3, 2.0, "sound3")
    $ Lovense.vibrate(1)
    play sound sfx_cloth_rustling4 volume 0.8
    scene d20s06-48 mc_op_date_leg with dissolve
    pause
    scene d20s06-49 mc_op_date with dissolve
    play voice2 mc_surprised_huh4 noloop
    mc "Oliver? What are you doing?"
    scene d20s06-50 mc_op_date with dissolve
    play voice3 oliver_huh5 noloop
    op "I... Do you want me to stop?"
    scene d20s06-51 mc_op_date with dissolve
    play voice2 mc_no_uhuh2 noloop
    mc "...No."
    scene d20s06-52 mc_op_date_hand with dissolve
    pause
    scene d20s06-53 mc_op_date_massage with dissolve
    pause
    scene d20s06-54 mc_op_date with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "I didn't pin you to be the adventurous type."
    scene d20s06-55 mc_op_date_smirk with dissolve
    pause
    scene d20s06-56 mc_op_date_chuckle with dissolve
    play voice2 d4s4_mclaugh noloop
    mc "*Chuckles* You're gonna get us caught."
    scene d20s06-57 mc_op_date with dissolve
    play voice3 oliver_ehh2 noloop
    op "I wouldn't mind."
    play sound sfx_jeans_fly1
    $ Lovense.vibrate(3)
    scene d20s06-58 mc_op_date_massage with dissolve
    pause
    scene d20s06-a59-1 mc-op-theater-jerking-01 with dissolve
    pause
    play sound sfx_handjob_cream1 loop
    play voice2 d7s4_mcbreathing volume 0.6
    $ Lovense.vibrate(5)
    scene d20s06-a1
    pause
    scene d20s06-a2 with dissolve
    pause
    $ Lovense.vibrate(7)
    scene d20s06-a1-f with dissolve
    pause
    scene d20s06-a2-f with dissolve
    pause
    stop sound fadeout 1.0
    scene d20s06-60 mc_op_date_benddown with dissolve
    pause
    play voice3 oliver_ah2 noloop
    stop voice2 fadeout 1.0
    play sound sfx_flashlight_on1
    $ Lovense.vibrate(1)
    scene d20s06-61 mc_op_date_caught with dissolve
    play voice4 pete_hey_angry noloop
    "Employee" "Hey! You two! You can't do that here!"
    scene d20s06-62 mc_op_date_stand with dissolve
    play voice2 d2s12_emmm noloop
    mc "We're cool, dude. Chill out."
    scene d20s06-63 mc_op_date with dissolve
    play voice4 pete_disappointed_mmm1 noloop
    "Employee" "I'm gonna have to escort you two out. Sorry, man. Policy."
    scene d20s06-64 mc_op_date with dissolve
    play voice3 oliver_ehh1 noloop
    op "Jus-just give us a second."
    scene d20s06-65 mc_op_date_leave with dissolve
    pause
    stop sound3 fadeout 2.0
    $ renpy.music.set_volume(0.4, 1.5, "sound2")
    play sound2 distanttraffic fadein 2.0
    scene d20s06-66 mc_op_date with Fade(0.4, 0.4, 0.4)
    play voice2 mc_disappointed_ehh2 noloop
    mc "I didn't even hear him coming near us."
    scene d20s06-67 mc_op_date with dissolve
    play voice3 oliver_aga1 noloop
    op "I know! It was kinda exciting."
    op "Do you, uhm, want to continue in the car?"
    scene d20s06-68 mc_op_date with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "*Chuckles* Yes. I'd like that."
    play sound sfx_car_door_open1
    scene d20s06-69 mc_op_date_gettingn with dissolve
    pause
    stop sound2 fadeout 2.0
    play sound sfx_car_door_closed1
    $ renpy.music.set_volume(1.0, 0.5, "sound3")
    play sound3 sfx_car_enter1 noloop
    scene d20s06-70 mc_op_daten back with dissolve
    pause
    play voice3 mc_sex_sucking_slow1 noloop
    $ Lovense.vibrate(6)
    scene d20s06-a71-1 mc-op-outside-bj-01 with dissolve
    stop voice3 fadeout 0.5
    pause
    $ renpy.music.set_volume(0.4, 3.0, "music")
    play voice2 d7s4_mcbreathing
    play voice3 oliver_fsuck
    $ Lovense.pattern("6;10", 1200)
    scene d20s06-a3
    pause
    scene d20s06-a5 with dissolve
    pause
    stop voice3 fadeout 1.0
    $ Lovense.stop()
    $ Lovense.vibrate(3)
    scene d20s06-72 mc_op_date with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "Fuck, Oliver... You've gotten even better at this."
    play voice3 oliver_happy_hmm1 noloop
    scene d20s06-73 mc_op_date_smile with dissolve
    pause
    play voice2 d7s4_mcbreathing
    play voice3 oliver_suck2
    $ Lovense.pattern("6;10", 1200)
    scene d20s06-a4 with dissolve
    pause
    play voice3 oliver_fsuck2
    $ Lovense.pattern("6;10", 700)
    scene d20s06-a3-f with dissolve
    pause
    scene d20s06-a5-f with dissolve
    pause
    stop voice3 fadeout 1.0
    $ Lovense.stop()
    $ Lovense.vibrate(10)
    scene d20s06-74 mc_op_date with dissolve
    play voice2 mc_pain_mff5 noloop
    mc "Oliver... Oliver, I'm close."
    play voice2 d7s4_mcbreathing
    play voice3 oliver_fsuck2
    $ Lovense.pattern("8;12", 700)
    scene d20s06-a4-f with dissolve
    pause
    play voice3 oliver_ah1 noloop
    play voice2 d1s5_orgasm2 noloop
    $ Lovense.stop()
    $ Lovense.vibrate(17)
    scene d20s06-75 mc_op_date_cum with vpunch
    pause
    $ Lovense.vibrate(2)
    scene d20s06-76 mc_op_date_cumface with dissolve
    play voice3 oliver_laugh1 noloop
    op "Woah, you came a lot."
    scene d20s06-77 mc_op_date with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "Shit, sorry."
    scene d20s06-78 mc_op_date with dissolve
    play voice3 oliver_no1 noloop volume 0.8
    op "No, no, I like it."
    menu:
        "Kiss him"(hint="d20s06m01c01"):
            $ d20s06_kiss_op = True

            play voice3 oliver_relief1 noloop
            scene d20s06-79 mc_op_date_lick with dissolve
            pause
            scene d20s06-80 mc_op_date_kiss_cupface with dissolve
            pause
            play sound dahlia_kiss_french1
            play voice3 oliver_mmm2 noloop
            scene d20s06-81 mc_op_date_kiss with dissolve
            pause
            scene d20s06-82 mc_op_date_kiss with dissolve
            play voice3 oliver_huh2 noloop
            op "[mcname]? What are you—?"
            play voice2 d1s1_mmm noloop
            play sound maria_kiss1
            scene d20s06-83 mc_op_date_kiss with dissolve
            pause
            scene d20s06-84 mc_op_date_kiss with dissolve
            play voice3 oliver_ah2 noloop
            op "I— You— Why—"
            scene d20s06-85 mc_op_date_dont with dissolve
            play voice2 shhh noloop
            mc "Shh. Don't say anything."
        "Don't"(hint="d20s06m01c02"):

            scene d20s06-85 mc_op_date_dont with dissolve
            play voice2 mc_arrogant_hm1 noloop
            mc "Now it's my turn."

    scene d20s06-86 mc_op_date_spoon with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "Let me take care of you now."
    scene d20s06-87 mc_op_date_ear with dissolve
    queue voice2 d14s16_smell noloop
    mc "Just keep your eyes closed and lean back on me."
    play voice3 oliver_sex_closedmoan1 noloop
    play sound sfx_jeans_on1
    scene d20s06-88 mc_op_date_eyesclosed with dissolve
    pause
    scene d20s06-89 mc_op_date_pants with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "All ready to go, huh?"
    scene d20s06-90 mc_op_date_blush with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "Block out every other sensation and just feel my hand and my body on you."
    scene d20s06-91 mc_op_date_blush_jerk with dissolve
    pause
    scene d20s06-92 mc_op_date_blush_balls with dissolve
    play voice3 oliver_ehh2 noloop
    op "*Whimpers* [mcname]..."
    scene d20s06-a91-1 mc-op-blush-jerk-01 with dissolve
    pause
    play voice3 oliver_sex_closedmoans1
    play voice2 d7s4_mcbreathing volume 0.2 fadein 2.5
    play sound sfx_handjob_cream1 loop
    $ Lovense.vibrate(6)
    scene d20s06-a6
    pause
    scene d20s06-a8 with dissolve
    pause
    scene d20s06-a7 with dissolve
    pause
    play voice3 oliver_sex_openmoans1
    $ Lovense.vibrate(7)
    scene d20s06-a6-f with dissolve
    pause
    scene d20s06-a8-f with dissolve
    pause
    play voice3 oliver_sex_openmoan1 noloop
    stop sound fadeout 1.0
    stop voice2 fadeout 1.0
    scene d20s06-92 mc_op_date_blush_balls with dissolve
    op "*Staggered moans* [mcname], I'm gonna c-cum!"
    scene d20s06-93 mc_op_date_blush_balls with dissolve
    play voice2 d9s2_mcyes noloop volume 2.0
    mc "Cum for me, Olie."
    $ Lovense.vibrate(8)
    play voice3 oliver_sex_openmoans1
    play voice2 d7s4_mcbreathing volume 0.4
    play sound sfx_handjob_cream1 loop
    scene d20s06-a7-f with dissolve
    pause
    play voice3 oliver_sex_orgasm1 noloop
    stop sound fadeout 1.0
    stop voice2 fadeout 1.0
    $ Lovense.vibrate(10)
    scene d20s06-94 mc_op_date_blush_cum with vpunch
    pause
    play voice3 oliver_sexphrase_fuck noloop
    $ Lovense.vibrate(12)
    scene d20s06-95 mc_op_date with vpunch
    op "Fuck."
    $ Lovense.vibrate(2)
    scene d20s06-96 mc_op_date_hold with dissolve
    play voice3 oliver_sex_openmoan2 noloop
    op "I've never cum that hard before."
    op "You're amazing!"
    scene d20s06-97 mc_op_date_chuckles with dissolve
    play voice2 d9s2_yeah noloop volume 1.8
    mc "*Chuckles* I've had practice with your Miss Harris."
    menu:
        "Eat Oliver's cum"(hint="d20s06m02c01"):
            $ d20s06_eat_cum = True

            play sound mc_sex_sucking_slow1 noloop
            scene d20s06-98 mc_op_date_eatcum with dissolve
            stop sound fadeout 0.5
            pause
            play voice3 oliver_ah1 noloop
            scene d20s06-99 mc_op_date_surprise with dissolve
            play voice2 mc_eating_mmm noloop
            mc "Hm. Sweeter than I thought it'd be."
            play voice3 oliver_heh1 noloop
            scene d20s06-100 mc_op_date_blush with dissolve
            pause
        "Don't"(hint="d20s06m02c02"):

            pass

    scene d20s06-101 mc_op_date_look with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "We should probably get cleaned up, and also check if we got any...\"foreign liquids\" anywhere."
    scene d20s06-102 mc_op_date_chuckle with dissolve
    play voice3 oliver_laugh1 noloop
    op "*Chuckles* Yeah, we should. But uhm... Would you mind if we stayed like this for just a bit longer?"
    scene d20s06-103 mc_op_date_hug with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Of course not."

    $ Lovense.stop()

    $ renpy.end_replay()
    $ unlock_gallery_slot("scene", "d20s06")

    stop music fadeout 3.0
    jump d20s07
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
