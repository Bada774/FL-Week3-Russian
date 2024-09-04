image d15s05-a1 = Movie(play = "images/Day-15/Scene-05/anim/d15s05-a1-4x-60fps.webm", start_image = "d15s05-00-a1 mk-bj-anim-1-01_i")
image d15s05-a1-f = Movie(play = "images/Day-15/Scene-05/anim/d15s05-a1-2x-50fps.webm", start_image = "d15s05-00-a1 mk-bj-anim-1-01_i")
image d15s05-a2 = Movie(play = "images/Day-15/Scene-05/anim/d15s05-a2-4x-60fps.webm", start_image = "d15s05-00-a2 mk-bj-anim-2-01_i")
image d15s05-a2-f = Movie(play = "images/Day-15/Scene-05/anim/d15s05-a2-2x-50fps.webm", start_image = "d15s05-00-a2 mk-bj-anim-2-01_i")
image d15s05-a3 = Movie(play = "images/Day-15/Scene-05/anim/d15s05-a3-4x-60fps.webm", start_image = "d15s05-00-a3 mk-bj-anim-3-01_i")
image d15s05-a3-f = Movie(play = "images/Day-15/Scene-05/anim/d15s05-a3-2x-50fps.webm", start_image = "d15s05-00-a3 mk-bj-anim-3-01_i")
image d15s05-a4 = Movie(play = "images/Day-15/Scene-05/anim/d15s05-a4-4x-60fps.webm", start_image = "d15s05-00-a4 mk-fuck-anim-4-01_i")
image d15s05-a4-f = Movie(play = "images/Day-15/Scene-05/anim/d15s05-a4-2x-50fps.webm", start_image = "d15s05-00-a4 mk-fuck-anim-4-01_i")
image d15s05-a5 = Movie(play = "images/Day-15/Scene-05/anim/d15s05-a5-4x-60fps.webm", start_image = "d15s05-00-a5 mk-fuck-anim-5-01_i")
image d15s05-a5-f = Movie(play = "images/Day-15/Scene-05/anim/d15s05-a5-2x-50fps.webm", start_image = "d15s05-00-a5 mk-fuck-anim-5-01_i")
image d15s05-a6 = Movie(play = "images/Day-15/Scene-05/anim/d15s05-a6-4x-60fps.webm", start_image = "d15s05-00-a6 mk-fuck-anim-6-01_i")
image d15s05-a6-f = Movie(play = "images/Day-15/Scene-05/anim/d15s05-a6-2x-50fps.webm", start_image = "d15s05-00-a6 mk-fuck-anim-6-01_i")
image d15s05-a7 = Movie(play = "images/Day-15/Scene-05/anim/d15s05-a7-4x-60fps.webm", start_image = "d15s05-00-a7 mk-anal-anim-7-01_i")
image d15s05-a7-f = Movie(play = "images/Day-15/Scene-05/anim/d15s05-a7-2x-50fps.webm", start_image = "d15s05-00-a7 mk-anal-anim-7-01_i")
image d15s05-a8 = Movie(play = "images/Day-15/Scene-05/anim/d15s05-a8-4x-60fps.webm", start_image = "d15s05-00-a8 mk-anal-anim-8-01_i")
image d15s05-a8-f = Movie(play = "images/Day-15/Scene-05/anim/d15s05-a8-2x-50fps.webm", start_image = "d15s05-00-a8 mk-anal-anim-8-01_i")
image d15s05-a9 = Movie(play = "images/Day-15/Scene-05/anim/d15s05-a9-4x-60fps.webm", start_image = "d15s05-00-a9 mk-anal-anim-9-01_i")
image d15s05-a9-f = Movie(play = "images/Day-15/Scene-05/anim/d15s05-a9-2x-50fps.webm", start_image = "d15s05-00-a9 mk-anal-anim-9-01_i")
image d15s05-pissing = Movie(play = "images/Day-15/Scene-05/anim/d15s05-a50-v1-2x-40fps.webm", start_image = "d15s05-50-a25 mc-mk-piss-anim-25-0001_i")

