image d16s03-a1 = Movie(play = "images/Day-16/Scene-03/anim/d16s03-a1-2x-50fps.webm", start_image = "d16s03-00-a1 mc-lc-sex-anim-1-01_i")
image d16s03-a2 = Movie(play = "images/Day-16/Scene-03/anim/d16s03-a2-2x-50fps.webm", start_image = "d16s03-00-a2 mc-lc-sex-anim-2-01_i")
image d16s03-a3 = Movie(play = "images/Day-16/Scene-03/anim/d16s03-a3-2x-50fps.webm", start_image = "d16s03-00-a3 mc-lc-sex-anim-3-01_i")
image d16s03-glambot = Movie(play = "images/Day-16/Scene-03/anim/d16s03-a0-2x-50fps.webm", start_image = "d16s03-97-01-a0 mc-lc-sit-up-talk-alt-pose-5-glambot-0-000_i", image = "d16s03-97-01-a0 mc-lc-sit-up-talk-alt-pose-5-glambot-0-236_i", loop = False)

label replay_d16s03:
label d16s03:

    $ d16s03_lie_to_lc = False
    $ d16s03_arj_watch = False
    $ d16s03_refuse_lc = False
    $ d16s03_agree_to_lc = False
    $ d16s03_darkest_fantasy = None
    $ d16s03_love_lc = False
    $ d16s03_points = 0

    if _in_replay:
        $ renpy.music.set_volume(0.7, 1.0, "music")
        play music saxophone_sexy2_stereo
    scene d16s03-01 lc-talk-mc-c1 with fade
    play voice3 lydia_hmmmm noloop
    lc "[mcname], are you still wearing your penis cage?"
    scene d16s03-01 lc-talk-mc-c2 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yep."
    play voice3 lydia_haha noloop
    lc "Cool! You can come up."
    scene d16s03-02 mc-poke-head with dissolve
    pause
    $ renpy.music.set_volume(1.0, 3.0, "music")
    play sound sfx_door_closed8 volume 3.0
    scene d16s03-03 mc-lc-amr-enter-room with dissolve
    play voice3 lydia_lydiahey noloop
    lc "Hey lover!"
    play voice2 d1s1_mmm noloop
    scene d16s03-04 mc-lc-amr-walk-up-to-mc with dissolve
    pause
    play sound maria_kiss2
    scene d16s03-05 mc-lc-kiss with dissolve
    pause
    if d16s02_arj_eatout is True:
        scene d16s03-06 mc-lc-taste-in-mouth with dissolve
        play voice3 lydia_thinking noloop
        lc "Mmmmm... {w}What is that taste?"
        scene d16s03-08 mc-lc-talk-after-choice with dissolve
        play voice2 mc_thinking_mmm1 noloop
        mc "All I taste is your beautiful lips."
        play voice3 dahlia_disappointed_hmm1 noloop
        lc "I meant the taste on your lips. I can't quite place it."
        play voice2 mc_surprised_huh4 noloop
        scene d16s03-09 mc-lc-amr-talk-look-at-amr with dissolve
        mct "Oh fuck, she can taste AmRose's pussy juices on my mouth."
        menu:
            "Tell the Truth"(hint="d16s03m01c01") if True:
                play voice2 mc_thinking_oh1 noloop
                mc "Oh, that would be AmRose."
                scene d16s03-10 mc-lc-amr-talk-variation-lc-turn with dissolve
                pause
                scene d16s03-10-02 mc-lc-amr-talk-variation-lc-turn with dissolve
                play voice3 lydia_morningoh noloop
                lc "Oh?"
                play voice4 amrose_happy_laugh3 noloop
                scene d16s03-11 mc-lc-amr-talk-variation-amr-focus with dissolve
                pause
                scene d16s03-11-02 mc-lc-amr-talk-variation-amr-focus with dissolve
                play voice4 amrose_yes_yeah1 noloop
                arj "He was just eating me out downstairs."
                scene d16s03-12 mc-lc-amr-talk-group-camera1 with dissolve
                play voice3 lydia_moan1 noloop
                lc "Damn. I wish I had seen that."
            "Lie About It"(hint="d16s03m01c02") if True:


                $ d16s03_lie_to_lc = True

                play voice2 mc_thinking_oh1 noloop
                mc "Oh, I'm sorry. I didn't brush my teeth this morning. My breath must taste terrible."
                scene d16s03-11-02 mc-lc-amr-talk-variation-amr-focus with dissolve
                play voice4 amrose_surprised_oh3 noloop
                arj "Oh, REALLY???"
                scene d16s03-08 mc-lc-talk-after-choice with dissolve
                play voice3 lydia_hmmmm noloop
                lc "Weird. It tastes like transmission fluid."
                play voice2 mc_surprised_what1 noloop
                mc "What?"
                lc "Transmission fluid."
                scene d16s03-13 mc-lc-amr-talk-amr-group-camera2 with dissolve
                play voice4 amrose_surprised_uh3 noloop
                arj "Why would you know what that tastes like?"
                scene d16s03-12 mc-lc-amr-talk-group-camera1 with dissolve
                play voice3 lydia_morningoh noloop
                lc "I tried to change my own oil once. {w}It didn't go well."
                scene d16s03-14 mc-lc-amr-talk-mc-group-camera3 with dissolve
                play voice2 mc_arrogant_heh3 noloop
                mc "Sounds like it."
    elif True:
        scene d16s03-07 mc-lc-tasty with dissolve
        play voice3 dahlia_happy_hmm1 noloop
        lc "Mmmmm... tasty."
        scene d16s03-08 mc-lc-talk-after-choice with dissolve
        play voice2 mc_yes_yeah1 noloop
        mc "You too."
        lc "Thanks!"

    scene d16s03-15-02 mc-lc-amr-talk-mc-pov with dissolve
    play voice3 lydia_thinking noloop
    lc "Are you okay? I couldn't reach you last night. You always call."
    scene d16s03-15 mc-lc-amr-talk-mc-pov with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Oh, yeah. Um, my phone kinda died. I didn't get it working again until this morning."
    scene d16s03-15-02 mc-lc-amr-talk-mc-pov with dissolve
    lc "Really? {w}Why does it sound like you're being awfully cagey with the truth?"
    scene d16s03-13-02 mc-lc-amr-talk-amr-group-camera2 with dissolve
    play voice4 amrose_thinking_emm noloop
    arj "He's just trying to spare you the details. It didn't die, we were just visiting someplace that... couldn't get a signal."
    scene d16s03-15-02 mc-lc-amr-talk-mc-pov with dissolve
    play voice3 lydia_morningoh noloop
    lc "Oh. You spent the night in a dark tunnel or something like that?"
    scene d16s03-14-02 mc-lc-amr-talk-mc-group-camera4 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "Something like that."
    scene d16s03-15-02 mc-lc-amr-talk-mc-pov with dissolve
    play voice4 dahlia_thinking_mmm1 noloop
    lc "Mysterious. {w}Promise to tell me sometime?"
    scene d16s03-15 mc-lc-amr-talk-mc-pov with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "Definitely."
    scene d16s03-15-02 mc-lc-amr-talk-mc-pov with dissolve
    lc "Fair enough. Next time, could you warn me ahead of time? I was up half the night worried about what happened to you."
    scene d16s03-17 mc-lc-amr-we-can with dissolve
    play voice2 d1s5b_ehhh noloop
    if love_lc is True:
        mc "I'm so sorry, love. It didn't even occur to me."
        mc "I'll make sure to tell you if that happens again."
    elif True:
        mc "Sure. That shouldn't be a problem."
    scene d16s03-16 mc-lc-can-we-talk-infront-of-her with dissolve
    play voice3 dahlia_thinking_mmm2 noloop
    lc "Um, can we talk in front of her?"
    scene d16s03-17 mc-lc-amr-we-can with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sure. AmRose is one of my closest friends."
    scene d16s03-18 mc-lc-amr-down-there with dissolve
    play voice3 lydia_haha noloop
    lc "So, I was hoping to take advantage of your little... situation."
    mc "I think you mentioned that. Something about my being caged is a turn-on for you?"
    scene d16s03-19 mc-lc-talk-excited with dissolve
    lc "You're the ultimate turn on. {w}You being caged just ... safe? comfortable? Do you know what I mean?"
    scene d16s03-20 mc-lc-amr-talk-sad with dissolve
    play voice4 amrose_old_huh noloop
    arj "You want to fuck him, but you don't want him to be able to fuck you."
    scene d16s03-12 mc-lc-amr-talk-group-camera1 with dissolve
    play voice3 lydia_lydyes noloop
    lc "Exactly! It's still really early. We have a lot of time before classes start, right? So, I was thinking..."
    scene d16s03-20 mc-lc-amr-talk-sad with dissolve
    play voice4 amrose_happy_mmm noloop
    arj "You want to fuck him every way possible..."
    scene d16s03-12 mc-lc-amr-talk-group-camera1 with dissolve
    play voice3 lydia_aga noloop
    lc "... without actually penetrating each other. Yeah!"
    scene d16s03-21 mc-lc-amr-talk-sad-02 with dissolve
    play voice4 amrose_disappointed_ehh2 noloop
    arj "I get it. I guess I'll leave you two alone."
    scene d16s03-12 mc-lc-amr-talk-group-camera1 with dissolve
    play voice3 lydia_oof noloop
    lc "Sorry about that. I didn't expect you to be here."
    scene d16s03-22 mc-lc-amr-mc-make-choice-thoughts with dissolve
    play voice2 d1s5_mcthinks noloop
    mct "Lydia wants me to fuck her every way that doesn't involve fucking."
    mct "They both want AmRose to leave.{w} Hmm... I'm thinking..."
    menu:
        "Refuse Lydia's Request"(hint="d16s03m02c01") if True:

            $ d16s03_refuse_lc = True
            $ d16s03_arj_watch = False
            $ love_lc = False

            $ renpy.music.set_volume(0.4, 8.0, "music")
            scene d16s03-18 mc-lc-amr-down-there with dissolve
            play voice2 mc_disappointed_off1 noloop
            mc "I would love to, but I've really got to get ready for class."
            play voice4 amrose_surprised_huh2 noloop
            arj "You do?"
            play voice3 lydia_ah noloop
            lc "Oh?"
            scene d16s03-17 mc-lc-amr-we-can with dissolve
            play voice2 mc_disappointed_ehh1 noloop
            mc "It's just that it's finals week. I've been trying to study as much as possible."
            scene d16s03-19 mc-lc-talk-excited with dissolve
            play voice3 dahlia_thinking_oh noloop
            lc "Oh, I guess that's smart."
            scene d16s03-18 mc-lc-amr-down-there with dissolve
            play voice2 mc_thinking_hmm4 noloop
            mc "We can do this some other time. There's no rush."
            play voice3 dahlia_yes_ugu noloop
            lc "You're right. When you get that one off I can buy you a new one, and I can keep the key to it."
            play voice2 mc_surprised_what2 noloop
            mc "What?"
            scene d16s03-15-02 mc-lc-amr-talk-mc-pov with dissolve
            play voice3 lydia_haha noloop
            lc "Only while we're having sex, you know? You wouldn't have to wear it all day or anything like that."
            scene d16s03-15 mc-lc-amr-talk-mc-pov with dissolve
            play voice2 mc_thinking_mmm5 noloop
            mc "Um, sure. Sounds like fun."
            scene d16s03-15-02 mc-lc-amr-talk-mc-pov with dissolve
            play voice3 lydia_hmmmm noloop
            lc "Okay. Well, I guess you two had better get going."
            scene d16s03-23 mc-lc-amr-mc-goodbye with dissolve
            play voice4 amrose_yes_yeah2 noloop
            arj "I'll try to keep him free from distractions and keep him hard... at work on his studying."
            lc "Thanks!"

            $ renpy.end_replay()
            stop music fadeout 4.0
            jump d16s04
        "Agree & Want AmRose to Watch"(hint="d16s03m02c02") if True:


            $ d16s03_refuse_lc = False
            $ d16s03_arj_watch = True
            $ d16s03_points = 15

            $ renpy.music.set_volume(0.4, 8.0, "music")
            scene d16s03-18 mc-lc-amr-down-there with dissolve
            play voice2 mc_thinking_emm1 noloop
            mc "Actually, I have an idea."
            play voice3 dahlia_thinking_hmm4 noloop
            lc "What's that?"
            scene d16s03-17 mc-lc-amr-we-can with dissolve
            play voice2 mc_happy_a1 noloop
            mc "A little something to spice things up."
            mc "AmRose - why don't you stay here and watch."
            play voice4 amrose_surprised_huh3 noloop
            if date_arj_romance is True:
                scene d16s03-21 mc-lc-amr-talk-sad-02 with dissolve
                arj "Why?"
            elif True:
                scene d16s03-15-02 mc-lc-amr-talk-mc-pov with dissolve
                lc "Why?"
            play voice2 mc_thinking_hmm5 noloop
            mc "Two reasons."
            scene d16s03-14 mc-lc-amr-talk-mc-group-camera3 with dissolve
            mc "First, Lydia likes to hear about my sex stories and even watch. I want you to experience what it feels like to be watched."
            mc "Second, it would be good for AmRose. It would help you to get past your jealousy and accept my relationship with Lydia."
            scene d16s03-19 mc-lc-talk-excited with dissolve
            play voice3 lydia_haha noloop
            lc "Huh. Okay, I can agree to that."
            scene d16s03-11-02 mc-lc-amr-talk-variation-amr-focus with dissolve
            play voice4 amrose_thinking_hmm3 noloop
            if date_arj_romance is True:
                arj "I guess I can try this.{w}.. for you."
                mc "Thanks."
            elif True:
                arj "Okay, sir. If that's what you want."
            stop music fadeout 4.0
            scene d16s03-30 mc-lc-amr-take-off-clothes-with-amr with dissolve
        "Agree & Ask AmRose to Leave"(hint="d16s03m02c03") if True:


            $ d16s03_refuse_lc = False
            $ d16s03_arj_watch = False
            $ d16s03_points = 12

            $ renpy.music.set_volume(0.4, 8.0, "music")
            scene d16s03-21 mc-lc-amr-talk-sad-02 with dissolve
            play voice2 mc_arrogant_hm1 noloop
            mc "AmRose, um, could I meet you at class?"
            play voice4 daisy_ugu noloop
            arj "Sure, we've got plenty of time."
            scene d16s03-12 mc-lc-amr-talk-group-camera1 with dissolve
            play voice3 lydia_lydiahey noloop
            lc "I'll try not to keep him too long."
            scene d16s03-21 mc-lc-amr-talk-sad-02 with dissolve
            play voice4 amrose_yes_okay2 noloop
            arj "Okay. Just remember that it is finals week."
            play voice2 mc_yes_yeah6 noloop
            mc "Anything said today will certainly be on the test. Yeah."
            scene d16s03-23 mc-lc-amr-mc-goodbye with dissolve
            play voice4 amrose_arrogant_hmm2 noloop
            arj "I'll take detailed notes if you are late."
            play voice2 d9s2_ugu noloop
            mc "Thanks."
            play sound sfx_door_openclosed2
            stop music fadeout 4.0
            scene d16s03-30-02 mc-lc-amr-take-off-clothes-without-amr with dissolve

    queue music deep_romance2
    play voice3 lydia_moan1 noloop
    lc "Let's get these clothes off. I want to explore every inch of you."
    $ renpy.music.set_volume(0.8, 8.0, "music")
    play sound ["<silence 0.3>", sfx_cloth_rustling2]
    scene d16s03-31 mc-lc-lay-down-lc-talk with fade
    play voice3 dahlia_thinking_hmm4 noloop
    lc "Lay down on the bed. I want to start with your back."
    if cage_ntr is True:
        scene d16s03-33 mc-lc-massage-close-up-talk with dissolve
        play voice3 dahlia_arrogant_hm noloop
        lc "You look like a cut of fuckable meat. Are you?"
        play voice2 mc_surprised_what3 noloop
        mc "What?!"
        scene d16s03-32 mc-lc-massage-set-up with dissolve
        play voice3 dahlia_disappointed_ehh3 noloop
        lc "Sorry, just a line I heard somewhere. I wanted to try it out."
        play voice2 mc_scared_oh1 noloop
        mc "Oh, okay."
    if d16s03_arj_watch is True:
        scene d16s03-52 amr-turned-on with dissolve
        pause
    scene d16s03-33 mc-lc-massage-close-up-talk with dissolve
    play voice3 stacy_smell noloop
    lc "You smell delicious"
    lc "Do you work out?"
    play voice2 mc_arrogant_huh3 noloop
    mc "Not today, but sure, yeah. I mean, I exercise."
    scene d16s03-34 mc-lc-massage-talk-near-rear with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    lc "You've got the perfect body."
    lc "The ideal man."
    lc "My ideal man."


    $ Lovense.stop()

    scene d16s03-36 mc-lc-massage-butt with dissolve
    $ Lovense.vibrate(1)
    play voice3 lydia_huh2 noloop
    lc "You have an amazing butt."
    mc "Thank you."
    play voice3 amrose_angry_argh2 noloop
    scene d16s03-35 mc-lc-massage-bite with dissolve
    pause
    $ Lovense.vibrate(3)
    scene d16s03-37 mc-lc-after-bite-ouch with dissolve
    play voice2 mc_pain_ou1 noloop
    mc "Ow! {w}Ohhhh... that actually feels good."
    play voice3 dahlia_thinking_hmm2 noloop
    lc "I could just eat you all up."
    scene d16s03-38 mc-lc-after-bite-not-bad with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "I'd be happy to let you."
    $ Lovense.vibrate(1)
    scene d16s03-34 mc-lc-massage-talk-near-rear with dissolve
    play voice3 lydia_hmmmm noloop
    lc "I would ask you to roll over, but I'm afraid I would bury my head in your sensitive parts and make you painfully uncomfortable."
    scene d16s03-38 mc-lc-after-bite-not-bad with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "I'm already hurting from this cage."
    if d16s03_arj_watch is False:
        scene d16s03-39-01 mc-lc-talk-after-bite-no-amr with dissolve
    elif True:
        scene d16s03-41 mc-lc-talk-oh-my with dissolve
    lc "Shall we change places?"
    play voice2 mc_yes_sure1 noloop
    mc "Sure, but why don't you start face-up?"
    scene d16s03-40 mc-lc-talk-turn-over with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    lc "You sure?"
    play voice2 mc_yes_ugu1 noloop
    mc "I want to stimulate your most sensitive parts."
    scene d16s03-41 mc-lc-talk-oh-my with dissolve
    play voice3 lydia_oops noloop
    lc "Oh my."
    play sound sfx_cloth_rustling4
    $ Lovense.vibrate(3)
    scene d16s03-42 mc-lc-hold-breast-c3 with dissolve
    play voice3 dahlia_sex_closedmoan2 noloop
    lc "That feels amazing."
    lc "I'm so conflicted. {w}You have the most glorious penis in all mankind, yet it frightens me so."
    play voice2 mc_thinking_hmm4 noloop
    mc "Why's that?"
    scene d16s03-00-a1 mc-lc-sex-anim-1-01_i with dissolve
    play voice3 lydia_orgasm2 noloop
    lc "It's like alcohol to an alcoholic, heroin to a junkie, cocaine to a crack addict."
    play voice2 d14s19_lc_licking noloop
    play voice3 ["<silence 0.3>", dahlia_sex_closedmoan1, "<silence 1.3>", dahlia_sex_closedmoan2, "<silence 1.3>", dahlia_sex_closedmoan3, "<silence 1.3>", dahlia_sex_closedmoan4, "<silence 1.3>", dahlia_sex_closedmoan5, "<silence 1.0>"]
    $ Lovense.vibrate(5)
    scene d16s03-a1
    lc "I am so frightened that I would abandon everything for your penis."
    lc "I would do anything for just another look, another touch, another taste of your cock."
    lc "I would abandon everything else and spend my life worshiping your hard manmeat."
    lc "I'd fuck you until we both died of hunger and thirst."
    scene d16s03-00-a2 mc-lc-sex-anim-2-01_i with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "You can trust me. {w}I'll make sure we always eat and stay hydrated."
    play voice2 d14s19_lc_licking noloop
    play voice3 lydia_orgasm3 noloop
    queue voice3 ["<silence 0.3>", dahlia_sex_closedmoan1, "<silence 1.3>", dahlia_sex_closedmoan2, "<silence 1.3>", dahlia_sex_closedmoan3, "<silence 1.3>", dahlia_sex_closedmoan4, "<silence 1.3>", dahlia_sex_closedmoan5, "<silence 1.0>"]
    scene d16s03-a2
    if cage_ntr is False:
        lc "I want to trust you so much."
    elif True:
        lc "I want you to fuck me so much right now."
        lc "I want to grab you by the cage and shove the whole damn thing inside me."






    lc "I'll go down on any woman you want if you just fuck me now."
    scene d16s03-00-a3 mc-lc-sex-anim-3-01_i with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "I'm afraid I have a different idea in mind."
    play voice2 d14s19_lc_licking noloop
    play voice3 ["<silence 0.3>", dahlia_sex_closedmoan1, "<silence 1.3>", dahlia_sex_closedmoan2, "<silence 1.3>", dahlia_sex_closedmoan3, "<silence 1.3>", dahlia_sex_closedmoan4, "<silence 1.3>", dahlia_sex_closedmoan5, "<silence 1.0>"]
    scene d16s03-a3
    lc "Your tongue is amazing."
    lc "I can't wait to feel your hard cock deep inside me."
    pause

    if d16s03_arj_watch is True:
        $ renpy.music.set_pan(-0.8, 1.5, "voice3")
        $ renpy.music.set_pan(-0.8, 1.5, "voice2")
        play voice4 amrose_old_moaning2
        scene d16s03-53 amr-turned-on-masturbate with dissolve
        pause
        play voice4 amrose_old_orgasming noloop
        $ Lovense.vibrate(7)
        scene d16s03-54 amr-turned-on-masturbate-cum with vpunch
        pause
        $ renpy.music.set_pan(0.0, 1.0, "voice3")
        $ renpy.music.set_pan(0.0, 1.0, "voice2")
        $ renpy.music.set_volume(0.6, 1.0, "voice3")
        $ renpy.music.set_volume(0.6, 1.0, "voice2")
        scene d16s03-51 mc-lc-amr-watching-afar with hpunch
        pause
        stop voice4 fadeout 2.5
    $ renpy.music.set_volume(1.0, 1.0, "voice3")
    $ renpy.music.set_volume(1.0, 1.0, "voice2")
    play voice3 lydia_orgasm1 noloop
    play voice2 d1s5_orgasm2 noloop
    $ Lovense.vibrate(7)
    scene d16s03-50 mc-lc-pussy-eating with hpunch
    lc "Ohhhh yesssss..."
    $ Lovense.vibrate(1)
    $ renpy.end_replay()

    if d16s03_arj_watch is True and cage_ntr is False:
        scene d16s03-01_mc-lc-amr-cuddle-post-climax with fade
        play voice2 mc_hey_hey2 noloop
        mc "AmRose? Come over here."
        scene d16s03-00_mc-lc-amr-cuddle-post-climax with dissolve
        play voice3 lydia_haha noloop
        lc "I love you."
        scene d16s03-02_mc-lc-amr-cuddle-post-climax with dissolve
        play voice2 mc_yes_yeah1 noloop
        mc "I know, hon. So does she. {w}AmRose - I could use a kiss right now."
        play sound maria_kiss1
        scene d16s03-03_mc-lc-amr-cuddle-post-climax with dissolve
        pause
        scene d16s03-04_mc-lc-amr-cuddle-post-climax with dissolve
        play voice2 mc_angry_huh2 noloop
        mc "I have strong feelings for you both, you know that?"
        scene d16s03-05_mc-lc-amr-cuddle-post-climax with dissolve
        play voice4 amrose_yes_ugu noloop
        arj "I understand. Thank you for letting me watch this. {w}It was very informative."

    if d16s03_arj_watch is True:
        scene d16s03-06_mc-lc-amr-cuddle-post-climax with dissolve
        play voice3 lydia_lydiahey noloop
        lc "[mcname]? Would you mind if we have some private time alone?"
        scene d16s03-07_mc-lc-amr-cuddle-post-climax with dissolve
        play voice2 mc_thinking_oh1 noloop
        mc "You want AmRose to leave?"
        lc "If that's okay with you."
        scene d16s03-08_mc-lc-amr-cuddle-post-climax with dissolve
        play voice2 mc_thinking_mmm4 noloop
        mc "Just a second. AmRose - I have a question for you."
        mc "What did you think? What did it feel like to watch us together?"
        scene d16s03-09_mc-lc-amr-cuddle-post-climax with dissolve
        if date_arj_romance is True:
            play voice4 amrose_surprised_uh2 noloop
            arj "Honestly? It felt really weird at first."
            arj "I was sitting over there grinding my teeth and getting angry, frustrated, jealous."
            arj "Then my brain kicked in. I realized that you like to be watched."
            scene d16s03-10_mc-lc-amr-cuddle-post-climax with dissolve
            play voice4 amrose_thinking_hmm3 noloop
            arj "I realized that part of the pleasure for you was the feeling of being watched by someone, and that I was filling that role."
            arj "I was helping to make you feel good. I felt good about it."
            arj "Then I kinda got into it."
        elif True:
            play voice4 amrose_thinking_hmm3 noloop
            arj "I just did what you wanted of me."
            arj "At first I thought you were punishing me. That I was supposed to feel humiliated."
            scene d16s03-11_mc-lc-amr-cuddle-post-climax with dissolve
            play voice2 mc_thinking_hmm2 noloop
            mc "Did you?"
            scene d16s03-10_mc-lc-amr-cuddle-post-climax with dissolve
            play voice4 amrose_thinking_hmm5 noloop
            arj "That was kinda kinky. My nipples started to tingle thinking about that."
            arj "I started thinking of other ways you could humiliate and punish me."
            scene d16s03-09_mc-lc-amr-cuddle-post-climax with dissolve
            play voice4 amrose_happy_laugh1 noloop
            arj "However, I snapped back when you started pleasuring Lydia."
            arj "It was... different. Unexpected."
            arj "I guess I got pretty aroused watching you two together."
        scene d16s03-11_mc-lc-amr-cuddle-post-climax with dissolve
        play voice2 mc_yes_yeah7 noloop
        mc "Yeah?"
        scene d16s03-14_mc-lc-amr-cuddle-post-climax with dissolve
        play voice4 amrose_yes_yeah1 noloop
        arj "Yeah. {w}Lydia wasn't the only one who came here today."
        mc "Nice."
        scene d16s03-12_mc-lc-amr-cuddle-post-climax with dissolve
        play voice3 lydia_laugh noloop
        lc "Congratulations."
        play voice4 amrose_old_upset noloop
        arj "Um, thanks."
        scene d16s03-15_mc-lc-amr-cuddle-post-climax with dissolve
        play voice2 mc_thinking_hmm3 noloop
        mc "What about you, Lydia? How did you feel about AmRose watching us together?"
        scene d16s03-13_mc-lc-amr-cuddle-post-climax with dissolve
        play voice3 lydia_oof noloop
        lc "Terrific. It was interesting being the one who is watched by someone else."
        if date_arj_romance is True:
            lc "Maybe sometime she could even join us."
            scene d16s03-17_mc-lc-amr-cuddle-post-climax with dissolve
            play voice4 amrose_yes_yap noloop
            arj "I think I would like that."
        elif cage_ntr is False:
            lc "Maybe next time we could join together in pleasuring you and being pleasured by you."
            scene d16s03-17_mc-lc-amr-cuddle-post-climax with dissolve
            play voice4 amrose_yes_yap noloop
            arj "I think I would like that."
            arj "Anyway, I should go get ready for class and all that."
            play voice2 mc_yes_aga1 noloop
            mc "Sounds good. I'll see you later."
        elif True:
            lc "Maybe next time she could join in and service us both."
            scene d16s03-18_mc-lc-amr-cuddle-post-climax with dissolve
            play voice2 mc_thinking_hmm5 noloop
            mc "What do you think about that?"
            scene d16s03-17_mc-lc-amr-cuddle-post-climax with dissolve
            play voice4 amrose_yes_happy1 noloop
            arj "Yes, master."
            play voice2 mc_hey_hey3 noloop
            mc "I didn't suggest it."
            play voice4 amrose_surprised_oh4 noloop
            arj "Oh, I mean... Yes, mistress."
            scene d16s03-16_mc-lc-amr-cuddle-post-climax with dissolve
            play voice3 lydia_moan1 noloop
            lc "Good enough."
            scene d16s03-11_mc-lc-amr-cuddle-post-climax with dissolve
            play voice2 mc_disappointed_ah2 noloop
            mc "Alright, slave. You may go."
            scene d16s03-14_mc-lc-amr-cuddle-post-climax with dissolve
            play voice4 amrose_thinking_emm noloop
            arj "Sure, I'll get ready for class... and meet you there?"
            play voice2 mc_yes_yeah2 noloop
            mc "Sounds like a plan."
        scene d16s03-20_mc-lc-amr-cuddle-post-climax with dissolve
        play voice3 dahlia_happy_hmm1 noloop
        lc "Bye!"
        play voice4 amrose_old_huh noloop
        scene d16s03-19_mc-lc-amr-cuddle-post-climax with dissolve
        pause
        play sound sfx_door_openclosed2

    $ renpy.music.set_volume(0.4, 8.0, "music")
    scene d16s03-00_mc-lc-amr-cuddle-post-climax with fade


    $ Lovense.stop()

    play voice3 lydia_thinking noloop
    lc "So... it's just us."
    call buzz from _call_buzz_21
    scene d16s03-01_mc-lc-amr-cuddle-post-climax with dissolve
    play voice3 lydia_oops noloop
    lc "I think that's your phone."
    play sound sfx_cloth_rustling2
    scene d16s03-70 mc-lc-lean-over-get-phone-c5
    if cage_ntr is False:
        show d16s03-70-lc-overlay
    with dissolve
    pause
    scene d16s03-71 mc-lc-give-phone-c5
    if cage_ntr is False:
        show d16s03-71-lc-overlay
    with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "Give me just a second."
    scene d16s03-72 mc-lc-talk-need-phone-check-c3 with dissolve
    mct "Fuck. I need to make sure the tracking program is working."
    scene d16s03-73 mc-on-phone-thinking-c2 with dissolve
    call add_points (d16s03_points) from _call_add_points_10
    flr "You have earned [d16s03_points] points."
    play voice2 d1s1_mmm noloop
    mct "That was fast. Or maybe I was just laying in bed too long here."
    mct "Hopefully I'm not too late for this thing to work."

    scene d16s03-78 mc-lc-talk-variation-5-c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "So, it's just us. Together. Naked except for the penis cage."
    scene d16s03-77 mc-lc-talk-variation-4-c1 with dissolve
    play voice3 lydia_lydyes noloop
    lc "I know. Isn't it wonderful?"
    scene d16s03-76 mc-lc-talk-variation-3-c1 with dissolve
    mc "Is it everything you fantasized about?"
    scene d16s03-75 mc-lc-talk-variation-2-c1 with dissolve
    lc "Oh, this wasn't even my fantasy."
    scene d16s03-78 mc-lc-talk-variation-5-c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "No? What's your fantasy then?"
    scene d16s03-74 mc-lc-talk-variation-c1 with dissolve
    play voice3 lydia_moan1 noloop
    lc "I can only tell you if you agree to do it someday... if it is even possible."
    scene d16s03-76 mc-lc-talk-variation-3-c1 with dissolve
    play voice2 d2s9_confused noloop
    mc "Tell me what it is, and then I'll agree."
    scene d16s03-77 mc-lc-talk-variation-4-c1 with dissolve
    play voice3 lydia_uhuh noloop
    lc "Nope. Leap of faith. You trust me by agreeing to it. I'll trust you by telling you what you agreed to."
    mct "Hmmm..."










    menu:
        "Agree to whatever it is"(hint="d16s03m03c01") if True:

            $ d16s03_agree_to_lc = True

            scene d16s03-95 mc-lc-sit-up-talk-alt-pose-3-c1 with dissolve
            play voice2 mc_disappointed_ehh1 noloop
            mc "Alright, I agree."
            play sound ["<silence 1.0>", sfx_camera_fly1]
            play sound3 ["<silence 4.0>", sfx_camera_fly1] noloop
            scene d16s03-glambot with dissolve
            pause
            scene d16s03-97 mc-lc-sit-up-talk-alt-pose-5-c1 with dissolve
            play voice3 lydia_huh2 noloop
            lc "You promise?"
            scene d16s03-95 mc-lc-sit-up-talk-alt-pose-3-c1 with dissolve
            play voice2 mc_yes_yes3 noloop
            mc "I promise. Whatever it is, I'll do it someday... if possible."
            scene d16s03-96 mc-lc-sit-up-talk-alt-pose-4-c1 with dissolve
            play voice3 lydia_oof noloop
            lc "Okay. Brace yourself."
            queue voice3 stacy_smell noloop
            scene d16s03-93 mc-lc-sit-up-talk-alt-pose-1-c1 with dissolve
            pause
            if cage_ntr is False:
                scene d16s03-96 mc-lc-sit-up-talk-alt-pose-4-c1 with dissolve
                play voice3 lydia_moan1 noloop
                lc "I want to jerk your erection to completion."
                scene d16s03-95 mc-lc-sit-up-talk-alt-pose-3-c1 with dissolve
                play voice2 mc_surprised_huh6 noloop
                mc "That's it?"
                scene d16s03-97 mc-lc-sit-up-talk-alt-pose-5-c1 with dissolve
                play voice3 dahlia_no_high3 noloop
                lc "No, that's not it. {w}I'm just struggling to say the other part."
                scene d16s03-95 mc-lc-sit-up-talk-alt-pose-3-c1 with dissolve
                play voice2 mc_thinking_mmm3 noloop
                mc "Sorry, sorry. Go on."
                scene d16s03-96 mc-lc-sit-up-talk-alt-pose-4-c1 with dissolve
                play voice3 dahlia_thinking_mmm2 noloop
                lc "Have you ever heard of... tossing salad?"
                scene d16s03-95 mc-lc-sit-up-talk-alt-pose-3-c1 with dissolve
                play voice2 mc_thinking_hmm2 noloop
                mc "Analingus? Like a rimjob?"
                play sound sfx_cloth_rustling1
                scene d16s03-88 mc-lc-talk-variation-alt-pose-2-c1 with dissolve
                play voice3 lydia_haha noloop
                lc "I don't know. Maybe?"
                scene d16s03-87 mc-lc-talk-variation-alt-pose-1-c1 with dissolve
                mc "You want to jerk me off while I lick your asshole?"
                scene d16s03-88 mc-lc-talk-variation-alt-pose-2-c1 with dissolve
                play voice3 dahlia_surprised_what noloop
                lc "What?! No!"
                scene d16s03-87 mc-lc-talk-variation-alt-pose-1-c1 with dissolve
                play voice2 mc_thinking_oh1 noloop
                mc "Oh."
                scene d16s03-88 mc-lc-talk-variation-alt-pose-2-c1 with dissolve
                play voice3 dahlia_thinking_hmm2 noloop
                lc "I want to jerk you off... while I lick your anus."
                scene d16s03-87 mc-lc-talk-variation-alt-pose-1-c1 with dissolve
                play voice2 mc_surprised_huh3 noloop
                mc "Really?"
                scene d16s03-88 mc-lc-talk-variation-alt-pose-2-c1 with dissolve
                play voice3 lydia_oof noloop
                lc "Not want. I fantasize about it. Some awful part of me wants it."
                scene d16s03-90 mc-lc-talk-variation-alt-pose-2-c2 with dissolve
                play voice2 mc_happy_yay2 noloop
                mc "You want to give me a Rusty Trombone?"
                scene d16s03-89 mc-lc-talk-variation-alt-pose-1-c2 with dissolve
                play voice3 dahlia_surprised_huh2 noloop
                lc "What's that?"
                scene d16s03-90 mc-lc-talk-variation-alt-pose-2-c2 with dissolve
                play voice2 mc_yes_yeah4 noloop
                mc "It's what that is called. You toss my salad while jerking my cock."
                scene d16s03-89 mc-lc-talk-variation-alt-pose-1-c2 with dissolve
                play voice3 dahlia_disappointed_hmm2 noloop
                lc "It's horrible and disgusting. I don't think I could ever put my mouth down there..."
                scene d16s03-90 mc-lc-talk-variation-alt-pose-2-c2 with dissolve
                play voice2 mc_thinking_hmm4 noloop
                mc "But you dream about it."
                scene d16s03-89 mc-lc-talk-variation-alt-pose-1-c2 with dissolve
                play voice3 daisy_ugu noloop
                lc "... I do."
                scene d16s03-90 mc-lc-talk-variation-alt-pose-2-c2 with dissolve
                play voice2 mc_yes_okay2 noloop
                mc "That's okay."
            elif True:
                play sound sfx_cloth_rustling1
                scene d16s03-87 mc-lc-talk-variation-alt-pose-1-c1 with dissolve
                play voice3 dahlia_disappointed_hmm2 noloop
                lc "Did you ever see that old movie... Watchmen?"
                scene d16s03-88 mc-lc-talk-variation-alt-pose-2-c1 with dissolve
                play voice2 mc_yes_yeah7 noloop
                mc "I wouldn't call it old, but yeah."
                scene d16s03-87 mc-lc-talk-variation-alt-pose-1-c1 with dissolve
                play voice3 lydia_haha noloop
                lc "It's not ancient, but it's pretty old."
                scene d16s03-88 mc-lc-talk-variation-alt-pose-2-c1 with dissolve
                play voice2 mc_yes_yes3 noloop
                mc "Anyway, yes. I've seen it."
                scene d16s03-87 mc-lc-talk-variation-alt-pose-1-c1 with dissolve
                play voice3 dahlia_old_upset noloop
                lc "There's this scene where that blue guy... there's several of him. Almost all of them are focused on making love to his wife... girlfriend... whatever she was."
                scene d16s03-88 mc-lc-talk-variation-alt-pose-2-c1 with dissolve
                play voice2 mc_yes_yeah4 noloop
                mc "Yeah. Doctor Manhattan and Laurie Jupiter."
                scene d16s03-87 mc-lc-talk-variation-alt-pose-1-c1 with dissolve
                play voice3 dahlia_thinking_hmm4 noloop
                lc "I think that's like every woman's dream."
                scene d16s03-90 mc-lc-talk-variation-alt-pose-2-c2 with dissolve
                play voice2 mc_arrogant_huh1 noloop
                mc "Sex with a blue man?"
                scene d16s03-89 mc-lc-talk-variation-alt-pose-1-c2 with dissolve
                play voice3 lydia_uhuh noloop
                lc "To be surrounded by cocks. In my pussy. In my ass. In my mouth."
                lc "One in each hand. Another guy between my breasts. One each rubbing against my feet."

                lc "Inside me. Around me. Until I couldn't breathe. Just everywhere."
                scene d16s03-90 mc-lc-talk-variation-alt-pose-2-c2 with dissolve
                play voice2 mc_scared_oh4 noloop
                mc "I don't know if I could physically do that."
                scene d16s03-89 mc-lc-talk-variation-alt-pose-1-c2 with dissolve
                play voice3 lydia_hmmmm noloop
                lc "Maybe someday?"
                scene d16s03-90 mc-lc-talk-variation-alt-pose-2-c2 with dissolve
                play voice2 mc_thinking_emm1 noloop
                mc "I don't ... how?"
                scene d16s03-89 mc-lc-talk-variation-alt-pose-1-c2 with dissolve
                play voice3 lydia_morningoh noloop
                lc "I don't know. {w}Like you said, it's just a fantasy."
                scene d16s03-90 mc-lc-talk-variation-alt-pose-2-c2 with dissolve
                play voice2 mc_yes_aga2 noloop
                mc "Which you said was a window to your unconscious desires."
                scene d16s03-97 mc-lc-sit-up-talk-alt-pose-5-c1 with dissolve
                play voice3 lydia_lydiahey noloop
                lc "I know it can't happen... it's just not possible..."
                scene d16s03-79 mc-lc-talk-variation-1-c2 with dissolve
                play voice2 mc_yes_okay2 noloop
                mc "Okay, okay."
                mc "So, who are these guys in this fantasy?"
                scene d16s03-81 mc-lc-talk-variation-3-c2 with dissolve
                play voice3 lydia_moan1 noloop
                lc "You?"
                scene d16s03-81 mc-lc-talk-variation-3-c2 with dissolve
                play voice2 mc_thinking_hmm5 noloop
                mc "It's okay. You can tell me. Who do you really fantasize about?"
                play voice3 stacy_smell noloop
                scene d16s03-93 mc-lc-sit-up-talk-alt-pose-1-c1 with dissolve
                lc "...{w} the University Lacrosse Team."
                play voice2 mc_arrogant_huh1 noloop
                mc "There are ten guys on that team, aren't there?"
                scene d16s03-96 mc-lc-sit-up-talk-alt-pose-4-c1 with dissolve
                play voice3 lydia_lydyes noloop
                lc "Yes."
                scene d16s03-81 mc-lc-talk-variation-3-c2 with dissolve
                play voice2 mc_thinking_mmm2 noloop
                mc "Strong, athletic, long hair... those kinds of guys?"
                scene d16s03-96 mc-lc-sit-up-talk-alt-pose-4-c1 with dissolve
                lc "Yes."
                play voice2 mc_arrogant_huh3 noloop
                scene d16s03-81 mc-lc-talk-variation-3-c2 with dissolve
                mc "Huh. Good to know."
                scene d16s03-95 mc-lc-sit-up-talk-alt-pose-3-c1 with dissolve
                play voice3 lydia_laugh noloop
                lc "Please don't arrange it. I'm not anywhere near ready to experience that."
                scene d16s03-81 mc-lc-talk-variation-3-c2 with dissolve
                play voice2 mc_disappointed_ah2 noloop
                mc "Lydia, honey. I know we've got this open relationship and all that, and I know I agreed to fulfill your fantasy someday, but..."
                mc "I'm not anywhere near ready to allow you to get gangbanged."
                scene d16s03-97 mc-lc-sit-up-talk-alt-pose-5-c1 with dissolve
                play voice3 dahlia_thinking_oh noloop
                lc "Oh good. {w}Me neither."
        "Demand to know what it is"(hint="d16s03m03c02") if True:


            $ d16s03_agree_to_lc = False

            scene d16s03-95 mc-lc-sit-up-talk-alt-pose-3-c1 with dissolve
            play voice2 mc_no_no4 noloop
            mc "I can't agree without knowing what I'm agreeing to."
            scene d16s03-96 mc-lc-sit-up-talk-alt-pose-4-c1 with dissolve
            play voice3 dahlia_thinking_hmm4 noloop
            lc "Well, then I guess you don't find out what it is."
            scene d16s03-95 mc-lc-sit-up-talk-alt-pose-3-c1 with dissolve
            play voice2 mc_disappointed_ah2 noloop
            mc "C'mon, you can tell me."
            scene d16s03-97 mc-lc-sit-up-talk-alt-pose-5-c1 with dissolve
            play voice3 lydia_aga noloop
            lc "I could. {w}Anyway, how are your studies going?"
            scene d16s03-95 mc-lc-sit-up-talk-alt-pose-3-c1 with dissolve
            play voice2 mc_arrogant_huh3 noloop
            mc "Huh? Oh, I'm doing okay."
            scene d16s03-97 mc-lc-sit-up-talk-alt-pose-5-c1 with dissolve
            lc "It's finals week. You better be doing a heck of a lot better than okay."
            scene d16s03-95 mc-lc-sit-up-talk-alt-pose-3-c1 with dissolve
            mc "You're just changing the subject, aren't you?"
            scene d16s03-96 mc-lc-sit-up-talk-alt-pose-4-c1 with dissolve
            play voice3 lydia_hmmmm noloop
            lc "Maybe..."
            play sound ["<silence 1.0>", sfx_camera_fly1]
            play sound3 ["<silence 4.0>", sfx_camera_fly1] noloop
            scene d16s03-glambot with dissolve
            pause

    scene d16s03-88 mc-lc-talk-variation-alt-pose-2-c1 with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    lc "So, anyway... since we're talking about fantasies..."
    scene d16s03-87 mc-lc-talk-variation-alt-pose-1-c1 with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Yes?"
    scene d16s03-88 mc-lc-talk-variation-alt-pose-2-c1 with dissolve
    lc "What's yours?"
    scene d16s03-87 mc-lc-talk-variation-alt-pose-1-c1 with dissolve
    mc "I don't have one."
    scene d16s03-88 mc-lc-talk-variation-alt-pose-2-c1 with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    lc "Bullcrap."
    scene d16s03-90 mc-lc-talk-variation-alt-pose-2-c2 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Well, I don't have just one. Every time I zone out or daydream I have a new one."
    mc "It's not a window to my subconscious. It's just a guy who's watched too much porn."
    scene d16s03-89 mc-lc-talk-variation-alt-pose-1-c2 with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    lc "Just a guy? I don't believe that about you."
    scene d16s03-90 mc-lc-talk-variation-alt-pose-2-c2 with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "Well, most of the time. This fucking cage makes me feel like a lot less than that."
    scene d16s03-89 mc-lc-talk-variation-alt-pose-1-c2 with dissolve
    play voice3 lydia_hmmmm noloop
    lc "Well, if you had a fantasy - what would you do?"
    scene d16s03-90 mc-lc-talk-variation-alt-pose-2-c2 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "You. {w}You are my greatest fantasy."
    scene d16s03-88 mc-lc-talk-variation-alt-pose-2-c1 with dissolve
    play voice3 lydia_morningoh noloop
    lc "That's sweet. What would you do to me?"
    lc "If I allowed you - or you could make me do it. What would your deepest, darkest fantasy be?"
    lc "What would you do to me if you could do anything at all?"


    scene d16s03-87 mc-lc-talk-variation-alt-pose-1-c1 with dissolve
    play voice2 mc_scared_oh1 noloop
    mc "Well, there is something I really want to do."
    scene d16s03-88 mc-lc-talk-variation-alt-pose-2-c1 with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    lc "What's that?"
    scene d16s03-87 mc-lc-talk-variation-alt-pose-1-c1 with dissolve
    mc "Have you ever experienced... no, you wouldn't have."
    scene d16s03-88 mc-lc-talk-variation-alt-pose-2-c1 with dissolve
    lc "What? You can tell me."
    scene d16s03-87 mc-lc-talk-variation-alt-pose-1-c1 with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "Okay, I'm just going to blurt it out."
    scene d16s03-92 mc-lc-talk-variation-alt-pose-4-c1 with dissolve
    play voice3 lydia_haha noloop
    lc "Go ahead."
    mc "3.{w=0.5}.. 2.{w=0.5}.. 1...."
    menu:
        "Want to Cum in Lydia's Pussy"(hint="d16s03m04c01") if True:

            $ d16s03_darkest_fantasy = "creampie"

            scene d16s03-79 mc-lc-talk-variation-1-c2 with dissolve
            play voice2 mc_yes_okay3 noloop
            mc "Okay, okay. It's pretty simple, really."
            scene d16s03-80 mc-lc-talk-variation-2-c2 with dissolve
            mc "I would make love to you for hours, and when I was ready to climax I would cum deep inside you."
            scene d16s03-81 mc-lc-talk-variation-3-c2 with dissolve
            play voice3 lydia_huh2 noloop
            lc "Inside me?"
            scene d16s03-79 mc-lc-talk-variation-1-c2 with dissolve
            play voice2 mc_yes_yes1 noloop
            mc "In your pussy."
            mc "I would just hold onto that moment as long as possible."
            scene d16s03-80 mc-lc-talk-variation-2-c2 with dissolve
            mc "Then when I finally withdrew myself, I would watch my sperm and semen drip out of your vagina."
            scene d16s03-81 mc-lc-talk-variation-3-c2 with dissolve
            play voice3 lydia_moan1 noloop
            lc "Drip out?"
            scene d16s03-79 mc-lc-talk-variation-1-c2 with dissolve
            play voice2 mc_yes_yeah4 noloop
            mc "Yep. I would creampie you and watch it come out."
        "Want to Fuck Lydia's Ass"(hint="d16s03m04c02") if True:


            $ d16s03_darkest_fantasy = "anal"

            scene d16s03-79 mc-lc-talk-variation-1-c2 with dissolve
            play voice2 mc_disappointed_ah1 noloop
            mc "Someday... you know, when you're ready and practice with toys a bit and there's plenty of lube..."
            scene d16s03-81 mc-lc-talk-variation-3-c2 with dissolve
            lc "...?"
            scene d16s03-80 mc-lc-talk-variation-2-c2 with dissolve
            play voice2 mc_arrogant_heh1 noloop
            mc "I want to fuck your ass."
        "Want to Piss on & in Lydia"(hint="d16s03m04c03") if True:


            $ d16s03_darkest_fantasy = "pissonher"

            scene d16s03-79 mc-lc-talk-variation-1-c2 with dissolve
            play voice2 mc_thinking_emm1 noloop
            mc "Well, I'm kinda into watersports."
            if date_mes is False:
                scene d16s03-81 mc-lc-talk-variation-3-c2 with dissolve
                play voice3 dahlia_thinking_hmm1 noloop
                lc "Like kayaking and canoeing?"
                scene d16s03-80 mc-lc-talk-variation-2-c2 with dissolve
                play voice2 mc_no_uhuh1 noloop
                mc "More like urination and peeing."
            scene d16s03-81 mc-lc-talk-variation-3-c2 with dissolve
            play voice3 lydia_oops noloop
            lc "Oh, so you would want me to..."
            if date_mes is False:
                scene d16s03-79 mc-lc-talk-variation-1-c2 with dissolve
            elif True:
                scene d16s03-80 mc-lc-talk-variation-2-c2 with dissolve
            play voice2 mc_yes_yeah1 noloop
            mc "Someday, when you're ready... I'd like to piss on you."
            mc "In your hair, on your face, in your mouth, on your breasts and body..."
            if date_mes is False:
                scene d16s03-80 mc-lc-talk-variation-2-c2 with dissolve
            elif True:
                scene d16s03-79 mc-lc-talk-variation-1-c2 with dissolve
            mc "I just really think it would be a wonderful experience for both of us."
        "Want to Gag, Choke, and Deepthroat Lydia"(hint="d16s03m04c04") if True:


            $ d16s03_darkest_fantasy = "gagging"

            scene d16s03-79 mc-lc-talk-variation-1-c2 with dissolve
            play voice2 mc_disappointed_ah1 noloop
            mc "You did say darkest fantasy..."
            scene d16s03-80 mc-lc-talk-variation-2-c2 with dissolve
            play voice2 mc_arrogant_heh1 noloop
            mc "Well, it's not anything dangerous or violent... it's just a power fantasy."
            scene d16s03-81 mc-lc-talk-variation-3-c2 with dissolve
            play voice3 dahlia_thinking_hmm2 noloop
            lc "You want me to be submissive?"
            scene d16s03-79 mc-lc-talk-variation-1-c2 with dissolve
            play voice2 mc_angry_huh2 noloop
            mc "I want to gag you with my cock."
            mc "I want to make you choke."
            scene d16s03-80 mc-lc-talk-variation-2-c2 with dissolve
            mc "I want to shove my hard cock deep into your throat and cum directly into your stomach."
        "Want to Bind and Dominate Lydia"(hint="d16s03m04c05") if True:


            $ d16s03_darkest_fantasy = "bdsm"

            scene d16s03-79 mc-lc-talk-variation-1-c2 with dissolve
            play voice2 mc_thinking_emm1 noloop
            mc "Have you ever heard of BDSM?"
            scene d16s03-81 mc-lc-talk-variation-3-c2 with dissolve
            play voice3 dahlia_thinking_hmm3 noloop
            lc "Sadism and masochism?"
            scene d16s03-80 mc-lc-talk-variation-2-c2 with dissolve
            play voice2 mc_yes_yeah4 noloop
            mc "I was thinking more of the bondage and domination."
            mc "I would tie you up all sorts of different ways, and fuck you every way possible."

    scene d16s03-96 mc-lc-sit-up-talk-alt-pose-4-c1 with dissolve
    play voice3 dahlia_surprised_wow noloop
    lc "Wow... {w}Fuck me."
    play voice2 mc_disappointed_ehh3 noloop
    mc "I would if I could."
    play voice3 lydia_hmmmm noloop
    lc "I know I said your deepest, darkest fantasy, but..."
    scene d16s03-84 mc-lc-talk-variation-2-c3 with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Too much?"
    scene d16s03-85 mc-lc-talk-variation-3-c3 with dissolve
    play voice3 lydia_uhuh noloop
    lc "I just don't know if I'll ever be ready for that."
    scene d16s03-86 mc-lc-talk-variation-4-c3 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Don't worry. We don't ever need to do that. It's just a fantasy."
    scene d16s03-85 mc-lc-talk-variation-3-c3 with dissolve
    play voice3 daisy_ugu noloop
    lc "Yeah, I know. It's just..."
    scene d16s03-86 mc-lc-talk-variation-4-c3 with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Did I upset you?"
    scene d16s03-85 mc-lc-talk-variation-3-c3 with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    lc "Is that the time? {w}Don't you need to get ready for class?"
    scene d16s03-83 mc-lc-talk-variation-1-c3 with dissolve
    play voice2 mc_scared_huh3 noloop
    mc "What? Oh, yeah. {w}You didn't-"
    scene d16s03-85 mc-lc-talk-variation-3-c3 with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    lc "You really shouldn't miss any classes during finals week."
    scene d16s03-86 mc-lc-talk-variation-4-c3 with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "Look, I'm sorry if I-"
    scene d16s03-85 mc-lc-talk-variation-3-c3 with dissolve
    play voice3 lydia_aga noloop
    lc "We can talk about that later. You really should get to class."
    scene d16s03-84 mc-lc-talk-variation-2-c3 with dissolve
    play voice2 mc_disappointed_ehh2 noloop
    mc "... sure."
    mc "I just want to say that I'm sorry if I upset you."
    scene d16s03-85 mc-lc-talk-variation-3-c3 with dissolve
    play voice3 dahlia_no_nah noloop
    lc "Forget about that, okay? {w}Now get your ass to class!"
    play sound sfx_jeans_fly1
    play sound3 sfx_clothes_undress1 noloop
    scene d16s03-102 mc-lc-wait-talk-pose-2-c1 with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "Okay, okay."
    scene d16s03-100 mc-lc-dressed-ready-pose-3-go-to-class-c5 with dissolve
    pause
    scene d16s03-101 mc-lc-wait-talk-pose-1-c1 with dissolve
    play voice3 lydia_lydiahey noloop
    lc "[mcname] wait!"
    scene d16s03-98 mc-lc-dressed-ready-pose-1-c4 with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Yes?"
    scene d16s03-103 lc-i-love-you-pov-c2 with dissolve
    play voice3 lydia_moan1 noloop
    lc "I love you. Thank you so much for... everything. Especially today."
    menu:
        "Tell Lydia You Love Her Too"(hint="d16s03m05c01") if True:

            $ d16s03_love_lc = True

            scene d16s03-98 mc-lc-dressed-ready-pose-1-c4 with dissolve
            play voice2 mc_thinking_mmm2 noloop
            mc "I love you too. {w}You know something?"
            scene d16s03-99 mc-lc-dressed-ready-pose-2-go-to-class-c4 with dissolve
            play voice3 lydia_morningoh noloop
            lc "What's that?"
            scene d16s03-105 mc-response-pov-c3 with dissolve
            play voice2 mc_happy_a1 noloop
            mc "You're my favorite girl."
        "Tell Lydia That You Enjoyed It As Well"(hint="d16s03m05c02") if True:


            $ d16s03_love_lc = False

            scene d16s03-105 mc-response-pov-c3 with dissolve
            play voice2 mc_happy_a1 noloop
            mc "Thank you. I enjoyed it at least as much as you did!"

    scene d16s03-106 mc-lc-talk-pose-1-c5 with dissolve
    play voice3 lydia_huh2 noloop
    lc "You're so sweet."
    scene d16s03-107 mc-lc-leave-goodbye-c1 with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "Alright, I'm gonna get my ass to class."
    play voice3 dahlia_yes_ugu noloop
    lc "Right. Go go go!"
    play sound ["<silence 1.5>", sfx_door_closed1]
    $ unlock_gallery_slot("cg", "d16s03")
    if d16s03_lie_to_lc is False:
        $ unlock_gallery_slot("scene", "d16s03")

    stop music fadeout 4.0
    jump d16s04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
