image d19s01ntr_glambot_1 = Movie(play = "images/Day-19/s01ntr/anim/d19s01ntr-a11-2-4x-60fps.webm", start_image = "d19s01ntr-a11-2 glambot-11-2-00_i", image = "d19s01ntr-a11-2 glambot-11-2-00_i", loop = False)
image d19s01ntr_glambot_2 = Movie(play = "images/Day-19/s01ntr/anim/d19s01ntr-a11-4x-60fps.webm", start_image = "d19s01ntr-a11 glambot-11-00_i", image = "d19s01ntr-a11 glambot-11-69_i", loop = False)

image d19s01ntr-a1 = Movie(play = "images/Day-19/s01ntr/anim/d19s01ntr-a1-2x-50fps.webm", start_image = "d19s01ntr-a1 lc-pb-jerome-sex-anim-1-000")
image d19s01ntr-a2 = Movie(play = "images/Day-19/s01ntr/anim/d19s01ntr-a2-2x-50fps.webm", start_image = "d19s01ntr-a2 lc-pb-jerome-sex-anim-2-000_i")
image d19s01ntr-a3 = Movie(play = "images/Day-19/s01ntr/anim/d19s01ntr-a3-2x-50fps.webm", start_image = "d19s01ntr-a3 lc-pb-jerome-sex-anim-3-000_i")
image d19s01ntr-a4 = Movie(play = "images/Day-19/s01ntr/anim/d19s01ntr-a4-2x-50fps.webm", start_image = "d19s01ntr-a4 lc-pb-jerome-sex-anim-4-000_i")