label replay_d15s05:
label d15s05:

    $ d15s05_leave = False
    $ d15s05_rescue = False
    $ d15s05_suck = False
    $ d15s05_vaginal = False
    $ d15s05_anal = False
    $ d15s05_rimjob = False
    $ d15s05_done = False
    $ d15s05_goldstar = False
    $ d15s05_sexacts = 0
    $ d15s05_points = 0

    stop music fadeout 3.5
    if d12s01_mk_pussy is True or d12s01_cum_pussy is True:
        $ d15s05_mk_virgin_pussy = False
    elif True:
        $ d15s05_mk_virgin_pussy = True

    if d12s01_mk_ass is True or d12s01_cum_ass is True:
        $ d15s05_mk_virgin_ass = False
    elif True:
        $ d15s05_mk_virgin_ass = True

    if date_mk_tr is False:
        if is_extended_edition is True:
            jump d15s05b_ext
        elif True:
            jump d15s06
    if not _in_replay:
        scene black
        show screen scene_transistion(_("30 minutes later"))
        with Fade(0.9, 0.5, 0.5)
        pause
        hide screen scene_transistion
        scene d15s05-01 mc-mk-toilet-entry1_c1
        with Fade(0.5, 0.5, 0.9)
        queue music felt_in_sex
        pause
    elif True:
        play music felt_in_sex
    scene d15s05-01 mc-mk-toilet-entry1_c2 with dissolve
    play voice3 min_arrogant_hm noloop
    mk "[mcname]. Good, you came."
    scene d15s05-02 mc-mk-toilet-entry2_c1 with dissolve
    play voice2 mc_angry_daugh1 noloop
    mc "Not fucking likely today."
    scene d15s05-02 mc-mk-toilet-entry2_c2 with dissolve
    play voice3 maria_what noloop
    mk "What are you talking about?"
    scene d15s05-03 mc-mk-toilet-entry3_c1 with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "Nothing. What am I doing here, Maria?"
    scene d15s05-03 mc-mk-toilet-entry3_c2 with dissolve
    play voice3 min_pain_ah noloop
    mk "Are you angry at me?"
    scene d15s05-04 mc-mk-toilet-entry4_c1 with dissolve
    play voice2 mc_no_no3 noloop
    mc "Sorry, I'm just pissed off in general today. You just happen to be in range."
    mc "Why did you call me here?"
    scene d15s05-04 mc-mk-toilet-entry4_c2 with dissolve
    play voice3 min_thinking_hmm3 noloop
    mk "Okay... {w}I wanted to show you something."
    scene d15s05-05 mc-mk-toilet-entry5_c1 with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "I think I've seen it."
    scene d15s05-05 mc-mk-toilet-entry5_c2 with dissolve
    play voice3 min_surprised_huh1 noloop
    mk "From this side?"
    scene d15s05-06 mc-mk-toilet-entry6_c1 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "In your photos."
    scene d15s05-06 mc-mk-toilet-entry6_c2 with dissolve
    play voice3 min_surprised_oh noloop
    mk "Well, I guess I want to show you something that maybe wasn't in the photos."
    scene d15s05-07 mc-mk-toilet-entry7_c1 with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What's that?"
    scene d15s05-07 mc-mk-toilet-entry7_c2 with dissolve
    play voice3 min_happy_relief noloop
    mk "My complete and utter debasement."
    scene d15s05-08 mc-mk-toilet-entry8_c1 with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "What the fuck are you talking about?"
    scene d15s05-08 mc-mk-toilet-entry8_c2 with dissolve
    play voice3 min_angry_breath noloop
    mk "I love it. {w}Do you fucking believe that? I come in here and get used. And I love it."
    mk "I'm not even a person to the guy on the other side of this wall. I'm just a hole."
    mk "I want you to see that. Not just a photograph. I want you to stand right here and see what you've made me."
    scene d15s05-09 mc-mk-toilet-entry9_c1 with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "Look, Maria, if you're pissed at me I understand-"
    scene d15s05-09 mc-mk-toilet-entry9_c2 with dissolve
    play voice3 maria_aah noloop
    mk "Pissed? {w}Do I sound upset to you?"
    scene d15s05-06 mc-mk-toilet-entry6_c1 with dissolve
    play voice2 mc_no_no2 noloop
    mc "Well, no."
    scene d15s05-06 mc-mk-toilet-entry6_c2 with dissolve
    play voice3 min_yes_simple noloop
    mk "I've finally found my purpose in life."
    scene d15s05-08 mc-mk-toilet-entry8_c1 with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "Sucking cocks in a gloryhole?"
    scene d15s05-07 mc-mk-toilet-entry7_c2 with dissolve
    play voice3 maria_argh noloop
    mk "It's so much more than that. {w}That's what I want to show you."
    menu:
        "Leave her alone to her fate"(hint="d15s05m01c01"):
            $ d15s05_leave = True
            jump d15s05_gtfo
        "She needs help. I'm getting her out of here"(hint="d15s05m01c02"):

            $ d15s05_rescue = True
            jump d15s05_help
        "Alright. I'm happy to watch this"(hint="d15s05m01c03"):

            $ d15s05_points = 12
            jump d15s05_sexmenu

label d15s05_gtfo:

    scene d15s05-09 mc-mk-toilet-entry9_c1 with dissolve
    play voice2 mc_no_no1 noloop
    mc "No. I'm out."
    scene d15s05-09 mc-mk-toilet-entry9_c2 with dissolve
    play voice3 maria_what noloop
    mk "But I need you to see this!"
    scene d15s05-10 mc-mk-toilet-entry10_c1 with dissolve
    play voice2 mc_disgust_booeah4 noloop
    mc "Don't you get it? You're disgusting."
    scene d15s05-10 mc-mk-toilet-entry10_c2 with dissolve
    play voice3 min_surprised_ehh1 noloop
    mk "You can keep all the money. They keep offering, but I've been giving it back."
    scene d15s05-10 mc-mk-toilet-entry10_c1 with dissolve
    play voice2 mc_angry_errr3 noloop
    mc "Let me make this perfectly clear - I don't want to ever see you again."
    scene d15s05-10 mc-mk-toilet-entry10_c3 with dissolve
    play voice3 min_scared_ah3 noloop
    mk "Fuck me! Use me!! Make me your whore!!!"
    play voice2 mc_no_no4 noloop
    mc "No."
    stop music fadeout 3.5
    $ renpy.end_replay()

    if is_extended_edition is True:
        jump d15s05b_ext
    elif True:
        jump d15s06

