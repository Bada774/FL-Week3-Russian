label d21s02:

    $ d21s02_arj_points = 0
    $ d21s02_sy_points = 0

    if d19s09_creampie_arj is True:
        $ d21s02_arj_points += 1
    elif True:
        $ d21s02_sy_points += 1

    if d20s08_copy_files is True:
        $ d21s02_sy_points += 1
    elif True:
        $ d21s02_arj_points += 1

    $ d21s02_bring_arj = False
    $ d21s02_bring_sy = False

    scene black
    show screen scene_transistion(_("In the Police Department's Lobby"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.2, 0.0, "sound3")
    play sound3 classroom fadein 3.0
    scene d21s02-01 mc-sy-arj-meeting-up
    with Fade(0.4, 0.5, 0.5)
    play voice2 mc_thinking_hmm1 noloop
    mc "Thank you for meeting me... angels."
    scene d21s02-03 mc-sy-arj-meeting-up with dissolve
    $ renpy.music.set_volume(1.0, 4.0, "sound2" )
    play voice3 amrose_yes_yeah2 noloop
    arj "Yeah, I don't know why she wore that."
    scene d21s02-04 sy-arj-talking with dissolve
    play voice4 stacy_angry noloop
    sy "It's our mission outfit! Why aren't you wearing yours?"
    scene d21s02-05 sy-arj-talking with dissolve
    play voice3 amrose_no_justno2 noloop
    arj "No. Just no. Why would you even-?"
    scene d21s02-06 mc-sy-arj-meeting-up with dissolve
    play voice4 polly_pollyangry noloop
    sy "I'm going to break that bitch. She's going down, and I'm the shovel."
    scene d21s02-07 arj-talking with dissolve
    play voice3 amrose_surprised_what noloop
    arj "What?"
    scene d21s02-08 sy-arj-talking with dissolve
    play voice4 stacy_angryhuh noloop
    sy "She's going away for life and I'm gonna punch her prison ticket."
    play voice3 amrose_arrogant_huh2 noloop
    arj "That doesn't even-"
    scene d21s02-09 sy-arj-talking with dissolve
    play voice4 polly_angry noloop
    sy "She's going downtown and upstate, and I'm her taxi."
    scene d21s02-10 sy-arj-talking with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "You can stop now."
    scene d21s02-11 mc-sy-talking with dissolve
    play voice4 stacy_hmm noloop
    sy "Let me at her. I'm here to chew gum and send Lydia to GenPop-"
    scene d21s02-12 arj-talking with dissolve
    play voice3 amrose_surprised_ahh2 noloop
    arj "PLEASE STOP!"
    scene d21s02-13 mc-police officer-talking with dissolve
    play voice4 captain_hmm4 noloop
    "Police Officer" "Excuse me, are you [mcname] Young?"
    scene d21s02-14 mc-police officer-talking with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "Yes, we're here to see Lydia Cox. I made an appointment."
    scene d21s02-15 mc-police officer-talking with dissolve
    play voice4 captain_yeah noloop
    "Police Officer" "Yeah, she signed for you to visit. I'm afraid she's only allowed two visitors at any time."
    scene d21s02-16 mc-sy-police officer-talking with dissolve
    play voice3 stacy_angry noloop
    sy "Let me at her. Let me at her!{w} I'll put that bitch away so long she'll never meet her great grandchildren!"
    scene d21s02-17 mc-sy-talking with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "That doesn't even make any sense."
    scene d21s02-18 mc-sy-arj-police officer-talking with dissolve
    play voice4 amrose_disappointed_ehh1 noloop
    arj "Go ahead, take Stacy. If I see that cunt again I'll break her fucking neck."
    scene d21s02-19 arj-police officer-talking with dissolve
    play voice3 captain_erghh noloop
    "Police Officer" "I'll pretend I didn't hear that."
    scene d21s02-20 mc-thinking with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.7
    mct "Shit. Which unhinged lunatic do I bring with me?"
    if d21s02_arj_points == 2 or d21s02_arj_points == 1 and date_sy is False:
        $ d21s02_bring_arj = True
        scene d21s02-21 mc-arj-choosing-amrose with dissolve
        play voice2 mc_arrogant_hm1 noloop
        mc "AmRose, you're with me.{w} No killing."
        scene d21s02-22 mc-arj-talking with dissolve
        play voice3 amrose_thinking_emm noloop
        arj "What about maiming?"
        scene d21s02-21 mc-arj-choosing-amrose with dissolve
        play voice2 mc_arrogant_huh1 noloop
        mc "Ask permission first."
    elif d21s02_sy_points == 2:
        $ d21s02_bring_sy = True
        scene d21s02-23 mc-sy-choosing-stacy with dissolve
        play voice2 mc_arrogant_hm1 noloop
        mc "Stacy, get your shit together. You're with me."
        scene d21s02-24 sy-talking with dissolve
        play voice3 stacy_yes2 noloop
        sy "Oh yeah, time to fuck this bitch up."
        scene d21s02-25 mc-sy-talking with dissolve
        play voice2 mc_angry_hm2 noloop
        mc "I said, \"Get your shit together.\" That means behave."
        play voice3 stacy_smell noloop
        sy "Fine..."
    elif True:
        menu:
            "Select AmRose"(hint="d21s02m01c01") if True:
                $ d21s02_bring_arj = True
                scene d21s02-21 mc-arj-choosing-amrose with dissolve
                play voice2 mc_arrogant_hm1 noloop
                mc "Alright. AmRose, you're with me. Don't fuck this up."
            "Select Stacy"(hint="d21s02m01c02") if True:

                $ d21s02_bring_sy = True
                scene d21s02-23 mc-sy-choosing-stacy with dissolve
                play voice2 mc_arrogant_hm1 noloop
                mc "Alright. Stacy, you're with me. Don't fuck this up."

    jump d21s02_meet_lc

label d21s02_meet_lc:

    stop sound3 fadeout 2.0
    play sound sfx_double_door1
    scene d21s02-26 mc-talking with Fade(0.5, 0.5, 0.5)
    play music music_killbilly fadein 0.2
    play voice2 mc_happy_a1 noloop
    mc "Ah. Hello, Clarice"
    if cage_ntr is True:
        scene d21s02-28 mc-arj-lc-talking-aggressively with dissolve
        play voice3 dahlia_thinking_hmm1 noloop
        lc "That's my line."
        scene d21s02-26 mc-talking with dissolve
        play voice2 d3s11b_mcheh noloop
        mc "It seemed appropriate, given the terrain."
        scene d21s02-28 mc-arj-lc-talking-aggressively with dissolve
        play voice3 dahlia_thinking_mmm2 noloop
        lc "Except you're on the wrong side of the bars... for now."
    elif True:
        scene d21s02-27 mc-arj-lc-talking-sweetly with dissolve
        play voice3 dahlia_thinking_hmm1 noloop
        lc "I ain't seen nobody buffalo Bill like you buffalo'd Bill."
        scene d21s02-26 mc-talking with dissolve
        play voice2 d3s11b_mcheh noloop
        mc "Kill Bill."
        scene d21s02-27 mc-arj-lc-talking-sweetly with dissolve
        play voice3 dahlia_happy_hmm2 noloop
        lc "Volume 2."
        scene d21s02-26 mc-talking with dissolve
        play voice2 mc_thinking_hmm4 noloop
        mc "Good to see you, too."

    if cage_ntr is True:
        if d21s02_bring_arj is True:
            jump d21s02_ntr_arj
        elif True:
            jump d21s02_ntr_sy
    elif True:
        if d21s02_bring_arj is True:
            jump d21s02_lc_arj
        elif True:
            jump d21s02_lc_sy

label d21s02_ntr_arj:

    play sound sfx_cloth_rustling2
    scene d21s02-29 mc-arj-talking with dissolve
    play voice4 amrose_old_psst2 noloop
    pause
    scene d21s02-30 mc-arj-talking with dissolve
    pause
    play voice4 amrose_pain_sobs1 noloop
    scene d21s02-31 mc-arj-talking with dissolve
    arj "I know I talked a good game in front of Stacy, but honestly... I'm scared."
    scene d21s02-32 mc-arj-talking with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "It's a scary place. Just remember that we get to walk out of here."
    scene d21s02-33 mc-arj-talking with dissolve
    play voice4 amrose_happy_mmm noloop
    arj "It's not that. Lydia scares me. What you've told me about the real person hiding behind that frigid mask..."
    scene d21s02-34 mc-arj-talking with dissolve
    play voice2 mc_hey_hey2 noloop volume 0.8
    mc "It's all good. You're safe."
    mc "Just remember who is on which side of the bars."
    play voice4 stacy_smell noloop
    scene d21s02-35 mc-arj-thinking with dissolve
    pause
    scene d21s02-36 mc-arj-confidently-talking with dissolve
    play voice4 amrose_yes_ugu noloop
    arj "Okay. Let's do this."
    scene d21s02-37 mc-arj-ly-talking with fade
    play voice4 amrose_arrogant_huh1 noloop
    arj "What's up, bitch? Enjoying the view?"
    scene d21s02-38 mc-arj-ly-talking with dissolve
    play voice3 dahlia_arrogant_pff noloop volume 0.75
    lc "Girl, you missed out. If our boyfriend hadn't interfered you'd be happily lapping up my juices right now and you know it."
    scene d21s02-39 mc-arj-ly-talking with dissolve
    play voice4 amrose_angry_errr noloop
    arj "Fuck you. You don't know me."
    scene d21s02-40 mc-arj-ly-talking with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    lc "I can practically feel it. Can you taste me from there?"
    lc "Why don't you get down on your knees right now and stick your tongue through the bars."
    scene d21s02-41 mc-arj-ly-talking with dissolve
    play voice4 amrose_surprised_oh3 noloop
    arj "Nice cage. Shouldn't you have some sort of Hannibal Lector mask or something?"
    play sound sfx_metal_fence2
    scene d21s02-44 mc-arj-ly-talking with dissolve
    play voice3 dahlia_disappointed_ehh1 noloop
    lc "Why? Are you afraid I might eat you instead?"
    scene d21s02-41 mc-arj-ly-talking with dissolve
    play voice4 amrose_angry_argh1 noloop
    arj "Fuck you."
    scene d21s02-43 mc-arj-ly-talking with dissolve
    play voice4 amrose_disappointed_ehh2 noloop
    arj "I can't do this. I don't know if I want to kill her or-"
    scene d21s02-42 mc-arj-ly-talking with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "It's alright. Give me a couple minutes to talk to her. Then we can leave."
    scene d21s02-43 mc-arj-ly-talking with dissolve
    play voice4 amrose_yes_yeah3 noloop
    arj "Fine. Make it quick."
    scene d21s02-45 mc-arj-ly-talking-lc with dissolve
    play voice3 lydia_laugh noloop
    lc "That's what she said. *chuckles*"

    jump d21s02_mc_ntr

label d21s02_lc_arj:

    scene d21s02-28 mc-arj-lc-talking-aggressively with dissolve
    play voice3 lydia_hmmmm noloop
    lc "AmRose? Why is she here?"
    scene d21s02-30 mc-arj-talking with dissolve
    play voice2 d2s9_confused noloop volume 1.5
    mc "Moral support. She wanted to-"
    scene d21s02-41 mc-arj-ly-talking with dissolve
    play voice4 amrose_angry_argh1 noloop
    arj "I'm here to kick your ass if you step out of line."
    arj "Maybe even strangle you for the shit you pulled already."
    scene d21s02-40 mc-arj-ly-talking with dissolve
    play voice3 lydia_morningoh noloop volume 1.4
    lc "The shit I pulled? Look who's talking."
    scene d21s02-39 mc-arj-ly-talking with dissolve
    play voice4 amrose_angry_errr noloop
    arj "Shut your fucking mouth right there!!!"
    scene d21s02-44 mc-arj-ly-talking with dissolve
    play voice3 lydia_haha noloop volume 1.5
    lc "Don't worry. I'm not about to out you in front of our boyfriend."
    scene d21s02-37 mc-arj-ly-talking with dissolve
    play voice4 amrose_arrogant_hmm1 noloop
    arj "You better forget all about that and never say a damn thing or else I swear I'll-"
    scene d21s02-38 mc-arj-ly-talking with dissolve
    play voice3 lydia_oof noloop
    lc "I wouldn't. I'm sorry. I shouldn't have said anything."
    play voice4 amrose_happy_mmm noloop
    arj "Alright then."
    scene d21s02-45 mc-arj-ly-talking-lc with dissolve
    play voice3 lydia_thinking noloop volume 1.6
    lc "But you better talk to Jerome. He probably watched everything."
    if is_antagonist_mode is True:
        scene d21s02-41 mc-arj-ly-talking with dissolve
        play voice4 amrose_surprised_oh3 noloop
        arj "God dammit. Why are you doing this to me?"
        play voice3 lydia_lydiahey noloop
        lc "I'm not doing anything. I didn't know you would do that."
        play voice4 amrose_angry_argh3 noloop
        arj "You blackmailed me into doing those livestreams or else-"
        play voice3 dahlia_no_high3 noloop
        scene d21s02-38 mc-arj-ly-talking with dissolve
        lc "That wasn't me! Maybe that was Jerome. Maybe it was just the A.I."
        lc "I didn't know anything about that at the time. I thought you were just doing it for points."
    scene d21s02-39 mc-arj-ly-talking with dissolve
    play voice4 amrose_angry_ehh noloop
    arj "I'm not done with you."
    scene d21s02-50 mc-arj-ly-talking-lc with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    lc "I'm not the person you think I am."
    lc "But I am so sorry this all happened. That's why I'm here. I hope you can see that someday."

    jump d21s02_mc_lc

label d21s02_ntr_sy:

    scene d21s02-52 mc-sy-ly-talking with hpunch
    play voice4 polly_pollyangry noloop
    sy "Shut your cunt mouth, bitch.{w} Now, tell me who you work for!"
    scene d21s02-53 mc-sy-ly-talking with dissolve
    play voice3 dahlia_arrogant_huh noloop
    lc "I'm sorry, was I supposed to shut up or talk?"
    scene d21s02-54 mc-sy-ly-talking with dissolve
    play voice4 polly_angry noloop
    sy "TALK, BITCH!"
    scene d21s02-55 mc-sy-ly-talking with dissolve
    play voice3 dahlia_no_nah noloop
    lc "Nobody paid me nothing."
    scene d21s02-56 mc-sy-ly-talking with dissolve
    play voice4 stacy_impressed noloop
    sy "Ah ha!{w} So, you admit that you're the mastermind behind Fetish Locator!"
    scene d21s02-53 mc-sy-ly-talking with dissolve
    play voice3 dahlia_arrogant_pff noloop
    lc "I admitted nothing. I just said that nobody paid me."
    scene d21s02-57 mc-sy-ly-talking with dissolve
    play voice4 stacy_angry noloop
    sy "Don't play games with me, Slut!"
    scene d21s02-58 mc-sy-ly-talking with dissolve
    play voice2 mc_surprised_wow2 noloop
    mc "Whoa whoa whoa. Let's dial it back a bit."
    scene d21s02-59 mc-sy-ly-talking with dissolve
    play voice3 dahlia_happy_relief noloop
    lc "You realize these \"visitations\" aren't recorded, and are illegal to record, right?"
    scene d21s02-60 mc-sy-ly-talking with dissolve
    play voice4 stacy_huh2 noloop
    sy "What?"
    scene d21s02-61 mc-sy-ly-talking with dissolve
    play voice2 mc_no_no5 noloop
    mc "No, I don't think she realized that."
    scene d21s02-63 mc-sy-ly-talking with dissolve
    play voice3 dahlia_arrogant_heh noloop
    lc "How exactly did you think this was going to play out? That I would sign a full confession or something?"
    scene d21s02-62 mc-sy-ly-talking with dissolve
    play voice4 stacy_upset1 noloop
    sy "Well, yeah. After I berated you-"
    scene d21s02-63 mc-sy-ly-talking with dissolve
    play voice3 dahlia_no_uhuh noloop
    lc "Not gonna happen.{w} What about you? Why are you here?"
    scene d21s02-61 mc-sy-ly-talking with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "I was just planning on visiting my girlfriend and/or ex-girlfriend."
    scene d21s02-45 mc-arj-ly-talking-lc with dissolve
    play voice3 dahlia_surprised_oh noloop
    lc "How sweet."
    scene d21s02-64 mc-sy-ly-talking with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "Stacy, can you give us a couple minutes."
    scene d21s02-65 mc-sy-ly-talking with dissolve
    play voice4 stacy_hey noloop
    sy "You want me to leave? I'm not done with her."
    scene d21s02-66 mc-sy-ly-talking with dissolve
    play voice3 dahlia_angry_hm2 noloop
    lc "Oh yes, you are."
    scene d21s02-67 mc-sy-ly-talking with dissolve
    play voice2 d9s3_no noloop volume 2.0
    mc "You don't have to leave. Just take a couple steps back for a minute."
    scene d21s02-68 mc-sy-ly-talking with dissolve
    play voice4 stacy_angryhuh noloop
    sy "Sure, okay."

    jump d21s02_mc_ntr

label d21s02_lc_sy:

    scene d21s02-69 mc-sy-ly-talking-lc with hpunch
    play voice4 stacy_angryhuh noloop
    sy "Shame. Shame! Shame!!!"
    scene d21s02-70 mc-sy-ly-talking-lc with dissolve
    play voice3 lydia_hmmmm noloop
    lc "Um... Stacy, right?"
    scene d21s02-71 mc-sy-ly-talking-lc with dissolve
    play voice4 stacy_huh2 noloop
    sy "So you admit you know who I am?!"
    scene d21s02-72 mc-sy-ly-talking-lc with dissolve
    play voice3 dahlia_yes_ugu noloop
    lc "I think so. What is all this?"
    scene d21s02-73 mc-sy-ly-talking-lc with dissolve
    play voice4 polly_angry noloop
    sy "I'm here to beat a confession out of you."
    scene d21s02-74 mc-sy-ly-talking-lc with dissolve
    play voice2 mc_arrogant_hm2 noloop
    mc "She already confessed."
    scene d21s02-75 mc-sy-ly-talking-lc with dissolve
    play voice4 stacy_huh noloop
    sy "What?"
    scene d21s02-75-03 mc-sy-ly-talking-lc with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    lc "I already confessed to everything. That's why I'm here."
    scene d21s02-75-02 mc-sy-ly-talking-lc with dissolve
    play voice4 polly_impressed noloop
    sy "So..."
    scene d21s02-75-05 mc-sy-ly-talking-lc with dissolve
    play voice3 lydia_thinking noloop volume 1.6
    lc "I'm sorry. Did you lose your train of thought?"
    scene d21s02-75-04 mc-sy-ly-talking-lc with dissolve
    play voice4 stacy_upset1 noloop
    sy "Yeah, I had this whole thing planned. Do you mind if I ask you a question about all that?"
    scene d21s02-75-06 mc-sy-ly-talking-lc with dissolve
    play voice3 lydia_haha noloop
    lc "Sure. Why not?"
    scene d21s02-75-07 mc-sy-ly-talking-lc with dissolve
    play voice4 stacy_mmm2 noloop
    sy "How did you do it?"
    scene d21s02-76 mc-sy-ly-talking-lc with dissolve
    play voice3 dahlia_thinking_mmm2 noloop
    lc "Well, Jerome really did the bulk of it. He created the app and-"
    scene d21s02-75-08 mc-sy-ly-talking-lc with dissolve
    play voice4 stacy_uhuh noloop
    sy "Not that part. I mean, how did you get so many people playing?"
    scene d21s02-75-09 mc-sy-ly-talking-lc with dissolve
    play voice3 lydia_morningoh noloop
    lc "Oh, I did do that part. It was just about recognizing social nexuses."
    scene d21s02-60 mc-sy-ly-talking with dissolve
    play voice4 stacy_mmm1 noloop
    sy "Social nexii?"
    scene d21s02-61 mc-sy-ly-talking with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "I think the plural of nexus is nexus."
    scene d21s02-63 mc-sy-ly-talking with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    lc "Although maybe it would be better to think of it as confluence points."
    scene d21s02-56 mc-sy-ly-talking with dissolve
    play voice4 stacy_nono noloop
    sy "I'm not sure I understand."
    scene d21s02-70 mc-sy-ly-talking-lc with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop volume 0.8
    lc "Every social group has a single central hub. Often many different social groups center around a specific hub."
    lc "[mcname] is a great example. Over the past few weeks his social group has exploded, and he's become central to many existing social groups. They all revolve around him."
    scene d21s02-72 mc-sy-ly-talking-lc with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    lc "All those people he's met. All those people he's influenced. They're like threads in a spider's web."
    lc "He makes decisions that ripple through the lives of everyone around him."
    scene d21s02-75-07 mc-sy-ly-talking-lc with dissolve
    play voice4 stacy_oh noloop
    sy "So, you found people - these social nexus or confluence points - and you provoked them into playing Fetish Locator?"
    scene d21s02-75-09 mc-sy-ly-talking-lc with dissolve
    play voice3 dahlia_yes_yeah2 noloop
    lc "I'd say that I influenced them. Sometimes it was a person. Sometimes it was just a place where people gathered."
    lc "Drop an invite customized to that nexus, then watch the app spread to their group."
    scene d21s02-75-04 mc-sy-ly-talking-lc with dissolve
    play voice4 stacy_hmm noloop
    sy "Huh. That gives me a lot to think about."
    scene d21s02-77 mc-sy-ly-talking-lc with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "This is all very interesting, but... Can you give us a minute?"
    play voice4 stacy_oh2 noloop
    sy "Oh, sure."
    play voice2 mc_yes_ugu1 noloop
    if persistent.is_special is True:
        mc "Thanks, sis."
    elif True:
        mc "Thanks, Stacy."
    scene d21s02-78 mc-sy-ly-talking-lc with dissolve
    play voice3 dahlia_arrogant_heh noloop
    lc "I'm sure she means well."
    play voice2 mc_yes_yeah5 noloop volume 0.75
    mc "I hope so."

    jump d21s02_mc_lc

label d21s02_mc_ntr:

    scene d21s02-79 mc-sy-ly-talking-lc with dissolve
    play voice2 mc_disappointed_ehh2 noloop
    mc "What the hell happened to you?"
    scene d21s02-80 mc-ly-talking with dissolve
    play voice3 dahlia_arrogant_hm noloop
    lc "I'm in jail. My carefully sculpted reputation is ruined."
    lc "Clearly I overestimated you."
    scene d21s02-81 mc-ly-talking with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "From where I'm standing it seems like you underestimated me. I proved stronger than you expected."
    scene d21s02-82 mc-ly-talking with dissolve
    play voice3 dahlia_arrogant_ha noloop
    lc "Ha! Stronger? Your devotion was weak. You're selfish and remorseless."
    lc "You claimed to love me, but when you got the chance to know the real me-"
    scene d21s02-83 mc-ly-talking with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "It's not my fault that the real you turned out to be a psychopathic narcissistic bitch."
    scene d21s02-84 mc-ly-talking with dissolve
    play voice3 dahlia_angry_argh1 noloop
    lc "You betrayed me at the first opportunity."
    scene d21s02-85 mc-ly-talking with dissolve
    play voice2 mc_angry_errr2 noloop
    mc "You manipulated me. You lied to me. You betrayed me!"
    play sound sfx_metal_fence1
    scene d21s02-86 mc-ly-talking with dissolve
    play voice3 dahlia_pain_argh noloop
    lc "Bullshit! I would never lie."
    scene d21s02-81 mc-ly-talking with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "Lie of omission?"
    scene d21s02-87 mc-ly-talking with dissolve
    play voice3 dahlia_angry_oh noloop
    lc "Fuck off. That's not a real thing."
    scene d21s02-88 mc-ly-talking with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "What the hell happened to the sweet girl I idolized? How did you become this twisted slut?"
    scene d21s02-90 mc-ly-talking with dissolve
    play voice3 dahlia_thinking_oh noloop
    lc "If you think I'm twisted - you should meet my parents."
    scene d21s02-89 mc-ly-talking with dissolve
    play voice2 mc_angry_huh2 noloop
    mc "They raised you to be like this?"
    scene d21s02-80 mc-ly-talking with dissolve
    play voice3 dahlia_surprised_huh1 noloop
    lc "Raised me? They've been drunk and stoned for decades."
    lc "They hired people to look after me. Tutors, babysitters, au pairs."
    lc "Some of them lasted weeks. Some of them lasted months. Eventually they all left."
    scene d21s02-91 mc-ly-talking with dissolve
    play voice2 mc_angry_huh1 noloop
    mc "What happened to them?"
    play sound sfx_metal_fence2
    scene d21s02-87 mc-ly-talking with dissolve
    play voice3 dahlia_pain_sobs noloop
    lc "I did. Don't you get it? I am unlovable."
    scene d21s02-83 mc-ly-talking with dissolve
    play voice2 mc_no_nah2 noloop
    mc "I doubt that."
    scene d21s02-84 mc-ly-talking with dissolve
    play voice3 dahlia_angry_oof noloop
    lc "I really thought you might be different."
    scene d21s02-85 mc-ly-talking with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, I get it. You're trying to guilt me, aren't you?"
    scene d21s02-92 mc-ly-talking with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    lc "Is it working?"
    scene d21s02-93 mc-ly-talking with dissolve
    play voice2 d9s5_auch2 noloop
    mc "Fuck off. I'm done with you."
    scene d21s02-94 mc-ly-talking with dissolve
    play voice3 dahlia_yes_aga noloop
    lc "You'll come back. You know you can't live without me."

    jump d21s02_ending

label d21s02_mc_lc:

    scene d21s02-79 mc-sy-ly-talking-lc with dissolve
    play voice2 d2s9_mchey noloop volume 1.3
    mc "Are you okay?"
    scene d21s02-80 mc-ly-talking with dissolve
    play voice3 dahlia_surprised_huh1 noloop
    lc "I'm in jail. My reputation is ruined. My life is over."
    lc "Sure, I'm just delighted. How are you?"
    if d21s02_bring_arj is True:
        scene d21s02-97 mc-arj-ly-talking-lc with dissolve
    elif True:
        scene d21s02-97-02 mc-sy-ly-talking-lc with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Lydia, hon. I'm sorry. Stupid question."
    mc "Has anyone hurt you? Is there anything I can do to help?"
    scene d21s02-86 mc-ly-talking with dissolve
    play voice3 dahlia_pain_mmh noloop
    lc "I'm fine, I guess. Just the reality of what has happened is sinking in."
    if d12s05_stop is True:
        lc "You remember that prostitute? She was in here for a few hours."
    elif True:
        lc "There was some prostitute in here for a few hours."
    scene d21s02-50 mc-arj-ly-talking-lc with dissolve
    play voice3 lydia_moan1 noloop
    lc "Other than that I haven't had any \"guests\". I've just been alone in this cage."
    lc "She told me a bit about what prison is like. Real prison - not this holding cell."
    lc "It sounds horrifying, but I can survive that."
    scene d21s02-91 mc-ly-talking with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "Maybe you can recant your confession? Or get out on bail?"
    scene d21s02-96 mc-ly-talking-lc with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    lc "I won't see the judge for a bail hearing until Monday."
    scene d21s02-95 mc-ly-talking-lc with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "What about the prostitute? Didn't she get a hearing?"
    scene d21s02-82 mc-ly-talking with dissolve
    play voice3 dahlia_no_high1 noloop
    lc "No. She was just fined. Somebody paid it for her. Also, I think she has a friend among the cops. Maybe a client, I don't know."
    lc "She said she'll talk to them for me. Maybe get me a better dinner or something."
    lc "Frick. I hope they don't think... I hope they don't expect anything from me... like something she would do."
    scene d21s02-99 mc-ly-talking-lc with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "I'm so sorry this is happening to you. If I could get you out of here I would."
    scene d21s02-75-03 mc-sy-ly-talking-lc with dissolve
    play voice3 lydia_lydiahey noloop
    lc "You know I love you, don't you?"
    play voice2 d9s2_ugu noloop volume 2.0
    mc "Of course."
    lc "Can I ask you a favor? Not now, but maybe after the bail hearing if I get transferred to a real prison."
    scene d21s02-79 mc-sy-ly-talking-lc with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Anything."
    scene d21s02-76 mc-sy-ly-talking-lc with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    lc "Okay. Thank you."
    scene d21s02-102 mc-ly-talking-lc with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "I'm still your man. You got that?"
    scene d21s02-100 mc-ly-talking-lc with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    lc "It's you and me until the wheels come off."
    scene d21s02-81 mc-ly-talking with dissolve
    play voice2 d9s2_mcyes noloop volume 2.0
    mc "Exactly."
    scene d21s02-105 mc-ly-talking-lc with dissolve
    play voice3 dahlia_old_upset noloop
    lc "Tell me if the wheels came off."
    scene d21s02-101 mc-ly-talking-lc with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "I'm still here with you."
    scene d21s02-103 mc-ly-talking-lc with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    lc "Thank you."
    play sound sfx_jail_notification volume 0.4
    "Bzzzzz" with hpunch
    scene d21s02-105 mc-ly-talking-lc with dissolve
    play voice3 dahlia_surprised_oh noloop
    lc "That's your cue. Visiting time is over."
    scene d21s02-102 mc-ly-talking-lc with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "You can survive this. Whatever happens. I've got your back."
    scene d21s02-107 mc-ly-talking-lc with dissolve
    play voice3 stacy_smell noloop
    lc "I love you."
    scene d21s02-106 mc-ly-talking-lc with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.8
    if d20s09_lc_love >= 2:
        mc "I love you too."
    elif True:
        mc "I know."

    jump d21s02_ending

label d21s02_ending:

    if d21s02_bring_arj is True:
        jump d21s02_arj_ending
    elif True:
        jump d21s02_sy_ending

label d21s02_arj_ending:

    play voice4 amrose_thinking_oh2 noloop
    scene d21s02-108 arj-ly-talking-ending with dissolve
    arj "Oh, Lydia, I wanted to tell you something."
    scene d21s02-109 arj-ly-talking-ending with dissolve
    play voice3 dahlia_yes_yeah2 noloop
    lc "What's that?"
    scene d21s02-110 arj-ly-talking-ending with dissolve
    play voice4 amrose_happy_laugh1 noloop
    arj "I did a little research. You know there's only one female prison in this state?"
    lc "..."
    arj "I didn't think so. They have a five year waiting list.{w} Your best chance is getting into the female wing of one of the coed penitentiaries. There are four of those."
    arj "Of course, there isn't much chance of that."
    scene d21s02-108 arj-ly-talking-ending with dissolve
    play voice4 amrose_thinking_hmm2 noloop
    arj "Our justice system is really fucked."
    arj "Odds are you'll be either in solitary or gen pop at a male prison by the end of the week."
    arj "Enjoy getting passed around for half a pack of smokes."
    scene d21s02-38 mc-arj-ly-talking with dissolve
    play voice3 dahlia_surprised_huh2 noloop
    lc "You're bluffing."
    scene d21s02-49 mc-arj-ly-talking-lc with dissolve
    play voice4 amrose_no_nah noloop
    arj "You know, I almost wish I were... almost."
    arj "May I never see nor hear from you ever again."

    jump d21s02_end

label d21s02_sy_ending:

    scene d21s02-111 sy-ly-talking-ending with dissolve
    play voice4 stacy_mmm1 noloop
    sy "Lydia, I wanted to tell you something while [mcname] wasn't around."
    scene d21s02-112 sy-ly-talking-ending with dissolve
    play voice3 lydia_aga noloop
    lc "Obviously. So, what is it?"
    scene d21s02-113 sy-ly-talking-ending with dissolve
    play voice4 stacy_upset1 noloop
    sy "You might think I'm a silly little girl, but let me tell you something."
    if persistent.special is True:
        sy "You hurt my brother. I won't forget that."
    elif True:
        sy "You hurt [mcname]. I won't forget that."
    scene d21s02-114 sy-ly-talking-ending with dissolve
    play voice4 stacy_mmm2 noloop
    sy "Maybe I'll come up with something tomorrow. Maybe it will take twenty years."
    sy "Maybe I'll bribe one of your cell mates. Maybe I'll have to seduce a guard."
    scene d21s02-115 sy-ly-talking-ending with dissolve
    play voice4 stacy_hmm noloop
    sy "You might even go free and think you can hide on the other side of the world."
    sy "I don't care if it takes me decades and you're living in Bali under a different name."
    sy "I will make you pay for hurting him."
    scene d21s02-113 sy-ly-talking-ending with dissolve
    play voice4 stacy_angryhuh noloop
    sy "Until then, you'll never know who you can trust - who's coming after you - or what I got them to do."
    sy "Sleep lightly."

    jump d21s02_end

label d21s02_end:

    $ renpy.music.set_volume(0.3, 3.0, "music" )
    play sound sfx_double_door1
    scene d21s02-116 mc-sy-arj-talking with Fade(0.5, 0.5, 0.5)
    play voice2 mc_happy_oof3 noloop
    mc "Well, that was an experience."
    if d21s02_bring_arj is True:
        scene d21s02-118 mc-sy-arj-talking with dissolve
        play voice4 amrose_disappointed_ehh1 noloop
        arj "I'm sure neither of us want to experience anything like that again."
    elif True:
        $ unlock_gallery_slot("cg", "d21s02")
        scene d21s02-117 mc-sy-arj-talking with dissolve
        play voice4 stacy_laugh4 noloop
        sy "I don't know. It was kinda fun."

    jump d21s03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
