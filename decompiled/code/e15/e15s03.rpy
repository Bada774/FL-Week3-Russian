image e15s03-a67-1 = Movie(play = "images/E-15/s03/anims/e15s03-a67-01-2x-50fps.webm", start_image = "e15s03-a67-01 onboarding_olivia_toilet_arj_talk_anim-67-01-00_i")
image e15s03-a67-2 = Movie(play = "images/E-15/s03/anims/e15s03-a67-02-2x-50fps.webm", start_image = "e15s03-a67-02 onboarding_olivia_toilet_arj_talk_anim-67-02-00")
image e15s03-a67-3 = Movie(play = "images/E-15/s03/anims/e15s03-a67-03-2x-50fps.webm", start_image = "e15s03-a67-03 onboarding_olivia_toilet_arj_talk_anim-67-03-00_i")
image e15s03-a67-4 = Movie(play = "images/E-15/s03/anims/e15s03-a67-04-2x-50fps.webm", start_image = "e15s03-a67-04 onboarding_olivia_toilet_arj_talk_anim-67-04-01")

image e15s03-a78-1 = Movie(play = "images/E-15/s03/anims/e15s03-a78-01-2x-50fps.webm", start_image = "e15s03-a78-01 onboarding_olivia_toilet_mk_talk_anim-78-01-00_i")
image e15s03-a78-2 = Movie(play = "images/E-15/s03/anims/e15s03-a78-02-2x-50fps.webm", start_image = "e15s03-a78-02 onboarding_olivia_toilet_mk_talk_anim-78-02-00_i")
image e15s03-a78-3 = Movie(play = "images/E-15/s03/anims/e15s03-a78-03-2x-50fps.webm", start_image = "e15s03-a78-03 onboarding_olivia_toilet_mk_talk_anim-78-03-_0_61_i")
image e15s03-a78-4 = Movie(play = "images/E-15/s03/anims/e15s03-a78-04-2x-50fps.webm", start_image = "e15s03-a78-04 onboarding_olivia_toilet_mk_talk_anim-78-04-00")

image e15s03-a112-1 = Movie(play = "images/E-15/s03/anims/e15s03-a112-1-2x-50fps.webm", start_image = "e15s03-a112-1 sy-handjob-anim-01")
image e15s03-a112-1-f = Movie(play = "images/E-15/s03/anims/e15s03-a112-1-2x-60fps.webm", start_image = "e15s03-a112-1 sy-handjob-anim-01")
image e15s03-a112-2 = Movie(play = "images/E-15/s03/anims/e15s03-a112-2-2x-50fps.webm", start_image = "e15s03-a112-2 sy-handjob-anim-01")
image e15s03-a112-2-f = Movie(play = "images/E-15/s03/anims/e15s03-a112-2-2x-60fps.webm", start_image = "e15s03-a112-2 sy-handjob-anim-01")
image e15s03-a112-3 = Movie(play = "images/E-15/s03/anims/e15s03-a112-3-2x-50fps.webm", start_image = "e15s03-a112-3 sy-handjob-anim-01")
image e15s03-a112-3-f = Movie(play = "images/E-15/s03/anims/e15s03-a112-3-2x-60fps.webm", start_image = "e15s03-a112-3 sy-handjob-anim-01")

image e15s03-a137-1 = Movie(play = "images/E-15/s03/anims/e15s03-a137-01-2x-50fps.webm", start_image = "e15s03-a137-01 onboarding_olivia_toilet_os_talk_animation-137-01-00_i")
image e15s03-a137-2 = Movie(play = "images/E-15/s03/anims/e15s03-a137-02-2x-50fps.webm", start_image = "e15s03-a137-02 onboarding_olivia_toilet_os_talk_animation-137-02-00_i")
image e15s03-a137-3 = Movie(play = "images/E-15/s03/anims/e15s03-a137-03-2x-50fps.webm", start_image = "e15s03-a137-03 onboarding_olivia_toilet_os_talk_animation-137-03-00")
image e15s03-a137-4 = Movie(play = "images/E-15/s03/anims/e15s03-a137-04-2x-50fps.webm", start_image = "e15s03-a137-04 onboarding_olivia_toilet_os_talk_animation-137-04-00")

