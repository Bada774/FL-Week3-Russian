default persistent.d17s05_mh = False
default persistent.d17s05_mh_sy = False
default persistent.d17s05_mh_op = False

label d17s05:

    $ d17s05_mh_op = False
    $ d17s05_love_mh_op = False

    $ d17s05_mh_sy = False
    $ d17s05_love_mh_sy = False

    $ d17s05_mh = False
    $ d17s05_mh_bj = False
    $ d17s05_mh_jerk = False
    $ d17s05_mh_edge = False
    $ d17s05_mh_cum_ass = False
    $ d17s05_love_mh = False
    $ d17s05_mh_points = 0

    if date_mh is False:
        jump d17s06

    scene black
    show screen scene_transistion(_("1 hour later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene d17s05-04-mc-walking
    with Fade(0.5, 0.5, 0.9)
    call buzz from _call_buzz_31
    scene d17s05-05-mc-pick-up-phone with dissolve
    play voice2 d1s2_mchey noloop
    mct "Lyssa?"
    scene d17s05-01-lh-on-phone with dissolve
    $ renpy.music.set_volume(0.7, 3.0, "music")
    play music "<silence 0.6>" noloop
    queue music bass_sexy2
    play voice3 daisy_hey noloop
    mh "{i}Hey{/i}, Casanova."
    scene d17s05-06-mc-against-wall-talk-smirk-c2 with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "Mm, that voice is honey to my ears."
    scene d17s05-02-lh-on-phone-close-up with dissolve
    play voice3 lissa_moan1 noloop
    mh "Are you free?"
    scene d17s05-08-mc-against-wall-talk with dissolve
    play voice2 d9s2_mcyes noloop volume 1.8
    mc "For you? Always."
    scene d17s05-15-lh-on-phone-close-up-talk-c2 with dissolve
    play voice3 lissa_moan2 noloop
    mh "Good. I'm home today. I was wondering if you wanted to come over?"
    scene d17s05-06-mc-against-wall-talk-smirk-c2 with dissolve
    play voice2 d1s2_hmm noloop volume 1.5
    mc "Come over? Hmm, but what oh what could we {i}possibly{/i} do together?"
    scene d17s05-03-lh-on-phone-alt-angle with dissolve
    play voice3 lissa_laugh2 noloop
    mh "We never had problems figuring out what to do before, I'm sure we won't have problems now."
    mh "Plus, I have plenty of {i}board games{/i} that we could play if we really don't find anything to do."
    scene d17s05-08-mc-against-wall-talk with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Board games, huh?"
    mc "I think I like the sound of that."
    scene d17s05-14-lh-on-phone-talk-c5 with dissolve
    play voice3 lissa_aga noloop
    mh "Maybe you can bring someone else over as well. It's more the merrier when it comes to {i}board games{/i}, right? I wouldn't mind."
    play sound maria_kiss2
    scene d17s05-16-lh-on-phone-blow-kiss-c1 with dissolve
    pause
    scene d17s05-07-mc-against-wall-listen with dissolve
    play voice2 mc_thinking_mmm4 noloop


    menu:
        mct "Whom should I invite?"
        "Bring Oliver"(hint="d17s05m01c01") if date_op is True:

            $ d17s05_mh_op = True

            scene d17s05-08-mc-against-wall-talk with dissolve
            play voice2 mc_happy_a1 noloop
            mc "What about Oliver?"
            play voice3 lissa_oh2 noloop
            scene d17s05-02-lh-on-phone-close-up with dissolve
            mh "Oliver? He's growing on you, isn't he?"
            scene d17s05-10-mc-talk-c2 with dissolve
            play voice2 mc_thinking_emm1 noloop
            mc "Well, what can I say. He's cute."
            scene d17s05-01-lh-on-phone with dissolve
            play voice3 lissa_ugu2 noloop
            mh "That he is. And competitive too."
            scene d17s05-06-mc-against-wall-talk-smirk-c2 with dissolve
            play voice2 mc_thinking_oh1 noloop
            mc "Seriously?"
            scene d17s05-14-lh-on-phone-talk-c5 with dissolve
            play voice3 lissa_ugu noloop
            mh "Mm-hm."
            mh "I think Oliver would be lovely."

        "Bring Stacy"(hint="d17s05m01c02") if date_sy is True:

            $ d17s05_mh_sy = True

            scene d17s05-08-mc-against-wall-talk with dissolve
            play voice2 d1s5_mchappy noloop volume 1.5
            mc "How about Stacy?"
            play voice3 lissa_oh noloop
            scene d17s05-02-lh-on-phone-close-up with dissolve
            mh "Stacy?{w} Sure. I've been meaning to talk to her a bit more."
            mh "I think Stacy would be lovely."
        "Bring no one"(hint="d17s05m01c03"):


            $ d17s05_mh = True

            scene d17s05-08-mc-against-wall-talk with dissolve
            play voice2 mc_happy_hah2 noloop
            mc "I could, but I'd rather have you for myself."
            scene d17s05-02-lh-on-phone-close-up with dissolve
            play voice3 lissa_mmm1 noloop
            mh "Mmm, I'd like that very much as well."

    scene d17s05-10-mc-talk-c2 with dissolve
    if d17s05_mh_sy or d17s05_mh_op is True:
        play voice2 mc_yes_okay3 noloop
        mc "I'll be right over with our guests then."
    elif True:
        play voice2 mc_yes_yeah1 noloop
        mc "I'll be right over then."
        mc "Why don't you prepare yourself for me in the meantime?"
    scene d17s05-11-mc-listen-c2 with dissolve
    play voice3 lissa_phonetalk_yes noloop
    if date_mh_bdsm is True:
        mh "Yes, Sir."
    elif True:
        mh "I'll be waiting."

    if d17s05_mh_op is True:

        scene d17s05-09-mc-call-oliver-or-stacy with dissolve
        play voice2 mc_arrogant_hm1 noloop
        mct "Lets call Oliver."
        scene d17s05-11-mc-listen-c2 with dissolve
        play voice3 oliver_phonetalk_hello noloop
        op "Hello?"
        scene d17s05-10-mc-talk-c2 with dissolve
        play voice2 mc_hey_hey5 noloop
        mc "Oliver? Sorry for the call out of nowhere."
        scene d17s05-11-mc-listen-c2 with dissolve
        play voice3 oliver_phonetalk_oh noloop
        op "Oh, it's fine. What's up?"
        scene d17s05-10-mc-talk-c2 with dissolve
        play voice2 mc_thinking_mmm5 noloop
        mc "Lyssa invited me to come over to her place. Play some games, vibe, just shoot the shit."
        scene d17s05-07-mc-against-wall-listen with dissolve
        play voice3 oliver_phonetalk_mmm noloop
        op "That sounds nice."
        scene d17s05-08-mc-against-wall-talk with dissolve
        play voice2 mc_yes_yeah4 noloop
        mc "Yeah. I was wondering if you'd wanna tag along?"
        scene d17s05-07-mc-against-wall-listen with dissolve
        play voice3 oliver_phonetalk_eh noloop
        op "M—me? Why me?"
        scene d17s05-10-mc-talk-c2 with dissolve
        play voice2 d2s9_confused noloop volume 1.3
        mc "Well, Lyssa said she'd be fine with someone else tagging along, so I thought why not you?"
        mc "You don't have to come if you don't want to. I just thought it'd be a nice opportunity for all of us to get to know each other."
        scene d17s05-11-mc-listen-c2 with dissolve
        play voice3 oliver_phonetalk_huh noloop
        op "...This is all a bit sudden, but I suppose it's fine."
        scene d17s05-10-mc-talk-c2 with dissolve
        play voice2 mc_arrogant_heh3 noloop
        mc "Does that mean you're in?"
        scene d17s05-11-mc-listen-c2 with dissolve
        play voice3 oliver_phonetalk_yes noloop
        op "...Yes."
        scene d17s05-10-mc-talk-c2 with dissolve
        play voice2 mc_happy_yay2 noloop
        mc "Cool. I'll see you there then."
        scene d17s05-12-mc-hang-up-leave-c1 with dissolve
        pause
        scene d17s05-13-mc-walk-away-c1 with dissolve
        pause

        stop music fadeout 3.5
        jump d17s05mo

    elif d17s05_mh_sy is True:

        scene d17s05-09-mc-call-oliver-or-stacy with dissolve
        play voice2 mc_arrogant_hm1 noloop
        mct "Lets call Stacy."
        scene d17s05-11-mc-listen-c2 with dissolve
        play voice3 stacy_phonetalk_huh noloop
        sy "Who's dead?"
        scene d17s05-10-mc-talk-c2 with dissolve
        play voice2 mc_surprised_what1 noloop
        mc "Wha—? Huh?"
        scene d17s05-11-mc-listen-c2 with dissolve
        play voice3 stacy_phonetalk_hm noloop
        sy "You called, so something big must've happened."
        scene d17s05-10-mc-talk-c2 with dissolve
        play voice2 mc_thinking_emm1 noloop
        mc "And your first thought was to jump to {i}death{/i}?"
        scene d17s05-07-mc-against-wall-listen with dissolve
        play voice3 stacy_phonetalk_hmm noloop
        sy "I dunno man. It's your fault for calling when you could've just as easily sent a text."
        scene d17s05-08-mc-against-wall-talk with dissolve
        play voice2 d1s5b_ehhh noloop volume 1.3
        mc "I— You know what? I refuse to engage with your inane dumbassery right now."
        mc "Do you wanna go over to Lyssa's—?"
        scene d17s05-07-mc-against-wall-listen with dissolve
        play voice3 stacy_phonetalk_yes noloop
        sy "Yes!"
        scene d17s05-10-mc-talk-c2 with dissolve
        play voice2 mc_happy_yay2 noloop
        mc "I didn't even explain what we're doing."
        scene d17s05-11-mc-listen-c2 with dissolve
        play voice3 stacy_phonetalk_laugh noloop
        sy "I don't care. The answer is yes."
        scene d17s05-10-mc-talk-c2 with dissolve
        play voice2 mc_happy_a1 noloop
        mc "Alright then. Get ready, I'll pick you up—"
        scene d17s05-09-mc-call-oliver-or-stacy with dissolve
        play voice2 mc_angry_hm1 noloop
        mct "She dropped the call before I could even finish my damn sentence."
        scene d17s05-12-mc-hang-up-leave-c1 with dissolve
        pause
        scene d17s05-13-mc-walk-away-c1 with dissolve
        pause

        stop music fadeout 3.5
        jump d17s05ms
    elif True:

        scene d17s05-12-mc-hang-up-leave-c1 with dissolve
        pause
        scene d17s05-13-mc-walk-away-c1 with dissolve
        pause

        stop music fadeout 3.5
        jump d17s05mh

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
