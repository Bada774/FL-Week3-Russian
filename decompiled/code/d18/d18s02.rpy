label d18s02:

    $ fl_data_collected = 4
    if d16s02_arj_eatout is True:
        $ fl_data_collected += 1
    if d16s03_refuse_lc is False:
        $ fl_data_collected += 1
    if d16s06_aw_sex is True:
        $ fl_data_collected += 1
    if d16s07_jf_sex is True:
        $ fl_data_collected += 2
    if date_vw is True:
        $ fl_data_collected += 1
    if d17s05_mh is True:
        $ fl_data_collected += 1
    if d17s06_choice_study is False:
        $ fl_data_collected += 1
    if date_sy is True:
        $ fl_data_collected += 1

    scene black
    show screen scene_transistion(_("1 hour later\nAt Stacy's house"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene d18s02-1 sy-arj-talk1_c1
    with Fade(0.5, 0.5, 0.9)
    queue music thinking_music_2
    play sound sfx_keyboard_typing2
    pause
    scene d18s02-2 sy-arj-talk2_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Morning.{w} You two are already at it, huh?"
    scene d18s02-2 sy-arj-talk2_c2 with dissolve
    play voice3 amrose_old_hey1 noloop volume 1.5
    arj "Hey, good morning.{w} I think we're close to cracking this thing."
    scene d18s02-5 sy-arj-face1_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "Did we get enough data?"
    scene d18s02-6 sy-arj-face2_c1 with dissolve
    if fl_data_collected < 6:
        play voice4 stacy_no2 noloop
        sy "Barely, but I think we'll manage.{w} All due to my extraordinary genius of course."
        play voice2 mc_yes_yeah3 noloop
        mc "Right, right. I'll buy you some of that cookie dough ice cream you like after all this."
    elif True:
        play voice4 polly_aga noloop
        sy "Yep. We got plenty. Now we just need to turn it into something useful."
    scene d18s02-7 sy-arj-face3_c1 with dissolve
    play voice4 stacy_hmm noloop
    sy "Alrighty. It's now or never, baby.{w} Show me the money."
    play sound sfx_keyboard_enter1
    scene d18s02-8 sy-arj-face4_c1 with dissolve
    play voice2 d2s12_emmm noloop volume 1.5
    mc "...That it? Two IPs?"
    mc "Thought there might be a bit more fanfare than that, but alright."
    scene d18s02-9 sy-arj-face5_c1 with dissolve
    play voice4 stacy_laugh noloop
    sy "We have to provide the fanfare ourselves."
    scene d18s02-7 sy-arj-face3_c1 with dissolve
    play voice3 amrose_surprised_uh2 noloop
    arj "Holy shirt balls."
    play voice4 stacy_angryhuh noloop
    sy "There's the fanfare."
    scene d18s02-10 sy-arj-talk1_c1 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "Don't tell me you recognize some random IPs?"
    scene d18s02-10 sy-arj-talk1_c2 with dissolve
    play voice3 amrose_no_uhuh noloop
    arj "They're not random. Both of these are part of the college's private network."
    scene d18s02-3 sy-arj-talk3_c2 with dissolve
    queue voice3 amrose_thinking_emm noloop
    arj "Pretty sure this one is for the main facility. Most of it anyway."
    arj "But {i}this{/i} one is faculty-only."
    scene d18s02-3 sy-arj-talk3_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "...So the college is responsible? Or someone hired by the college?"
    scene d18s02-10 sy-arj-talk1_c3 with dissolve
    play voice4 stacy_angry noloop
    sy "...Well shit."
    scene d18s02-10-2 sy-arj-talk1-2_c1 with dissolve
    play voice3 amrose_no_simple2 noloop
    arj "Well, no. I don't know. It doesn't {i}necessarily{/i} mean that the college is responsible."
    scene d18s02-10-2 sy-arj-talk1-2_c2 with dissolve
    arj "I have access to the network in the main facility. And I can get access to the faculty-only network by just asking one of the professors I know."
    arj "So it could be practically anyone in the college, not just the faculty."
    scene d18s02-10-2 sy-arj-talk1-2_c3 with dissolve
    play voice4 stacy_mmm1 noloop
    sy "But if Fetish Locator is pinging the college's network, then whatever server it's running off of must be located somewhere in the college!"
    scene d18s02-10-2 sy-arj-talk1-2_c4 with dissolve
    play voice3 amrose_yes_yeah2 noloop
    arj "Exactly. Well..."
    scene d18s02-10-3 sy-arj-talk1-3_c2 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Well?"
    scene d18s02-10-3 sy-arj-talk1-3_c4 with dissolve
    play voice3 amrose_thinking_hmm1 noloop
    arj "Well, they could also be using the college network as a VPN, bouncing traffic off of it to obscure where their data is actually going to."
    scene d18s02-10-2 sy-arj-talk1-2_c2 with dissolve
    play voice4 stacy_oh noloop
    sy "Feck... That's true."

    scene d18s02-11 sy-arj-talk2_c1 with dissolve
    play voice2 d2s9_mchey noloop volume 1.4
    mc "It's still progress.{w} They could just as well {i}not{/i} be doing that."
    scene d18s02-11 sy-arj-talk2_c2 with dissolve
    play voice3 amrose_yes_yap noloop
    arj "True. We don't know."
    scene d18s02-12 sy-arj-talk3_c2 with dissolve
    play voice4 stacy_hey noloop volume 0.7
    sy "But we can find out! We just need to figure out where in the college this server is."
    sy "Even if it's a VPN, if we can get access to it, we should be able to figure out where the data is actually being sent. And if it's not—"
    scene d18s02-13 sy-arj-talk4_c1 with dissolve
    play voice3 amrose_thinking_oh2 noloop
    arj "We'll have direct access to Fetish Locator's server."
    scene d18s02-12 sy-arj-talk3_c2 with dissolve
    play voice4 stacy_yes3 noloop
    sy "Which we then burn to the ground!"
    scene d18s02-12 sy-arj-talk3_c3 with dissolve
    play voice2 d2s9_confused noloop volume 1.7
    mc "Alright, that's good a plan, but let's try to only break one law at a time here. No need to add arson to our trespassing."
    scene d18s02-13 sy-arj-talk4_c2 with dissolve
    play voice3 amrose_disappointed_oh3 noloop
    arj "Oh what's wrong with a little arson?"
    scene d18s02-13 sy-arj-talk4_c3 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "God, she has infected you as well, hasn't she?"

    scene d18s02-15 sy-arj-mc-leave2_c2 with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "What are you doing?"
    scene d18s02-14 sy-arj-mc-leave1_c3 with dissolve
    play voice4 stacy_mmm2 noloop
    sy "Gonna step out for a bit. I need to send Hana the plan and go shopping for a couple of things."
    scene d18s02-15 sy-arj-mc-leave2_c3 with dissolve
    play voice3 amrose_thinking_hmm5 noloop
    arj "Shopping?"
    scene d18s02-13 sy-arj-talk4_c3 with dissolve
    play voice4 stacy_laugh4 noloop
    sy "We can't have a super spy mission without something special to wear!"
    scene d18s02-16 arj-mc-leave3_c1 with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "We didn't even discuss when and how we're gonna find the server."
    play sound sfx_door_closed6 volume 0.2
    scene d18s02-16 arj-mc-leave3_c2 with dissolve
    play voice3 amrose_yes_ugu noloop
    arj "We can do that after lunch. Hana will probably be there as well."
    scene d18s02-19 arj-mc-phone_c2 with dissolve
    pause
    scene d18s02-16 arj-mc-leave3_c2 with dissolve
    play voice3 amrose_surprised_oh1 noloop
    arj "Yikes, and {i}I{/i} need to get going. I got my finals today."
    arj "Are you going?"
    scene d18s02-18 arj-mc-leave5_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "In a bit."
    play voice3 amrose_yes_okay2 noloop
    arj "Okay."
    if d14s03_arj_kiss is True:
        play voice3 amrose_thinking_hmm4 noloop
        play voice2 d1s1_mmm noloop
        play sound maria_kiss1
        scene d18s02-20 arj-mc-kiss1_c1 with dissolve
        pause
        play sound maria_kiss3
        scene d18s02-20 arj-mc-kiss1_c2 with dissolve
        pause
        play sound maria_kiss2
        scene d18s02-20 arj-mc-kiss1_c3 with dissolve
        pause
        scene d18s02-21 arj-mc-bag1_c1 with dissolve
        play voice3 amrose_disappointed_ehh2 noloop
        arj "I love you. See you at lunch."
    elif True:
        scene d18s02-21 arj-mc-bag1_c1 with dissolve
    queue voice3 amrose_disappointed_oh4 noloop
    arj "Oh, and I'll tell Stacy to meet up after lunch as well!"
    scene d18s02-21 arj-mc-bag1_c2 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Good luck with your finals!"
    arj "Bye!"
    scene d18s02-22 arj-mc-look_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "...Welp, guess I got some time to kill before class."
    play sound sfx_bed_fall1
    scene d18s02-22 arj-mc-phone_c1 with dissolve
    pause

    stop music fadeout 3.0
    jump d18s03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
