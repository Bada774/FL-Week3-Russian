image e16s02-a02-glambot-1 = Movie(play = "images/E-16/s02/anim/e16s02-a02-2x-50fps.webm", start_image = "e16s02-a02 mc-jf-mo-farm2-glambot-02-000_i", image = "e16s02-a02 mc-jf-mo-farm2-glambot-02-179_i", loop = False)

label e16s02:

    scene black
    show screen scene_transistion(_("A week later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound sfx_dishes_fryingpan1 fadein 2.0
    scene e16s02-01 mc-jf-mo-farm1_c1
    with Fade(0.5, 0.5, 0.5)
    $ renpy.music.set_volume(0.8, 1.0, "music")
    play music music_lizards_breakfast
    pause
    stop sound fadeout 1.5
    play sound2 sfx_dishes_slicing1 noloop
    scene e16s02-01 mc-jf-mo-farm1_c2 with dissolve
    stop sound2 fadeout 2.0
    pause
    scene e16s02-02 mc-jf-mo-farm2_c1 with dissolve
    play voice2 mc_hey_hey10 noloop
    mc "Here you go, Molly."
    scene e16s02-a02 mc-jf-mo-farm2-glambot-02-000_i with dissolve
    pause
    play voice4 girl35_zdog_breathing2 fadein 1.5
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 2.5>", sfx_camera_fly1] volume 2.0 noloop
    scene e16s02-a02-glambot-1
    pause
    play sound sfx_heels_steps1
    stop sound2 fadeout 1.0
    stop voice4 fadeout 3.0
    scene e16s02-03 mc-jf-mo-walk_c2 with dissolve
    play voice3 jessie_mmm noloop
    jf "This all smells great. Thanks for breakfast, [mcname]."
    scene e16s02-03 mc-jf-mo-walk_c1 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Of course."
    play sound sfx_plate_place1 volume 1.5
    play sound2 sfx_bed_slide3 noloop volume 0.5
    scene e16s02-05 mc-jf-mo-eat1_c1 with dissolve
    queue sound2 sfx_fork_eating1
    play voice2 d1s2_hmm noloop volume 1.5
    mc "It tastes better right? I'm not crazy."
    scene e16s02-05 mc-jf-mo-eat1_c2 with dissolve
    play voice3 min_no_nope noloop
    jf "Nope. I was thinking the same thing."
    scene e16s02-06 mc-jf-mo-eat2_c1_1 with dissolve
    play voice2 mc_eating_mmm noloop
    pause
    scene e16s02-07 mc-jf-mo-talk1_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "How about that."
    scene e16s02-07 mc-jf-mo-talk1_c2 with dissolve
    play voice3 min_thinking_oh noloop
    jf "I figured out what I want to do with this place."
    scene e16s02-08 mc-jf-mo-talk2_c1 with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Lay it on me."
    scene e16s02-06 mc-jf-mo-eat2_c2 with dissolve
    play voice3 min_thinking_hmm3 noloop
    jf "I was thinking about Molly. She loves it here, but I'm sure she didn't start at my Aunt's farm."
    play voice4 girl35_zdog_bark3 noloop
    mdog "Arff."
    jf "Maybe she grew up in a place where people weren't open-minded. I know when some people reveal some of their... kinks and likes, they get shunned by their parents."
    jf "Or worse."
    scene e16s02-11 mc-jf-mo-talk5_c1 with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yeah. When will people learn the world is such a boring place if all you eat is vanilla ice cream for every desert?"
    scene e16s02-11 mc-jf-mo-talk5_c2 with dissolve
    play voice3 min_yes_yeah1 noloop
    jf "Exactly."
    jf "So I thought that we could set the place up like a shelter. For animal-girls."
    scene e16s02-12 mc-jf-mo-talk6_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "So you want to build an animal girl farm."
    scene e16s02-12 mc-jf-mo-talk6_c2 with dissolve
    play voice3 min_thinking_emm noloop
    jf "Well, less animal farm, more like a sanctuary for people who need it."
    jf "People could come here and explore their passion in comfort and safety. No judgments."
    scene e16s02-13 mc-jf-mo-eat1_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "That sounds great. Especially if it can help people out."
    scene e16s02-13 mc-jf-mo-eat1_c2 with dissolve
    play voice3 min_yes_aga noloop
    jf "Exactly. It can be a tough world out there for people who are super into animal-play."
    play sound sfx_cloth_rustling4
    scene e16s02-13 mc-jf-mo-eat1_c3 with dissolve
    play voice3 min_thinking_hmm1 noloop
    jf "Not everyone is as lucky as me. I've had very supportive friends."
    jf "And I already found my mate."
    scene e16s02-14 mc-jf-mo-eat2_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    if d01s05_meetjf:

        mc "Yup. Prowling for pussy in the dead of night."
        scene e16s02-14 mc-jf-mo-eat2_c2 with dissolve
        play voice3 jessie_laugh noloop
        jf "I should have known then what a beast you were."
    else:


        mc "Yup. Prowling for pussy to lick at a wild kink party."
        scene e16s02-14 mc-jf-mo-eat2_c2 with dissolve
        play voice3 jessie_laugh noloop
        jf "I should have known then what a beast you were."

    jf "Bah. It's so easy to get distracted. Hmmm. I've never been this horny before."
    scene e16s02-15 mc-jf-mo-talk1_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Must be all that country air."
    scene e16s02-15 mc-jf-mo-talk1_c2 with dissolve
    play voice3 min_yes_simple noloop
    jf "I guess. Anyhow. The only issue is setting up a way to spread the word to animal-girls who might be looking for a place like what we have in mind."
    stop sound2 fadeout 1.0
    scene e16s02-16 mc-jf-mo-talk2_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Hmmm. But there must be a way to reach our consumers. Or I guess, they're more like associates in this case."
    mc "Is there like a meetup site for animal-girls?"
    scene e16s02-16 mc-jf-mo-talk2_c2 with dissolve
    play voice3 jessie_ah2 noloop
    jf "I've skirted around a couple. But we have a bigger problem."
    jf "I don't really think a post on a meetup site would be enough."
    scene e16s02-17 mc-jf-mo-talk3_c1 with dissolve
    play voice2 d9s2_ugu noloop volume 1.7
    mc "You're right. We really need our own website."
    scene e16s02-18 mc-jf-mo-talk4_c1 with dissolve
    play sound sfx_finger_snap1
    play voice2 mc_surprised_huh7 noloop
    mc "Why don't we do that?"
    scene e16s02-18 mc-jf-mo-talk4_c2 with dissolve
    play voice3 min_surprised_ehh2 noloop
    jf "Really? I wouldn't know the first step to making one."
    scene e16s02-19 mc-jf-mo-talk5_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Heh. You don't take a mountain of business classes without knowing a little web design these days."
    mc "I'll handle that end."
    play sound sfx_cloth_rustling1
    scene e16s02-19 mc-jf-mo-talk5_c2 with dissolve
    play voice3 min_surprised_oh noloop
    jf "That's great, [mcname]!"
    jf "Is there anything I can do to help?"
    scene e16s02-21 mc-jf-mo-point_c1 with dissolve
    play voice2 mc_yes_yes6 noloop
    mc "Hmm. Yes. We'll need some pictures?"
    scene e16s02-21 mc-jf-mo-point_c2 with dissolve
    play voice3 jessie_jhuh noloop
    jf "Pictures of what? The farm?"
    play voice2 mc_yes_aga1 noloop
    mc "Kind of."
    mc "We take some pictures of Molly to put them on our own website. Visual content always helps with web user traffic."
    play sound sfx_cloth_rustling5
    scene e16s02-22 mc-jf-mo-hand1_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "You can dress up, too. Other animal-girls will see how a zebra girl and a dog girl are already living at the farm."
    scene e16s02-22 mc-jf-mo-hand1_c2 with dissolve
    play voice3 jessie_yes noloop
    jf "Yes. And Kanya wanted to visit us soon anyhow. She can probably take some real professional pictures."
    scene e16s02-23 mc-jf-mo-hand2_c1 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.8
    mc "What are you saying my photos were that bad?"
    scene e16s02-23 mc-jf-mo-hand2_c2 with dissolve
    play voice3 min_no_happy noloop
    jf "They were great. I was just thinking..."
    jf "If Kanya is taking pictures... that means your hands are still free to have fun with me."
    play sound sfx_bed_slide2 volume 0.5
    scene e16s02-24 mc-jf-mo-hand3_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "Good thinking."
    scene e16s02-24 mc-jf-mo-hand3_c2 with dissolve
    pause
    scene e16s02-25 mc-jf-mo-kiss_c1 with dissolve
    play voice3 min_happy_mmm noloop
    play voice2 d1s1_mmm noloop
    play sound dahlia_kiss_french1
    pause
    scene e16s02-25 mc-jf-mo-kiss_c2 with dissolve
    play sound maria_kiss2
    pause
    $ renpy.music.set_volume(1.0, 1.0, "music")
    scene black
    show screen scene_transistion(_("After chores"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.5, 3.0, "music")
    scene e16s02-26 mc-jf-mo-phone1_c1
    with Fade(0.5, 0.5, 0.5)
    play voice3 min_happy_yay noloop
    jf "I'm so glad you like it."
    scene e16s02-26 mc-jf-mo-phone1_c2 with dissolve
    play sound sfx_keyboard_typing2 volume 1.5
    play voice3 min_yes_yeah2 noloop
    jf "Yes, [mcname] is already working hard on the website."
    scene e16s02-27 mc-jf-mo-phone2_c2 with dissolve
    play voice4 allison_phoned_hey_long noloop
    kv "Let me know if I can help out, Jessie."
    scene e16s02-26 mc-jf-mo-phone1_c1 with dissolve
    play voice3 min_surprised_huh2 noloop
    jf "You read my mind. Yeah, I wanted to see, if you weren't too busy with conventions or whatever, if could come out to the farm."
    scene e16s02-26 mc-jf-mo-phone1_c3 with dissolve
    play voice3 min_thinking_hmm2 noloop
    play voice5 girl35_zdog_snif3 noloop
    jf "You can meet Molly and then take some pictures of me and her playing around the farm."
    scene e16s02-27 mc-jf-mo-phone2_c3 with dissolve
    play voice4 allison_phoned_yes_yeah2 noloop
    kv "That sounds great. I can come over this weekend."
    scene e16s02-28 mc-jf-mo-phone3_c1 with dissolve
    play voice3 min_happy_yeah noloop
    jf "Wonderful."
    scene e16s02-28 mc-jf-mo-phone3_c2 with dissolve
    play voice4 allison_phoned_happy_relief2 noloop
    kv "I can't wait to see you two, Jessie."
    scene e16s02-27 mc-jf-mo-phone2_c1 with dissolve
    play voice3 min_yes_happy noloop
    jf "Me too. You're going to be helping us out a lot."
    scene e16s02-27 mc-jf-mo-phone2_c3 with dissolve
    play voice4 allison_phoned_thinking_eeh3 noloop
    kv "You know... maybe after the photos with Molly are done, you, me, and [mcname] can have a private shoot."
    scene e16s02-28 mc-jf-mo-phone3_c1 with dissolve
    play voice3 amrose_old_haha2 noloop volume 1.6
    jf "*Laughs nervously* You're such a slut."
    scene e16s02-28 mc-jf-mo-phone3_c2 with dissolve
    play voice4 allison_phoned_yes_aga4 noloop
    kv "A slut who wants that Dee."
    kv "But only if you're cool with that Jessie. But you know that last time I only got a teaser."
    kv "I thought that would be enough, but now I want the whole steak."
    scene e16s02-26 mc-jf-mo-phone1_c1 with dissolve
    play voice3 min_surprised_ehh1 noloop
    jf "It was pretty hot having you watch us. But... I'm not sure."
    scene e16s02-27 mc-jf-mo-phone2_c2 with dissolve
    play voice4 allison_phoned_thinking_hmm4 noloop
    kv "Come on. You're not just a little curious to try some three-player co-op."
    play voice3 jessie_mmm noloop
    jf "Hmm. I didn't think of it like that. That doesn't sound as bad."
    kv "See. It's all good, girl."
    scene e16s02-28 mc-jf-mo-phone3_c1 with dissolve
    play voice3 min_disappointed_ehh1 noloop
    jf "Okay. I think that all sounds good."
    play voice4 allison_phoned_happy_woohoo noloop
    kv "Great! I'll see you this weekend."
    scene e16s02-29 mc-jf-mo-phone4_c1 with dissolve
    play voice3 min_arrogant_heh2 noloop
    play sound ["<silence 0.5>", sfx_phone_button1] volume 3.0
    jf "Love you."
    scene e16s02-31 mc-jf-mo-ask_c2 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Everything alright?"
    scene e16s02-31 mc-jf-mo-ask_c1 with dissolve
    play voice3 min_yes_ugu noloop
    jf "Yes. She's coming over this weekend."
    play voice2 mc_scared_oh4 noloop
    mc "A little photography and chill?"
    play voice3 min_arrogant_huh2 noloop
    jf "Haha. You could say that. I think the image of you dominating me last time got seared into her brain."
    scene e16s02-31 mc-jf-mo-ask_c2 with dissolve
    play voice2 mc_thinking_hmm9 noloop
    mc "And now she wants to join in?"
    play sound sfx_cloth_rustling2
    scene e16s02-34 mc-jf-mo-pull_c1 with dissolve
    play voice3 min_disappointed_ehh3 noloop
    pause
    scene e16s02-34 mc-jf-mo-pull_c2 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Come here."
    play sound2 sfx_hair_scratch1 noloop
    scene e16s02-35 mc-jf-mo-kiss_c1 with dissolve
    play voice2 d1s5_orgasm noloop
    play sound maria_kiss2
    play voice3 min_thinking_mhh noloop
    jf "Mmm."
    scene e16s02-35 mc-jf-mo-kiss_c2 with dissolve
    play sound maria_kiss3
    pause
    scene e16s02-36 mc-jf-mo-chin_c2 with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.7
    mc "Jessie, if you're truly okay with it, I'm down."
    scene e16s02-36 mc-jf-mo-chin_c1 with dissolve
    play voice3 allison_laugh noloop
    jf "I'm okay with it. Actually... Now that I've had a moment to think about it, if I'm being completely honest, it sounds kind of exciting."
    scene e16s02-37 mc-jf-mo-rest_c2 with dissolve
    play voice2 mc_happy_yay1 noloop
    mc "Awesome."
    play sound sfx_cloth_rustling2
    scene e16s02-37 mc-jf-mo-rest_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "And no matter what, you'll always be my number one girl."
    mc "Regular, and animal-style."
    play voice3 allison_aah noloop
    jf "I don't know what I was worried about."
    scene e16s02-38 mc-jf-mo-talk_c1 with dissolve
    play voice3 min_thinking_hmm3 noloop
    jf "I think with Molly around, and knowing she is... curious about you... it made me more territorial."
    jf "Kanya is certainly as kinky as I am."
    scene e16s02-38 mc-jf-mo-talk_c2 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yup. And I think she wants more than the taste she got earlier."
    mc "But if things ever get too dicey, just say the word, sweetie."
    scene e16s02-39 mc-jf-mo-kiss_c1 with dissolve
    play sound maria_kiss1
    pause
    scene e16s02-39 mc-jf-mo-kiss_c2 with dissolve
    pause
    scene e16s02-40 mc-jf-mo-look_c1 with dissolve
    play voice3 jessie_yes noloop
    jf "I know."
    scene e16s02-40 mc-jf-mo-look_c2 with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mc "Alright, enough with the long face. Time for me to show off a truly kickass website."
    scene black
    show screen scene_transistion(_("After Jessie checks the website"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene e16s02-40-2 mc-jf-mo-stand_c1
    with Fade(0.5, 0.5, 0.5)
    play voice3 min_surprised_oh noloop
    jf "This is wonderful, [mcname]. You outdid yourself."
    scene e16s02-40-2 mc-jf-mo-stand_c2 with dissolve
    play voice2 d9s2_yeah noloop volume 1.7
    mc "Thanks. It should be easy to use."
    scene e16s02-40-3 mc-jf-mo-stand2_c1 with dissolve
    play voice3 min_happy_relief noloop
    jf "And this registration form is perfect. They can answer the questions, and we'll know their pet name if they have one, along with how active they are in pet mode."
    scene e16s02-40-3 mc-jf-mo-stand2_c2 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "I never imagined setting up a site like this with my skills, but if you're going to do a job, you better do it right."
    play sound sfx_cloth_rustling3
    scene e16s02-40-4 mc-jf-mo-stand4_c1 with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    jf "Mmhmm."
    jf "Do you think such a good job deserves a good reward."
    scene e16s02-40-4 mc-jf-mo-stand4_c2 with dissolve
    play voice2 mc_happy_laugh2 noloop
    mc "Haha. Well... now that you mention it."
    call knock from _call_knock_24
    play voice3 min_old_argh noloop
    jf "God... If those are our neighbors, their timing sucks."
    play voice2 d3s11b_mcheh noloop
    mc "Haha."
    scene e16s02-40-4 mc-jf-mo-stand4_c3 with dissolve
    play voice4 girl35_zdog_rrraf6 noloop
    mdog "Grrrr..."
    play voice2 mc_surprised_wow2 noloop
    mc "Woah. Easy girl."
    stop music fadeout 6.0
    $ renpy.music.set_volume(0.7, 3.0, "sound4")
    play sound4 park fadein 2.0
    play sound sfx_door_openclosed1
    scene e16s02-41 mc-jf-mo-stand1_c1 with fade
    queue voice4 girl35_zdog_rrraf4 noloop
    pause
    scene e16s02-41 mc-jf-mo-stand1_c2 with dissolve
    play voice5 boy4_thinking_mmm1 noloop
    pause
    scene e16s02-42 mc-jf-mo-talk1_c1 with dissolve
    play voice5 boy4_hey_simple noloop
    "Some Guy" "It really is you, Jessie."
    scene e16s02-42 mc-jf-mo-talk1_c2 with dissolve
    queue music music_villainous_brother
    play voice3 jessie_jhuh noloop
    jf "I'm sorry, do I know you?"
    scene e16s02-43 mc-jf-mo-talk2_c1 with dissolve
    play voice5 boy4_yes_yeah noloop
    rf "I should think so. Then again, it has been years. I'm Ryan, Rose's son."
    scene e16s02-43 mc-jf-mo-talk2_c2 with dissolve
    play voice3 min_thinking_oh noloop
    jf "Oh. Sorry, of course, Ryan. Yeah it's been a long time. It's nice to see you."
    scene e16s02-44 mc-jf-mo-talk3_c2 with dissolve
    play voice3 min_thinking_hmm2 noloop
    jf "So uh... how are you?"
    scene e16s02-44 mc-jf-mo-talk3_c1 with dissolve
    play voice5 boy4_arrogant_mmm1 noloop
    rf "I'll be better after this."
    play voice2 mc_thinking_mmm3 noloop
    mc "Hmm..."
    scene e16s02-45 mc-jf-mo-point_c1 with dissolve
    play voice5 boy4_disappointed_ehh2 noloop
    rf "I was pretty surprised to hear you'd come out here, Jessie."
    rf "All these years I always imagined you'd be more of a city girl."
    scene e16s02-45 mc-jf-mo-point_c2 with dissolve
    play voice3 min_yes_simple noloop
    jf "Yes, well, Rose, I mean your mom asked me to take care of the farm. So that's the plan."
    scene e16s02-47 mc-jf-mo-talk2_c2 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "And we can still drive down to the city when we want."
    play voice3 min_yes_aga noloop
    jf "Of course. Oh. Ryan, this is my boyfriend, [mcname]."
    scene e16s02-48 mc-jf-mo-talk3_c2 with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Nice to meet you."
    scene e16s02-48 mc-jf-mo-talk3_c1 with dissolve
    play sound sfx_hair_scratch1
    play voice5 boy5_yes_yeah noloop
    rf "Yeah."
    scene e16s02-50 mc-jf-mo-talk5_c1 with dissolve
    play voice5 boy4_disappointed_ehh1 noloop
    rf "Like I said, I was surprised because obviously there has been some kind of mixup with my mother's will. The house and the farm belong to me."
    scene e16s02-50 mc-jf-mo-talk5_c2 with dissolve
    play voice3 min_surprised_huh1 noloop
    jf "Huh?"
    scene e16s02-50 mc-jf-mo-talk5_c1 with dissolve
    play voice5 boy4_disappointed_oh noloop
    rf "Oh come on. Jessie. You had to realize that the will that idiot lawyer made is not a legally binding one. Before the end... my mom... she wasn't well."
    rf "She hadn't been for a long time. I'm sure you all know that a sick mind makes mistakes."
    scene e16s02-50 mc-jf-mo-talk5_c2 with dissolve
    play voice3 min_arrogant_hm noloop
    jf "Wait. If you think it was a mistake, why show up now?"
    scene e16s02-46 mc-jf-mo-talk_c1 with dissolve
    play voice5 boy4_disappointed_geh2 noloop
    rf "Some of us can't just drop out of college and travel to a farm on a moment's notice, Jessie."
    play sound sfx_cloth_rustling2
    scene e16s02-51 mc-jf-mo-talk6_c2 with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "Woah. What the hell, man?"
    scene e16s02-52 mc-jf-mo-talk7_c1 with dissolve
    play voice5 boy4_arrogant_mmm2 noloop
    rf "Excuse me. This whole thing... it's been making me super anxious."
    rf "I've been grieving for my mother and naturally didn't assume she'd bequeath her home to someone besides her son."
    scene e16s02-52 mc-jf-mo-talk7_c2 with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "But she did."
    scene e16s02-53 mc-jf-mo-talk8_c1 with dissolve
    play voice5 boy4_angry_err1 noloop
    rf "If she did, she had no idea what she was doing. I mean, think about it, Jessie, please."
    rf "You were studying art. I'm a businessman who's successfully developed several properties in the area."
    rf "Who is the better choice to take over?"
    scene e16s02-53 mc-jf-mo-talk8_c2 with dissolve
    play voice2 mc_no_uhuhno noloop
    mc "We're not leaving. We've already started turning this place into a home."
    scene e16s02-45 mc-jf-mo-point_c1 with dissolve
    play voice5 boy4_hey_angry noloop
    rf "Jessie listen to me. This kind of thing isn't for you. There is no shame in admitting that."
    rf "What are you going to do with a big farm like this?"
    play sound sfx_paper_rustl1 volume 1.5
    scene e16s02-54 mc-jf-mo-check_c1 with dissolve
    play voice5 boy4_happy_mmm2 noloop
    rf "And of course, I'll compensate you for the hassle. It's all silly, just some clerical error, and I'm quite embarrassed about it."
    rf "But I'll still do right by you. We're family after all."
    scene e16s02-54 mc-jf-mo-check_c2 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "So you want to kick us off so you can farm tomatoes or something?"
    scene e16s02-54 mc-jf-mo-check_c1 with dissolve
    play voice5 boy4_no_arrogant noloop
    rf "Of course not. No, I'm going to develop the land. Then I'll turn it into a solar farm."
    rf "And my timetable is incredibly tight."
    scene e16s02-55 mc-jf-mo-point_c1 with dissolve
    play voice5 boy4_angry_breath1 noloop
    rf "So as soon as you take the check and get that... mutt off my property, I'll put in a call to my contractor to get the ball rolling."
    scene e16s02-55 mc-jf-mo-point_c2 with dissolve
    play voice4 girl35_zdog_barking10 noloop
    pause
    scene e16s02-56 mc-jf-mo-look_c1 with dissolve
    play voice3 min_angry_breath noloop
    jf "*sighs*"
    scene e16s02-56 mc-jf-mo-look_c2 with dissolve
    play voice4 girl35_zdog_bark2 noloop
    pause
    scene e16s02-56 mc-jf-mo-look_c3 with dissolve
    play voice3 min_no_simple noloop
    jf "No..."
    scene e16s02-57 mc-jf-mo-fight_c1 with dissolve
    play sound sfx_hair_scratch1
    play voice5 boy4_surprised_huh1 noloop
    rf "Excuse me?"
    scene e16s02-57 mc-jf-mo-fight_c2 with dissolve
    play voice3 min_no_angry noloop
    jf "No. N. O. We're not leaving. I don't know why Aunt Rose left the farm to me, but she did."
    jf "I don't intend to ignore her last wishes. I'm sorry, Ryan."
    scene e16s02-58 mc-jf-mo-talk_c1 with dissolve
    play voice5 boy4_disappointed_ooh2 noloop
    rf "I'm really disappointed in you, Jessie. I hoped it wouldn't come to this."
    play sound sfx_paper_slide1
    scene e16s02-59 mc-jf-mo-talk2_c1 with dissolve
    play voice5 boy4_disappointed_geh1 noloop
    rf "But since you won't leave willingly, my hands are tied."
    scene e16s02-59 mc-jf-mo-talk2_c2 with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "You're suing us?"
    scene e16s02-60 mc-jf-mo-paper_c3 with dissolve
    play voice4 girl35_zdog_whining1 noloop
    mdog "*Sad whining noises*"
    scene e16s02-60 mc-jf-mo-paper_c2 with dissolve
    play voice3 min_disappointed_ehh2 noloop
    jf "Ryan..."
    scene e16s02-61 mc-jf-mo-look_c1 with dissolve
    play voice5 boy4_arrogant_he1 noloop
    rf "See you at the next family reunion."
    play sound sfx_footsteps_grass1
    scene e16s02-62 mc-jf-mo-walk_c1 with dissolve
    pause
    scene e16s02-62 mc-jf-mo-walk_c2 with dissolve
    play voice4 girl35_zdog_barking11 noloop
    mdog "Ruff ruff ruff!"
    queue voice4 girl35_zdog_barking9 noloop
    play voice5 boy4_angry_dough2 noloop
    play sound sfx_fall_mud1
    scene e16s02-63 mc-jf-mo-fear_c1 with hpunch
    rf "Get away from me, you freak!"
    $ renpy.music.set_volume(1.0, 1.0, "sound2")
    play sound2 sfx_sand_run1
    scene e16s02-63 mc-jf-mo-fear_c2 with dissolve
    queue voice4 girl35_zdog_barking8 noloop
    stop sound2 fadeout 8.0
    pause
    scene e16s02-64 mc-jf-mo-look_c1 with dissolve
    play voice4 girl35_zdog_whining2 noloop
    mdog "*soft whimpering*"
    pause
    scene e16s02-64 mc-jf-mo-look_c2 with dissolve
    play voice4 girl35_zdog_bark3 noloop
    mdog "Ruff?"
    scene e16s02-65 mc-jf-mo-talk_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "It's okay, Jessie. We're not going to let that asshat get away with this."
    jf "..."
    scene e16s02-65 mc-jf-mo-talk_c3 with dissolve
    play voice2 d2s9_mchey noloop
    mc "Jessie?"
    play voice3 min_disappointed_ehh1 noloop
    jf "Oh... yes... What were you saying?"
    scene e16s02-66 mc-jf-mo-talk2_c1 with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "I said we're going to fight this. Your cousin obviously has it in for your aunt's lawyer."
    mc "We'll start with them. They must know something we can use."
    scene e16s02-66 mc-jf-mo-talk2_c2 with dissolve
    play voice3 min_happy_mmm noloop
    jf "I've... I've never been sued before, [mcname]."
    scene e16s02-67 mc-jf-mo-end1_c1 with dissolve
    play voice2 mc_no_nah2 noloop
    mc "It's going to be alright. One of my old teachers said you haven't truly lived until you've been sued."
    mc "The context was if you were starting a business, but I think the lesson still applies."
    scene e16s02-67 mc-jf-mo-end1_c2 with dissolve
    play voice3 daisy_ugu noloop
    jf "Okay. We'll... we'll figure this out."
    play sound sfx_cloth_rustling3
    scene e16s02-68 mc-jf-mo-end2_c1 with dissolve
    play voice3 jessie_breathe3 noloop
    jf "I'm so glad you're here with me, [mcname]."
    jf "I don't want to leave this place."
    scene e16s02-68 mc-jf-mo-end2_c2 with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "We're not going to."
    stop music fadeout 3.0
    stop sound4 fadeout 3.0

    jump e16s03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
