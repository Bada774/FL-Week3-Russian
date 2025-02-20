label d19s01lc:

    scene black
    show screen scene_transistion(_("Friday\nDay-19"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(1.0, 0.0, "sound2")
    play sound2 sfx_toilet_drops1 volume 2.5
    scene d19s01-01 mc-lc-prison1_c1
    with Fade(0.5, 0.5, 2.0)
    pause
    scene d19s01-01 mc-lc-prison1_c3 with dissolve
    play music music_let_me_out fadein 3.0
    play voice2 mc_disgust_booeah3 noloop
    mc "Ugh.{w} Did anyone get the number of that bus?"
    scene d19s01-01 mc-lc-prison1_c4 with dissolve
    play voice3 lydia_hmmmm noloop
    lc "Was it the 0-0-7-1?"
    scene d19s01-01 mc-lc-prison1_c2 with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "Huh?"
    $ renpy.music.set_volume(0.6, 10.0, "sound2")
    play sound sfx_metal_fence2
    scene d19s01-02 mc-lc-prison2_c2 with dissolve
    play voice2 mc_surprised_huh3 noloop
    mc "Lydia?!{w} What are you doing in jail?"
    scene d19s01-02 mc-lc-prison2_c1 with dissolve
    play voice3 lydia_haha noloop
    lc "Getting you released, silly."
    scene d19s01-03 mc-lc-prison3_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Oh.{w} Ugh, what happened to me?"
    scene d19s01-02 mc-lc-prison2_c3 with dissolve
    play voice3 lydia_thinking noloop
    lc "Unofficially, you got drunk at a cop bar and took a swing at an off-duty police officer."
    scene d19s01-03 mc-lc-prison3_c2 with dissolve
    play voice2 mc_scared_oh1 noloop
    mc "Oh, shit.{w} And officially?"
    scene d19s01-03 mc-lc-prison3_c3 with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    lc "Officially, you were never here, never there, and expected never to go back there again."
    scene d19s01-04 mc-lc-prison4_c2 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Is the cop alright?"
    scene d19s01-04 mc-lc-prison4_c1 with dissolve
    play voice3 lydia_morningoh noloop
    lc "You missed him by a mile, but it's sweet of you to ask."
    play voice2 d2s9_confused noloop volume 1.5
    mc "So, can I get out of here?"
    scene d19s01-04 mc-lc-prison4_c3 with dissolve
    play voice3 lydia_lydyes noloop
    lc "Yes, as soon as I tell them you are awake."
    scene d19s01-06 mc-lc-prison6_c2 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Thank you for that."
    mc "Um, why aren't you telling them that now?"
    scene d19s01-06 mc-lc-prison6_c1 with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    lc "*sigh* Because we need to talk.{w} Then we're going to change places."
    scene d19s01-07 mc-lc-prison7_c2 with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What does that mean? I don't understand."
    scene d19s01-07 mc-lc-prison7_c1 with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    lc "You're probably still too hungover to remember, but..."
    lc "Why did you get smashed drunk in a random bar last night?"
    scene d19s01-08 mc-lc-prison8_c2 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "I was angry about something..."
    mc "It seemed really important..."
    scene d19s01-09-3 mc-lc-talk2_c2 with dissolve
    play voice2 mc_pain_ou1 noloop
    mc "OH."
    scene d19s01-09 mc-lc-prison9_c1 with dissolve
    play voice3 lydia_moan1 noloop
    lc "Yeah. OH."
    scene d19s01-09-2 mc-lc-talk1_c2 with dissolve
    play voice2 mc_pain_mff2 noloop
    mc "You-"
    scene d19s01-09-2 mc-lc-talk1_c1 with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    lc "Yeah, I did.{w} It was all me.{w} It was always me."
    scene d19s01-08 mc-lc-prison8_c2 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "I don't understand.{w} How could you-"
    scene d19s01-08 mc-lc-prison8_c1 with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    lc "It just seemed like a fun idea."
    scene d19s01-09-6 mc-lc-talk5_c2 with dissolve
    play voice2 mc_angry_errr4 noloop
    if is_antagonist_mode is False:
        mc "Fetish Locator?{w} The VIP Program!{w} You've been manipulating me since the beginning?!"
    else:
        mc "Fetish Locator?{w} The Retention Program!{w} Blackmailing people was fun for you?!"
    scene d19s01-09-6 mc-lc-talk5_c1 with dissolve
    play voice3 dahlia_no_high2 noloop
    lc "No!{w} I didn't know anything about that until yesterday!"
    scene d19s01-09-5 mc-lc-talk4_c2 with dissolve
    play voice2 mc_angry_huh2 noloop
    mc "You just said-"
    scene d19s01-09-5 mc-lc-talk4_c1 with dissolve
    play voice3 lydia_lydiahey noloop
    lc "Fetish Locator was my idea. It was my dream!"
    if is_antagonist_mode is False:
        lc "I didn't know it would start a VIP Program or promise one million dollars!!! I just thought it would be something fun and sexy!"
    else:
        lc "I didn't know it would blackmail people!!! I just thought it would be something fun and sexy!"
    scene d19s01-09-3 mc-lc-talk2_c2 with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Hold on.{w} I'm still a little drunk. I'm a lot hungover. And I'm ANGRY."
    mc "Can we talk this over after breakfast or something?"
    scene d19s01-09-4 mc-lc-talk3_c1 with dissolve
    play voice3 lydia_oof noloop
    lc "I can't.{w} This is the only way I can guarantee that you'll listen to me."
    scene d19s01-09-7 mc-lc-talk6_c2 with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "So, you are literally holding me prisoner-"
    scene d19s01-09-7 mc-lc-talk6_c1 with dissolve
    play voice3 dahlia_thinking_mmm2 noloop
    lc "I'm sorry.{w} I just need to explain this to you. It can't wait and I can't let you go just yet."
    scene d19s01-09-6 mc-lc-talk5_c2 with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "*sigh* Lovely. I guess we're past the point of trusting each other."
    scene d19s01-09-12 mc-lc-talk11_c1 with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    lc "[mcname]..."
    scene d19s01-09-8 mc-lc-talk7_c2 with dissolve
    play voice2 mc_no_no5 noloop
    mc "No. Go ahead.{w} I'm your captive audience."
    scene d19s01-09-8 mc-lc-talk7_c1 with dissolve
    play voice3 lydia_moan1 noloop
    lc "*sigh* Fetish Locator was a dream of mine."
    lc "It was a way to deal with my, ya'know, sexual desires yet intimacy issues."
    lc "To create a sex app that people would want to play - and they would provide me with an unfathomable wealth of..."
    scene d19s01-09 mc-lc-prison9_c2 with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Of amateur porn for you to fap off to?"
    scene d19s01-09-8 mc-lc-talk7_c1 with dissolve
    play voice3 lydia_hmmmm noloop
    lc "Of vicarious experiences."
    lc "I could watch and learn and experience without being involved."
    scene d19s01-09-12 mc-lc-talk11_c1 with dissolve
    lc "I know it sounds ridiculous, but no one was supposed to get hurt."
    lc "It never even occurred to me that anyone could get harmed by this. Jerome told me it was all secure and encrypted and 100%% safe."
    scene d19s01-09-3 mc-lc-talk2_c2 with dissolve
    play voice2 d9s5_auch2 noloop
    mc "JEROME?!{w} What did that asshole have to do with this?"
    scene d19s01-12 lc-talk2_c1 with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    lc "I'm not a tech genius. I struggle posting videos online. I needed an expert techie to make the site."
    lc "Jerome was someone I thought I could trust."
    scene d19s01-09-8 mc-lc-talk7_c2 with dissolve
    play voice2 mc_angry_hm1 noloop
    if is_antagonist_mode is False:
        mc "So, Jerome's behind all this?{w} I can break him."
    else:
        mc "So, Jerome's the one blackmailing people?{w} I can break him."
    scene d19s01-07 mc-lc-prison7_c1 with dissolve
    play voice3 dahlia_no_high3 noloop
    lc "Um... no..."
    lc "Ridley is."
    scene d19s01-09-2 mc-lc-talk1_c2 with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Ridley? Who's Ridley?"
    scene d19s01-09-2 mc-lc-talk1_c1 with dissolve
    lc "Ridley is the artificial intelligence that Jerome created."
    scene d19s01-09 mc-lc-prison9_c2 with dissolve
    play voice2 d3s7_mcemm noloop volume 1.6
    mc "...{w} what?"
    scene d19s01-09-3 mc-lc-talk2_c1 with dissolve
    play voice3 lydia_hmmmm noloop
    lc "Ridley. Like Ridley Scott.{w} Jerome is obsessed with everything Aliens and wanted to name it Ripley, but decided the A.I. should be a guy-"
    scene d19s01-09-7 mc-lc-talk6_c2 with dissolve
    play voice2 d2s12_emmm noloop volume 1.3
    mc "He created an A.I.?{w} Is that even possible?"
    scene d19s01-09-4 mc-lc-talk3_c1 with dissolve
    play voice3 lydia_aga noloop
    lc "I mean, that's what he called it. It wouldn't pass as a human, but it runs the app."
    scene d19s01-06 mc-lc-prison6_c2 with dissolve
    play voice2 mc_angry_errr1 noloop
    mc "I'm...{w} I'm so confused and angry right now I don't know what to do with myself."
    scene d19s01-09-5 mc-lc-talk4_c1 with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    lc "Then just listen."
    scene d19s01-04 mc-lc-prison4_c2 with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "This is ridiculous! You're telling me that Fetish Locator is some sort of HAL 9000 of sex and smut!!!"
    scene d19s01-09-6 mc-lc-talk5_c1 with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    lc "Well, kinda.{w} I mean, it would probably be easy to fix if Jerome hadn't disappeared."
    play sound sfx_metal_fence1
    scene d19s01-06 mc-lc-prison6_c2 with dissolve
    play voice2 mc_angry_errr2 noloop
    mc "Where is that fucker?! I'll kill him!{w} Then I'll drag him back from Hell so he can fix this Ridley bullshit."
    scene d19s01-09-7 mc-lc-talk6_c1 with dissolve
    play voice3 lydia_morningoh noloop
    lc "No idea.{w} Nobody has seen him in about a week."
    scene d19s01-07 mc-lc-prison7_c2 with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "Bullshit! He was at Min's Party harassing the bartender!"
    play voice3 dahlia_yes_ugu noloop volume 0.75
    scene d19s01-04 mc-lc-prison4_c3 with dissolve
    lc "That was a week ago.{w} Nobody has seen him since then."
    scene d19s01-03 mc-lc-prison3_c1 with dissolve
    play voice2 d1s1_mmm noloop
    mct "Min joked like she was going to kill him after that."
    mct "That was a joke, right?"
    scene d19s01-03 mc-lc-prison3_c3 with dissolve
    play voice3 lydia_oof noloop
    lc "Love, [mcname], please. I need you to calm down and focus."
    scene d19s01-08 mc-lc-prison8_c2 with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.6
    mc "Why?"
    scene d19s01-09-16 mc-lc-talk15_c1 with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    lc "Because I need you.{w}.. I need you to listen."
    scene d19s01-04 mc-lc-prison4_c2 with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "Fine. So, you had this dream."
    if is_antagonist_mode is False:
        mc "Jerome built a BISHOP and it got out of control..."
    else:
        mc "Jerome built a BISHOP and it started blackmailing people..."
    scene d19s01-04 mc-lc-prison4_c3 with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    lc "I think it was just programmed to obtain sexy content for me, and it is doing that too well."
    scene d19s01-07 mc-lc-prison7_c2 with dissolve
    play voice2 mc_angry_errr3 noloop
    if is_antagonist_mode is False:
        mc "Jerome is and was an asshole.{w} I assume he created the VIP Program to hurt you for rejecting his advances."
    else:
        mc "Jerome is and was an asshole.{w} I assume blackmailing people was always part of his plan."
    scene d19s01-08 mc-lc-prison8_c1 with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    lc "Maybe."
    play voice2 mc_angry_hm2 noloop
    mc "Is that all?"
    scene d19s01-09-15 mc-lc-talk14_c1 with dissolve
    play voice3 dahlia_thinking_mmm2 noloop
    lc "...?"
    scene d19s01-09-6 mc-lc-talk5_c2 with dissolve
    play voice2 mc_arrogant_hm2 noloop
    mc "You wanted me to listen. Is that everything you had to say?"
    scene d19s01-11 lc-talk1_c1 with dissolve
    play voice3 lydia_lydyes noloop
    lc "I mean, I guess so."
    scene d19s01-04 mc-lc-prison4_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Alright then."
    scene d19s01-03 mc-lc-prison3_c3 with dissolve
    play voice3 lydia_moan1 noloop
    lc "[mcname], can you ever forgive me?"
    scene d19s01-08 mc-lc-prison8_c2 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "Maybe.{w} Maybe when you're not keeping me in a jail cell."
    scene d19s01-02 mc-lc-prison2_c3 with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop volume 0.75
    lc "I see.{w} Well, I guess there's just one thing left for me to do."
    scene d19s01-09-5 mc-lc-talk4_c2 with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Have the cops release me?"
    scene d19s01-13 lc-talk3_c1 with dissolve
    play voice3 daisy_ugu noloop
    lc "Well, that.{w} And turning myself in."
    scene d19s01-09-7 mc-lc-talk6_c2 with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "What are you talking about?"
    scene d19s01-09-14 mc-lc-talk13_c1 with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    if is_antagonist_mode is False:
        lc "People are being lied to, and ultimately I am responsible."
    else:
        lc "People got hurt. People are being blackmailed. I'm responsible."
    play voice2 mc_yes_sure1 noloop
    mc "Ethically, sure. But legally, Jerome did all that."
    scene d19s01-09-16 mc-lc-talk15_c1 with dissolve
    play voice3 lydia_uhuh noloop
    lc "I'm responsible."
    scene d19s01-04 mc-lc-prison4_c1 with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "I don't understand."
    scene d19s01-09-10 mc-lc-talk9_c1 with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    lc "It's just something I need to do."
    play sound sfx_metal_fence2
    scene d19s01-06 mc-lc-prison6_c2 with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "Lydia! Wait!"
    scene d19s01-09-15 mc-lc-talk14_c1 with dissolve
    lc "...?"
    menu:
        "Kiss Her"(hint="d19s01lcm01c01") if d16s03_love_lc is True or love_lc is True:
            $ d19s01lc_kiss = True

            play voice2 d1s5b_ehhh noloop volume 1.7
            mc "I Still Love You."
            play sound maria_kiss1
            scene d19s01-10 mc-lc-kiss_c1 with dissolve
            pause
            queue sound maria_kiss3
            play voice3 dahlia_sex_closedmoan1 noloop
            scene d19s01-10 mc-lc-kiss_c2 with dissolve
            pause
            queue sound maria_kiss2
            scene d19s01-10 mc-lc-kiss_c3 with dissolve
            pause
            scene d19s01-09 mc-lc-prison9_c2 with dissolve
            play voice2 mc_yes_yeah1 noloop
            mc "I don't care what you've done."
            mc "I don't care what you do."
            mc "You'll always be my girl."
            play voice3 lydia_huh2 noloop
            scene d19s01-19 lc-talk9_c1 with dissolve
            lc "Thank you."
            lc "I love you too."
            lc "But I have to do this."
            scene d19s01-09 mc-lc-prison9_c2 with dissolve
            play voice2 mc_thinking_mmm5 noloop
            mc "I understand."
        "Say Something Nice"(hint="d19s01lcm01c02"):

            $ d19s01lc_talk_nice = True

            scene d19s01-09 mc-lc-prison9_c2 with dissolve
            play voice2 d1s5b_ehhh noloop volume 1.7
            if is_antagonist_mode is False:
                mc "I didn't like being lied to, but..."
            else:
                mc "I didn't like the blackmail, but..."
            play voice3 lydia_thinking noloop
            lc "Yes?"
            mc "I enjoyed the app. I enjoyed the game."
            scene d19s01-15 lc-talk5_c1 with dissolve
            play voice3 lydia_laugh noloop
            lc "At least there's that, I guess."
            play voice2 mc_hey_hey2 noloop
            mc "And I loved every moment I spent with you."
            scene d19s01-14 lc-talk4_c1 with dissolve
            play voice3 lydia_morningoh noloop
            lc "Thanks. Me too."
            scene d19s01-09 mc-lc-prison9_c2 with dissolve
            play voice2 mc_yes_yeah4 noloop
        "Tell Her It Was Fun"(hint="d19s01lcm01c03"):

            $ d19s01lc_was_fun = True

            scene d19s01-09-7 mc-lc-talk6_c2 with dissolve
            play voice2 mc_arrogant_heh1 noloop
            mc "It was fun, once."
            scene d19s01-16 lc-talk6_c1 with dissolve
            play voice3 lydia_thinking noloop
            lc "What's that?"
            scene d19s01-09 mc-lc-prison9_c2 with dissolve
            play voice2 mc_arrogant_hm3 noloop
            if is_antagonist_mode is False:
                mc "Fetish Locator - it was fun, once.{w} Before... ya'know."
            else:
                mc "Fetish Locator - it was fun, once.{w} Before the blackmail."
            scene d19s01-14 lc-talk4_c1 with dissolve
            play voice3 lydia_laugh noloop
            lc "Well, at least there is that."
            scene d19s01-09 mc-lc-prison9_c2 with dissolve
            play voice2 mc_yes_yeah4 noloop

    mc "Just don't forget about me."
    scene d19s01-12 lc-talk2_c1 with dissolve
    play voice3 lydia_aga noloop
    lc "I'll have them release you in a jiffy."
    play voice2 mc_thinking_mmm4 noloop
    mc "That isn't what I meant."
    lc "I know."

    stop music fadeout 3.5
    stop sound2 fadeout 2.5
    jump d19s02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