label d15s05_help:

    scene d15s05-11 mc-mk-toilet-help1_c1 with dissolve
    play voice2 mc_disgust_ooh1 noloop
    mc "What the hell is wrong with you?"
    scene d15s05-11 mc-mk-toilet-help1_c2 with dissolve
    play voice3 min_pain_ah noloop
    mk "I need you to see this! I need you!"
    scene d15s05-12 mc-mk-toilet-help2_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "What would AmRose say if she saw you like this?"
    scene d15s05-12 mc-mk-toilet-help2_c2 with dissolve
    play voice3 min_surprised_ehh1 noloop
    mk "Anything she wants. Anything you want."
    mk "Fuck me! Use me!! Make me your whore!!!"
    scene d15s05-11 mc-mk-toilet-help1_c1 with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "Put your clothes on."
    scene d15s05-11 mc-mk-toilet-help1_c2 with dissolve
    play voice3 min_no_happy noloop
    mk " No..."
    scene d15s05-14 mc-mk-toilet-help4_c1 with dissolve
    play voice2 mc_disappointed_off1 noloop
    mct "*sigh* How do you solve a problem like Maria?"
    mc "You want to please me, right? You want to do what I would want - what AmRose would want you to do?"
    scene d15s05-13 mc-mk-toilet-help3_c2 with dissolve
    play voice3 min_yes_simple noloop
    mk "Yes! Anything!!"
    scene d15s05-13 mc-mk-toilet-help3_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "No matter what it is?"
    scene d15s05-14 mc-mk-toilet-help4_c2 with dissolve
    play voice3 maria_yes noloop
    mk "YES!!! No matter how depraved or-"
    scene d15s05-15 mc-mk-toilet-help5_c1 with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "Then put your fucking clothes on. We're getting you out of here."
    scene d15s05-15 mc-mk-toilet-help5_c2 with dissolve
    play voice3 maria_what noloop
    mk "What?{w} I don't understand."
    scene d15s05-15 mc-mk-toilet-help5_c1 with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "Be a good slave. Don't think - just do what you're told."
    scene d15s05-15 mc-mk-toilet-help5_c2 with dissolve
    play voice3 min_disappointed_off noloop
    mk "Yes... sir."
    mct "I need to take her somewhere she can get help."
    mk "Sir, Master, [mcname]?"
    play sound sfx_cloth_rustling2
    scene d15s05-16 mc-mk-toilet-help6_c1 with dissolve
    play voice2 mc_disgust_meh4 noloop
    mc "Are you ready to go?"
    scene d15s05-17 mc-mk-toilet-help7_c1 with dissolve
    play voice3 min_happy_mmm noloop
    mk "But there's a cock waiting."
    scene d15s05-16 mc-mk-toilet-help6_c1 with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "Let it wait. I don't want you ever coming back here again, understood?"
    mct "She needs some tough love."
    mc "Don't forget who owns you, bitch. AmRose & I don't want some fucked up cock slut."
    scene d15s05-17 mc-mk-toilet-help7_c1 with dissolve
    play voice2 mc_angry_errr2 noloop
    mc "You don't whore yourself out unless we tell you to do it. Understood?"
    scene d15s05-17 mc-mk-toilet-help7_c2 with dissolve
    play voice3 min_yes_simple noloop
    mk "Yes, sir. I'm so sorry, sir."
    scene d15s05-18 mc-mk-toilet-help8_c1 with dissolve
    play voice2 mc_happy_thatsgood noloop
    mc "That's better. Now let's go."
    scene d15s05-18 mc-mk-toilet-help8_c2 with dissolve
    play voice3 min_disappointed_ehh2 noloop
    mk "Of course, master."
    mct "Let's start at the nurse's office. She clearly needs some serious psychological help."
    stop music fadeout 3.5
    $ renpy.end_replay()

    if is_extended_edition is True:
        jump d15s05b_ext
    elif True:
        jump d15s06

label d15s05_sexmenu:

    $ Lovense.stop()

    scene d15s05-08 mc-mk-toilet-entry8_c2 with dissolve
    play voice3 min_thinking_oh noloop
    mk "Oh, there's another cock coming through the hole."
    mk "What would you like me to do?"

    menu:
        "Order Maria to:"
        "Suck That Cock"(hint="d15s05m02c01") if d15s05_suck is False:
            $ d15s05_suck = True
            $ d15s05_sexacts += 1

            jump d15s05_bj

        "Fuck That Cock (Pussy)"(hint="d15s05m02c02") if d15s05_vaginal is False:
            $ d15s05_sexacts += 1
            $ d15s05_vaginal = True

            jump d15s05_pussyfuck

        "Fuck That Cock (Anal)"(hint="d15s05m02c03") if d15s05_anal is False:
            $ d15s05_sexacts += 1
            $ d15s05_anal = True

            jump d15s05_assfuck

        "Rim My Ass While Getting Fucked"(hint="d15s05m02c04") if d15s05_rimjob is False:
            $ d15s05_sexacts += 1
            $ d15s05_rimjob = True

            jump d15s05_rimmed

        "Wrap this Up"(hint="d15s05m02c05") if d15s05_sexacts >= 4:
            $ d15s05_done = True

            jump d15s05_end

