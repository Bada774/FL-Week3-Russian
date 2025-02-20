image e07s02-a23-glambot-1 = Movie(play = "images/E-07/s02/anim/e07s02-a23-2x-50fps.webm", start_image = "e07s02-a23 lc-mc-food1-glambot-23-000", image = "e07s02-a23 lc-mc-food1-glambot-23-198", loop = False)

image e07s02-a60-1 = Movie(play = "images/E-07/s02/anim/e07s02-a60-1-2x-50fps.webm", start_image = "e07s02-a60-1 mc-lick-lc-pb-anim-01")
image e07s02-a60-1-f = Movie(play = "images/E-07/s02/anim/e07s02-a60-1-2x-60fps.webm", start_image = "e07s02-a60-1 mc-lick-lc-pb-anim-01")
image e07s02-a60-2 = Movie(play = "images/E-07/s02/anim/e07s02-a60-2-2x-50fps.webm", start_image = "e07s02-a60-2 mc-lick-lc-pb-anim-01")
image e07s02-a60-2-f = Movie(play = "images/E-07/s02/anim/e07s02-a60-2-2x-60fps.webm", start_image = "e07s02-a60-2 mc-lick-lc-pb-anim-01")
image e07s02-a60-3 = Movie(play = "images/E-07/s02/anim/e07s02-a60-3-2x-50fps.webm", start_image = "e07s02-a60-3 mc-lick-lc-pb-anim-01")
image e07s02-a60-3-f = Movie(play = "images/E-07/s02/anim/e07s02-a60-3-2x-60fps.webm", start_image = "e07s02-a60-3 mc-lick-lc-pb-anim-01")
image e07s02-a60-4 = Movie(play = "images/E-07/s02/anim/e07s02-a60-4-2x-50fps.webm", start_image = "e07s02-a60-4 mc-lick-lc-pb-anim-01")
image e07s02-a60-4-f = Movie(play = "images/E-07/s02/anim/e07s02-a60-4-2x-60fps.webm", start_image = "e07s02-a60-4 mc-lick-lc-pb-anim-01")

image e07s02-a61-1 = Movie(play = "images/E-07/s02/anim/e07s02-a61-1-2x-50fps.webm", start_image = "e07s02-a61-1 mc-lick-lc-pb-anim-01")
image e07s02-a61-1-f = Movie(play = "images/E-07/s02/anim/e07s02-a61-1-2x-60fps.webm", start_image = "e07s02-a61-1 mc-lick-lc-pb-anim-01")
image e07s02-a61-2 = Movie(play = "images/E-07/s02/anim/e07s02-a61-2-2x-50fps.webm", start_image = "e07s02-a61-2 mc-lick-lc-pb-anim-01")
image e07s02-a61-2-f = Movie(play = "images/E-07/s02/anim/e07s02-a61-2-2x-60fps.webm", start_image = "e07s02-a61-2 mc-lick-lc-pb-anim-01")
image e07s02-a61-3 = Movie(play = "images/E-07/s02/anim/e07s02-a61-3-2x-50fps.webm", start_image = "e07s02-a61-3 mc-lick-lc-pb-anim-01")
image e07s02-a61-3-f = Movie(play = "images/E-07/s02/anim/e07s02-a61-3-2x-60fps.webm", start_image = "e07s02-a61-3 mc-lick-lc-pb-anim-01")

image e07s02-a63-1 = Movie(play = "images/E-07/s02/anim/e07s02-a63-1-2x-50fps.webm", start_image = "e07s02-a63-1 lc-mc-pb-lick-anim-01")
image e07s02-a63-1-f = Movie(play = "images/E-07/s02/anim/e07s02-a63-1-2x-60fps.webm", start_image = "e07s02-a63-1 lc-mc-pb-lick-anim-01")
image e07s02-a63-2 = Movie(play = "images/E-07/s02/anim/e07s02-a63-2-2x-50fps.webm", start_image = "e07s02-a63-2 lc-mc-pb-lick-anim-01")
image e07s02-a63-2-f = Movie(play = "images/E-07/s02/anim/e07s02-a63-2-2x-60fps.webm", start_image = "e07s02-a63-2 lc-mc-pb-lick-anim-01")
image e07s02-a63-3 = Movie(play = "images/E-07/s02/anim/e07s02-a63-3-2x-50fps.webm", start_image = "e07s02-a63-3 lc-mc-pb-lick-anim-01")
image e07s02-a63-3-f = Movie(play = "images/E-07/s02/anim/e07s02-a63-3-2x-60fps.webm", start_image = "e07s02-a63-3 lc-mc-pb-lick-anim-01")