label e15s03:

    scene black
    show screen scene_transistion(_("The next day"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.7, 0.0, "music")
    queue music music_youarehired fadein 2.5
    scene e15s03-01 onboarding_olivia_sitting_desk
    with Fade(0.5, 0.5, 0.5)
    pause
    scene e15s03-02 onboarding_olivia_knock with dissolve
    call knock from _call_knock_28
    scene e15s03-03 onboarding_olivia_mc_talk_sy with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Want to get the door, intern?"
    mc "I'm sure it's Olivia."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_cloth_rustling1 noloop volume 1.5
    scene e15s03-04 onboarding_olivia_sy_talk_off with dissolve
    pause
    play sound sfx_door_openclosed1
    scene e15s03-05 onboarding_olivia_sy_talk_olivia_back with dissolve
    play voice4 stacy_happy_yay2 noloop
    sy "Here she is."
    scene e15s03-06 onboarding_olivia_sy_talk_olivia with dissolve
    play voice4 stacy_oh2 noloop
    sy "Oh. I'm Stacy by the way."
    play sound sfx_cloth_rustling3
    scene e15s03-07 onboarding_olivia_os_talk_hands with dissolve
    play voice3 girl34_surprised_oh4 noloop
    ovs "Oh, right. Mr. Young's intern."
    scene e15s03-08 onboarding_olivia_sy_talk_hand with dissolve
    play voice4 stacy_yes_yap1 noloop
    if persistent.is_special is True:
        sy "I do like helping out. But I'm actually [mcname]'s sister."
    else:
        sy "I'm actually [mcname]'s best friend."
    scene e15s03-09 onboarding_olivia_sy_talk_os_look_mc with dissolve
    pause
    scene e15s03-11 onboarding_olivia_os_talk_os_look_sy with dissolve
    play voice3 girl34_disappointed_oh3 noloop
    ovs "Oh. Are you starting to work here too?"
    scene e15s03-10 onboarding_olivia_sy_talk_smiling with dissolve
    play voice4 stacy_no_simple1 noloop
    sy "No, just visiting."
    if persistent.is_special is True:
        sy "Well, and having fun with my big bro."
    else:
        sy "Well, and having fun with the best guy I know."
    scene e15s03-11 onboarding_olivia_os_talk_os_look_sy with dissolve
    play voice3 girl34_disappointed_eeh2 noloop
    ovs "I-I... I see."
    scene e15s03-12 onboarding_olivia_os_talk_focus_mc with dissolve
    play voice3 girl34_thinking_emm1 noloop
    ovs "Well, I am here, Mr. Young."
    scene e15s03-13 onboarding_olivia_mc_talk with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Please, call me [mcname]."
    scene e15s03-14 onboarding_olivia_os_talk_smile with dissolve
    play voice3 girl34_yes_aga4 noloop
    ovs "Okay. [mcname]."
    play sound sfx_chair_slide1
    play sound2 sfx_heels_steps2
    scene e15s03-15 onboarding_olivia_mc_talk_stand with dissolve
    pause
    stop sound2 fadeout 1.0
    scene e15s03-16 onboarding_olivia_mc_talk_gesture with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "So. We're all set to go on my end."
    mc "But if there is anything you'd like to ask me, feel free."
    scene e15s03-17 onboarding_olivia_mc_talk_side with dissolve
    play voice2 mc_thinking_hmm1 noloop
    if persistent.is_special is True:
        mc "Naturally, there might be some things that you'd like to ask without your parents around."
    else:
        mc "I imagine there might be some things you'd like to ask without your employers around."
    scene e15s03-18 onboarding_olivia_os_talk_shake with dissolve
    play voice3 girl34_no_nouh5 noloop volume 1.3
    ovs "Nothing comes to mind."
    scene e15s03-19 onboarding_olivia_mc_talk_nobuy with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Surely there is something you want to ask me."
    scene e15s03-20 onboarding_olivia_os_talk_question with dissolve
    play voice3 girl34_thinking_emm3 noloop
    ovs "So... will we be having sex? You and I?"
    scene e15s03-21 onboarding_olivia_mc_talk_smug with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "We'll only ever do what you are comfortable with, Olivia."
    scene e15s03-22 onboarding_olivia_mc_talk_sideshot with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "Everyone is different, but I've definitely found a lot of success pairing lessons about watersports with sexual relief."
    mc "But we also have people who prefer massages or yoga to get them into the right mindset to learn."
    scene e15s03-23 onboarding_olivia_mc_talk_sideshot with dissolve
    mc "It's really up to you. But I can say that nothing beats the rush of pissing all over someone right after you had an incredible orgasm."
    play voice2 mc_thinking_hm noloop
    mc "So, did that answer your question?"
    if persistent.is_special is True:
        scene e15s03-25 onboarding_olivia_os_talk_kinky with dissolve
        play voice3 girl34_happy_yeah2 noloop
        ovs "Yes. You know my friend Penny said that you made every lesson with her a very..."
        ovs "Memorable, and... addictive experience."
        scene e15s03-26 onboarding_olivia_mc_talk_os_blush with dissolve
        play voice2 mc_thinking_hmm8 noloop
        mc "Well, I'm sure I can do the same for you."
        scene e15s03-27 onboarding_olivia_mc_talk_mc_smile with dissolve
        play voice2 mc_yes_okay3 noloop
        mc "Let's continue on."
    else:
        scene e15s03-24 onboarding_oliviaos_talk_thinking with dissolve
        play voice3 girl34_yes_happy2 noloop
        ovs "Yes. I'm uh... I think I'm getting a little excited to begin our first class, [mcname]."
        scene e15s03-27 onboarding_olivia_mc_talk_mc_smile with dissolve
        play voice2 mc_thinking_hmm8 noloop
        mc "Patience, Olivia. We'll be in the thick of it soon enough."
        scene e15s03-26 onboarding_olivia_mc_talk_os_blush with dissolve
        play voice3 girl34_disappointed_mmf4 noloop
        ovs "Mmm."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene e15s03-28 onboarding_olivia_mc_lead_out with dissolve
    pause
    play sound sfx_door_openclosed1
    stop sound2 fadeout 1.0
    stop music fadeout 3.0

    jump e15s03_pool

label e15s03_pool:

    play sound4 sfx_waterfall_cathedral fadein 3.5
    $ renpy.music.set_volume(1.0, 0.0, "music2")
    play music2 music_waterfall_cathedral fadein 3.0
    scene e15s03-29 onboarding_olivia_mc_talk_pool_room with Fade(0.6, 1.0, 0.6)
    play voice2 mc_yes_yeah4 noloop
    mc "And this is the pool room. It's perfect for a nice, relaxing dip if the training gets too hard."
    scene e15s03-30 onboarding_olivia_os_talk_nervous with dissolve
    play voice3 girl34_thinking_emm2 noloop
    ovs "Does that happen often?"
    scene e15s03-31 onboarding_olivia_mc_talk_shake with dissolve
    play voice2 mc_no_uhuh1 noloop
    mc "I haven't failed a student yet, Olivia. And I don't think you will be the first."
    scene e15s03-31 onboarding_olivia_mc_talk_waves_os_smile with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Min and I have put our heart and soul into this place. It's our proudest achievement."
    scene e15s03-32 onboarding_olivia_mc_talk_waves_os_smile with dissolve
    mc "We spent six months on just research alone, figuring out how to make the best spa experience possible."
    scene e15s03-33 onboarding_olivia_mc_talk_turnback_proud with dissolve
    play voice2 mc_happy_a1 noloop
    mc "And now we're going steadily in our second year. But I still hold myself to the same standard as when we just started out."
    scene e15s03-34 onboarding_olivia_mc_talk_proud with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "I promise to be a determined and fair-minded teacher to you."
    scene e15s03-35 onboarding_olivia_os_talk_relieved with dissolve
    play voice3 girl34_happy_nice1 noloop
    ovs "That's very good to hear."
    scene e15s03-36 onboarding_olivia_sy_talk_smiles with dissolve
    play voice4 stacy_arrogant_ha2 noloop
    sy "And if he does anything dumb, you just tell me and I'll kick his butt for you."
    scene e15s03-37 onboarding_olivia_os_talk_mc_unamused with dissolve
    play voice3 girl34_no_nah3 noloop
    ovs "I don't think there will be any problems."
    scene e15s03-38 onboarding_olivia_os_talk_lookaround with dissolve
    play voice3 girl34_thinking_emm5 noloop
    if persistent.is_special is True:
        ovs "After I heard about this place, it became a fascination."
        ovs "Obviously, I want to do well for my parents."
        ovs "But I'm also very eager to try out watersports."
        scene e15s03-39 onboarding_olivia_os_talk_handmouth with dissolve
        play voice3 girl34_disappointed_mmf2 noloop
        ovs "It always seemed like such a... kinky fetish."
        scene e15s03-40 onboarding_olivia_sy_talk_mmmm with dissolve
        play voice4 stacy_yes_ugu1 noloop
        sy "Mmhmm."
    else:
        ovs "I'm here to improve my skill set, and I don't plan to let Mr. and Mrs. Melville down."
        scene e15s03-41 onboarding_olivia_os_talk_fist_kinky with dissolve
        play voice3 girl34_happy_laugh1 noloop
        ovs "They treat me very nicely, and they seem very interested in having a maid who is well-versed in watersports."
        ovs "Among other areas."
        scene e15s03-42 onboarding_olivia_sy_talk_surprised with dissolve
        play voice4 stacy_thinking_oh2 noloop
        sy "Oooouhah."
    scene e15s03-43 onboarding_olivia_mc_talk_clap with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Well then, we should move on to the next part of the tour."
    scene e15s03-44 onboarding_olivia_mc_talk_flirty with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "It's important that you know all the different areas, but I'd be lying if I said I wasn't interested to get your training started."
    scene e15s03-45 onboarding_olivia_os_talk with dissolve
    play voice3 girl34_yes_happy3 noloop
    ovs "Please, lead the way, [mcname]."
    stop sound4 fadeout 2.0
    stop music2 fadeout 3.0
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    play sound3 sfx_door_openclosed2 noloop volume 1.6
label replay_e15s03:
    if _in_replay:
        play sound sfx_heels_steps1 loop
        play sound2 sfx_heels_steps2
        play sound3 sfx_door_openclosed2 noloop volume 1.6
    scene e15s03-46 onboarding_olivia_sy_talk_impressed_osconfused_walkin with dissolve
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene e15s03-47 onboarding_olivia_sy_talk_impressed_osconfused with dissolve
    play music music_toilette_breeze
    play voice4 stacy_surprised_wow1 noloop
    sy "Woah. You really weren't kidding about human toilets."
    scene e15s03-48 onboarding_olivia_os_talk_ with dissolve
    play voice3 girl34_thinking_eeh2 noloop
    ovs "Haven't you been here before, Stacy?"
    scene e15s03-49 onboarding_olivia_sy_talk_smile with dissolve
    play voice4 stacy_no_nope1 noloop
    sy "Nope. He and Min have been keeping me busy in other areas."
    sy "But this is perfect. I get to experience it first with you, Olivia."
    scene e15s03-50 onboarding_olivia_os_talk with dissolve
    play voice3 girl34_yes_neutral8 noloop
    ovs "Yes..."
    scene e15s03-52 onboarding_olivia_mc_talk_pointing with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "As you can see here, we have stations set up for guys and girls to use as they wish."
    scene e15s03-53 onboarding_olivia_os_talk_worried with dissolve
    play voice3 girl34_disappointed_eem4 noloop
    ovs "Not a... not a lot of privacy."
    scene e15s03-54 onboarding_olivia_mc_talk_finger with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "That's by design. Watersports like a lot of fetishes, requires a liberated mind."
    mc "Opening yourself up and unlimbering yourself from usual restrictions goes a long way."
    scene e15s03-55 onboarding_olivia_os_talk with dissolve
    play voice3 girl34_surprised_wow2 noloop
    ovs "I see. You really know your stuff, [mcname]."
    play sound sfx_jeans_fly1
    scene e15s03-56 onboarding_olivia_mc_talk_taking_pantsoff with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "I've had a lot of lessons and experience. But I started out just like this."
    scene e15s03-57 onboarding_olivia_os_talk with dissolve
    play voice3 girl34_surprised_huh3 noloop
    ovs "Really?"
    play sound sfx_jeans_on1
    scene e15s03-58 onboarding_olivia_mc_talk with dissolve
    play voice2 d2s9_confused noloop volume 1.8
    mc "Well, technically it was a college bathroom, but the principle is the same."
    mc "I had to open up my mind to experience new pleasures."
    play sound sfx_skirt_off2
    play voice2 mc_hey_hey7 noloop
    mc "But overall, the best way to get to know the fetish is to dive right in."
    if date_arj_sexslave is True:
        scene e15s03-60 onboarding_olivia_arj_slave_mc_talk_arj with dissolve
        play voice2 mc_happy_a1 noloop
        mc "Ah, good morning, Am-Rose."
        scene e15s03-61 onboarding_olivia_arj_slave_arj_talk with dissolve
        play voice5 amrose_hey_whisper noloop
        arj "Good morning, Master."
        arj "I'm so happy you're visiting me today. That's always the best."
        scene e15s03-62 onboarding_olivia_arj_slave_mc_talk_gestures with dissolve
        play voice2 mc_thinking_mmm5 noloop
        mc "Come and watch you two."
        scene e15s03-63 onboarding_olivia_arj_slave_sy_talk_wave with dissolve
        play voice4 stacy_hey_happy1 noloop
        sy "Hi AmRose."
        scene e15s03-64 onboarding_olivia_arj_slave_arj_talk with dissolve
        play voice5 amrose_hey_active2 noloop
        arj "Hello Stacy. Who's this?"
        scene e15s03-65 onboarding_olivia_arj_slave_sy_talk with dissolve
        play voice4 stacy_disappointed_oh5 noloop
        sy "Oh, this is Olivia. [mcname]'s new student."
        scene e15s03-66 onboarding_olivia_arj_slave_mc_talk_oswaves with dissolve
        pause
        scene e15s03-a67-01 onboarding_olivia_toilet_arj_talk_anim-67-01 with dissolve
        play voice2 mc_arrogant_huh1 noloop
        mc "Going in front of other people is strange at first, but in my experience, it's a matter of practice makes perfect."


        $ Lovense.stop()

        play sound sfx_piss_loop1 loop
        play sound2 sfx_piss_loop2
        scene e15s03-a67-1 with dissolve
        $ Lovense.vibrate(10)
        play voice5 amrose_old_moaning
        play voice2 mc_sex_openmoans1
        "*pissing*"
        scene e15s03-a67-2 with dissolve
        play voice5 min_old_sinking
        arj "*soft moaning*"
        arj "Yes...."
        scene e15s03-a67-1 with dissolve
        play voice5 amrose_old_moaning2
        arj "Keep going, Master."
        arj "Give me all that hot, warm piss."
        pause
        scene e15s03-a67-3 with dissolve
        play voice5 min_old_sinking
        arj "Your slave wants every drop."
        arj "Ahhuaahhh..."
        pause
        scene e15s03-a67-4 with dissolve
        arj "If you're every in need of relief, you know you can always come and use me."
        mc "I know, AmRose. You're a good little slut."
        arj "*moaning*"
        pause
        stop sound fadeout 1.0
        stop sound2 fadeout 1.0
        stop voice5 fadeout 1.0
        $ Lovense.vibrate(3)
        scene e15s03-73 onboarding_olivia_toilet_mc_talk_os_staring with dissolve
        play voice2 mc_thinking_hmm2 noloop
        mc "I'll try to check on you later, AmRose."
        scene e15s03-74 onboarding_olivia_toilet_arj_talk with dissolve
        play voice5 amrose_happy_yes1 noloop
        arj "*sighing happily* Yes, Master. Awhuaahh..."
    if date_mk_tr is True:
        scene e15s03-75 onboarding_olivia_toilet_of_maria_mc_talk with dissolve
        play voice2 mc_thinking_oh1 noloop
        mc "Ah, and here is Maria. Looks like she's already had a lot of visitors."
        scene e15s03-76 onboarding_olivia_toilet_of_maria_sy_talk with dissolve
        play voice4 stacy_happy_laugh3 noloop
        sy "Hehehe."
        scene e15s03-77 onboarding_olivia_toilet_of_maria_mk_talk with dissolve
        play voice5 maria_aah noloop
        mk "Ahhuaahhah."
        scene e15s03-77-1 onboarding_olivia_toilet_of_maria_mc_talk_snap with dissolve
        play voice2 mc_hey_hey10 noloop
        mc "Hey, Maria, are you there?"
        scene e15s03-77-2 onboarding_olivia_toilet_of_maria_mk_talk_notice with dissolve
        play voice5 maria_what noloop
        mk "Oh hey, [mcname]. How's it going?"
        scene e15s03-77-3 onboarding_olivia_toilet_of_maria_mc_talk_turnedon with dissolve
        play voice2 mc_yes_yeah2 noloop
        mc "It's good, Maria. This is Olivia. She's my new student."
        scene e15s03-77-4 onboarding_olivia_toilet_of_maria_mk_talk_olivia with dissolve
        play voice5 min_hey_greeting noloop
        mk "Hey Olivia. I'm Maria, the biggest slut of the entire spa."
        scene e15s03-77-5 onboarding_olivia_toilet_of_maria_os_talk_flustered with dissolve
        play voice3 girl34_surprised_oh5 noloop
        ovs "Really?"
        scene e15s03-77-6 onboarding_olivia_toilet_of_maria_mk_talk_smile with dissolve
        play voice5 maria_yes noloop
        mk "Oh yeah. Just ask anyone. Dicks, pussies, tits, and asses... I love them all."
        scene e15s03-77-7 onboarding_olivia_toilet_of_maria_mc_talk_os with dissolve
        play voice2 mc_thinking_mmm7 noloop
        mc "Maria is the perfect example of someone who really pushed themselves to experiment with new fetishes."
        mc "For a while, she thought she was just a lesbian, but she's actually a whore for just about anything."
        scene e15s03-77-8 onboarding_olivia_toilet_of_maria_mk_talk with dissolve
        play voice5 min_disappointed_mph noloop
        mk "And I have [mcname] to thank for that. And speaking of thanks, how about you freshen me up, [mcname]?"
        mk "It's already been five minutes since someone used me!"
        scene e15s03-77-9 onboarding_olivia_toilet_of_maria_sy_talk_grinning with dissolve
        play voice4 stacy_disappointed_oh3 noloop
        sy "You poor thing."
        scene e15s03-a78-01 onboarding_olivia_toilet_mk_talk_anim-78-01 with dissolve
        play voice2 mc_yes_yes3 noloop
        mc "I think I can help."
        $ Lovense.vibrate(10)
        scene e15s03-a78-1 with dissolve
        play voice5 cynthia_sex_watersports
        play voice2 mc_sex_openmoans1
        play sound sfx_piss_loop1 loop
        play sound2 sfx_piss_loop2
        mk "Awhhuaaaahhh."
        mk "*gargling*"
        mc "As you can see, Maria loves when I piss right into her mouth."
        pause
        scene e15s03-a78-2 with dissolve
        ovs "..."
        mc "This can be a bit of an advanced technique, the taste alone is a shock."
        mc "But Maria is a Master Slut."
        mc "Isn't that right?"
        scene e15s03-a78-3 with dissolve
        mk "Mrrrrlrl-ffffff-llrrrrgggh."
        play voice4 stacy_moan6 noloop
        sy "Ooouhah. Keep filling her up, [mcname]."
        scene e15s03-a78-4 with dissolve
        play voice2 mc_hey_hey5 noloop
        mc "Don't feel like you'll have to do this on your first try, Olivia."
        mc "But it's certainly super hot just watching a hot girl gurgle down a full load of your piss."
        $ Lovense.vibrate(1)
        scene e15s03-85 onboarding_olivia_toilet_os_talk_hmm with dissolve
        play voice3 girl34_happy_relief3 noloop
        ovs "Mmmhmm..."
        stop sound fadeout 1.0
        stop sound2 fadeout 1.0
        stop voice5 fadeout 1.0
        stop voice2 fadeout 1.0

    jump e15s03_female_toiltes

label e15s03_female_toiltes:

    scene e15s03-86 onboarding_olivia_toilet_mc_talk_female_toilets_intro with dissolve
    play voice3 girl34_surprised_ohmy2 noloop
    ovs "Oh my."
    scene e15s03-87 onboarding_olivia_toilet_sy_talk with dissolve
    play voice4 stacy_happy_relief1 noloop
    sy "Nice."
    scene e15s03-88 onboarding_olivia_toilet_mc_talk_dee with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "This is Dee. She graduated last month, but she decided to extend her stay."
    scene e15s03-89 onboarding_olivia_toilet_db_talk_smile with dissolve
    play voice5 girl30_arrogant_hah1 noloop
    db "I'm totally going to leave in a week. I promise, [mcname]."
    scene e15s03-90 onboarding_olivia_toilet_mc_talk_dee with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, I've heard that before."
    mc "You're always welcome here, Dee."
    scene e15s03-91 onboarding_olivia_toilet_db_talk with dissolve
    play voice5 girl30_disappointed_oh2 noloop volume 1.5
    db "Oooh, who's the new girl?"
    scene e15s03-92 onboarding_olivia_toilet_mc_talk_intro_os with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "This is Olivia. My newest student."
    scene e15s03-93 onboarding_olivia_toilet_db_talk with dissolve
    play voice5 girl30_hey_greeting noloop
    db "Welcome Olivia. You here to watch my old teacher cover my face in his tasty piss?"
    db "It's simply the best."
    scene e15s03-94 onboarding_olivia_toilet_mc_talk_thinking with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Actually, Olivia, maybe you should take the lead."
    scene e15s03-95 onboarding_olivia_toilet_os_talk_olivia_catch with dissolve
    play voice3 girl34_disappointed_mmf1 noloop
    pause
    scene e15s03-96 onboarding_olivia_toilet_mc_talk_olivia with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "Olivia?"
    scene e15s03-97 onboarding_olivia_toilet_os_talk_olivia with dissolve
    play voice3 girl34_thinking_mmm noloop
    ovs "Hmmm?"
    scene e15s03-98 onboarding_olivia_toilet_mc_talk_gesture with dissolve
    play voice2 mc_thinking_hmm6 noloop
    mc "Would you like to piss on Dee's lovely face?"
    scene e15s03-99 onboarding_olivia_toilet_db_talk with dissolve
    play voice5 girl30_hey_whisper noloop
    db "I promise, I don't bite. Unless you ask."
    db "And that probably won't happen till I'm done playing toilet, haha."
    scene e15s03-100 onboarding_olivia_toilet_os_talk_unsure with dissolve
    play voice3 girl34_disappointed_eeh1 noloop
    ovs "I don't know about this..."
    scene e15s03-101 onboarding_olivia_toilet_mc_talk_thinking with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mc "Of course. Well, maybe we can try another way to get you started."
    scene e15s03-102 onboarding_olivia_toilet_mc_talk_looseningup with dissolve
    play voice2 d14s16_smell noloop
    mc "Just take a breath, nice and calmly. Try to relax, and let my voice guide you."
    scene e15s03-103 onboarding_olivia_unsure with dissolve
    play voice3 girl34_yes_ugu1 noloop
    ovs "O-okay."
    scene e15s03-104 onboarding_olivia_mc_talk with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "Watersports is all about letting go, literally and mentally."
    mc "The pleasure you get when that happens is so perfect."
    scene e15s03-105 onboarding_olivia_mc_talk_sy_look with dissolve
    play voice4 stacy_happy_hmm1 noloop volume 0.5
    mc "It's like that moment you slide onto a slip-n-slide during a hot summer day."
    mc "And when you do it the first time, you'll think-"
    scene e15s03-104 onboarding_olivia_mc_talk with dissolve
    play voice2 mc_surprised_how3 noloop
    mc "'How is this the first time I'm doing this?'"
    scene e15s03-109 onboarding_olivia_mc_talk_mc_look_sy with dissolve
    play voice2 mc_happy_hah2 noloop
    if date_arj_sexslave is True or date_mk_tr is True:
        mc "I don't need to piss anymore, but I'm sure I can give Dee something else."
    else:
        mc "I actually don't need to piss right now, but I'm sure I can give Dee something else."
        scene e15s03-108 onboarding_olivia_db_talk with dissolve
        play voice5 girl30_yes_aga1 noloop
        db "Ready and waiting, [mcname]."
    scene e15s03-110 onboarding_olivia_sy_talk with dissolve
    if persistent.is_special is True:
        mc "Help a brother out?"
    else:
        mc "Can you lend me a hand."
    play voice4 stacy_yes_yap2 noloop
    sy "Of course."
    scene e15s03-a112-1 sy-handjob-anim-01 with dissolve
    pause
    $ Lovense.pattern("7;12", 1400)
    scene e15s03-a112-1
    play voice2 mc_sex_openmoans2
    play voice4 stacy_moans2
    play sound sfx_handjob_cream1 loop
    play voice5 cynthia_sex_openmoans2
    mc "*lightly moaning*"
    mc "No... I can't cum on command, but you can see how eager my cock is already."
    pause
    scene e15s03-a112-2 with dissolve
    play voice3 girl34_yes_neutral7 noloop
    ovs "Yes..."
    db "Mmmm..."
    pause
    scene e15s03-a112-3 with dissolve
    mc "That's it, Stacy. Nrraah."
    pause
    $ Lovense.pattern("7;12", 700)
    scene e15s03-a112-1-f with dissolve
    if persistent.is_special is True:
        ovs "You're so bold, [mcname]."
        sy "Haha, you should have met him when he was younger."
        pause
        scene e15s03-a112-2-f with dissolve
        sy "Whole different story."
        mc "Well, I finally found my way."
        sy "Yup. With my help."
        pause
        scene e15s03-a112-3-f with dissolve
        play voice3 girl36_sex_closedmoans1
        ovs "*softly moans* U-um... that is... I'm very happy for you both."
    else:
        sy "Mmm. You're so nice and hot today, [mcname]."
        sy "This really is the best job for you."
        scene e15s03-a112-2-f with dissolve
        play voice3 girl36_sex_closedmoans1
        ovs "I don't mind. T-this... is part of my lessons."
        ovs "I want to be the best maid I can be."
        pause
        scene e15s03-a112-3-f with dissolve
        sy "Ooouhah. Maybe {b}you{/b} should hire her here, [mcname]."
    mc "Nhrra... get ready, Dee."
    mc "Keep going, Stacy. Let's give Olivia a show."
    sy "*playful moaning* Way ahead of you."
    scene e15s03-129 onboarding_olivia_mc_talk_cumming
    play voice2 mc_sex_orgasm1 noloop
    stop voice3 fadeout 1.0
    stop voice4 fadeout 1.0
    play voice5 cynthia_sex_openmoans1 noloop
    play sound mc_cum_sound1 volume 1.5
    $ Lovense.stop()
    $ Lovense.vibrate(18)
    with hpunch
    mc "Oh fuck."
    stop voice5 fadeout 1.5
    $ Lovense.vibrate(2)
    scene e15s03-129-1 onboarding_olivia_mc_talk_cumming with dissolve
    pause
    scene e15s03-130 onboarding_olivia_os_talk with dissolve
    play voice3 girl34_happy_relief1 noloop
    ovs "Oouhaah*"
    stop sound fadeout 1.0
    pause
    play sound sfx_cloth_rustling2 volume 1.4
    scene e15s03-131 onboarding_olivia_sy_talk_smiling with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "So... ahem. Do you think you can give it a go now?"
    scene e15s03-132 onboarding_olivia_os_talk with dissolve
    play voice3 girl34_disappointed_eem4 noloop
    ovs "I... well I'm certainly turned on, do you think that will help?"
    play voice4 stacy_yes_yap3 noloop
    sy "I only piss when I'm turned on."
    ovs "O-Okay..."
    play sound sfx_skirt_off2
    scene e15s03-133 onboarding_olivia_os_standn_front with dissolve
    pause
    play voice3 girl34_surprised_ah4 noloop
    ovs "Oh."
    scene e15s03-135 onboarding_olivia_mc_talk with dissolve
    play voice2 d2s9_mchey noloop
    mc "There is absolutely no rush, Olivia. This is your training."
    play sound sfx_cloth_rustling3
    scene e15s03-136 onboarding_olivia_os_talk with dissolve
    pause
    scene e15s03-a137-01 onboarding_olivia_toilet_os_talk_animation-137-01 with dissolve
    play voice2 d1s5_mchappy noloop
    mc "Take as much time as you-"
    play voice3 chastity_openmoans3
    play sound sfx_piss_loop1 loop
    play sound2 sfx_piss_loop2
    play voice5 cynthia_sex_watersports
    $ Lovense.vibrate(10)
    scene e15s03-a137-1 with dissolve
    ovs "Ooouhah."
    ovs "Oh my god, I'm pissing."
    ovs "Pissing in front of people. And on a girl's face!"
    ovs "I should stop. Stop at once."
    pause
    scene e15s03-a137-2 with dissolve
    ovs "This isn't good behavior. But... it feels so {b}good{/b}."
    play voice2 d9s2_ugu noloop volume 2.5
    mc "Just keep going, Olivia."
    mct "Looks like all we had to do was loosen the lid."
    mct "She's pissing so much."
    pause
    play voice4 stacy_surprised_ohmy1 noloop
    scene e15s03-a137-3 with dissolve
    sy "Oooouhah. She's really getting into it."
    sy "Go Olivia!"
    db "*gurgling*"
    pause
    scene e15s03-a137-4 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Good girl, Olivia."
    ovs "Ahhuaaahh."
    mc "You too, Dee."
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    stop voice5 fadeout 1.0
    play voice3 chastity_orgasm noloop
    $ Lovense.vibrate(15)
    scene e15s03-145 onboarding_olivia_end_os_talk with hpunch
    ovs "Ahuuah... that... I can't believe I did that."
    $ Lovense.vibrate(1)
    scene e15s03-148 onboarding_olivia_end_db_talk_os_silen with dissolve
    play voice5 girl30_disgust_mmm noloop
    db "Mmmm. That was amazing, you two."
    db "Thanks for the morning loads."
    play voice3 girl34_thinking_eeh1 noloop
    ovs "You're... you're okay, Dee?"
    play voice5 girl30_happy_yeah2 noloop
    db "Of course. That's what I'm here for, Olivia. Feel free to piss on me again if you visit."
    scene e15s03-147 onboarding_olivia_end_os_talk with dissolve
    play voice3 girl34_happy_relief1 noloop
    ovs "..."
    play sound sfx_cloth_rustling1
    scene e15s03-149 onboarding_olivia_end_mc_talk_nod with dissolve
    play voice2 mc_hey_hey6 noloop
    mc "Like I said, it's just a matter of relaxing."
    mc "And trust me, with each lesson, it will get easier."
    play sound sfx_cloth_rustling2
    scene e15s03-150 onboarding_olivia_end_os_talk_sparkling with dissolve
    play voice3 girl34_happy_mmm1 noloop
    ovs "Mmmhmm. I assume there are more lessons today?"
    scene e15s03-151 onboarding_olivia_end_mc_talk with dissolve
    play voice2 mc_yes_yes7 noloop
    mc "Yes. If you'll follow me."
    scene e15s03-152 onboarding_olivia_end_sy_talk_rub_os_dress with dissolve
    play voice4 stacy_thinking_emm2 noloop
    sy "I'm going to go find some food. Getting all horny works up an appetite."
    play sound sfx_underpants_off1 volume 2.5
    scene e15s03-153 onboarding_olivia_end_sy_talk_waves__mc_dress with dissolve
    play voice4 stacy_hey_byebye noloop
    sy "I'll find you later, [mcname]."
    $ unlock_gallery_slot("scene", "e15s03")
    sy "Bye bye Olivia."
    scene e15s03-154 onboarding_olivia_end_os_talk_waves with dissolve
    play voice3 girl34_hey_bye9 noloop
    ovs "Bye Stacy."
    play sound sfx_skirt_off1
    scene e15s03-155 onboarding_olivia_end_mc_talk_lookos with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "Alright, are you ready to begin your training in earnest?"
    scene e15s03-156 onboarding_olivia_end_os_talk with dissolve
    play voice3 girl34_yes_happy1 noloop
    ovs "Yes, [mcname]."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene e15s03-157 onboarding_olivia_end_walkout with dissolve
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    stop music fadeout 3.5

    $ Lovense.stop()


    $ renpy.end_replay()

    jump e15s04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