label d15s05_bj:

    scene d15s05-08 mc-mk-toilet-entry8_c1 with dissolve
    $ Lovense.vibrate(1)
    play voice2 mc_thinking_mmm2 noloop
    mc "Well, you know what to do."
    scene d15s05-21 mc-mk-toilet-blowjob-talk1_c2 with dissolve
    play voice3 min_yes_simple noloop
    mk "I'm sure he doesn't want just a handjob."
    scene d15s05-21 mc-mk-toilet-blowjob-talk1_c1 with dissolve
    play voice2 mc_angry_errr4 noloop
    mc "Suck that dick, slut."
    scene d15s05-21 mc-mk-toilet-blowjob-talk1_c3 with dissolve
    play voice3 maria_yes noloop
    mk "Yes, sir!"
    scene d15s05-20 mc-mk-toilet-blowjob1_c3 with dissolve
    pause
    play voice3 daisy_dlick noloop
    scene d15s05-20 mc-mk-toilet-blowjob1_c1 with dissolve
    pause
    $ Lovense.vibrate(3)
    play voice3 dahlia_sex_closedmoan2 noloop
    scene d15s05-00-a1 mk-bj-anim-1-01_i with dissolve
    pause
    play voice3 aaleyah_sucking_deep
    $ Lovense.vibrate(4)
    scene d15s05-a1
    pause
    play voice2 mc_arrogant_hm1 noloop
    mc "You look like you've done that before."
    scene d15s05-a2 with dissolve
    pause
    scene d15s05-a3 with dissolve
    mct "It's a shame I can't take advantage of her new skills."
    pause
    play voice3 maria_fsucking
    play voice4 aaleyah_sucking_soft
    scene d15s05-a1-f with dissolve
    pause
    scene d15s05-a2-f with dissolve
    mct "Stupid cock cage. {w}I really want to shove my dick inside her."
    pause
    scene d15s05-a3-f with dissolve
    pause
    stop voice4 fadeout 0.5
    play voice3 dahlia_sex_closedmoan1 noloop
    $ Lovense.vibrate(7)
    scene d15s05-00-a1 mk-bj-anim-1-01_i with hpunch
    pause
    play sound gulp
    with hpunch
    mct "Fuck me. She's really swallowing it all."
    play voice3 [polly_breathing, polly_breathing] noloop
    $ Lovense.vibrate(2)
    scene d15s05-60 mc-mk-toilet-bj-cum_c1 with dissolve
    pause
    scene d15s05-60 mc-mk-toilet-bj-cum_c2 with dissolve
    pause
    scene d15s05-60 mc-mk-toilet-bj-cum_c3 with dissolve
    pause
    scene d15s05-22 mc-mk-toilet-blowjob-talk2_c1 with dissolve
    play voice2 mc_surprised_wow2 noloop
    mc "I doubt I'll ever get tired of watching that."
    scene d15s05-22 mc-mk-toilet-blowjob-talk2_c2 with dissolve
    play voice3 min_happy_relief noloop
    mk "I'm so glad you really see me for what I am, sir."
    play voice2 mc_thinking_oh1 noloop
    mc "And what are you?"
    scene d15s05-22 mc-mk-toilet-blowjob-talk2_c3 with dissolve
    play voice3 min_angry_breath noloop
    mk "A three-holed cum slut available to all cummers."
    scene d15s05-23 mc-mk-toilet-blowjob-talk3_c1 with dissolve
    play voice2 mc_pain_mff1 noloop
    mct "Damn. This cage hurts so much when she says that."
    scene d15s05-23 mc-mk-toilet-blowjob-talk3_c2 with dissolve
    play voice3 min_disappointed_ehh1 noloop
    mk "I've been sucking cocks all morning."
    play voice2 mc_scared_oh3 noloop
    mc "How much money did you make?"
    scene d15s05-23 mc-mk-toilet-blowjob-talk3_c3 with dissolve
    play voice3 maria_meeh noloop
    mk "Sometimes they give me money. I hand it back after they cum."
    scene d15s05-24 mc-mk-toilet-blowjob-talk4_c1 with dissolve
    play voice2 mc_surprised_what3 noloop
    mc "You're supposed to keep the money."
    scene d15s05-24 mc-mk-toilet-blowjob-talk4_c3 with dissolve
    play voice3 maria_aah noloop
    mk "Why? I should be paying them for this."
    scene d15s05-24 mc-mk-toilet-blowjob-talk4_c2 with dissolve
    play voice2 mc_disgust_pfe1 noloop
    mct "What a stupid whore."

    jump d15s05_sexmenu