label e07s02:

    $ e07s02_challenge_win = False
    $ e07s02_drink = False

    scene black
    show screen scene_transistion(_("Next morning"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play voice3 dahlia_disappointed_snoring volume 0.5 fadein 3.0
    scene e07s02-01 lc-wake1_c1
    with Fade(0.5, 0.5, 0.5)
    play music music_sexy_clichehornya
    pause
    play sound sfx_cloth_planket2
    scene e07s02-02 lc-wake2_c1 with dissolve
    pause
    play sound sfx_cloth_rustling2
    scene e07s02-03 lc-wake3_c1 with dissolve
    play voice3 lydia_moan1 noloop
    pause
    play sound sfx_hands_clap3
    play sound2 ["<silence 0.2>", sfx_hands_clap4] noloop
    scene e07s02-04 lc-wake4_c1 with dissolve
    pause
    play sound sfx_door_open1
    scene e07s02-05 lc-entry1_c1 with dissolve
    pause
    scene e07s02-05 lc-entry1_c2 with dissolve
    pause
    play sound sfx_cloth_rustling1
    scene e07s02-06 lc-entry2_c1 with dissolve
    play voice3 dahlia_arrogant_huh noloop
    lc "Where is [e07_mcname!t]?"
    scene e07s02-06 lc-entry2_c2 with dissolve
    play voice4 amrose_thinking_emm noloop
    arj "He's, uhm..."
    play sound sfx_cloth_rustling2
    scene e07s02-07 lc-coffee1_c2 with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "I am so sorry, [e07_lcname!t]. I've got your morning coffee right here."
    play sound sfx_cloth_dress_off2 volume 1.4
    scene e07s02-08 lc-coffee2_c1 with dissolve
    play voice3 dahlia_disappointed_ehh1 noloop
    lc "I knew you were going to be a disappointment."
    scene e07s02-09 lc-coffee3_c1 with dissolve
    play sound sfx_drink_slurp2
    pause
    stop sound fadeout 1.0
    scene e07s02-10 lc-coffee4_c1 with dissolve
    play voice3 dahlia_disgust_yah noloop
    lc "This is dis-gus-ting. It's burnt, it's half cold, it's-"
    lc "It's just as disappointing as you are."
    scene e07s02-11 lc-coffee5_c1 with dissolve
    play voice3 dahlia_angry_hm2 noloop
    lc "And what about the rest of my breakfast, [e07_mcname!t]."
    scene e07s02-11 lc-coffee5_c2 with dissolve
    play voice2 d2s12_emmm noloop
    mc "Uhhh, I don't know how to poach an egg..."
    play sound sfx_cloth_dress_off3 volume 1.5
    scene e07s02-12 lc-coffee6_c1 with dissolve
    play voice3 dahlia_angry_argh1 noloop
    lc "Just - fucking leave. Get out of my sight."
    scene e07s02-12 lc-coffee6_c2 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "[e07_lcname!t], please. Give me a chance, I am so sorry. I can do better."
    play voice3 dahlia_angry_hm1 noloop
    lc "Can you?"
    play voice2 d9s2_mcyes2 noloop volume 2.5
    mc "Yes, [e07_lcname!t], I will do my best to improve."
    scene e07s02-12 lc-coffee6_c1 with dissolve
    play voice3 dahlia_angry_ah2 noloop
    lc "*sighs* At least you can follow directions. Now get out of my room!"
    play voice2 mc_yes_yes2 noloop
    mc "... Yes, [e07_lcname!t]."
    scene e07s02-13 lc-talk1_c1 with dissolve
    play voice3 dahlia_angry_oof noloop
    lc "You too, [e07_arjname!t]. I don't even know why you're still here."
    scene e07s02-13 lc-talk1_c2 with dissolve
    play voice3 amrose_yes_ugu noloop
    arj "Of course, [e07_lcname!t]."
    scene e07s02-13-2 lc-leave_c2 with dissolve
    pause
    play sound sfx_door_closed2
    scene e07s02-14 mc-arj-entry2_c2 with fade
    play voice4 amrose_disappointed_ehh2 noloop
    arj "She shouldn't treat you like that..."
    scene e07s02-14 mc-arj-entry2_c1 with dissolve
    play voice2 mc_no_no5 noloop
    mc "It's okay, AmRose. This is how I prove my love to Lydia."
    play sound sfx_dishes_slicing1
    scene e07s02-15 mc-arj-food1_c2 with dissolve
    play voice4 amrose_hey_happy3 noloop
    arj "This isn't what love looks like."
    stop sound fadeout 1.0
    scene e07s02-16 mc-arj-food2_c1 with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "You don't know that."
    scene e07s02-16 mc-arj-food2_c2 with dissolve
    play voice4 amrose_old_upset noloop
    arj "*Quietly* Actually, I do..."
    scene e07s02-18 mc-arj-talk2_c2 with dissolve
    play voice5 pete_hey_heyo noloop
    pb "Yo, [e07_lcname!t] wants to see you, [mcname]."
    scene e07s02-18 mc-arj-talk2_c1 with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "I have to go. We can talk more later."
    play voice4 amrose_yes_okay1 noloop
    arj "Okay, I'll-"
    scene e07s02-17 mc-arj-talk1_c2 with dissolve
    play voice4 amrose_happy_mmm noloop
    arj "*Quietly* See you later..."
    scene e07s02-19-2 mc-arj-extra_c2 with dissolve
    play voice5 pete_hey_happy noloop
    pb "What's up?"
    scene e07s02-19-2 mc-arj-extra_c1 with dissolve
    play voice4 amrose_disappointed_oh5 noloop
    arj "Leave me alone, Pete. I'm not in the mood."
    play voice5 pete_yes_ugu1 noloop
    pb "Fine, see you around."

    play sound sfx_door_open2
    scene e07s02-23 lc-mc-food1_c1 with Fade(0.5, 0.5, 0.5)
    play voice2 d1s5_mchappy noloop
    mc "You summoned me, [e07_lcname!t]?"
    scene e07s02-a23 lc-mc-food1-glambot-23-000 with dissolve
    play voice3 dahlia_arrogant_heh noloop
    lc "Huh... This is real for you. This isn't an act."
    play sound ["<silence 0.5>", sfx_camera_fly1] volume 2.5
    play sound2 ["<silence 3.0>", sfx_camera_fly1] volume 2.5 noloop
    scene e07s02-a23-glambot-1
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene e07s02-24 lc-mc-food2_c1 with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What do you mean, [e07_lcname!t]?"
    scene e07s02-24 lc-mc-food2_c2 with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    lc "This - you - being my little slave. This is who you are now, [e07_mcname!t]. Just my little toy."
    scene e07s02-25 lc-mc-talk1_c1 with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "I am whatever you want me to be."
    scene e07s02-25 lc-mc-talk1_c2 with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    lc "What about [e07_arjname!t]?"
    scene e07s02-26 lc-mc-talk2_c1 with dissolve
    play voice2 mc_arrogant_hm2 noloop
    mc "What about her?"
    scene e07s02-26 lc-mc-talk2_c2 with dissolve
    play voice3 lydia_hmmmm noloop volume 1.6
    lc "I mean, she came here {i}for you{/i}. That has to mean something."
    scene e07s02-27 lc-mc-talk3_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "I mean... Sure? It means that you have one more person here to fill your needs."
    scene e07s02-27 lc-mc-talk3_c2 with dissolve
    play voice3 dahlia_arrogant_ha noloop
    lc "Well, she filled {i}your needs{/i} at the very least."
    scene e07s02-28 lc-mc-talk4_c1 with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "...All that matters is that you enjoyed it."
    scene e07s02-28 lc-mc-talk4_c2 with dissolve
    play voice3 lydia_lydwow noloop
    lc "God... You really are one in a million, aren't you?"
    play sound sfx_cup_slide1
    scene e07s02-29 lc-mc-talk5_c2 with dissolve
    play voice3 dahlia_thinking_mmm2 noloop
    lc "I mean, if you really want to win me over you still have a long way to go."
    lc "But I think you've got some real promise, [e07_mcname!t]."
    lc "You've brought a little spark back into the dungeon."
    scene e07s02-29 lc-mc-talk5_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "What do you mean?"
    scene e07s02-30 lc-mc-talk6_c2 with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    lc "Can I be honest with you, [e07_mcname!t]?"
    play voice2 mc_yes_yes1 noloop
    mc "Always, [e07_lcname!t]."
    lc "I've been so fucking bored lately. [e07_pbname!t] is just... He does the same thing, over and over. And I just..."
    lc "I'm tired of him. And don't even get me started about [e07_trname!t] and [e07_ahname!t]."
    scene e07s02-30 lc-mc-talk6_c1 with dissolve
    play voice2 mc_pain_mff1 noloop
    mct "She said she's tired of Pete! That means I've got a chance!"
    scene e07s02-31 lc-mc-talk7_c2 with dissolve
    play voice3 lydia_laugh noloop volume 1.4
    lc "I think you might just be the thing I've been missing all this time."
    scene e07s02-32 lc-mc-talk8_c1 with dissolve
    play voice2 d3s7_mcemm noloop
    mc "Lydia, I..."
    scene e07s02-32 lc-mc-talk8_c2 with dissolve
    play voice3 lydia_oof noloop
    lc "I'm suddenly thirsty. Can you go grab me a glass of water, [e07_mcname!t]?"
    play voice2 mc_happy_yes1 noloop
    mc "Ahem, yes. Erm, of course [e07_lcname!t]."
    scene e07s02-33 lc-mc-talk9_c2 with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    lc "I'm going to take a bath. Bring the glass to me in there, okay?"
    play sound sfx_heels_steps2 loop
    scene e07s02-41 lc-mc-walk2_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Your wish is my command, [e07_lcname!t]."
    scene e07s02-42 lc-mc-walk3_c1 with dissolve
    pause
    play sound sfx_door_closed9
    scene e07s02-88 lc-mc-pb-entry1_c1 with fade
    queue sound sfx_heels_steps2 loop
    pause
    scene e07s02-89 lc-mc-pb-talk1_c2 with dissolve
    play voice4 amrose_hey_scared noloop
    arj "You're back!"
    stop sound fadeout 1.0
    scene e07s02-90 lc-mc-pb-talk2_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "I need to grab a glass of water for [e07_lcname!t]."
    play voice4 amrose_disappointed_oh3 noloop
    arj "Oh..."
    scene e07s02-90 lc-mc-pb-talk2_c2 with dissolve
    play voice4 amrose_thinking_hmm3 noloop
    arj "What'd she want?"
    scene e07s02-91 lc-mc-pb-talk3_c1 with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "It wasn't really important. But-"
    mc "-It sounds like I might have a chance."
    scene e07s02-92 lc-mc-pb-talk4_c2 with dissolve
    play voice4 amrose_surprised_huh3 noloop
    arj "What do you mean?"
    scene e07s02-92 lc-mc-pb-talk4_c1 with dissolve
    play voice2 mc_happy_yay3 noloop
    mc "Sounds like [e07_lcname!t] may be looking for a change of pace. And that I'm the right guy for the job."
    play voice4 amrose_disappointed_oh2 noloop
    arj "[mcname]..."
    play sound sfx_barefoot_steps1
    scene e07s02-94 lc-mc-pb-glass2_c3 with dissolve
    play voice5 pete_hey_attention noloop
    pb "'Sup man?"
    scene e07s02-94 lc-mc-pb-glass2_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Not much, just getting some water for [e07_lcname!t]."
    scene e07s02-94 lc-mc-pb-glass2_c2 with dissolve
    play voice4 amrose_surprised_uh2 noloop
    arj "What the hell are you doing, Pete?"
    stop sound fadeout 1.0
    scene e07s02-96 lc-mc-pb-talk2_c2 with dissolve
    play voice5 pete_surprised_oh1 noloop
    pb "[e07_lcname!t] wants me to edge. Don't know why."
    pb "Hey, have I told you lately that you're pretty hot?"
    scene e07s02-97 lc-mc-pb-end1_c1 with dissolve
    play voice4 amrose_surprised_huh2 noloop
    arj "Huh?"
    play voice5 pete_happy_mmm2 noloop
    pb "You're hot, AmRose. I never really checked you out before, but-"
    pb "You've got a great ass."
    play voice4 amrose_arrogant_huh1 noloop
    arj "Uhm, thanks? I guess?"
    pb "Don't mention it."
    play sound sfx_bottle_pouring1
    scene e07s02-94 lc-mc-pb-glass2_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "See you two later."
    scene e07s02-97 lc-mc-pb-end1_c1 with dissolve
    play voice5 pete_yes_yeah noloop
    pb "I'll see you around."
    play voice4 amrose_yes_yeah4 noloop
    arj "Yeah... I'll see ya'."

    jump e07s02_bathroom

label replay_e07s02:
label e07s02_bathroom:

    if _in_replay:
        $ renpy.music.set_volume(0.6, 0.0, "music")
        play music music_sexy_clichehornya
    play sound sfx_door_open4 volume 1.8
    play sound3 sfx_bath_waterplay1
    scene e07s02-43 lc-mc-entry1_c1 with Fade(0.5, 0.5, 0.5)
    pause
    scene e07s02-44 lc-mc-entry2_c2 with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    lc "Do I have something on my face?"
    scene e07s02-44 lc-mc-entry2_c1 with dissolve
    play voice2 mc_no_no2 noloop
    mc "No- I, uhhh-"
    scene e07s02-44 lc-mc-entry2_c2 with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    lc "I'm still thirsty, [e07_mcname!t]."
    play voice2 mc_yes_yes3 noloop
    mc "Yes, of course, [e07_lcname!t]."
    scene e07s02-45 lc-mc-kneel1_c2 with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    lc "Kneel."
    scene e07s02-45 lc-mc-kneel1_c1 with dissolve
    lc "Good boy."
    play sound sfx_drink_loop1 loop volume 2.0
    scene e07s02-47 lc-mc-talk2_c2 with dissolve
    pause
    stop sound fadeout 1.0
    scene e07s02-48 lc-mc-talk3_c2 with dissolve
    play voice3 dahlia_happy_relief noloop
    lc "Refreshing."
    lc "Just like you, [e07_mcname!t]."
    scene e07s02-48 lc-mc-talk3_c1 with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.7
    mc "Thank you, [e07_lcname!t]."
    scene e07s02-50 lc-mc-talk5_c2 with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    lc "I've been thinking about you, sitting here, all wet and naked."
    play sound sfx_drink_slurp2
    scene e07s02-49 lc-mc-talk4_c2 with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "Oh my God..."
    play sound gulp
    "*GULP*"
    scene e07s02-50 lc-mc-talk5_c1 with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Really?"
    scene e07s02-51 lc-mc-talk6_c2 with dissolve
    play voice3 dahlia_yes_ugu noloop
    lc "Mmhmm, and do you know what I've been thinking about, sitting here all wet and naked."
    mct "Oh fuck... It's happening."
    scene e07s02-52 lc-mc-talk7_c1 with dissolve
    play voice2 d1s5b_emmm noloop
    mc "Uhhh, no. I... Don't know."
    scene e07s02-52 lc-mc-talk7_c2 with dissolve
    play voice3 lydia_moan1 noloop
    lc "I was thinking, you might just be the thing that completes me."
    play voice2 mc_pain_mff2 noloop
    mct "Ohmygodohmygodohmygodohmygooooood."
    scene e07s02-53 lc-mc-talk8_c1 with dissolve
    play voice2 mc_scared_oh1 noloop
    mc "You have no idea how happy that makes me, [e07_lcname!t]."
    scene e07s02-53 lc-mc-talk8_c2 with dissolve
    play voice3 lydia_lydiahey noloop
    lc "You would do {i}anything{/i} for me, wouldn't you [e07_mcname!t]."
    scene e07s02-54 lc-mc-talk9_c1 with dissolve
    play voice2 mc_happy_yes1 noloop
    mc "Yes, [e07_lcname!t]. Anything to make you happy."
    scene e07s02-55 lc-mc-talk10_c2 with dissolve
    play voice3 dahlia_arrogant_heh noloop
    lc "Let's see if you mean it."
    play sound sfx_finger_snap1
    "*SNAP*"
    play sound sfx_door_openclosed1
    play sound3 sfx_bath_out1 noloop volume 1.5
    scene e07s02-58 lc-mc-pb-talk1_c3 with dissolve
    play voice5 pete_yes_simple2 noloop
    pb "Yes, [e07_lcname!t]?"
    scene e07s02-59 lc-mc-pb-talk2_c1 with dissolve
    play voice2 d2s9_confused noloop volume 1.5
    mc "What's he doing here?"
    scene e07s02-58 lc-mc-pb-talk1_c2 with dissolve
    play voice3 lydia_thinking noloop volume 2.0
    lc "I want to play a game."
    scene e07s02-59 lc-mc-pb-talk2_c2 with dissolve
    play voice3 lydia_haha noloop volume 2.2
    lc "It's a really straightforward game. [e07_mcname!t], I want you to eat me out."
    lc "And you need to make me orgasm before [e07_pbname!t] cums into my bathtub."
    scene e07s02-58 lc-mc-pb-talk1_c1 with dissolve
    play voice2 mc_surprised_what3 noloop
    mc "Wait, what?"
    scene e07s02-58 lc-mc-pb-talk1_c2 with dissolve
    play voice3 dahlia_arrogant_huh noloop
    lc "What's confusing about it? I want to see who finishes first, me or [e07_pbname!t]."
    lc "If you make me cum first, I'll give you a little reward; I'll let you drink some of my bath water. Give you a little taste of your love."
    scene e07s02-59 lc-mc-pb-talk2_c2 with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    lc "But if [e07_pbname!t] cums before me, you'll have to drink a glass of bath water. With his cum in it."
    lc "Otherwise, you can refuse. But you'll have to leave. If you can't show me how far you're willing to go for your devotion, you have no place here."
    scene e07s02-59 lc-mc-pb-talk2_c1 with dissolve
    play voice2 d4s8_scared noloop volume 1.6
    mc "Of course, [e07_lcname!t]. Anything for you."
    lc "Good boy."


    $ Lovense.stop()

    scene e07s02-59 lc-mc-pb-talk2_c3 with dissolve
    play voice3 dahlia_yes_aga noloop
    lc "All right boys, on your marks-"
    lc "-Get set-"
    scene e07s02-a60-1 mc-lick-lc-pb-anim-01 with dissolve
    pause
    scene e07s02-a60-1
    play voice3 dahlia_sex_closedmoan2 noloop
    queue voice3 dahlia_sex_openmoans2
    play voice2 mc_sex_sucking_fast1
    play voice5 pete_sex_openmoans1
    play sound sfx_handjob_cream1 loop
    $ Lovense.vibrate(3)
    lc "Go."
    pause
    scene e07s02-a60-2 with dissolve
    mct "Holy shit, it's finally happening."
    pause
    scene e07s02-a60-3 with dissolve
    lc "Mmmm, that's nice."
    pause
    scene e07s02-a60-4 with dissolve
    pause
    $ Lovense.vibrate(6)
    scene e07s02-a60-1-f with dissolve
    pause
    scene e07s02-a60-2-f with dissolve
    pause
    scene e07s02-a60-3-f with dissolve
    pause
    lc "Maybe you're not completely useless, [e07_mcname!t]."
    scene e07s02-a60-4-f with dissolve
    pause
    lc "But it looks like [e07_pbname!t] is really getting close."
    scene e07s02-a61-1 with dissolve
    lc "Mmmm, you need to start working harder, [e07_mcname!t]."
    pause
    scene e07s02-a61-3 with dissolve
    mct "God, she tastes {i}incredible{/i}."
    pause
    scene e07s02-a61-2 with dissolve
    lc "You're not going to let me down, are you?"
    pause
    $ Lovense.vibrate(8)
    scene e07s02-a61-1-f with dissolve
    pause
    scene e07s02-a61-3-f with dissolve
    pause
    scene e07s02-a61-2-f with dissolve
    pause
    stop voice2 fadeout 1.0
    scene e07s02-62 lc-mc-pb-lick3_c3 with dissolve
    play voice3 dahlia_hey_angry noloop
    lc "Come on, [e07_mcname!t], is this the best you've got?"
    scene e07s02-62 lc-mc-pb-lick3_c1 with dissolve
    play voice3 lydia_huh2 noloop
    lc "Are you going to let [e07_pbname!t] cum before me?"
    play voice2 mc_pain_mff3 noloop
    mct "Fuck. No."
    scene e07s02-a63-1 with dissolve
    play voice3 dahlia_sex_openmoans2
    play voice2 mc_sex_sucking_fast1
    lc "Mmmm, that's better! Come on, [e07_mcname!t], make your [e07_lcname!t] cum."
    pause
    scene e07s02-a63-3 with dissolve
    play voice5 pete_sex_openmoans2
    pb "Oh fuck."
    pause
    scene e07s02-a63-2 with dissolve
    lc "Uh oh, sounds like [e07_pbname!t] is getting close."
    lc "What are you going to do, [e07_mcname!t]?"
    pause
    scene e07s02-a63-1-f with dissolve
    play voice3 dahlia_sex_openmoans1
    lc "Fuuuuck, I'm getting close."
    scene e07s02-a63-3-f with dissolve
    lc "But I don't think this is going to be enough."
    lc "Mmmmmm, fuck, [e07_mcname!t], eat my ass and make me cum."
    menu:
        "Eat [e07_lcname!t]'s ass"(hint="e07s02m01c01"):
            $ e07s02_challenge_win = True
            jump e07s02_challenge_win
        "Keep eating out [e07_lcname!t]"(hint="e07s02m01c02"):

            $ e07s02_challenge_win = False
            jump e07s02_challenge_lose

label e07s02_challenge_win:

    scene e07s02-a63-2-f with dissolve
    $ Lovense.vibrate(12)
    play voice3 dahlia_sex_orgasming2
    lc "Fuck, this is what I needed!"
    lc "Just like that, eat my dirty ass, [e07_mcname!t]!"
    lc "Get your tongue in there, yes!"
    play voice3 dahlia_sex_orgasming1
    lc "Yes, yes, YES!!"
    stop voice2 fadeout 1.0
    $ Lovense.vibrate(16)
    scene e07s02-62 lc-mc-pb-lick3_c3 with hpunch
    lc "Fuuuuuhuuuck! I'm cumming!"
    stop voice3 fadeout 1.0
    scene e07s02-64 lc-mc-pb-lick5_c3 with dissolve
    $ Lovense.vibrate(1)
    play voice3 dahlia_hey_angry noloop
    lc "Stop jerking off, [e07_pbname!t]."
    pb "Fuck, [e07_lcname!t]. I'm so close. Can I please finish?"
    stop voice5 fadeout 1.0
    stop sound fadeout 1.0
    scene e07s02-64 lc-mc-pb-lick5_c2 with dissolve
    play voice3 dahlia_no_serious noloop
    lc "No."

    jump e07s02_bath_water

label e07s02_challenge_lose:

    play voice5 pete_sex_orgasm1 noloop
    scene e07s02-64 lc-mc-pb-lick5_c3 with hpunch
    pb "Fuck, here it comes."
    mct "Oh no..."
    stop voice2 fadeout 1.0
    stop voice3 fadeout 1.0
    play voice5 pete_sex_orgasm2 noloop
    play sound mc_cum_sound1
    $ Lovense.vibrate(14)
    scene e07s02-64-2 lc-mc-pb-cum_c2 with hpunch
    pause
    play voice5 pete_sex_orgasm3 noloop
    scene e07s02-64-2 lc-mc-pb-cum_c3 with hpunch
    play voice3 dahlia_thinking_hmm3 noloop
    lc "Hmmm, good job, [e07_pbname!t]."
    scene e07s02-65 lc-mc-pb-lick6_c2 with dissolve
    $ Lovense.vibrate(1)
    play voice3 dahlia_disgust_oof noloop
    lc "And about what I expected from you."

    jump e07s02_bath_water

label e07s02_bath_water:

    scene e07s02-66 lc-mc-pb-talk2_c1 with dissolve
    pause
    play sound sfx_cloth_dress_off2 volume 1.5
    scene e07s02-67 lc-mc-pb-talk3_c2 with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    lc "At least you can listen."
    scene e07s02-67 lc-mc-pb-talk3_c1 with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Yes, [e07_lcname!t]."
    play sound sfx_bath_out1
    scene e07s02-68 lc-mc-pb-glass1_c2 with dissolve
    pause
    if e07s02_challenge_win is True:
        scene e07s02-68 lc-mc-pb-glass1_c3 with dissolve
        pause
        scene e07s02-69 lc-mc-pb-glass2_c2 with dissolve
        play voice3 lydia_aga noloop
        lc "Your winnings, [e07_mcname!t]."
    else:
        scene e07s02-68-2 lc-mc-pb-cum_c3 with dissolve
        pause
        scene e07s02-69 lc-mc-pb-glass2_c2 with dissolve
        play voice3 dahlia_disgust_oeah noloop
        lc "You deserve to see what a real man taste like after doing such a bad job."
    lc "Drink."
    menu:
        "Accept"(hint="e07s02m02c01"):
            $ e07s02_drink = True
            jump e07s02_drink
        "Refuse"(hint="e07s02m02c02"):

            $ e07s02_drink = False
            jump e07s02_early_end

label e07s02_drink:

    scene e07s02-70 lc-mc-pb-glass3_c1 with dissolve
    play sound sfx_drink_loop1 volume 2.0 loop
    play voice2 d9s2_ugu noloop
    mc "Of course, [e07_lcname!t]."
    scene e07s02-70 lc-mc-pb-glass3_c2 with dissolve
    play voice3 dahlia_happy_laugh2 noloop
    lc "Good. Now both of you, go wait for me in my bedroom. I'll be out... When I want to."
    scene e07s02-70 lc-mc-pb-glass3_c3 with dissolve
    play voice5 pete_yes_simple1 noloop
    pb "Of course, [e07_lcname!t]."
    play voice2 mc_yes_ugu1 noloop
    mc "Whatever you desire, [e07_lcname!t]."
    stop sound fadeout 1.0

    $ Lovense.stop()


    $ renpy.end_replay()

    jump e07s02_end

label e07s02_end:

    scene e07s02-70-5 lc-mc-pb-room4_c2 with Fade(0.5, 0.5, 0.5)
    play voice5 pete_disappointed_oof1 noloop
    if e07s02_challenge_win is True:
        pb "Yeah man, [e07_lcname!t] can be real cruel. She's left me like this for hours."
    else:
        pb "Yeah man, the cock ring [e07_lcname!t] has me wear makes it impossible for my erection to go away."
    $ unlock_gallery_slot("scene", "e07s02")
    scene e07s02-70-2 lc-mc-pb-room1_c1 with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "You don't appreciate [e07_lcname!t]."
    scene e07s02-70-4 lc-mc-pb-room3_c2 with dissolve
    play voice5 pete_thinking_mmf noloop
    pb "Okay... Sure. But, what about AmRose? I mean, some of the shit [e07_lcname!t] has done to her... And she's stuck around for you."
    scene e07s02-70-5 lc-mc-pb-room4_c1 with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yeah, and?"
    scene e07s02-70-5 lc-mc-pb-room4_c2 with dissolve
    play voice5 pete_thinking_emm1 noloop
    pb "Man, just between us, I've got no idea why you've got such a hard-on for Lydia when AmRose would do anything for you."
    scene e07s02-71 lc-mc-pb-entry1_c1 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "And that's exactly my point."
    mc "You don't get it."
    play sound sfx_door_open2
    scene e07s02-71 lc-mc-pb-entry1_c2 with dissolve
    play voice3 dahlia_hey_active1 noloop
    lc "That little competition we did is probably the highlight of the month for me. And it got me thinking, what if we did more of them?"
    scene e07s02-72 lc-mc-pb-talk1_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "I think that's a great idea, [e07_lcname!t]."
    scene e07s02-72 lc-mc-pb-talk1_c3 with dissolve
    play voice5 pete_surprised_huh1 noloop
    pb "You want me to jerk off into your tub again?"
    scene e07s02-72 lc-mc-pb-talk1_c2 with dissolve
    play voice3 dahlia_disappointed_ehh1 noloop
    lc "Every time you open your mouth, [e07_pbname!t], it makes me question why I let you fuck me."
    lc "No. I was thinking that we could go have some fun in my friend's dungeon."
    scene e07s02-74 lc-mc-pb-closet1_c2 with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    lc "So go and pack a bag, boys. We're on the first flight out."
    lc "And, [e07_mcname!t], get ready for a nice little vacation present!"
    play sound sfx_jeans_fly1
    scene e07s02-75 lc-mc-pb-cage1_c2 with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mct "I wonder what it could be!"
    play voice3 dahlia_happy_laugh1 noloop
    play sound sfx_cloth_planket2
    scene e07s02-76 lc-mc-pb-cage2_c1 with hpunch
    lc "Here is your carry-on."
    scene e07s02-76 lc-mc-pb-cage2_c2 with dissolve
    play voice2 mc_pain_mff5 noloop
    mc "Oh..."
    mct "It's okay. This is just another test. I'm sure she'll let my cock free once I perform better."
    scene e07s02-77 lc-mc-pb-cage3_c1 with dissolve
    play voice3 dahlia_surprised_huh2 noloop
    lc "It's your favorite little thing. Aren't you excited?"
    scene e07s02-77 lc-mc-pb-cage3_c2 with dissolve
    play voice2 d9s2_mcyes2 noloop volume 2.5
    mc "Of course, [e07_lcname!t]... Every gift from you is a treasure..."
    scene e07s02-77 lc-mc-pb-cage3_c3 with dissolve
    play voice5 pete_hey_happy noloop
    pb "Where we going?"
    scene e07s02-78 lc-mc-pb-walk1_c1 with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    lc "You'll see when we get there. Now go, or I'll make you both go through the airport with gags and leashes."
    play voice2 mc_yes_okay1 noloop
    mc "Of course, [e07_lcname!t],"
    scene e07s02-78 lc-mc-pb-walk1_c2 with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    lc "Wait, [e07_pbname!t]."
    scene e07s02-79 lc-mc-pb-talk1_c2 with dissolve
    play voice5 pete_yes_yeah noloop
    pb "Yeah?"
    play voice3 lydia_moan1 noloop
    lc "I'm feeling a little worked up after my bath. Satisfy my needs, then go pack a bag."
    scene e07s02-79 lc-mc-pb-talk1_c1 with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    lc "Make sure you shut the door tight on your way out, [e07_mcname!t]."
    play voice2 mc_yes_yes1 noloop
    mc "... yes, [e07_lcname!t]."
    scene e07s02-80 lc-mc-pb-talk2_c1 with dissolve
    pause
    play sound sfx_door_closed1

    stop music fadeout 3.0
    jump e07s03

label e07s02_early_end:

    $ Lovense.stop()


    $ renpy.end_replay()
    scene e07s02-81 lc-mc-pb-glass1_c1 with dissolve
    play voice2 mc_disgust_ooh1 noloop
    mc "I... I can't do it."
    play voice3 dahlia_angry_argh1 noloop
    scene e07s02-81 lc-mc-pb-glass1_c2 with hpunch
    lc "You're fucking useless."
    play voice3 dahlia_angry_argh2 noloop
    play sound sfx_hands_clap1
    scene e07s02-82 lc-mc-pb-glass2_c2 with hpunch
    lc "Get the fuck out of my house."
    scene e07s02-83 lc-mc-pb-out1_c1 with dissolve
    play voice2 mc_pain_ou1 noloop
    mc "Please, Lydia-"
    play voice3 lydia_ah noloop
    scene e07s02-83 lc-mc-pb-out1_c2 with hpunch
    lc "{i}What did you just call me!?{/i}"
    play voice2 mc_scared_huuuh3 noloop
    mc "Wait, I-"
    play voice3 dahlia_angry_ah1 noloop
    lc "NO. It's too little, too late. [e07_pbname!t], throw this useless piece of shit out."
    scene e07s02-83 lc-mc-pb-out1_c3 with dissolve
    play voice2 mc_pain_mff5 noloop
    mc "No, I'm sorry! I'll do whatever you want."
    play voice3 dahlia_angry_ah2 noloop
    lc "Faster, [e07_pbname!t]. His groveling is just as pathetic as he is, and it's disturbing my bath."
    play voice5 pete_disappointed_ehh1 noloop
    pb "Come on, [mcname]."
    scene e07s02-84 lc-mc-pb-talk1_c1 with dissolve
    play voice2 mc_no_no4 noloop
    mc "No, {i}please!{/i}"
    play sound sfx_cloth_rustling1
    scene e07s02-86 lc-mc-pb-end1_c1 with dissolve
    play voice2 mc_pain_rrrr noloop
    mc "Please, [e07_lcname!t]!"
    scene e07s02-86 lc-mc-pb-end1_c3 with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "Come on, Pete, don't do this."
    play voice5 pete_disappointed_ehh4 noloop
    pb "Sorry man, you did this to yourself."
    stop music fadeout 3.0
    play sound sfx_door_closed2

    jump e07_early_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
