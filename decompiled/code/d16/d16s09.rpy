label d16s09:

    $ d16s09_ending = False

    if date_nk_preg is False:
        jump d16s10

    scene black
    show screen scene_transistion(_("20 minutes later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    play music caffee_theme_2_slowed fadein 1.5
    hide screen scene_transistion
    scene d16s09-000-2
    with Fade(0.5, 0.5, 0.9)
    pause
    $ unlock_ending("13")
    call update_ending_variables from _call_update_ending_variables_9
    menu:
        "Runaway with Nora"(hint="d16s09m01c01"):
            $ d16s09_ending = True
            jump d16s09_nk_end
        "Go to AmRose's House"(hint="d16s09m01c02"):

            stop music fadeout 3.0
            jump d16s10

label d16s09_nk_end hide:

    if from_ending_menu is True:
        play music caffee_theme_2_slowed fadein 1.5
    play sound sfx_door_closed8 volume 1.5
    scene d16s09-001-2 with dissolve
    play voice2 d2s9_mchey noloop
    mc "You ready?"
    scene d16s09-002 with dissolve
    play voice3 nora_aga noloop
    nk "Yeah, are you?"
    scene d16s09-001-2 with dissolve
    if cockcage_released is True:
        play voice2 mc_yes_yeah2 noloop
        mc "Yep"
    elif True:
        play voice2 mc_thinking_mmm3 noloop
        mc "I need your help with something."
        scene d16s09-003 with dissolve
        play voice3 nora_hmm noloop
        nk "What's that?"
        play sound sfx_jeans_on1
        scene d16s09-004
        if cage_ntr is False:
            show d16s09-004_005
        with dissolve
        play voice2 d1s5b_ehhh volume 1.4 noloop
        mc "Any thoughts on how to get this off?"
        play voice3 nora_heh noloop
        nk "Sledgehammer? Bolt cutters?"
        scene d16s09-005-1
        if cage_ntr is False:
            show d16s09-004_005
        with dissolve
        play voice2 mc_thinking_emm1 noloop
        mc "Preferably without crushing my cock."
        scene d16s09-006
        if cage_ntr is False:
            show d16s09-006-1
        with dissolve
        play voice3 nora_pleasure noloop
        nk "I've got an idea..."
        play voice2 mc_yes_yeah8 noloop
        mc "Yeah?"
        play sound2 sfx_sextoy_uncuff1 noloop
        play sound ["<silence 0.2>", sfx_cockcage_destroy] volume 0.9
        scene d16s09-007-2
        if cage_ntr is False:
            show d16s09-007_008
        with dissolve
        play voice3 nora_nhey noloop
        nk "There you go!"
        scene d16s09-008
        if cage_ntr is False:
            show d16s09-007_008
        with dissolve
        play voice2 mc_scared_huuuh1 noloop
        mc "How did you-?"
        play voice3 aaleyah_happy_laugh1 noloop
        nk "Please. Do you know how complicated espresso machines are?{w} That was easy by comparison."
        nk "At least it didn't start frothing and steaming unexpectedly."
    play sound sfx_paper_rustl1
    scene d16s09-009 with Fade(0.5, 0.5, 0.5)
    play voice3 nora_angrymoan noloop
    nk "That's it. All signed and dated."
    nk "Crossed every I; Dotted every T."
    scene d16s09-010 with dissolve
    play voice2 d1s5_mcthinks volume 1.5 noloop
    mc "And there's my contribution. Let's get out of here."
    play voice3 nora_hey noloop
    nk "What about your friends and fuckbuddies?"
    mc "What about Polly - your blind date?"
    scene d16s09-011 with dissolve
    play voice3 nora_huuuh noloop
    nk "We're really going to just leave it all behind us?"
    play voice2 mc_yes_yeah1 noloop
    mc "I'm willing if you are."
    play voice3 nora_oh noloop
    nk "And monogamy? Do you think it will suit you?"
    scene d16s09-013 with dissolve
    play voice2 d4s4_mclaugh volume 1.3 noloop
    mc "I can't wait to find out.{w}.. together."
    play voice3 nora_mmm noloop
    nk "Well, then there's just one thing left to do."
    scene d16s09-012 with dissolve
    play voice2 d1s2_hmm volume 1.5 noloop
    mc "What's that?"
    nk "Kiss me."
    play voice3 nora_huh noloop
    scene d16s09-014-1 with dissolve
    play sound maria_kiss1
    pause
    play voice2 d1s1_mmm noloop
    scene d16s09-015 with dissolve
    play voice3 aaleyah_closed_moan1 noloop
    play sound maria_kiss2
    pause
    play sound maria_kiss3
    scene d16s09-016 with dissolve
    pause
    scene d16s09-018 with dissolve
    play voice3 nora_orgasm3 noloop
    nk "More..."
    scene d16s09-017 with dissolve
    play voice2 mc_angry_huh2 noloop
    mc "Soon enough.{w} Let's get out of here."
    play voice3 nora_yes noloop
    nk "Yes, sir."
    play sound sfx_door_open3 volume 1.4
    scene d16s09-019-1 with dissolve
    play voice3 aaleyah_happy_mmm1 noloop
    pause
    stop music fadeout 3.0

    jump ending_13

label ending_13_return:

    jump d16s10

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