label d15s05_pussyfuck:

    scene d15s05-25 mc-mk-toilet-pussy1_c1 with dissolve
    if d15s05_mk_virgin_pussy is True:
        play voice2 mc_hey_hey3 noloop
        mc "Have you ever fucked dick with your cunt, slut?"
        play voice3 min_no_simple noloop
        mk "Only dildos and strap-ons, sir."
        scene d15s05-26 mc-mk-toilet-pussy-talk1_c1 with dissolve
        play voice2 mc_happy_hah2 noloop
        mc "Well, get ready."
        play voice3 maria_what noloop
        mk "You mean-? You want me to-?"
        scene d15s05-25 mc-mk-toilet-pussy1_c1 with dissolve
        play voice2 mc_angry_errr4 noloop
        mc "Fuck your virgin pussy with that stranger's cock."
    elif True:
        play voice2 mc_hey_hey3 noloop
        mc "Do you know what I want you to do this time?"
        play voice3 min_no_simple noloop
        mk "No, sir. Anything you want, sir."
        scene d15s05-26 mc-mk-toilet-pussy-talk1_c1 with dissolve
        play voice2 mc_happy_hah2 noloop
        mc "Get your pussy against that strangers cock and fuck yourself."
    play voice3 min_yes_simple noloop
    mk "Yes, master [mcname]!"
    $ Lovense.vibrate(5)
    play voice3 maria_ah2 noloop
    scene d15s05-28 mc-mk-toilet-pussy-talk3_c2 with dissolve
    pause
    scene d15s05-00-a4 mk-fuck-anim-4-01_i with dissolve
    pause
    play voice3 daisy_moaning2
    scene d15s05-a4
    play voice2 mc_yes_yeah1 noloop
    mc "That's it. Take it all the way. Get your dirty cunt touching the wall."
    mc "Good girl. Now don't just make him do all the work."
    pause
    scene d15s05-a5 with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "Fuck that cock!"
    pause
    mc "There you go, slut. Just like that."
    scene d15s05-a6 with dissolve
    play voice2 d1s5_mchappy noloop
    mc "He's gotta be close by now."
    mk "What do you want me to do?"
    pause
    scene d15s05-a4-f with dissolve
    play voice2 mc_angry_errr1 noloop
    mc "Slam your pussy all the way down on his shaft."
    mc "Now hold that position and let him fuck you."
    pause
    scene d15s05-a5-f with dissolve
    play voice3 maria_orgasming
    if d15s05_mk_virgin_pussy is True:
        play voice2 mc_arrogant_huh1 noloop
        mc "Are you on any sort of birth control?"
        mk "I was on the pill. But I thought you might want to impregnate me."
        play voice2 mc_no_noway noloop
        mc "Not me, slut."
        mk "You mean-?"
    elif True:
        mk "He's getting close. I can feel it!"
    $ Lovense.vibrate(7)
    scene d15s05-a6-f with dissolve
    play voice2 mc_pain_rrrr noloop
    mc "Let that stranger fill your cunt with his seed."
    mk "Anything you want, [mcname]!"
    pause
    $ Lovense.vibrate(10)
    scene d15s05-29 mc-mk-toilet-pussy-talk4_c2 with hpunch
    pause
    mk "I think {w}he's cumming{w} inside me{w}, master!"
    scene d15s05-29 mc-mk-toilet-pussy-talk4_c1 with dissolve
    play voice3 [polly_breathing, polly_breathing] noloop
    mk "He's cum and gone, sir."
    $ Lovense.vibrate(5)
    scene d15s05-29 mc-mk-toilet-pussy-talk4_c3 with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "Show me."
    scene d15s05-61 mc-mk-toilet-pussy-cum_c1 with dissolve
    pause
    scene d15s05-61 mc-mk-toilet-pussy-cum_c2 with dissolve
    pause
    play voice2 d1s5_orgasm noloop
    if d15s05_anal is True:
        scene d15s05-62 mc-mk-toilet-ass-pussy-cum with dissolve
        mc "You're dripping from both holes."
        play voice3 maria_aah noloop
        mk "As I should be."
    elif True:
        scene d15s05-62 mc-mk-toilet-pussy-cum with dissolve
        mc "That's how you should be."
        play voice3 maria_aah noloop
        mk "My dirty cunt wet and dripping with cum?"
    scene d15s05-27 mc-mk-toilet-pussy-talk2_c1 with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Exactly."
    mk "I can hardly wait for the next one."

    $ d15s05_mk_virgin_pussy = False

    jump d15s05_sexmenu

