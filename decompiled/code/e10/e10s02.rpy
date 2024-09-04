label e10s02:

    $ e10s02_mes_partner = False

    scene black
    show screen scene_transistion(_("The next day"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.5, 0.0, "sound2")
    play sound2 park fadein 3.0
    scene e10s02-02 mc-mes-walk1_c1
    with Fade(0.5, 0.5, 0.9)
    pause
    scene e10s02-01 mc-mes-entry1_c2 with dissolve
    play voice3 min_thinking_hmm1 noloop
    mes "[mcname]. This is my family. They're important to me. So, be respectful."
    scene e10s02-01 mc-mes-entry1_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "Of course, Min."
    scene e10s02-02 mc-mes-walk1_c2 with dissolve
    play voice3 min_thinking_oh noloop
    mes "Oh fuck. I should have told you sooner. Min is my family name."
    scene e10s02-03 mc-mes-walk2_c1 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "That makes sense. So your parents are-"
    scene e10s02-04 mc-mes-walk3_c2 with dissolve
    play voice3 min_thinking_emm noloop
    mes "Just call them Mr. & Mrs. Min. You'll be fine."
    scene e10s02-04 mc-mes-walk3_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Anyone else I should know about tonight?"
    scene e10s02-06 mc-mes-walk5_c1 with dissolve
    play voice3 min_arrogant_huh1 noloop
    mes "My older brother will probably be there. He's important. He's set to take over the family business when my father retires."
    scene e10s02-06 mc-mes-walk5_c2 with dissolve
    play voice2 d1s2_hmm noloop volume 1.6
    mc "Is your father planning on retiring soon?"
    scene e10s02-07 mc-mes-walk6_c2 with dissolve
    play voice3 min_no_happy noloop
    mes "Not for a few decades, hopefully."
    scene e10s02-07 mc-mes-walk6_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay. What do I call your brother?"
    scene e10s02-08 mc-mes-walk7_c2 with dissolve
    play voice3 min_old_hmm noloop
    mes "He'll introduce himself, but calling him Do-yun should be fine."
    scene e10s02-08 mc-mes-walk7_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "His name is Do-yun Min?"
    scene e10s02-08 mc-mes-walk7_c2 with dissolve
    play voice3 min_no_simple noloop
    mes "No. His name is Min Do-yun. We put the surname before the given name."
    scene e10s02-09 mc-mes-walk8_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Right, sorry. Anything else I should know?"
    scene e10s02-09 mc-mes-walk8_c2 with dissolve
    play voice3 min_surprised_ehh1 noloop
    mes "Just try not to-"
    mes "You know what, just try not to talk too much. Be respectful. Don't embarrass yourself or me."
    scene e10s02-09 mc-mes-walk8_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "I'll do my best."
    scene e10s02-09 mc-mes-walk8_c2 with dissolve
    play voice3 min_yes_ugu noloop
    mes "Alright."
    $ renpy.music.set_volume(0.1, 2.0, "sound2")
    play sound sfx_cloth_rustling2
    scene e10s02-10 mc-mes-md-greet1_c2 with dissolve
    $ renpy.music.set_volume(0.5, 0.0, "music")
    play music music_korean_garden
    pause
    scene e10s02-10 mc-mes-md-greet1_c4 with dissolve
    play voice4 pete_thinking_hmm2 noloop
    md "{i}*says something in language you don't understand*{/i}"
    scene e10s02-10 mc-mes-md-greet1_c3 with dissolve
    play voice3 min_yes_simple noloop
    mes "Yes, father.{w} This is the man I told you about."
    scene e10s02-10 mc-mes-md-greet1_c1 with dissolve
    play voice2 d1s1_mmm noloop
    mct "What's happening? Should I bow? Should I say something?{w} Crap. I am not prepared for this."
    play sound sfx_cloth_rustling2
    scene e10s02-12 mc-mes-md-greet3_c2 with dissolve
    pause
    scene e10s02-11 mc-mes-md-greet2_c1 with dissolve
    play voice2 d2s9_mchey noloop
    mc "Hello. My name is [mcname] Young.{w} Well, I guess in your custom I am Young [mcname]."
    scene e10s02-11 mc-mes-md-greet2_c4 with dissolve
    play voice4 pete_disappointed_ehh4 noloop
    md "{i}*speaks in a language you don't understand*{/i}"
    scene e10s02-13 mc-mes-md-talk1_c1 with dissolve
    play voice3 min_no_nah noloop
    mes "No, father. That was my ex-boyfriend. He...{w} disrespected me. I am with [mcname] now."
    scene e10s02-11 mc-mes-md-greet2_c3 with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "This is a power play."
    scene e10s02-11-2 mc-mes-md-greet2_c2 with dissolve
    mc "You're the head of a successful multinational corporation. You speak English."
    scene e10s02-16 mc-mes-md-talk4_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Moreover, you already spoke to M-"
    mc "-To your daughter. You know who I am. You're just bringing up her ex-boyfriend to amplify your own power."
    scene e10s02-16 mc-mes-md-talk4_c4 with dissolve
    play voice4 pete_happy_laugh2 noloop
    md "*laughs* Very good, [mcname]. You might not be completely useless after all."
    scene e10s02-16 mc-mes-md-talk4_c3 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "So, shall we drop these pretenses and behave like ordinary people?"
    scene e10s02-15 mc-mes-md-talk3_c4 with dissolve
    play voice4 pete_no_simple3 noloop
    md "No.{w} Please seat down. Lunch will be served."
    $ renpy.music.set_volume(0.8, 2.0, "music")
    scene black
    show screen scene_transistion(_("Some time later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.4, 2.0, "music")
    scene e10s02-20 mc-mes-md-mm-mb-talk1_c2
    with Fade(0.5, 0.5, 0.5)
    pause
    play voice4 pete_arrogant_hm2 noloop
    md "I don't believe you have met my wife nor my son."
    scene e10s02-20 mc-mes-md-mm-mb-talk1_c1 with dissolve
    play voice5 claudie_hey_simple noloop
    mm "It is a pleasure to meet you, [mcname]. Our daughter speaks highly of you."
    scene e10s02-20 mc-mes-md-mm-mb-talk1_c3 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Thank you, ma'am."
    scene e10s02-20 mc-mes-md-mm-mb-talk1_c4 with dissolve
    play voice4 boy5_hey_calm noloop
    mb "Hey [mcname]. Just call me Don."
    scene e10s02-21 mc-mes-md-nb-mm-talk1_c1 with dissolve
    play voice5 pete_angry_ehh2 noloop
    md "There is no need to be so informal."
    scene e10s02-21 mc-mes-md-nb-mm-talk1_c4 with dissolve
    play voice4 boy5_thinking_huh noloop
    mb "Relax, dad. This isn't a business deal. It's a social occasion."
    mb "During social interactions it is optimal to relax the rules and go with the flow."
    scene e10s02-21 mc-mes-md-nb-mm-talk1_c2 with dissolve
    play voice5 pete_thinking_eeh1 noloop
    md "I suppose you are right, but it does not sit well with me."
    scene e10s02-22 mc-mes-md-mb-mm-talk2_c3 with dissolve
    play voice2 d2s9_confused noloop volume 1.6
    mc "Thank you both. I agree with Do-yun, er... Don?{w} I am not yet comfortable with the formalities-"
    scene e10s02-21 mc-mes-md-nb-mm-talk1_c3 with dissolve
    play voice3 min_happy_relief noloop
    mes "I'm certain that in time [mcname] will learn - and that he will impress you, father."
    scene e10s02-22 mc-mes-md-mb-mm-talk2_c4 with dissolve
    play voice4 boy5_arrogant_hm noloop
    mb "[mcname], what do you think about the baseball season? Do you have a favorite team?"
    scene e10s02-23 mc-mes-md-mb-mm-talk3_c2 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "Um, actually I've never followed baseball...{w} I could tell you about football, but we have a few months before the season starts."
    scene e10s02-23 mc-mes-md-mb-mm-talk3_c4 with dissolve
    play voice4 boy5_disappointed_oh3 noloop
    mb "Oh."
    scene e10s02-20 mc-mes-md-mm-mb-talk1_c2 with dissolve
    play voice5 claudie_happy_mmm1 noloop
    mm "I've always been a fan of the Tigers."
    scene e10s02-20 mc-mes-md-mm-mb-talk1_c3 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "The Detroit Tigers? I've heard of them. \"Go Lions and take the Tigers with you\"."
    scene e10s02-22 mc-mes-md-mb-mm-talk2_c2 with dissolve
    play voice4 boy5_no_confident noloop
    mb "Sorry, no. Mother means the Hanshin Tigers. She's a bit obsessed with Japan."
    scene e10s02-20 mc-mes-md-mm-mb-talk1_c2 with dissolve
    play voice5 claudie_thinking_hmm2 noloop
    mm "Don't forget that you were born there, Bruce. Have you heard this story?"
    play voice2 mc_angry_huh2 noloop
    mct "Oh bother, I have the feeling I'm in for a long story about Bruce's birth..."
    $ renpy.music.set_volume(0.8, 2.0, "music")
    scene black
    show screen scene_transistion(_("Some time later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.4, 2.0, "music")
    scene e10s02-24 mc-mes-md-mb-mm-talk4_c2
    with Fade(0.5, 0.5, 0.5)
    pause
    scene e10s02-24 mc-mes-md-mb-mm-talk4_c1 with dissolve
    play voice4 pete_angry_hmm5 noloop
    md "If I may interrupt to discuss business."
    scene e10s02-25 mc-mes-md-mb-mm-talk5_c2 with dissolve
    queue voice4 pete_thinking_hmm7 noloop
    md "Daughter, you will be working at headquarters. There is a job opening that you must fill."
    scene e10s02-21 mc-mes-md-nb-mm-talk1_c3 with dissolve
    play voice3 min_yes_happy noloop
    mes "Of course, father. The summer internships start in a couple of weeks, so-"
    scene e10s02-26 mc-mes-md-mb-mm-talk6_c2 with dissolve
    play voice4 pete_no_uhuh noloop
    md "Not this time.{w} I believe that you are ready for something different"
    scene e10s02-21 mc-mes-md-nb-mm-talk1_c4 with dissolve
    play voice3 min_old_huh noloop
    mes "I don't understand-"
    play voice4 pete_yes_simple1 noloop
    md "We have discussed it and decided that you are ready for a real position. You can start tomorrow."
    scene e10s02-21 mc-mes-md-nb-mm-talk1_c3 with dissolve
    play voice3 min_scared_huh noloop
    mes "Wha-?"
    mes "What? Should I continue my education somewhere else?"
    scene e10s02-26 mc-mes-md-mb-mm-talk6_c4 with dissolve
    play voice5 boy5_thinking_hmm3 noloop
    mb "Father and I have discussed it. You may return in the autumn, but you're clearly ready to start full-time."
    play voice3 min_thinking_mhh noloop
    mes "But I don't-"
    scene e10s02-26 mc-mes-md-mb-mm-talk6_c3 with dissolve
    mes "I was supposed to-"
    play voice5 boy5_hey_active noloop
    mb "There is nothing to understand. This is a terrific opportunity."
    scene e10s02-25 mc-mes-md-mb-mm-talk5_c2 with dissolve
    play voice4 pete_happy_mmm2 noloop
    md "Your brother was initially against this - he thought you deserved a break after your studies - but neither of us want to waste your potential."
    scene e10s02-21 mc-mes-md-nb-mm-talk1_c3 with dissolve
    play voice3 min_disappointed_ehh3 noloop
    mes "Yes, father.{w} I understand."
    play voice2 mc_arrogant_huh2 noloop
    mc "Excuse me, but what the fuck?"
    scene e10s02-11 mc-mes-md-greet2_c4 with dissolve
    play voice4 pete_angry_hmm4 noloop
    mb "This is family business, [mcname].."
    scene e10s02-22 mc-mes-md-mb-mm-talk2_c1 with dissolve
    menu:
        "Ask her what she really thinks about this"(hint="e10s02m01c01"):
            $ e10s02_mes_partner = True

            scene e10s02-23 mc-mes-md-mb-mm-talk3_c3 with dissolve
            play voice2 mc_hey_hey3 noloop
            mc "Min, what do you really think about this?"
            scene e10s02-22-2 mc-mes-md-mb-mm-talk2_c2 with dissolve
            play voice3 min_pain_ah noloop
            mes "[mcname], please. Don't do this."
        "Tell them that she has other plans"(hint="e10s02m01c02"):

            scene e10s02-21 mc-mes-md-nb-mm-talk1_c3 with dissolve
            play voice2 mc_angry_hm1 noloop
            mc "She has told me she wanted to do something else."
            mc "Did it ever occur to you to ask her about her plans? About her goals?"
            scene e10s02-22-2 mc-mes-md-mb-mm-talk2_c2 with dissolve
            play voice3 min_pain_ah noloop
            mes "[mcname], please. Don't do this."

    if e10s02_mes_partner is True:
        scene e10s02-23 mc-mes-md-mb-mm-talk3_c3 with dissolve
        play voice2 mc_angry_errr2 noloop
        mc "What the hell, Min?! You're the strongest person that I know. You'd cut a birthday cake with a battle axe."
        mc "It makes no sense that someone - let alone your own flesh & blood - would disrespect your opinion and tell you-"
    elif True:
        scene e10s02-21 mc-mes-md-nb-mm-talk1_c3 with dissolve
        play voice2 mc_angry_errr2 noloop
        mc "Ask her about High Frequency Trading! Ask her about Sentimental Analysis of Social Media! Ask her about what she wants to do with her life!"
        mc "I've listened to her. I'll can tell you what Min is going to do-"
    scene e10s02-13 mc-mes-md-talk1_c4 with dissolve
    play voice4 pete_angry_argh3 noloop
    md "Enough!"
    md "You do not understand. This is our family business. \"Min\" is who we are, and Eun-Soo will follow the path I set down."
    md "Is that understood?!"
    scene e10s02-21-2 mc-mes-md-nb-mm-talk1_c3 with dissolve
    play voice3 min_yes_serious noloop
    mes "Yes, father."
    play voice5 boy5_yes_active noloop
    mb "Yes, father."
    play voice2 d3s7_mcemm noloop
    mc "..."
    scene e10s02-20 mc-mes-md-mm-mb-talk1_c2 with dissolve
    play voice4 pete_angry_hmm1 noloop
    md "It seems that the meal is finished. Our guest would not want to overstay his welcome."
    play sound sfx_cloth_rustling1
    scene e10s02-27 mes-stands-up_c1 with dissolve
    pause 0.5
    scene e10s02-28 mc-left-speechless-mes-obeys-her-father_c1 with dissolve
    mc "..."
    play voice3 min_disappointed_ehh1 noloop
    mes "Of course, father. [mcname], let's go."
    scene e10s02-29 mc-stands-up-watching-mes-says-of-course_c1 with dissolve
    pause
    scene e10s02-30 mc-makes-clear-he-wants-whats-best-for-min_c1 with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Of course."
    mc "Let me just be clear. I have your daughter's best interests at heart."
    mc "We merely disagree at what is in her best interests."
    scene e10s02-31 mc-takes-mes-hand-towards-exit-md-talks-about-apartment-salary_c1 with dissolve
    play voice4 pete_arrogant_heh2 noloop
    md "I have arranged a suitable apartment for my daughter and whomever she decides to live with her."
    play voice2 d1s5b_ehhh noloop volume 1.6
    mc "You mentioned full-time work. I assume there is a reasonable salary?"
    play voice4 pete_yes_ugu1 noloop
    md "She will have a substantial salary on paper. Of course, that will be reinvested in the company and she will receive her allowance from the family cards."
    scene e10s02-32 mc-leads-mes-outside-tells-md-its-unacceptable_c1 with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "That is unacceptable. You will track and control her home and purchases?!"
    play voice3 amrose_old_psst2 noloop
    mes "*whisper* [mcname]! Can we discuss this later?"
    scene e10s02-33 mc-understands-mc-care-for-mes-md-does-not_c1 with dissolve
    play voice5 boy5_hey_simple noloop
    mb "I'm sure we understand that - in your own way - you are trying to look out for my sister."
    play voice4 pete_no_simple3 noloop
    md "I do not."
    scene e10s02-34 mc-mes-leave-location_c1 with dissolve
    play voice4 pete_angry_cough1 noloop
    md "Stay out of our family's business, [mcname]."
    play voice3 fshhh noloop
    mes "Shh. Let's just go."

    stop sound2 fadeout 3.0
    stop music fadeout 3.0
    jump e10s03

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