label d19s01ntr:

    scene black
    show screen scene_transistion(_("Friday\nDay-19"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene d19s01ntr-00 mc_lc_pd_ntr_lydias_dungeon
    with Fade(0.5, 0.5, 2.0)
    queue music music_cumtusion
    pause
    play voice2 mc_angry_huh2 noloop
    mc "Huh?{w} What?!{w} Where am I?"
    scene d19s01ntr-01 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice3 dahlia_disappointed_ehh1 noloop
    lc "You're finally awake."
    scene d19s01ntr-02 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice2 mc_surprised_huh3 noloop
    mc "Lydia?"
    scene d19s01ntr-03 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    lc "You may call me, \"Mistress\" here."
    scene d19s01ntr-04 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice2 mc_pain_rrrr noloop
    mc "Fuck. I must be dreaming or having a nightmare or something."
    scene d19s01ntr-05 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice3 dahlia_thinking_oh noloop
    lc "Do you want me to pinch you?{w} I'd rather have Jerome punch you."
    scene d19s01ntr-06 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice4 boy4_thinking_mmm2_muffled noloop
    pause
    scene d19s01ntr-07 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice3 dahlia_disgust_yah noloop
    lc "That wasn't a request. Heel, bitch."
    scene d19s01ntr-08 mc_lc_pd_ntr_lydias_dungeon with dissolve
    pause
    play voice2 mc_surprised_huh6 noloop
    mc "What the fuck is going on here?"
    scene d19s01ntr-09 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    lc "Everything is going according to plan. Let me clear this up for you."
    scene d19s01ntr-a11 glambot-11-00_i with dissolve
    lc "I'm the baddddd guy.{w} duh."
    play sound ["<silence 0.7>", sfx_camera_fly1] volume 2.0
    scene d19s01ntr_glambot_2
    pause
    stop sound fadeout 1.0
    scene d19s01ntr-10 mc_lc_pd_ntr_lydias_dungeon with dissolve
    pause
    scene d19s01ntr-a11-2 glambot-11-2-00_i with dissolve
    pause
    $ renpy.music.set_volume(1.0, 0.0, "sound4")
    play sound sfx_camera_fly1 volume 2.0
    play sound4 ["<silence 1.4>", sfx_camera_fly1] volume 2.0 noloop
    scene d19s01ntr_glambot_1
    pause
    stop sound fadeout 1.0
    stop sound4 fadeout 1.0
    scene d19s01ntr-12 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice2 d2s12_emmm noloop
    mc "...?!"
    scene d19s01ntr-13 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice3 lydia_haha noloop volume 1.6
    lc "Welcome to my Dungeon, slave."
    scene d19s01ntr-14 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice2 mc_pain_mff3 noloop
    mc "...?!?!"
    scene d19s01ntr-15 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice3 dahlia_arrogant_heh noloop
    lc "Good. You're at a complete loss for words. I thought this might happen."
    scene d19s01ntr-16 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "Actually, I've just got a raging headache.{w} Do you have any Tylenol?"
    scene d19s01ntr-17 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice3 lydia_morningoh noloop volume 1.6
    lc "Cute.{w} Gag him."
    scene d19s01ntr-18 mc_lc_pd_ntr_lydias_dungeon with dissolve
    pause
    play sound ["<silence 0.25>", sfx_underpants_off1] volume 3.0
    scene d19s01ntr-19 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice2 mc_pain_mff2 noloop
    mct "What the fuck!{w} This isn't some bizarre nightmare...{w} It is real."
    scene d19s01ntr-20 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice3 lydia_hmmmm noloop volume 1.6
    lc "To answer your earlier statement - this dungeon is my dream. Fetish Locator was merely the audition.{w} This is your Reality now."
    lc "I am your goddess; your sun & moon; your everything.{w} You are my latest creation."
    scene d19s01ntr-21 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice3 lydia_thinking noloop volume 1.6
    lc "There have been others, of course."
    lc "Jerome here has his uses. And Pete, of course..."
    lc "Isn't Pete such a lovely toy? I get bored of him so often, yet sometimes he's just wonderful."

    jump d19s01ntr_flashback

label replay_d19s01ntr:
label d19s01ntr_flashback:

    $ Lovense.stop()

    play sound sfx_memory_back4
    $ renpy.music.set_volume(0.6, 0.0, "sound2")
    play sound2 sfx_water_mill volume 0.2 fadeout 0.6 fadein 1.5
    play voice4 pete_sex_openmoans1 volume 0.2 fadeout 0.6 fadein 1.5
    play voice3 dahlia_sex_openmoans2 volume 0.2 fadeout 0.6 fadein 1.5
    play sound4 sfx_anal_penetration1 volume 0.2 fadeout 0.6 fadein 1.5
    scene d19s01ntr_flashback-00 mc_lc_pd_ntr_lydias_dungeon_flashback
    $ Lovense.pattern("5;8", 1400)
    show memory-cloud at image_opacity(0.4)
    with pixellate
    pause
    $ renpy.music.set_volume(1.0, 0.0, "sound4")
    $ renpy.music.set_volume(1.0, 0.0, "sound2")
    play voice4 pete_sex_openmoans1
    play voice3 dahlia_sex_openmoans2
    play sound4 sfx_anal_penetration1
    play sound2 sfx_water_mill volume 0.8 fadeout 0.6
    scene d19s01ntr-a1
    show memory-cloud at image_opacity(0.4)
    with dissolve
    pause
    play sound4 sfx_anal_penetration1
    play sound2 sfx_water_mill volume 0.7
    scene d19s01ntr-a2
    show memory-cloud at image_opacity(0.4)
    with dissolve
    lc "*sigh* So very boring, yet so very useful. I'm half inclined to simply let it drown."
    lc "Perhaps it is time for a change.{w} Peter, why don't you take Jerome's place for a few minutes."
    pb "Mistress?!"
    pause
    play sound4 sfx_anal_penetration1
    scene d19s01ntr-a4
    show memory-cloud at image_opacity(0.4)
    with dissolve
    lc "What alternative is there? This slave's app could bring me dozens or hundreds of fresh servants and slaves."
    pb "Yes, mistress."
    stop voice4 fadeout 1.0
    scene d19s01ntr_flashback-06 mc_lc_pd_ntr_lydias_dungeon_flashback
    show memory-cloud at image_opacity(0.4)
    with dissolve
    stop sound4 fadeout 1.0
    play voice3 dahlia_angry_hm1 noloop
    $ Lovense.stop()
    $ Lovense.vibrate(4)
    lc "What can you offer me that might compare?"
    scene d19s01ntr_flashback-07 mc_lc_pd_ntr_lydias_dungeon_flashback
    show memory-cloud at image_opacity(0.4)
    with dissolve
    play voice4 pete_angry_hmm2 noloop
    pb "Perhaps a new game, mistress. A game you can play - with a new toy."
    queue voice4 pete_sex_openmoans1
    play voice3 dahlia_sex_openmoans1
    play sound4 sfx_anal_penetration1
    $ Lovense.pattern("7;10", 1400)
    scene d19s01ntr-a2
    show memory-cloud at image_opacity(0.4)
    with dissolve
    lc "Intrigue me."
    pause
    play sound4 sfx_anal_penetration1
    scene d19s01ntr-a3
    show memory-cloud at image_opacity(0.4)
    with dissolve
    pause
    stop sound4 fadeout 2.0
    stop voice3 fadeout 2.0
    stop voice4 fadeout 2.0
    stop sound2 fadeout 2.0
    play sound sfx_memory_in4
    $ renpy.end_replay()
    $ unlock_gallery_slot("scene", "d19s01ntr")

    jump d19s01ntr_continue

label d19s01ntr_continue:

    scene d19s01ntr-22 mc_lc_pd_ntr_lydias_dungeon with pixellate
    $ Lovense.stop()
    $ Lovense.vibrate(1)
    play voice3 lydia_laugh noloop
    lc "He told me about you. How infatuated you were with me{w} - with my public face."
    lc "How many times he suggested just drugging you and dragging you here. It would have been so easy."
    lc "That would have been so boring."
    scene d19s01ntr-23 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice3 lydia_moan1 noloop
    lc "I fed your infatuation. Meanwhile Jerome here worked night & day on the app."
    lc "Pete told you how to meet me... using the app."
    lc "It was a delicious coincidence. The app was ready just as you disappeared. No one knew what had happened to you."
    scene d19s01ntr-24 mc_lc_pd_ntr_lydias_dungeon with dissolve
    lc "While Min danced to my perversions and your friends fell into my grasp you were nowhere to be found."
    lc "I became rather intrigued."
    scene d19s01ntr-25 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice2 mc_pain_mff1 noloop
    mct "My friends? Min? I don't understand..."
    scene d19s01ntr-26 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    lc "I didn't specifically target your little friends. Like so many others they fell willingly into my trap.{w} I think they'll like it here."
    lc "As for Min - we have competed with each other since the time we were little girls."
    scene d19s01ntr-27 mc_lc_pd_ntr_lydias_dungeon with dissolve
    lc "Min is quite obsessed with sex these days. She has no idea that I've defeated her."
    lc "She isn't ripe yet.{w} Min entertains me. I haven't decided to bend her will to my own... yet."
    scene d19s01ntr-28 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    lc "I know what you're thinking. What about my little gimp, Jerome?"
    lc "That little play acting at Min's party? Where I let you play the hero, then lay silent while you jerked off?"
    scene d19s01ntr-29 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice3 dahlia_arrogant_hm noloop
    lc "It was all calculated.{w} You never even realized the theme of that party, did you?"
    lc "It was all about blue balling and spoiled climaxes."
    scene d19s01ntr-30 mc_lc_pd_ntr_lydias_dungeon with dissolve
    lc "It was part of the agreement between Min and Fetish Locator for the party."
    lc "Of course, there was always the possibility of someone like Chloe taking pity on you, but the best laid plans and all that."
    lc "And like all of my plans... it worked out perfectly."
    scene d19s01ntr-24 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    lc "I've manipulated you since before we ever met.{w} Of course, you might be a little upset about that."
    lc "But think about what you have gotten out of it."
    scene d19s01ntr-26 mc_lc_pd_ntr_lydias_dungeon with dissolve
    lc "You are my creation. Who knew you existed a few weeks ago?"
    lc "You're popular! You're loved! You've fucked how many people?!"
    scene d19s01ntr-33 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice3 lydia_oof noloop
    lc "Before that you were nothing."
    lc "When you disappeared for weeks, who cared except for me and mine?"
    lc "And now you get to enjoy pleasuring me for the rest of your existence. Isn't it wonderful?"
    scene d19s01ntr-31 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice4 aaleyah_disappointed_mff2 noloop
    pause
    scene d19s01ntr-32 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice2 terrell_pain3 noloop volume 1.5
    pause
    scene d19s01ntr-30 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice3 dahlia_thinking_oh noloop
    lc "Oh, don't worry. You won't have to do it alone. Jerome, Pete, Terrell, Aaleyah..."
    lc "Your feisty redhead will join you here shortly.{w}.. along with many of your other friends and lovers."
    lc "I might even need to expand this Dungeon."
    scene d19s01ntr-34 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice3 dahlia_old_moan1 noloop volume 1.5
    lc "I am all you need to worry about for the rest of your life."
    lc "I am your beginning and will be your end. I am everything and you are nothing."
    lc "I am your Mistress and you are my slave."
    scene d19s01ntr-35 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice2 mc_pain_mff5 noloop
    mc "MMmpph!"
    scene d19s01ntr-36 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice3 dahlia_old_argh2 noloop volume 1.5
    lc "*sigh* Release his mouth so he can speak."
    scene d19s01ntr-37 mc_lc_pd_ntr_lydias_dungeon with dissolve
    pause
    play sound sfx_tracker_uncuff1 volume 1.5
    scene d19s01ntr-38 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "There is still something I don't understand."
    play sound sfx_camera_fly1
    scene d19s01ntr-38-1 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    pause
    play voice2 mc_scared_huh2 noloop
    scene d19s01ntr-38-2 mc_lc_pd_ntr_lydias_dungeon_end_blur with dissolve
    pause
    play voice2 mc_pain_rrrr noloop
    play sound sfx_kick3

    $ Lovense.stop()

    scene d19s01ntr-39 mc_lc_pd_ntr_lydias_dungeon_blur with hpunch
    pause
    scene d19s01ntr-40 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice3 dahlia_angry_hm2 noloop
    lc "Say it properly when you speak to your betters."
    scene d19s01ntr-41 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "There is still something I don't understand, Mistress."
    scene d19s01ntr-42 mc_lc_pd_ntr_lydias_dungeon with dissolve
    play voice3 dahlia_arrogant_huh noloop
    lc "What is it, slave?"

    jump d19s01ntr_questions

label d19s01ntr_questions:

    scene d19s01ntr-43 mc_lc_pd_ntr_lydias_dungeon_questions with dissolve
    menu:
        "How did I get here?"(hint="d19s01ntrm01c01"):
            $ d19s01ntr_q1 = True
            scene d19s01ntr-44 mc_lc_pd_ntr_lydias_dungeon_questions with dissolve
            lc "Apparently you called a taxi. You were passed out in the back seat when it arrived at my house."
            play voice3 dahlia_arrogant_ha noloop
            scene d19s01ntr-45 mc_lc_pd_ntr_lydias_dungeon_questions with dissolve
            play voice2 d2s9_confused noloop volume 1.6
            mc "So, this place... this is part of your home?"
            scene d19s01ntr-46 mc_lc_pd_ntr_lydias_dungeon_questions with dissolve
            play voice3 dahlia_happy_laugh4 noloop
            lc "This is my true home."
        "I thought you were a virgin!"(hint="d19s01ntrm01c02"):

            $ d19s01ntr_q2 = True
            scene d19s01ntr-48 mc_lc_pd_ntr_lydias_dungeon_questions with dissolve
            play voice3 dahlia_arrogant_ha noloop
            lc "I'm sure I was, once."
            scene d19s01ntr-49 mc_lc_pd_ntr_lydias_dungeon_questions with dissolve
            play voice2 mc_disappointed_ehh3 noloop
            mc "You lied to me."
            scene d19s01ntr-50 mc_lc_pd_ntr_lydias_dungeon_questions with dissolve
            play voice3 dahlia_no_uhuh noloop
            lc "Never!{w} I talked about the rumors, but never confirmed them."
            lc "We spoke about Fetish Locator, but I never confirmed or denied my involvement."
            scene d19s01ntr-51 mc_lc_pd_ntr_lydias_dungeon_questions with dissolve
            play voice2 mc_disappointed_ah1 noloop
            mc "You implied..."
            scene d19s01ntr-52 mc_lc_pd_ntr_lydias_dungeon_questions with dissolve
            play voice3 dahlia_yes_yeah2 noloop
            lc "I did. I implied. I have manipulated. I even gaslit you - but I never lied."
        "How is Kevin involved in all this"(hint="d19s01ntrm01c03"):

            $ d19s01ntr_q3 = True
            scene d19s01ntr-54 mc_lc_pd_ntr_lydias_dungeon_questions with dissolve
            play voice3 dahlia_thinking_hmm1 noloop
            lc "Kevin?{w} Oh, Echo and Bravo."
            scene d19s01ntr-53 mc_lc_pd_ntr_lydias_dungeon_questions with dissolve
            play voice2 mc_yes_yeah5 noloop
            mc "Yeah"
            scene d19s01ntr-44 mc_lc_pd_ntr_lydias_dungeon_questions with dissolve
            play voice3 lydia_aga noloop
            lc "Don't worry about them. They'll join you here in a day or two. I'm certain they'll be very excited to do my bidding."
        "Where are we?"(hint="d19s01ntrm01c04"):

            $ d19s01ntr_q4 = True
            scene d19s01ntr-56 mc_lc_pd_ntr_lydias_dungeon_questions with dissolve
            play voice3 dahlia_arrogant_pff noloop
            lc "We're in my Sex Dungeon. Do you have brain damage?"
            scene d19s01ntr-57 mc_lc_pd_ntr_lydias_dungeon_questions with dissolve
            play voice2 d2s9_confused noloop volume 1.6
            mc "Maybe, but where is this... really?"
            scene d19s01ntr-58 mc_lc_pd_ntr_lydias_dungeon_questions with dissolve
            play voice3 dahlia_thinking_hmm1 noloop
            lc "This is my home - my true home.{w} Conveniently located just beneath my house."
            scene d19s01ntr-59 mc_lc_pd_ntr_lydias_dungeon_questions with dissolve
            play voice2 d1s2_hmm noloop volume 1.6
            mc "You mean, we're in some basement of your parents' house?"
            scene d19s01ntr-60 mc_lc_pd_ntr_lydias_dungeon_questions with dissolve
            play voice3 dahlia_no_simple noloop
            lc "No.{w} My parents bought me the house, but I own it. And we're in... I suppose you could call it a sub-sub-basement."
            scene d19s01ntr-55 mc_lc_pd_ntr_lydias_dungeon_questions with dissolve
            play voice2 mc_arrogant_huh3 noloop
            mc "I didn't even realize there was a basement."
            scene d19s01ntr-52 mc_lc_pd_ntr_lydias_dungeon_questions with dissolve
            play voice3 lydia_aga noloop
            lc "You're better at finding g-spots than hidden doors."
        "No Questions"(hint="d19s01ntrm01c05"):

            $ d19s01ntr_no_ques = True
            pass

    jump d19s01ntr_decision

label d19s01ntr_decision:

    scene d19s01ntr-61 mc_lc_pd_ntr_lydias_dungeon_decision with dissolve
    play voice2 mc_thinking_hmm5 noloop
    if d19s01ntr_no_ques is True:
        mc "No questions."
    else:
        mc "No further questions."
    scene d19s01ntr-62 mc_lc_pd_ntr_lydias_dungeon_decision with dissolve
    play voice3 min_angry_cough noloop volume 0.7
    lc "*cough* How do you address me?"
    scene d19s01ntr-63 mc_lc_pd_ntr_lydias_dungeon_decision with dissolve
    play voice2 mc_surprised_oof1 noloop
    if d19s01ntr_no_ques is True:
        mc "I mean, \"No questions, Mistress\"."
    else:
        mc "I mean, \"No further questions, Mistress\"."
    scene d19s01ntr-64 mc_lc_pd_ntr_lydias_dungeon_decision with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    lc "Much better."
label e07_start_label hide:
    if from_ending_menu is False:
        scene d19s01ntr-65 mc_lc_pd_ntr_lydias_dungeon_decision with dissolve
    else:
        $ renpy.music.set_volume(0.6, 1.0, "music")
        scene d19s01ntr-65 mc_lc_pd_ntr_lydias_dungeon_decision with Fade(0.5, 0.5, 0.5)
        play music music_cumtusion
        play voice3 dahlia_happy_hmm1 noloop
    lc "So now, you have a choice to make."
    lc "You can choose to accept your life as my slave."
    scene d19s01ntr-66 mc_lc_pd_ntr_lydias_dungeon_decision with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "What is my other option, Mistress?"
    scene d19s01ntr-67 mc_lc_pd_ntr_lydias_dungeon_decision with dissolve
    play voice3 lydia_oops noloop
    lc "Oh no, there is no other option."
    lc "You have only one choice. You have only one option."
    scene d19s01ntr-68 mc_lc_pd_ntr_lydias_dungeon_decision with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "I see"
    scene d19s01ntr-69 mc_lc_pd_ntr_lydias_dungeon_decision with dissolve
    lc "You see... Whom?"
    scene d19s01ntr-70 mc_lc_pd_ntr_lydias_dungeon_decision with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "I see, Mistress."
label ending_07_return hide:
    scene d19s01ntr-71 mc_lc_pd_ntr_lydias_dungeon_decision with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    lc "So you've decided."
    scene d19s01ntr-72 mc_lc_pd_ntr_lydias_dungeon_decision with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Yes, Mistress. I have decided."
    $ unlock_ending("07")
    call update_ending_variables from _call_update_ending_variables_14
    menu:
        "That is a Really Good Deal"(hint="d19s01ntrm02c01"):
            $ d19s01ntr_slave = True
            scene d19s01ntr-73 mc_lc_pd_ntr_lydias_dungeon_decision with dissolve
            play voice2 mc_happy_a1 noloop
            mc "You have my heart, my soul, and my loyalty, Mistress."
            scene d19s01ntr-79 mc_lc_pd_ntr_lydias_dungeon_decision with dissolve
            play voice3 dahlia_arrogant_pff noloop
            lc "Easy words."
            scene d19s01ntr-80 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
            play voice3 dahlia_arrogant_heh noloop
            lc "I'll be certain to test your devotion once I get back from getting you... We'll call it a little surprise."
            stop music fadeout 3.0

            jump ending_07

        "Go Fuck Yourself"(hint="d19s01ntrm02c02") if from_ending_menu is False:
            scene d19s01ntr-74 mc_lc_pd_ntr_lydias_dungeon_decision with dissolve
            play voice2 mc_thinking_emm1 noloop
            mc "That sounds like a really good deal, but I have a better one."
            scene d19s01ntr-76 mc_lc_pd_ntr_lydias_dungeon_decision with dissolve
            play voice3 dahlia_angry_oh noloop
            lc "Oh?"
            scene d19s01ntr-77 mc_lc_pd_ntr_lydias_dungeon_decision with dissolve
            play voice2 mc_happy_hah2 noloop
            mc "How about I give you the finger?"
            scene d19s01ntr-78 mc_lc_pd_ntr_lydias_dungeon_decision with dissolve
            play voice2 mc_disappointed_off1 noloop
            mc "And then I want you to take a big step back{w} SHOVE YOUR HEAD UP YOUR ASS{w} AND FUCK YOUR OWN FACE!!!"
            scene d19s01ntr-75 mc_lc_pd_ntr_lydias_dungeon_decision with dissolve
            play voice2 mc_yes_yes2 noloop
            mc "...with all due respect, Mistress."
            scene d19s01ntr-79 mc_lc_pd_ntr_lydias_dungeon_decision with dissolve
            play voice3 dahlia_angry_oof noloop
            lc "What a disappointment."

            jump d19s01ntr_end

label d19s01ntr_end:

    play sound sfx_heels_steps1
    scene d19s01ntr-80 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    stop sound fadeout 2.2
    play voice3 dahlia_angry_hm1 noloop
    lc "Time will change your mind.{w} Jerome, have fun with him."
    scene d19s01ntr-81 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Oh no.{w} Is it time to \"Bring Out the Gimp\"?"
    scene d19s01ntr-82 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    play voice3 lydia_hmmmm noloop volume 1.5
    lc "Feel free to break him, but don't overdo it.{w} I'm going to go fetch his feisty redhead."
    lc "Maybe she can convince him to see the benefits of this situation."
    play sound sfx_camera_fly1
    scene d19s01ntr-83 mc_lc_pd_ntr_lydias_dungeon_end_blur with dissolve
    pause
    play voice2 mc_pain_mff3 noloop
    play sound sfx_kick3
    scene d19s01ntr-84 mc_lc_pd_ntr_lydias_dungeon_end with hpunch
    pause
    play voice2 mc_pain_cough2 noloop
    mc "Oooph!{w} *cough* That's a gut punch."
    scene d19s01ntr-85 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    play voice2 d4s4_mclaugh noloop volume 1.5
    mc "*laughing* You're probably asking yourself why I'm smiling."
    mc "It's because I know something you don't know..."
    play sound sfx_skirt_off2
    scene d19s01ntr-86 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    play voice2 mc_angry_errr4 noloop
    mc "I slipped the bindings."
    play voice3 boy4_scared_huh2_muffled noloop
    scene d19s01ntr-87 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    pause
    play sound sfx_kick2
    play voice3 boy4_pain_mmm1_muffled noloop
    scene d19s01ntr-88 mc_lc_pd_ntr_lydias_dungeon_end with vpunch
    pause
    scene d19s01ntr-89 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    pause
    play sound sfx_fall_down1
    scene d19s01ntr-90 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    pause
    scene d19s01ntr-91 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    pause
    play sound sfx_sand_run1
    scene d19s01ntr-92 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    pause
    stop sound fadeout 1.0
    play voice3 aaleyah_arrogant_hm noloop
    scene d19s01ntr-93 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    pause
    play sound sfx_sextoy_cuff2
    scene d19s01ntr-94 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    pause
    play sound sfx_sextoy_uncuff1
    scene d19s01ntr-95 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    play voice2 mc_happy_a1 noloop
    mc "That's one."
    play sound sfx_sand_run1
    scene d19s01ntr-96 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    pause
    scene d19s01ntr-97 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    pause
    stop sound fadeout 1.0
    $ renpy.music.set_volume(0.4, 5.0, "music")
    play sound sfx_sextoy_cuff2
    scene d19s01ntr-98 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "I feel just like Moses.{w} Freeing the slaves."
    play sound sfx_sextoy_uncuff1
    scene d19s01ntr-99 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    mc "Is there anyone else here?"
    scene d19s01ntr-100 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    play voice3 aaleyah_no_no1 noloop
    ah "No."
    scene d19s01ntr-101 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    play voice4 terrell_aga2 noloop
    tr "Just us."
    scene d19s01ntr-102 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Do you know where they put our clothes?"
    scene d19s01ntr-103 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    play voice3 terrell_yeah1 noloop
    tr "Uh, yeah. It should be over there."
    scene d19s01ntr-104 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Awesome."
    scene d19s01ntr-105 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    play voice3 aaleyah_happy_mmm1 noloop
    ah "You look good without them."
    scene d19s01ntr-106 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    play voice2 mc_arrogant_heh2 noloop volume 1.6
    mc "Uh, thanks..."
    scene d19s01ntr-107 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    mct "Weird thing to say..."
    scene d19s01ntr-108 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    pause
    scene d19s01ntr-109 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    play voice2 mc_scared_oh2 noloop
    mc "Oh, my phone!"
    play sound sfx_phone_tapping1 loop volume 1.8
    scene d19s01ntr-110 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    mct "There is something strange in this neighborhood. Whom am I gonna call?"
    stop sound fadeout 1.0
    scene d19s01ntr-111 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    queue sound sfx_phone_call1
    play voice2 mc_angry_errr3 noloop
    mc "Pick up!{w} AmRose!! Pick up!!!"
    mct "Damn.{w} I hope that means she's at Stacy's inside the Faraday cage."
    scene d19s01ntr-112 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    $ unlock_gallery_slot("cg", "d19s01ntr")
    pause
    play sound sfx_cloth_rustling1 volume 1.5
    scene d19s01ntr-113 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "Alright, I can't get AmRose on the phone, but at least I can call the police."
    scene d19s01ntr-114 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    play voice3 aaleyah_surprised_oh noloop
    ah "Woah, woah, woah. Wait.{w} Is that really the smart move here?"
    scene d19s01ntr-115 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "Are you serious?"
    if is_antagonist_mode is False:
        scene d19s01ntr-116 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice3 aaleyah_disappointed_eeh2 noloop
        ah "I know things look bad, but nothing is as fucked up as you think."
        scene d19s01ntr-117 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice2 mc_surprised_what3 noloop
        mc "What the hell are you talking about?"
        scene d19s01ntr-118 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice4 terrell_hey2 noloop
        tr "Some of us are here willingly.{w} We kinda enjoy... submitting."
        scene d19s01ntr-119 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice2 mc_yes_okay2 noloop
        mc "Even if that's true, Lydia abducted me-"
        scene d19s01ntr-120 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice3 aaleyah_no_nah noloop
        ah "You showed up last night passed out drunk. She didn't have to abduct you."
        scene d19s01ntr-121 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice2 mc_hey_hey4 noloop
        mc "Jerk-ass Jerome over there hit me!"
        scene d19s01ntr-124 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice4 terrell_yes noloop volume 1.5
        tr "Yeah, it's difficult to argue with that."
        scene d19s01ntr-122 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice2 mc_yes_aga1 noloop
        mc "And right now Lydia is going over to AmRose's house to abduct her and drag her back here against her will."
        scene d19s01ntr-123 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice3 aaleyah_disappointed_eh1 noloop
        ah "That is a fair point."
        scene d19s01ntr-124 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice4 terrell_geh noloop volume 1.5
        tr "Okay, but at least give some of us time to get out of here."
        scene d19s01ntr-125 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice2 mc_yes_yeah2 noloop
        mc "Fine. I'm only reporting Lydia and sending the cops to AmRose's house."
        scene d19s01ntr-126 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice3 aaleyah_happy_mmm2 noloop
        ah "Thank you."
        scene d19s01ntr-127 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice4 terrell_relief noloop
        tr "You rock."
        scene d19s01ntr-128 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice2 mc_yes_ugu1 noloop
        mc "Just get the fuck out of here."
        scene d19s01ntr-138 mc_lc_pd_ntr_lydias_dungeon with Fade(0.4, 0.2, 0.4)
        play sound sfx_phone_tapping1 loop volume 1.4
        pause
        play sound sfx_phone_call1
        scene d19s01ntr-139 mc_lc_pd_ntr_lydias_dungeon with dissolve
        "911 Operator" "Please state the nature of the emergency."
        play voice2 d1s5b_ehhh noloop volume 1.7
        mc "I need to report an abduction and an upcoming abduction attempt..."
    else:
        scene d19s01ntr-129 mc_lc_pd_ntr_lydias_dungeon_blackmailed with dissolve
        play voice3 aaleyah_disappointed_eeh2 noloop
        ah "Lydia's rich. The cops won't do anything."
        scene d19s01ntr-117 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice2 mc_surprised_what3 noloop
        mc "What the hell are you talking about?"
        scene d19s01ntr-130 mc_lc_pd_ntr_lydias_dungeon_blackmailed with dissolve
        play voice4 terrell_hey2 noloop
        tr "What if we just wait here and ambush her when she gets back?"
        scene d19s01ntr-134 mc_lc_pd_ntr_lydias_dungeon_blackmailed with dissolve
        play voice2 mc_yes_okay2 noloop
        mc "And then what? We jump her and...?"
        scene d19s01ntr-131 mc_lc_pd_ntr_lydias_dungeon_blackmailed with dissolve
        play voice3 aaleyah_angry_grrr1 noloop
        ah "Then we kill her."
        scene d19s01ntr-132 mc_lc_pd_ntr_lydias_dungeon_blackmailed with dissolve
        play voice4 terrell_yes noloop volume 1.5
        tr "We don't even have to hide the body. We just put it in one of these-"
        scene d19s01ntr-133 mc_lc_pd_ntr_lydias_dungeon_blackmailed with dissolve
        play voice2 mc_no_no4 noloop
        mc "No. Fuck that."
        scene d19s01ntr-116 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice3 aaleyah_disappointed_eh1 noloop
        ah "Well, in that case, at least let us call the cops."
        scene d19s01ntr-119 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice2 mc_arrogant_huh3 noloop
        mc "What? Why?"
        scene d19s01ntr-124 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice4 terrell_mmm1 noloop volume 1.7
        tr "You showed up drunk and passed out. You weren't abducted or forced to do anything."
        scene d19s01ntr-120 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice3 aaleyah_yes_yes2 noloop
        ah "Your story would only hurt the case. Whereas Terrell and I..."
        scene d19s01ntr-118 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice4 terrell_relief noloop
        tr "We were blackmailed, forced to come here, and...{w} tortured."
        scene d19s01ntr-122 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice2 mc_disgust_fu1 noloop
        mc "Fuck. You're right.{w} I'm sorry that happened to you."
        scene d19s01ntr-123 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice3 aaleyah_no_nah noloop
        ah "Doesn't matter now.{w} What does matter is that you get out of here."
        scene d19s01ntr-124 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice4 terrell_aga1 noloop
        tr "We'll talk to the police. We'll blow the lid off all of this. You don't need to be involved."
        scene d19s01ntr-125 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice2 d1s5_mchappy noloop volume 1.6
        mc "Thanks, I guess.{w} The police can probably find Lydia at AmRose's house."
        scene d19s01ntr-126 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice3 aaleyah_yes_aga1 noloop
        ah "We'll make sure to tell them."
        scene d19s01ntr-127 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice4 terrell_hey1 noloop volume 1.2
        tr "Just get out of here. You can't do anything to help here."
        scene d19s01ntr-128 mc_lc_pd_ntr_lydias_dungeon_end with dissolve
        play voice2 mc_yes_okay1 noloop
        mc "Okay."
        scene d19s01ntr-136-1 mc_lc_pd_ntr_lydias_dungeon_blackmailed with Fade(0.4, 0.2, 0.4)
        play voice2 mc_angry_hm1 noloop
        mct "I had no idea there was an entire dungeon in there."
        scene d19s01ntr-136-2 mc_lc_pd_ntr_lydias_dungeon_blackmailed with dissolve
        play voice2 d14s16_smell noloop
        mct "It's weird being back up here where everything is normal."

    stop music fadeout 3.5
    jump d19s02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