label d15s05_assfuck:

    mk "What is your dirtiest fantasy?"
    scene d15s05-27 mc-mk-toilet-pussy-talk2_c3 with dissolve
    play voice2 mc_scared_oh1 noloop
    mc "You're not remotely ready to even hear that."
    scene d15s05-28 mc-mk-toilet-pussy-talk3_c1 with dissolve
    play voice3 maria_argh noloop
    mk "You know what I mean. What is every man's dirtiest fantasy?"
    play voice2 mc_arrogant_hm1 noloop
    mc "You're talking about anal."
    mk "Please, master. Can I fuck my ass with this stranger's filthy cock?"
    scene d15s05-28 mc-mk-toilet-pussy-talk3_c3 with dissolve
    play voice2 d9s5_auch2 noloop
    mc "Go ahed, fill your dirtbox with that nasty dick."
    scene d15s05-31 mc-mk-toilet-anal2_c1 with dissolve
    play voice3 maria_yes noloop
    mk "Yes, sir!"

    play voice3 min_scared_ah1 noloop
    $ Lovense.vibrate(7)
    scene d15s05-00-a8 mk-anal-anim-8-01_i with hpunch
    pause
    play voice3 aaleyah_open_moans1
    scene d15s05-a8
    if d15s05_mk_virgin_ass is True:
        mk "Ow! {w}Oh, master!{w} It hurts!!!"
    mk "Oh, oh, oh... yes..."
    pause

    scene d15s05-a7 with dissolve
    mk "He's all the way inside me now, master."
    play voice2 mc_yes_yeah7 noloop
    mc "How does that feel?"
    mk "It hurts like a motherfucker."
    pause

    scene d15s05-a9 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Do you want to stop?"
    mk "I wouldn't have it any other way."
    mc "You are such a fucking slut."
    pause

    play voice3 aaleyah_open_moans2
    scene d15s05-a8-f with dissolve
    mk "Thank you, sir."
    mk "Master! Master!! He's fucking me!!!"
    play voice2 mc_pain_argh1 noloop
    mc "Keep your shithole pressed tight against that cock and let him do whatever he wants to you."
    pause

    scene d15s05-a7-f with dissolve
    mk "Sir, shouldn't I-?"
    mc "What is it?"
    mk "Sir, shouldn't I turn around and let him fuck my mouth with his shitstained dick?!"
    pause

    scene d15s05-a9-f with dissolve
    play voice2 mc_no_nah2 noloop
    mc "Not this time."
    mc "You want to keep your mouthhole clean enough for other guys to fuck."
    mk "Yes, master!"
    pause

    play voice3 aaleyah_orgasm_shortmoan1 noloop
    $ Lovense.vibrate(11)
    scene d15s05-35 mc-mk-toilet-anal6_c2 with hpunch
    mk "Master! {w}I can feel him!!"
    play voice3 aaleyah_pain_ah1 noloop
    with hpunch
    mk "He's cumminnnngggg!!!!"
    scene d15s05-34 mc-mk-toilet-anal5_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "It sounds like you are as well."
    scene d15s05-34 mc-mk-toilet-anal5_c2 with dissolve
    play voice3 min_yes_simple noloop
    $ Lovense.vibrate(4)
    mk "Yes..."
    mk "Yes, sir. I did."
    scene d15s05-35 mc-mk-toilet-anal6_c1 with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "What a good little anal slut you are, girl."
    scene d15s05-33 mc-mk-toilet-anal4_c2 with dissolve
    play voice3 min_disappointed_ehh2 noloop
    mk "I love cumming from my butt."
    if d15s05_rimjob is False:
        mct "That gives me an idea."
    scene d15s05-36 mc-mk-toilet-anal7_c2 with dissolve
    play voice3 min_surprised_ehh1 noloop
    mk "Maybe next time I can ATM someone?"
    scene d15s05-36 mc-mk-toilet-anal7_c1 with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "I'll think about it."

    $ d15s05_mk_virgin_ass = False

    jump d15s05_sexmenu

