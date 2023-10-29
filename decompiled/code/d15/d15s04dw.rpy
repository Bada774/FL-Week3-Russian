image d15s04dw_glambot1 = Movie(play = "images/Day-15/Scene-04/dahlia/anim/d15s04a-a0-4x-60fps.webm", start_image = "d15s04a-a0 glambot000_i", image = "d15s04a-a0 glambot196_i", loop = False)
image d15s04dw_glambot2 = Movie(play = "images/Day-15/Scene-04/dahlia/anim/d15s04a-a0-2-2x-50fps.webm", start_image = "d15s04a-34-02-a0-02-glambot-000_i", image = "d15s04a-34-02-a0-02-glambot-196_i", loop = False)

image d15s04dw_mc_book_spanking:
    "d15s04a-39 mc-dw-sb-dahlia-preparing_c3"
    pause (0.05)
    "d15s04a-45 mc-dw-sb-book-hit_c3"
    pause (0.05)
    "d15s04a-46 mc-dw-sb-book-hit_c3" with hpunch
    pause (0.05)

label replay_d15s04dw:
label d15s04dw:

    if not _in_replay:
        scene black
        show screen scene_transistion(_("30 minutes later"))
        with Fade(0.9, 0.5, 0.5)
        pause
        hide screen scene_transistion
        scene d15s04-15 mc-study-studying_c1
        with Fade(0.5, 0.5, 0.9)
        pause
    if _in_replay:
        play music slow_love
    scene d15s04a-01 mc-study-dahlia_c1 with dissolve
    play voice2 mc_arrogant_hm2 noloop
    mct "Hmm. {w}That should be enough time. They should be here soon."
    mct "I hope they arrive in the right order, otherwise this is never going to work."
    scene d15s04a-02 mc-dw-dahlia-knock_c1 with dissolve
    call knock from _call_knock
    mct "Hopefully that's Dahlia."
    scene d15s04a-03 mc-dw-come-in_c1 with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "Come in! It's open!"
    play sound sfx_door_closed2
    scene d15s04a-03 mc-dw-come-in_c2 with dissolve
    play voice3 dahlia_hey_angry noloop
    dw "Hey, [mcname]. What's going on? {w}You sounded so serious over the phone."
    scene d15s04a-04 mc-dw-gesture_c2 with dissolve
    play voice2 mc_no_nah2 noloop
    mc "Nothing bad, I just want to have a serious talk with you about something."
    mc "Why don't we sit down over here on my bed."
    scene d15s04a-05 mc-dw-sitting-on-bed_c1 with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "It's beautiful outside today, don't you think?"
    scene d15s04a-05 mc-dw-sitting-on-bed_c2 with dissolve
    play voice3 dahlia_angry_oh noloop
    dw "Oh fuck. You're dying?"
    scene d15s04a-06 mc-dw-mc-deny_c1 with dissolve
    play voice2 mc_no_no4 noloop
    mc "No! Nothing like that. {w}Look, I was thinking about ways I could improve our relationship."
    scene d15s04a-06 mc-dw-mc-deny_c2 with dissolve
    play voice3 dahlia_yes_angry noloop
    dw "I've got a few ideas about that too. {w}They start with getting your pants off."
    scene d15s04a-07 mc-dw-mc-talk_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "That sounds like fun too."
    scene d15s04a-08 mc-dw-mc-think_c1 with dissolve
    mct "Although maybe not if she finds out about my cage."
    scene d15s04a-07 mc-dw-mc-talk_c1 with dissolve
    play voice2 d2s9_confused noloop
    mc "Anyway, I got to thinking about how upset you are at-"
    $ renpy.music.set_volume(1.0, 0.0, "sound")
    play sound [sfx_camera_fly1, sfx_camera_fly1]
    scene d15s04dw_glambot1 with dissolve
    pause(7.0)
    play voice4 samiya_eeem1 noloop
    sb "What is this problem you needed me to-?"
    stop music fadeout 0.2
    play sound sfx_music_shutdown1
    queue music ("<silence 0.6>")
    queue music big_problems
    scene d15s04a-10 mc-dw-sb-dahlia-jump_c1 with hpunch
    play voice3 dahlia_old_argh3 noloop
    dw "What the fuck are you doing here?!"
    scene d15s04a-10 mc-dw-sb-dahlia-jump_c2 with dissolve
    play voice4 samiya_huh4 noloop
    sb "Oh, blow it somewhere else, sister. {w}[mcname], what am I doing here?"
    scene d15s04a-11 mc-dw-sb-mc-calming_c1 with dissolve
    play voice2 mc_surprised_wow1 noloop
    mc "Woah, woah, woah. I know there's some bad blood between you-"
    scene d15s04a-12 mc-dw-sb-yelling_c1 with dissolve
    play voice3 dahlia_angry_argh1 noloop
    dw "Did you call her over here to ambush me?"
    scene d15s04a-12 mc-dw-sb-yelling_c2 with dissolve
    play voice4 samiya_youu noloop
    sb "Fucking asshole! I don't want to see her lame ass!"
    scene d15s04a-12 mc-dw-sb-yelling_c3 with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Why don't we all just calm down and talk this over."
    scene d15s04a-13 mc-dw-sb-samiya-sarcastic_c2 with dissolve
    play voice4 samiya_laughing1 noloop
    sb "So this is supposed to be some sort of intervention? Are we talking about her drinking?"
    scene d15s04a-13 mc-dw-sb-samiya-sarcastic_c1 with dissolve
    play voice3 dahlia_arrogant_pff noloop
    dw "Oh, ha ha, bitch. Maybe we're here to discuss your sex addiction."
    scene d15s04a-14 mc-dw-sb-samiya-shrug_c2 with dissolve
    play voice4 samiya_yes3 noloop
    sb "Sure, let's do that. I love talking about all the people I've fucked."
    scene d15s04a-13 mc-dw-sb-samiya-sarcastic_c1 with dissolve
    play voice3 dahlia_angry_ah2 noloop
    dw "Including my boyfriend!!!"
    scene d15s04a-14 mc-dw-sb-samiya-shrug_c2 with dissolve
    play voice4 samiya_huh noloop
    sb "How many times do we have to have this argument?!"
    scene d15s04a-14 mc-dw-sb-samiya-shrug_c1 with dissolve
    play voice3 dahlia_angry_hm2 noloop
    dw "Yeah, [mcname]. How many times?!"
    scene d15s04a-14 mc-dw-sb-samiya-shrug_c3 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "I'm sure there's a perfectly reasonable-"
    scene d15s04a-15 mc-dw-sb-dahlia-commanding-to-strip_c2 with dissolve
    play voice4 samiya_ah noloop
    sb "Oh, like either of us are reasonable people. You must be the dumbest smart person-"
    scene d15s04a-15 mc-dw-sb-dahlia-commanding-to-strip_c1 with dissolve
    play voice3 dahlia_old_argh noloop
    dw "You know what, [mcname]? I've got an idea. Let's try this."
    scene d15s04a-15 mc-dw-sb-dahlia-commanding-to-strip_c3 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Dahlia, could you try to calm down for a second.{w} Samiya, could you just tell us-"
    scene d15s04a-16 mc-dw-sb-shocked_c1 with dissolve
    play voice3 dahlia_angry_argh1 noloop
    dw "PANTS OFF!"
    scene d15s04a-16 mc-dw-sb-shocked_c3 with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "What?"
    scene d15s04a-16 mc-dw-sb-shocked_c2 with dissolve
    play voice4 samiya_huh3 noloop
    sb "What?"
    scene d15s04a-17 mc-dw-sb-samyia-amused_c1 with dissolve
    play voice3 chloe_angry_argh2 noloop
    dw "Your Mistress Gave You An Order!"
    dw "GET YOUR FUCKING PANTS OFF NOW, SLAVE!!!"
    scene d15s04a-17 mc-dw-sb-samyia-amused_c2 with dissolve
    play voice4 samiya_kghhh noloop
    sb "Oh, fuck. You've gotta be kidding me."
    scene d15s04a-17 mc-dw-sb-samyia-amused_c3 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "This really isn't the time-"
    scene d15s04a-17 mc-dw-sb-samyia-amused_c2 with dissolve
    play voice4 samiya_laughing1 noloop
    sb "This is too funny."
    scene d15s04a-18 mc-dw-sb-infront-of-her_c1 with dissolve
    play voice3 dahlia_pain_ah2 noloop
    dw "No?! You want to disobey me?! HERE?! NOW?! IN FRONT OF THIS SLUT?!!!"
    play voice2 mc_disappointed_ehh4 noloop
    mc "Dahlia, be serious-"
    play sound sfx_kick1
    scene d15s04a-19 mc-dw-sb-pushing-mc_c1 with dissolve
    play voice3 dahlia_angry_argh1 noloop
    dw "Oh, I'm serious."
    play sound sfx_bed_slide1


    $ Lovense.stop()

    scene d15s04a-20 mc-dw-sb-pulling-pants_c1 with dissolve
    pause
    play sound sfx_jeans_on1
    play voice4 samiya_huh4 noloop
    $ Lovense.vibrate(1)
    sb "You want some help?"
    scene d15s04a-21 mc-dw-sb-cockcage_c1 with hpunch
    play voice3 dahlia_surprised_huh1 noloop
    dw "What. The. Fuck?"
    scene d15s04a-21 mc-dw-sb-cockcage_c3
    if cage_ntr is False:
        show d15s04a-21-over mc-dw-sb-cockcage-lc
    with dissolve
    play voice2 d2s12_emmm noloop
    mc "Dahlia, I can explain."
    scene d15s04a-21 mc-dw-sb-cockcage_c2 with dissolve
    play voice4 dahlia_happy_laugh2 noloop
    sb "Oh no. *giggles* It looks like your slave has given his manhood to someone else."
    scene d15s04a-22 mc-dw-sb-arguing_c1 with dissolve
    play voice3 dahlia_old_argh3 noloop
    dw "WHO HAS THE KEY?!"
    scene d15s04a-22 mc-dw-sb-arguing_c3 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "No one."
    scene d15s04a-22 mc-dw-sb-arguing_c1 with dissolve
    play voice3 chloe_angry_argh5 noloop
    dw "WHO HAS IT???!!!"
    play voice2 mc_disappointed_ehh1 noloop
    mc "It's electronic. {w}Fetish Locator-"
    scene d15s04a-22 mc-dw-sb-arguing_c2 with dissolve
    play voice4 dahlia_happy_laugh3 noloop
    sb "Oh, this just keeps getting better and better"
    scene d15s04a-23 mc-dw-sb-arguing_c1 with dissolve
    play voice3 dahlia_angry_ah2 noloop
    dw "Samiya?"
    scene d15s04a-23 mc-dw-sb-arguing_c2 with dissolve
    play voice4 samiya_yes2 noloop
    sb "Yes?"
    scene d15s04a-22 mc-dw-sb-arguing_c1 with dissolve
    play voice3 chloe_angry_argh6 noloop
    dw "I think I'm going to murder someone."
    scene d15s04a-23 mc-dw-sb-arguing_c2 with dissolve
    play voice4 samiya_hah1 noloop
    sb "You can try."
    scene d15s04a-23 mc-dw-sb-arguing_c1 with dissolve
    play voice3 dahlia_old_upset noloop
    dw "You don't want to see this. {w}I suggest you leave."
    scene d15s04a-22 mc-dw-sb-arguing_c2 with dissolve
    play voice4 samiya_cagh noloop
    sb "Oh, please, bitch. {w}Anything that much fun - I'm going to help."
    scene d15s04a-23 mc-dw-sb-arguing_c1 with dissolve
    play voice3 dahlia_old_argh2 noloop
    dw "You're welcome to try."
    scene d15s04a-22 mc-dw-sb-arguing_c1 with dissolve
    play voice3 chloe_angry_argh2 noloop
    dw "Grab your ankles."
    scene d15s04a-23 mc-dw-sb-arguing_c3 with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Dahlia, please."
    scene d15s04a-22 mc-dw-sb-arguing_c1 with dissolve
    play voice3 chloe_angry_cough noloop
    dw "FIRST - you WILL refer to me as MISTRESS."
    scene d15s04a-22 mc-dw-sb-arguing_c3 with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Yes, Mistress."
    scene d15s04a-22 mc-dw-sb-arguing_c1 with dissolve
    play voice3 chloe_angry_argh3 noloop
    dw "SECOND - you WILL do as you're ordered."
    scene d15s04a-24 mc-dw-sb-grabbing-ankles_c1
    if cage_ntr is False:
        show d15s04a-24-over mc-dw-sb-grabbing-ankles-lc
    with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Yes, Mistress."
    scene d15s04a-25 mc-dw-sb-grabbing-ankles-talk_c2 with dissolve
    play voice3 chloe_angry_breath noloop
    dw "Tell me you love me."
    scene d15s04a-25 mc-dw-sb-grabbing-ankles-talk_c1
    if cage_ntr is False:
        show d15s04a-25-over mc-dw-sb-grabbing-ankles-talk-lc
    with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "I love you, Mistress."
    scene d15s04a-26 mc-dw-sb-grabbing-ankles-talk_c2 with dissolve
    play voice3 dahlia_angry_hm1 noloop
    dw "Tell me you are my possession."
    scene d15s04a-26 mc-dw-sb-grabbing-ankles-talk_c1
    if cage_ntr is False:
        show d15s04a-26-over mc-dw-sb-grabbing-ankles-talk-lc
    with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "I am your possession, Mistress."
    scene d15s04a-25 mc-dw-sb-grabbing-ankles-talk_c2 with dissolve
    play voice3 dahlia_angry_oof noloop
    dw "Tell me you are my slave."
    scene d15s04a-26 mc-dw-sb-grabbing-ankles-talk_c1
    if cage_ntr is False:
        show d15s04a-26-over mc-dw-sb-grabbing-ankles-talk-lc
    with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "I am your slave, Mistress."
    scene d15s04a-27 mc-dw-sb-asking-for-dildo_c1 with dissolve
    play voice3 dahlia_angry_oh noloop
    dw "You're a total slut. Do you have a dildo or something?"
    scene d15s04a-27 mc-dw-sb-asking-for-dildo_c2 with dissolve
    play voice4 samiya_hm1 noloop
    sb "Do you mean in my car, or-"
    play voice3 dahlia_no_serious noloop
    dw "You have something on you?"
    scene d15s04a-28 mc-dw-sb-pulling-down-pants_c2 with dissolve
    play voice4 samiya_mmm3 noloop
    sb "Give me just a second..."
    play sound sfx_skirt_off2
    scene d15s04a-29 mc-dw-sb-samiya-bullet-vibe_c2 with dissolve
    pause
    play voice4 samiya_mmm2 noloop
    scene d15s04a-30 mc-dw-sb-samiya-bullet-vibe_c1 with dissolve
    sb "Will this do?"
    scene d15s04a-30 mc-dw-sb-samiya-bullet-vibe_c3 with dissolve
    play voice3 dahlia_disgust_yah noloop
    dw "Ew. {w}Also, yes."
    scene d15s04a-30 mc-dw-sb-samiya-bullet-vibe_c2 with dissolve
    play voice4 samiya_heeh noloop
    sb "I take it you don't want to touch this?"
    scene d15s04a-30-02 mc-dw-sb-samiya-bullet-vibe_c1 with dissolve
    play voice3 dahlia_arrogant_yeah noloop
    dw "Just shove it up his ass. Don't be gentle."
    play voice2 mc_hey_hey4 noloop
    $ Lovense.vibrate(4)
    scene d15s04a-31 mc-dw-sb-bullet-vibe-enters_c1 with dissolve
    pause
    play voice2 mc_pain_argh1 noloop
    $ Lovense.vibrate(10)
    scene d15s04a-32 mc-dw-sb-bullet-vibe-enters_c1 with dissolve
    pause
    play voice2 d9s5_auch2 noloop
    scene d15s04a-32 mc-dw-sb-bullet-vibe-enters_c2
    if cage_ntr is False:
        show d15s04a-32-over mc-dw-sb-bullet-vibe-enters-lc
    with dissolve
    mc "FUCKING HELL!"
    $ Lovense.vibrate(3)
    scene d15s04a-33 mc-dw-sb-use-talk_c1 with dissolve
    play voice3 dahlia_thinking_oh noloop
    dw "Well done."
    play voice4 samiya_hah1 noloop
    sb "Thanks.{w}.. Do you mind if I ride his face?"
    play voice3 dahlia_arrogant_heh noloop
    dw "Go ahead."
    scene d15s04a-34-02-a0-02-glambot-000_i with dissolve
    play voice4 samiya_huh4 noloop
    sb "Head's or tails, [mcname]?"
    scene d15s04dw_glambot2
    pause
    play voice2 mc_surprised_what1 noloop
    mc "What?"
    scene d15s04a-35 mc-dw-sb-samiya-sit-on-face_c1
    if cage_ntr is False:
        show d15s04a-35-over mc-dw-sb-symiya-sit-on-face-lc
    with dissolve
    play voice4 samiya_yes1 noloop
    queue voice4 samiya_moans1
    play voice2 [d2s12_flicking, d2s12_flicking, d2s12_flicking, d2s12_licking]
    $ Lovense.vibrate(7)
    sb "Tails it is. {w}Lick my ass."
    scene d15s04a-35 mc-dw-sb-samiya-sit-on-face_c2 with dissolve
    play voice3 dahlia_angry_hm1 noloop
    dw "Would you mind holding his ankles?"
    scene d15s04a-36 mc-dw-sb-samiya-holding-ankles_c1 with dissolve
    sb "Sure, no problem."
    scene d15s04a-36 mc-dw-sb-samiya-holding-ankles_c2 with dissolve
    play voice3 dahlia_happy_laugh4 noloop
    dw "He's got a talented tongue, don't you think?"
    scene d15s04a-36-02 mc-dw-sb-licking-ass_c1 with dissolve
    sb "He does. Are you going to spank his ass?"
    scene d15s04a-37 mc-dw-sb-samiya-holding-ankles-talk_c2 with dissolve
    play voice3 dahlia_happy_yay noloop
    dw "I'm sure he's got a book around here somewhere that I can use as a paddle."
    scene d15s04a-38 mc-dw-sb-book_c1 with dissolve
    sb "That's harsh. You can really hurt someone like that."
    scene d15s04a-37 mc-dw-sb-samiya-holding-ankles-talk_c2 with dissolve
    play voice3 dahlia_arrogant_heh noloop
    dw "Do you object?"
    scene d15s04a-38 mc-dw-sb-book_c2 with dissolve
    play voice4 samiya_no1 noloop
    queue voice4 samiya_moans1
    sb "No.{w} That was a compliment."
    scene d15s04a-39 mc-dw-sb-dahlia-preparing_c3 with dissolve
    menu:
        "Stop This Now"(hint="d15s04dwm01c01") if True:


            $ Lovense.stop()

            scene d15s04a-40 mc-dw-sb-abort_c1 with dissolve
            play voice2 mc_pain_argh1 noloop
            stop voice4 fadeout 1.0
            mc "FUCKING STOP IT!!!"
            scene d15s04a-40 mc-dw-sb-abort_c3 with dissolve
            play voice3 dahlia_surprised_what noloop
            dw "What?!"
            scene d15s04a-40 mc-dw-sb-abort_c2 with dissolve
            play voice4 samiya_huh5 noloop
            sb "Huh?"
            scene d15s04a-41 mc-dw-sb-abort-sitting-up_c1 with dissolve
            play voice2 mc_angry_errr2 noloop
            mc "I DID NOT CONSENT TO THIS!!!"
            scene d15s04a-41 mc-dw-sb-abort-sitting-up_c3 with dissolve
            play voice3 dahlia_hey_angry noloop
            dw "Listen, maybe we got carried away-"
            scene d15s04a-42 mc-dw-sb-abort-point-to-leave_c1
            if cage_ntr is False:
                show d15s04a-42-over mc-dw-sb-abort-point-to-leave-lc
            with dissolve
            play voice2 d9s5_auch2 noloop
            mc "JUST GET THE FUCK OUT!!! BOTH OF YOU!!!"
            scene d15s04a-43 mc-dw-sb-samiya-standing_c1 with dissolve
            play voice4 samiya_cagh noloop
            sb "Fine with me."
            play voice3 dahlia_happy_hmm1 noloop
            dw "Um... yeah, okay."
            scene d15s04a-44 mc-dw-sb-leaving_c1 with dissolve
            play voice2 mc_pain_mff5 noloop
            mct "Fucking hell. That couldn't have gone worse."
            scene d15s04a-44 mc-dw-sb-leaving_c2
            if cage_ntr is False:
                show d15s04a-44-over mc-dw-sb-leaving-lc
            with dissolve
            mct "Well,no. {w} I guess it was about to get even worse if I hadn't put an end to that."
            scene d15s04a-44 mc-dw-sb-leaving_c3 with dissolve
            play voice2 mc_pain_mff4 noloop
            mc "Fuck. {w}That woman is going to be the death of me."
            stop music fadeout 3.5

            $ renpy.end_replay()

            jump d15s05
        "Let Them Work Out Their Anger"(hint="d15s04dwm01c02") if True:

            $ d15s04_resolve_part1 = True

            mct "Fine. Whatever. {w}Just endure this a little longer."

    play sound ["<silence 0.1>", spank3]
    play voice2 mc_pain_mff3 noloop
    queue voice2 [d2s12_flicking, d2s12_flicking, d2s12_flicking, d2s12_licking]
    $ Lovense.vibrate(10)
    scene d15s04dw_mc_book_spanking
    pause
    $ Lovense.vibrate(7)
    scene d15s04a-39 mc-dw-sb-dahlia-preparing_c3 with dissolve
    play voice3 chloe_angry_argh5 noloop
    dw "Do you like it [mcname]?"
    play sound ["<silence 0.1>", spank2]
    play voice2 mc_pain_mff4 noloop
    queue voice2 [d2s12_flicking, d2s12_flicking, d2s12_flicking, d2s12_licking]
    $ Lovense.vibrate(11)
    scene d15s04dw_mc_book_spanking
    pause
    $ Lovense.vibrate(7)
    scene d15s04a-39 mc-dw-sb-dahlia-preparing_c3 with dissolve
    mct "This is starting to feel like a bad idea."
    play sound ["<silence 0.1>", spank3]
    play voice2 mc_pain_mff5 noloop
    queue voice2 [d2s12_flicking, d2s12_flicking, d2s12_flicking, d2s12_licking]
    $ Lovense.vibrate(12)
    scene d15s04dw_mc_book_spanking
    pause
    $ Lovense.vibrate(7)
    scene d15s04a-47 mc-dw-sb-dahlia-yelling_c1 with dissolve
    play voice3 [chloe_angry_argh3, chloe_angry_breath] noloop
    dw "I CAN'T {w}FUCKING {w}STAND {w}CHEATERS!!!"
    scene d15s04a-48 mc-dw-sb-climbing-off_c1 with dissolve
    play voice4 samiya_kghhh noloop
    stop voice2 fadeout 3.0
    sb "FINE!"
    scene d15s04a-48 mc-dw-sb-climbing-off_c2 with dissolve
    play voice3 dahlia_pain_sobs noloop
    dw "Fine? {w}What?"
    $ Lovense.vibrate(3)
    scene d15s04a-49 mc-dw-sb-yelling-in-face_c1 with dissolve
    play voice4 samiya_pain noloop
    sb "Fine - I fucked your boyfriend! There. Are you happy? I've finally admitted it!"
    scene d15s04a-49 mc-dw-sb-yelling-in-face_c2 with dissolve
    play voice3 dahlia_pain_ah3 noloop
    dw "You... what?"
    scene d15s04a-50 mc-dw-sb-yelling-in-face_c1 with dissolve
    play voice4 chloe_angry_argh1 noloop
    sb "I fucked your boyfriend. Then after prom I broke his clavicle and set fire to his prom date's car."
    scene d15s04a-50 mc-dw-sb-yelling-in-face_c2 with dissolve
    play voice3 dahlia_pain_argh noloop
    dw "I KNEW IT! {w}Wait... why?"
    $ Lovense.stop()
    queue music little_problem_nohorror
    scene d15s04a-51 mc-dw-sb-dahlia-desperate_c1 with dissolve
    play voice4 chloe_disappointed_ehh2 noloop
    sb "Because he fucked you over."
    scene d15s04a-51 mc-dw-sb-dahlia-desperate_c2 with dissolve
    play voice3 dahlia_old_upset noloop
    dw "Not because...?"
    scene d15s04a-52 mc-dw-sb-samiya-annoyed_c1 with dissolve
    play voice4 samiya_no1 noloop
    sb "No, I didn't want to date him. I didn't want to steal him from you. We just fucked that one time. That was it."
    scene d15s04a-52 mc-dw-sb-samiya-annoyed_c2 with dissolve
    play voice3 chloe_disappointed_off noloop
    dw "But he was always drooling over you. He even shouted out your name during sex!"
    scene d15s04a-51 mc-dw-sb-dahlia-desperate_c1 with dissolve
    play voice4 samiya_yes1 noloop
    sb "I can't help that. That was all him."
    scene d15s04a-51 mc-dw-sb-dahlia-desperate_c2 with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    dw "You didn't even want him?"
    scene d15s04a-52 mc-dw-sb-samiya-annoyed_c1 with dissolve
    play voice4 samiya_cugh noloop
    sb "Of course I wanted him, but he was yours. I would never steal from you."
    scene d15s04a-52 mc-dw-sb-samiya-annoyed_c1 with dissolve
    play voice3 dahlia_pain_sobs noloop
    dw "But you fucked him."
    play voice4 samiya_ah noloop
    sb "But I fucked him..."
    scene d15s04a-53 mc-dw-sb-fucked-mc_c1
    if cage_ntr is False:
        show d15s04a-53-over mc-dw-sb-fucked-mc-lc
    with dissolve
    play voice4 samiya_cagh noloop
    sb "And if we're being perfectly honest, I've fucked [mcname] too."
    scene d15s04a-54 mc-dw-sb-fucked-mc_c1
    if cage_ntr is False:
        show d15s04a-54-over mc-dw-sb-fucked-mc-lc
    with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "It was a bet."
    scene d15s04a-54 mc-dw-sb-fucked-mc_c2 with dissolve
    play voice3 chloe_angry_argh5 noloop
    dw "Shut up."
    scene d15s04a-55 mc-dw-sb-shut-up-mc_c1 with dissolve
    play voice4 samiya_yes3 noloop
    sb "Yes, shut up."
    scene d15s04a-56 mc-dw-sb-nervous_c1 with dissolve
    play voice3 dahlia_disappointed_ehh1 noloop
    dw "So, you really are-?"
    scene d15s04a-56 mc-dw-sb-nervous_c2 with dissolve
    play voice4 samiya_mfff noloop
    sb "A slut. A whore. A prostitute. Three-holed fuckmeat..."
    scene d15s04a-58 mc-dw-sb-smiles_c1 with dissolve
    play voice3 dahlia_sex_closedmoan1 noloop
    dw "-a sex addict?"
    scene d15s04a-58 mc-dw-sb-smiles_c2 with dissolve
    play voice4 samiya_laughing1 noloop
    sb "Probably. {w}I mean... yeah."
    scene d15s04a-57 mc-dw-sb-dahlia-laughing_c1 with dissolve
    play voice3 dahlia_happy_laugh6 noloop
    dw "*laughs*"
    scene d15s04a-54 mc-dw-sb-fucked-mc_c1
    if cage_ntr is False:
        show d15s04a-54-over mc-dw-sb-fucked-mc-lc
    with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "What's so funny?"
    scene d15s04a-57 mc-dw-sb-dahlia-laughing_c2 with dissolve
    play voice4 samiya_geh noloop
    sb "Shut it, [mcname]. {w}What is so funny?"
    scene d15s04a-58 mc-dw-sb-smiles_c1 with dissolve
    play voice3 dahlia_happy_relief noloop
    dw "This really did turn into an intervention."
    scene d15s04a-58 mc-dw-sb-smiles_c2 with dissolve
    play voice4 dahlia_happy_yay noloop
    sb "I guess so."
    scene d15s04a-58 mc-dw-sb-smiles_c3 with dissolve
    menu:
        "Take credit for reuniting them"(hint="d15s04dwm02c01") if True:

            scene d15s04a-59 mc-dw-sb-taking-credit-mc-smug_c1 with dissolve
            play voice2 mc_happy_wooh3 noloop
            mc "My clever plan worked out after all."
            scene d15s04a-59 mc-dw-sb-taking-credit-mc-smug_c3 with dissolve
            play voice3 chloe_angry_argh2 noloop
            dw "Which part of \"shut up\" did you not understand?"
            scene d15s04a-60 mc-dw-sb-taking-credit-samiya-leaving_c1 with dissolve
            play voice4 samiya_hm1 noloop
            sb "Look, I'm gonna get out of here."
            scene d15s04a-60 mc-dw-sb-taking-credit-samiya-leaving_c3 with dissolve
            play voice3 chloe_arrogant_yeah2 noloop
            dw "Go ahead. I'll take care of this imbecile."
            scene d15s04a-61 mc-dw-sb-taking-credit-mc-terrified_c1 with dissolve
            play voice2 mc_pain_auh6 noloop
            mct "Mommy? {w}Help!"
            $ renpy.end_replay()
            $ Lovense.vibrate(15)
            scene black with fade
            pause
            play voice2 mc_pain_ffff noloop
            scene d15s04a-73 mc-getting-points_c1 with fade

            $ Lovense.stop()
            pause
            play sound buzz
            call add_points (d15s04dw_points) from _call_add_points_5
            flr "You earned [d15s04dw_points] points."
            scene d15s04a-73 mc-getting-points_c2 with dissolve
            pause
            stop music fadeout 3.5

            jump d15s05
        "Let the girls think it was entirely up to them"(hint="d15s04dwm02c02") if True:


            $ d15s04_resolve_part2 = True

            if d15s03_quartet is True:
                $ d15s04_quartet_prep = True

            scene d15s04a-62 mc-dw-sb-right-choice_c3 with dissolve
            mc "..."

    scene d15s04a-63 mc-dw-sb-asking-for-hug_c1 with dissolve
    play voice3 chloe_disappointed_oh noloop
    dw "Can I-?"
    scene d15s04a-63 mc-dw-sb-asking-for-hug_c2 with dissolve
    play voice4 samiya_yes1 noloop
    sb "Always."
    play voice3 min_pain_sobs1 noloop
    scene d15s04a-64 mc-dw-sb-hug_c2 with dissolve
    pause
    scene d15s04a-65 mc-dw-sb-hug-talk_c1 with dissolve
    queue voice3 min_pain_sobs2 noloop
    dw "I hated you for years."
    scene d15s04a-65 mc-dw-sb-hug-talk_c2 with dissolve
    play voice4 samiya_ou1 noloop
    sb "I know."
    scene d15s04a-65 mc-dw-sb-hug-talk_c1 with dissolve
    play voice3 min_pain_ah noloop
    dw "Did you hate me?"
    scene d15s04a-65 mc-dw-sb-hug-talk_c2 with dissolve
    play voice4 samiya_no1 noloop
    sb "Never."
    scene d15s04a-66 mc-dw-sb-hug-talk_c1 with dissolve
    play voice3 min_pain_sobs1 noloop
    dw "Do you think... maybe... {w}Could we be friends again?"
    scene d15s04a-66 mc-dw-sb-hug-talk_c2 with dissolve
    play voice4 min_yes_simple noloop
    sb "I am now, and always have been, your friend."
    play voice3 dahlia_happy_laugh2 noloop
    dw "*giggles*"
    scene d15s04a-67 mc-dw-sb-talk_c2 with dissolve
    play voice4 samiya_huh noloop
    sb "So, what do we do with [mcname]?"
    scene d15s04a-67 mc-dw-sb-talk_c1 with dissolve
    play voice3 dahlia_sex_closedmoan4 noloop
    dw "I was thinking about riding his face until one of us passes out."
    scene d15s04a-68 mc-dw-sb-talk-mc-hopeful_c3 with dissolve
    play voice4 samiya_yes2 noloop
    sb "He kinda deserves that."
    scene d15s04a-68 mc-dw-sb-talk-mc-hopeful_c2 with dissolve
    play voice3 dahlia_thinking_oh noloop
    dw "On the other hand, maybe we should thank him for letting us get all this out there."
    scene d15s04a-68 mc-dw-sb-talk-mc-hopeful_c3 with dissolve
    play voice4 samiya_hm2 noloop
    sb "Let's not go crazy."
    scene d15s04a-68 mc-dw-sb-talk-mc-hopeful_c2 with dissolve
    play voice3 dahlia_yes_angry noloop
    dw "Good point."
    scene d15s04a-68 mc-dw-sb-talk-mc-hopeful_c1 with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "Have you considered a threesome?"
    scene d15s04a-68 mc-dw-sb-talk-mc-hopeful_c2 with dissolve
    play voice3 dahlia_happy_laugh4 noloop
    dw "Do you still carry toys around with you wherever you go?"
    scene d15s04a-68 mc-dw-sb-talk-mc-hopeful_c3 with dissolve
    play voice4 dahlia_yes_yeah3 noloop
    sb "Of course. What are you thinking?"
    scene d15s04a-68 mc-dw-sb-talk-mc-hopeful_c2 with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    dw "I'm thinking about two strap-ons, and we take turns."
    scene d15s04a-69 mc-dw-sb-talk-mc-regret_c1 with dissolve
    play voice2 mc_pain_mff3 noloop
    mct "I don't like this idea."
    scene d15s04a-69 mc-dw-sb-talk-mc-regret_c3 with dissolve
    play voice4 samiya_huh3 noloop
    sb "So, one of us fucks his mouth while the other fucks his ass, and then we switch?"
    scene d15s04a-69 mc-dw-sb-talk-mc-regret_c2 with dissolve
    play voice3 dahlia_surprised_ohmy noloop
    dw "Oh, that's even better than what I was thinking."
    scene d15s04a-70 mc-dw-sb-tired_c1 with dissolve
    play voice2 mc_pain_ffff noloop
    mct "I don't like this idea at all!"
    scene d15s04a-70 mc-dw-sb-tired_c3 with dissolve
    play voice4 samiya_mmm3 noloop
    sb "I don't know about you, but I'm kinda exhausted."
    scene d15s04a-70 mc-dw-sb-tired_c2 with dissolve
    play voice3 dahlia_old_argh2 noloop
    dw "Honestly? Same."
    scene d15s04a-70 mc-dw-sb-tired_c3 with dissolve
    play voice4 samiya_hm1 noloop
    sb "Why don't we go get some coffee or something."
    scene d15s04a-68 mc-dw-sb-talk-mc-hopeful_c2 with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    dw "Like.. friends?"
    scene d15s04a-70 mc-dw-sb-tired_c3 with dissolve
    play voice4 samiya_yes3 noloop
    sb "Sure. We can catch up on old times."

    $ fl_achievement_unlock("d15s04n01")
    $ unlock_gallery_slot("extra", "d15s04n01")

    scene d15s04a-71 mc-dw-sb-leaving_c1
    if cage_ntr is False:
        show d15s04a-71-over mc-dw-sb-leaving-lc
    with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Little help?"
    mc "No?"
    $ Lovense.vibrate(15)
    scene d15s04a-72 mc-diggin_c1 with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "Okay. I guess I'll do it myself."
    $ renpy.end_replay()
    $ unlock_gallery_slot("cg", "d15s04dw")
    $ unlock_gallery_slot("scene", "d15s04dw")
    play voice2 mc_pain_auh5 noloop
    scene d15s04a-73 mc-getting-points_c1 with Fade(0.5,1.0,0.5)

    $ Lovense.stop()
    pause
    play sound buzz
    call add_points (d15s04dw_points) from _call_add_points_6
    flr "You earned [d15s04dw_points] points."
    scene d15s04a-73 mc-getting-points_c2 with dissolve
    pause

    jump d15s05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