label d15s05_rimmed:

    scene d15s05-40 mc-mk-toilet-rim1_c2 with fade
    $ Lovense.vibrate(2)
    play voice3 dahlia_sex_closedmoan1 noloop
    mk "How would you like me to take this one, sir?"
    scene d15s05-40 mc-mk-toilet-rim1_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Have you ever rimmed ass before?"
    scene d15s05-40 mc-mk-toilet-rim1_c3 with dissolve
    play voice3 maria_what noloop
    mk "How would I do that? Only his cock is in the hole."
    scene d15s05-40-2 mc-mk-toilet-rim1-2_c1 with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "Have you ever done it?"
    scene d15s05-40-2 mc-mk-toilet-rim1-2_c2 with dissolve
    play voice3 min_no_happy noloop
    mk "No, sir."
    scene d15s05-40-2 mc-mk-toilet-rim1-2_c3 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "You're going to rim my ass while he fucks you."
    play voice3 maria_aah noloop
    mk "That's so nasty! {w}I'LL DO IT!!!"
    scene d15s05-40-2 mc-mk-toilet-rim1-2_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Now close your eyes and don't open them until I tell you."
    play voice3 min_pain_ah noloop
    mk "Why?"
    play voice2 mc_angry_hm1 noloop
    mc "Because I said so."
    scene d15s05-42 mc-mk-toilet-rim3_c2
    if cage_ntr is False:
        show d15s05-42-over mc-mk-toilet-rim3_lc_c2
    with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Good, now grab that toilet with both hands."
    scene d15s05-42 mc-mk-toilet-rim3_c3 with dissolve
    play voice3 min_yes_simple noloop
    mk "Done, sir."
    scene d15s05-44 mc-mk-toilet-rim4_c2
    if cage_ntr is False:
        show d15s05-44-over mc-mk-toilet-rim4-lc_c2
    with dissolve
    mct "Now I just need to get into position."
    $ renpy.music.set_volume(0.4, 0.0, "sound2")
    play sound2 sfx_bed_slide3 noloop
    scene d15s05-44-2 mc-mk-toilet-rim4_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Get your tongue out and move forward."
    play voice3 dahlia_sex_closedmoan3 noloop
    scene d15s05-44-2 mc-mk-toilet-rim4_c3
    if cage_ntr is False:
        show d15s05-44-2-over mc-mk-toilet-rim4-lc_c3
    with dissolve
    pause
    scene d15s05-45-2 mc-mk-toilet-rim5_c3 with dissolve
    play voice2 mc_yes_yes2 noloop
    queue voice2 d7s4_mcbreathing
    play voice3 daisy_licking noloop
    $ Lovense.vibrate(8)
    mc "Yes! Just like that!"
    queue voice3 d2s12_flicking
    scene d15s05-45-2 mc-mk-toilet-rim5_c1
    if cage_ntr is False:
        show d15s05-45-over mc-mk-toilet-rim5-lc_c1
    with dissolve
    play voice2 mc_pain_mff1 noloop
    queue voice2 d7s4_mcbreathing
    mct "That feels so good. {w}I might just cum like this."
    scene d15s05-45-2 mc-mk-toilet-rim5_c2 with dissolve
    mc "Don't be afraid to work the inside with that filthy slut tongue of yours."
    play voice2 mc_scared_oh4 noloop
    queue voice2 d7s4_mcbreathing
    mc "Oh yeah..."
    scene d15s05-45-2 mc-mk-toilet-rim5_c1
    if cage_ntr is False:
        show d15s05-45-over mc-mk-toilet-rim5-lc_c1
    with dissolve
    play voice2 mc_pain_mff2 noloop
    queue voice2 d7s4_mcbreathing
    $ Lovense.vibrate(12)
    mc "Just like that."
    play voice2 mc_pain_mff3 noloop
    queue voice2 d7s4_mcbreathing
    mc "You are such a dirty slut."
    scene d15s05-45-2 mc-mk-toilet-rim5_c3 with dissolve
    play voice2 d3s7_mcemm noloop
    queue voice2 d7s4_mcbreathing
    mc "I'm gonna-"
    $ Lovense.vibrate(17)
    play voice2 mc_pain_argh1 noloop
    queue voice3 d3s8_licking1
    scene d15s05-45 mc-mk-toilet-rim5_c3 with vpunch
    pause
    scene d15s05-45 mc-mk-toilet-rim5_c1
    if cage_ntr is False:
        show d15s05-45-over mc-mk-toilet-rim5-lc_c1
    with dissolve
    mc "Fuck Yeah!!!"
    scene d15s05-45-2 mc-mk-toilet-rim5_c2 with dissolve
    play voice2 d1s5_orgasm2 noloop
    mc "That was good. Very good."
    $ Lovense.vibrate(3)
    mc "You can stop now, but keep your eyes closed."
    stop voice3 fadeout 1.0
    scene d15s05-42 mc-mk-toilet-rim3_c2
    if cage_ntr is False:
        show d15s05-42-over mc-mk-toilet-rim3_lc_c2
    with dissolve
    play voice2 mc_happy_oof3 noloop
    play voice3 daisy_moaning2
    mct "Now just to get dressed again."
    scene d15s05-46 mc-mk-toilet-rim6_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "How's that dick fucking you?"
    scene d15s05-46 mc-mk-toilet-rim6_c2 with dissolve
    mk "I'm about to cum, sir! So is he!!"
    scene d15s05-46 mc-mk-toilet-rim6_c1 with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "You have my permission to cum when he does."
    mk "Thank you, sir!!!"
    play voice3 maria_orgasming noloop
    scene d15s05-46 mc-mk-toilet-rim6_c3 with hpunch
    $ Lovense.vibrate(8)
    mk "MMMmmmmppphhh yesshhhh..."
    play voice2 mc_arrogant_huh2 noloop
    mc "Did he have a good cum inside you?"
    play voice3 maria_yes noloop
    mk "Yes, master. We both did."
    scene d15s05-47 mc-mk-toilet-rim7_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "You can open your eyes now."
    $ Lovense.vibrate(2)
    scene d15s05-47 mc-mk-toilet-rim7_c3 with dissolve
    play voice3 maria_ah2 noloop
    mk "Sir?!"
    play voice2 mc_happy_hah1 noloop
    mc "I left you something down there. Clean it up!"
    play voice3 [d3s8_sucking, d3s8_licking3]
    scene d15s05-48 mc-mk-toilet-rim8_c1 with dissolve
    play voice2 mc_scared_oh3 noloop
    mc "You are such a dirty fucking slut, you know that?"
    mk "Yes, sir."
    scene d15s05-48 mc-mk-toilet-rim8_c3 with dissolve
    play voice2 mc_pain_ffff noloop
    mc "Rimming my shitbox, then licking my jizz off the floor of a public bathroom."
    scene d15s05-48 mc-mk-toilet-rim8_c2 with dissolve
    play voice3 maria_yes noloop
    mk "I'm a total gloryhole slut, master."
    scene d15s05-48 mc-mk-toilet-rim8_c4 with dissolve
    play voice2 mc_disgust_uah1 noloop
    mc "Alright, get up while I think of other ways to abuse you."
    mk "Anything you want, master."

    $ d15s05_mk_virgin_pussy = False

    jump d15s05_sexmenu

label d15s05_end:

    if fl_watersports is True:
        scene d15s05-50 mc-mk-toilet-piss1_c2
        if cage_ntr is False:
            show d15s05-50-2 mc-mk-toilet-piss1-lc_c2
        with fade
        play voice3 maria_what noloop
        mk "What is that?"
        scene d15s05-50 mc-mk-toilet-piss1_c1 with dissolve
        play voice2 mc_disappointed_ehh2 noloop
        mc "It's a cock cage. Long story."
        scene d15s05-50 mc-mk-toilet-piss1_c3
        if cage_ntr is False:
            show d15s05-50-over mc-mk-toilet-piss1-lc_c3
        with dissolve
        play voice3 min_surprised_huh2 noloop
        mk "Is that why you haven't fucked me today?"
        scene d15s05-51 mc-mk-toilet-piss2_c1
        if cage_ntr is False:
            show d15s05-51-over mc-mk-toilet-piss2-lc_c1
        with dissolve
        play voice2 mc_disgust_booeah4 noloop
        mc "Well, that and you completely disgust me now."
        scene d15s05-50 mc-mk-toilet-piss1_c2
        if cage_ntr is False:
            show d15s05-50-2 mc-mk-toilet-piss1-lc_c2
        with dissolve
        play voice3 maria_argh noloop
        mk "I do?"
        play voice2 mc_yes_yes1 noloop
        mc "Let me show you how much."
        $ renpy.music.set_volume(0.15, 0.0, "sound2")
        play sound sfx_piss_loop2 loop
        play sound2 sfx_piss_loop1
        $ Lovense.vibrate(4)
        scene d15s05-pissing with dissolve
        play voice3 min_old_sinking
        mk "Oh Yes!!!"
        play voice2 mc_happy_hah2 noloop
        mc "You like that, huh?"
        mk "Yes! Use me like a cheap whore!"
        play voice2 mc_angry_errr4 noloop
        mc "A cheap whore is better than you. {w}You're not even getting paid for this."
        stop sound2 fadeout 1.0
        stop sound fadeout 1.0
        stop voice3 fadeout 1.0

    $ Lovense.stop()

    scene d15s05-52 mc-mk-toilet-exit2_c1 with fade
    play voice2 mc_hey_hey2 noloop
    mc "How does it feel?"
    scene d15s05-52 mc-mk-toilet-exit2_c2 with dissolve
    play voice3 min_surprised_oh noloop
    mk "Wonderful."
    mct "What a complete slut she's turned out to be."
    play voice3 min_thinking_emm noloop
    mk "Those are my clothes by the way!"
    scene d15s05-53 mc-mk-toilet-exit3_c1 with dissolve
    play voice2 mc_no_nah2 noloop
    mc "You don't need them anymore."
    scene d15s05-53 mc-mk-toilet-exit3_c2 with dissolve
    play voice3 maria_aah noloop
    mk "You wouldn't?!"
    scene d15s05-54 mc-mk-toilet-exit4_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Don't worry - I'll leave them somewhere you'll never find them."
    mc "Unless..."
    scene d15s05-54 mc-mk-toilet-exit4_c2 with dissolve
    play voice3 min_thinking_mhh noloop
    mk "Unless what?"
    scene d15s05-55 mc-mk-toilet-exit1_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Unless you ask me not to take them."
    scene d15s05-55 mc-mk-toilet-exit1_c2 with dissolve
    play voice3 maria_what noloop
    mk "That's it?"
    scene d15s05-52 mc-mk-toilet-exit2_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "That's it. Just ask me nicely. I'll leave your clothes here. You can leave with your dignity somewhat intact."
    mc "Or you can choose to let me leave here, knowing that I'm not coming back."
    if fl_watersports is True:
        mc "Eventually you'll have to leave this toilet wearing nothing but dried cum and piss."
    elif True:
        mc "Eventually you'll have to leave this toilet wearing nothing but dried cum."
    play voice2 mc_thinking_hmm5 noloop
    mc "So, what do you want to do?"
    scene d15s05-52 mc-mk-toilet-exit2_c2 with dissolve
    play voice3 maria_meeh noloop
    mk "Take them."
    scene d15s05-53 mc-mk-toilet-exit3_c1 with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "Seriously?"
    scene d15s05-53 mc-mk-toilet-exit3_c2 with dissolve
    play voice3 min_yes_simple noloop
    mk "Just go."
    scene d15s05-54 mc-mk-toilet-exit4_c1 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "Alright. Take care of yourself, slut."
    scene d15s05-54 mc-mk-toilet-exit4_c2 with dissolve
    play voice3 min_disappointed_ehh2 noloop
    mk "[mcname]? {w}Thank you for-"
    mk "Just... {w}Thank you."
    scene d15s05-55 mc-mk-toilet-exit1_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "You know something, Maria? You are seriously fucked in the head."
    mc "When you get yourself out of here - seek professional help."
    scene d15s05-55 mc-mk-toilet-exit1_c2 with dissolve
    play voice3 min_no_angry noloop
    mk "No need. I've got everything I want right here."
    scene d15s05-56 mc-mk-toilet-phone_c1 with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "... Whatever.{w} Have a nice life."
    $ renpy.end_replay()
    $ unlock_gallery_slot("scene", "d15s05")
    play voice3 min_pain_ah noloop
    scene d15s05-56 mc-mk-toilet-phone_c2 with dissolve
    pause
    scene d15s05-56 mc-mk-toilet-phone_c3 with dissolve
    call buzz from _call_buzz_5
    call add_points (d15s05_points) from _call_add_points_2
    flr "You earned [d15s05_points] points."
    if d12s01_goldstar is False:
        flr "Congratulations! You also earned a GOLD STAR!"
        call add_gold_star from _call_add_gold_star_1
        if fl_goldstars > 1:
            mct "Oh, another Gold Star. Okay."
        elif True:
            mct "I earned a Gold Star? Sure, why not."
        mct "I guess I got credit for Maria's debasement."
        play voice2 mc_arrogant_heh2 noloop
        mct "Huh, I wonder what Maria earned."

        $ d15s05_goldstar = True
    elif True:
        play voice2 mc_happy_thatsgood noloop
        mct "That's good I guess."

    stop music fadeout 3.5
    if is_extended_edition is True:
        jump d15s05b_ext
    elif True:
        jump d15s06

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
