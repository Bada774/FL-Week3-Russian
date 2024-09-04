image e02s02-a14-1 = Movie(play = "images/E-02/s02/anim/e02s02-a14-1-2x-50fps.webm", start_image = "e02s02-a14-1 mh-bj1-01")
image e02s02-a14-1-f = Movie(play = "images/E-02/s02/anim/e02s02-a14-1-2x-60fps.webm", start_image = "e02s02-a14-1 mh-bj1-01")
image e02s02-a14-2 = Movie(play = "images/E-02/s02/anim/e02s02-a14-2-2x-50fps.webm", start_image = "e02s02-a14-2 mh-bj1-01")
image e02s02-a14-2-f = Movie(play = "images/E-02/s02/anim/e02s02-a14-2-2x-60fps.webm", start_image = "e02s02-a14-2 mh-bj1-01")
image e02s02-a14-3 = Movie(play = "images/E-02/s02/anim/e02s02-a14-3-2x-50fps.webm", start_image = "e02s02-a14-3 mh-bj1-01")
image e02s02-a14-3-f = Movie(play = "images/E-02/s02/anim/e02s02-a14-3-2x-60fps.webm", start_image = "e02s02-a14-3 mh-bj1-01")

image e02s02-a16-1 = Movie(play = "images/E-02/s02/anim/e02s02-a16-1-2x-50fps.webm", start_image = "e02s02-a16-1 mh-bj2-01")
image e02s02-a16-1-f = Movie(play = "images/E-02/s02/anim/e02s02-a16-1-2x-60fps.webm", start_image = "e02s02-a16-1 mh-bj2-01")
image e02s02-a16-2 = Movie(play = "images/E-02/s02/anim/e02s02-a16-2-2x-50fps.webm", start_image = "e02s02-a16-2 mh-bj2-01")
image e02s02-a16-2-f = Movie(play = "images/E-02/s02/anim/e02s02-a16-2-2x-60fps.webm", start_image = "e02s02-a16-2 mh-bj2-01")
image e02s02-a16-3 = Movie(play = "images/E-02/s02/anim/e02s02-a16-3-2x-50fps.webm", start_image = "e02s02-a16-3 mh-bj2-01")
image e02s02-a16-3-f = Movie(play = "images/E-02/s02/anim/e02s02-a16-3-2x-60fps.webm", start_image = "e02s02-a16-3 mh-bj2-01")

label e02s02:

    scene black
    show screen scene_transistion(_("The next day"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    queue music morning_vibes
    $ renpy.music.set_volume(0.7, 0.0, "sound2" )
    play sound2 sfx_weather_arctic_wind fadein 3.0
    scene e02s02-01 mc-mh-talk1_c1
    with Fade(0.5, 0.5, 0.9)
    $ renpy.music.set_volume(0.7, 3.0, "music" )
    pause
    play voice2 mc_surprised_huh3 noloop
    mc "I forgot our map in the hotel room."
    scene e02s02-01 mc-mh-talk1_c2 with dissolve
    play voice3 lissa_lno noloop
    mh "No, you didn't, it flew away."
    mh "Anyway, I think we'll manage without it."
    scene e02s02-02 mc-mh-talk2_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "How are you feeling?"
    play voice3 dahlia_thinking_mmm2 noloop
    mh "About what?"
    mc "You know."
    scene e02s02-02 mc-mh-talk2_c2 with dissolve
    play voice3 lissa_haha2 noloop
    mh "It’ll be fine. I doubt it’s anything to worry about. Forty deaths a year isn’t that extreme."
    scene e02s02-03 mc-mh-talk3_c1 with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yeah, that’s what I’ve been saying."
    scene e02s02-03 mc-mh-talk3_c2 with dissolve
    play voice3 lissa_thinking noloop
    mh "Though it makes you wonder, how many of those forty were beginners like us?"
    mh "In the case of car fatalities, for instance, do the deaths come mostly from experienced or inexperienced drivers?"
    scene e02s02-04 mc-mh-talk4_c1 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "You tell me, you’re the one who went to law school."
    scene e02s02-04 mc-mh-talk4_c2 with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    mh "Drinking and driving, as well as reckless speeding, transcend the paradigm of beginner and advanced."
    scene e02s02-05 mc-mh-talk5_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Good thing we're not day drinkings."
    scene e02s02-06 mc-mh-talk6_c2 with dissolve
    play voice3 lissa_shyoh noloop
    mh "Very good."
    scene e02s02-07 mc-mh-talk7_c1 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "On the other hand, a little wine might dull some of the pain we’re going to experience."
    scene e02s02-07 mc-mh-talk7_c2 with dissolve
    play voice3 lissa_mmm1 noloop
    mh "Thanks for making me feel better, you’d make a great grief counselor..."
    scene e02s02-08 mc-mh-talk8_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "I'm sure sure your friends will appreciate it."
    scene e02s02-08 mc-mh-talk8_c2 with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    pause
    scene e02s02-09 mc-mh-talk9_c1 with dissolve
    play voice2 d2s9_confused noloop
    mc "Since we’re stuck here for a while, maybe we should check Oliver's newest message."
    mc "This one is not about work. He hopes we're having a nice time here."
    scene e02s02-09 mc-mh-talk9_c2 with dissolve
    play voice3 lissa_ugu noloop
    mh "That’s sweet of him."
    scene e02s02-10 mc-mh-talk10_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "I {i}did{/i} check the first message. It sounds like he is buried in work. He might need a vacation of his own."
    scene e02s02-10 mc-mh-talk10_c2 with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    mh "He has been working pretty hard. I’ll find some way to make it up to him."
    scene e02s02-11 mc-mh-talk11_c2 with dissolve
    play voice3 dahlia_angry_oof noloop
    mh "How did we get to talking about work again?"
    scene e02s02-11 mc-mh-talk11_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "My fault."

label replay_e02s02 hide:

    mc "Say, have you wondered what would happen to us if we got stuck up here?"
    if _in_replay:
        play music morning_vibes
        $ renpy.music.set_volume(0.7, 0.0, "sound2" )
        play sound2 sfx_weather_arctic_wind fadein 3.0
    scene e02s02-11 mc-mh-talk11_c2 with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    mh "I’d jump."
    scene e02s02-10 mc-mh-talk10_c1 with dissolve
    play voice2 mc_surprised_what3 noloop
    mc "Really, you’d jump?"
    scene e02s02-10 mc-mh-talk10_c2 with dissolve
    play voice3 dahlia_arrogant_yeah noloop
    mh "Yeah. The snow would break my fall, right?"
    scene e02s02-09 mc-mh-talk9_c1 with dissolve
    play voice2 mc_no_no4 noloop
    mc "No, the snow would break you, are you joking?"
    play voice3 dahlia_no_nope noloop
    mh "I’m not really known for my sense of humor."
    mc "You’re going to jump at this height. You’re insane."
    scene e02s02-08 mc-mh-talk8_c2 with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    mh "It’s your hypothetical. Plus, the snow here is really fluffy and light. It wouldn’t be like what you’re imagining."
    scene e02s02-08 mc-mh-talk8_c1 with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "I was expecting a different answer. Maybe like calling someone for help."
    scene e02s02-07 mc-mh-talk7_c2 with dissolve
    play voice3 lissa_oh noloop
    mh "I don’t have my phone."
    play voice2 mc_thinking_mmm3 noloop
    mc "Yell out?"
    mh "My voice doesn’t project that much."

    $ Lovense.stop()

    play sound sfx_cloth_rustling4
    scene e02s02-12 mc-mh-hands_c1 with dissolve
    $ Lovense.vibrate(1)
    play voice2 mc_happy_hah2 noloop
    mc "It seems to project during sex."
    play voice3 lissa_oh2 noloop
    mh "Well, I wouldn't want to start an avalanche."
    scene e02s02-12 mc-mh-hands_c2 with dissolve
    play voice3 lissa_laugh2 noloop
    mh "You know, it’s hard to ski while having an erection in your pants."
    scene e02s02-12 mc-mh-hands_c3 with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "Mmm. I could say the same about you."
    play sound sfx_jeans_on1
    scene e02s02-14 mc-mh-hj2_c3 with dissolve
    $ Lovense.vibrate(3)
    play voice3 lissa_moan2 noloop
    mh "How much time do you think we have until we reach the top?"
    scene e02s02-14 mc-mh-hj2_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "It’ll be enough."
    play voice3 mc_sex_sucking_fast2 noloop
    $ Lovense.vibrate(7)
    scene e02s02-15 mc-mh-bj_c1 with dissolve
    stop voice3 fadeout 1.0
    play voice2 mc_pain_ou1 noloop
    mc "Fuck, it’s cold, but your mouth is so warm."
    $ Lovense.vibrate(3)
    scene e02s02-14 mc-mh-hj2_c2 with dissolve
    play voice3 lissa_moan3 noloop
    mh "My cock is still cold."
    play voice2 mc_yes_yeah4 noloop
    mc "I can help."
    scene e02s02-14 mc-mh-hj2_c1 with dissolve
    play voice3 lissa_moan1 noloop
    mh "You need to jerk me off faster than that."
    play voice2 mc_arrogant_heh1 noloop
    mc "Alright, then."
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    scene e02s02-a14-1 mh-bj1-01 with dissolve
    play voice3 aaleyah_sucking_deep
    play voice2 d7s4_mcbreathing fadein 1.5
    $ Lovense.pattern("7;11", 1700)
    scene e02s02-a14-1
    mh "*Glug* glug*"
    scene e02s02-a14-2 with dissolve
    pause
    scene e02s02-a14-3 with dissolve
    pause
    mh "*Pop*"
    $ renpy.music.set_volume(0.7, 2.0, "music" )
    $ Lovense.stop()
    $ Lovense.vibrate(4)
    scene e02s02-15 mc-mh-bj_c3 with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Wait a minute, are you getting harder? Thinking about what will happen if we fall off?"
    scene e02s02-14 mc-mh-hj2_c3 with dissolve
    play voice3 lissa_moan4 noloop
    mh "I didn’t even think of that."
    play voice2 d1s5_mcthinks noloop volume 1.6
    mc "How about I take some photos?"
    play sound cameraclick
    scene e02s02-15-2 mc-mh-bj-talk1_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Imagine looking at these photos years from now."
    play voice3 lissa_moan1 noloop
    mh "Mmm..."
    scene e02s02-15-2 mc-mh-bj-talk1_c2 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "You’re so bad, Lyssa. Sucking my dick two hundred feet up in the air?"
    scene e02s02-15-2 mc-mh-bj-talk1_c3 with dissolve
    play voice3 lissa_aga noloop
    mh "Honestly, this is a really bad idea... but a great new experience."
    play voice3 lissa_sucking
    $ Lovense.pattern("8;12", 1700)
    scene e02s02-a16-1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    queue voice2 d7s4_mcbreathing
    play sound sfx_handjob_cream1 loop fadein 1.5 volume 2.0
    mc "Keep going. Lick my balls too while my dick is in your mouth."
    scene e02s02-a16-2 with dissolve
    mc "We’re almost there..."
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    scene e02s02-a16-3 with dissolve
    pause
    $ Lovense.pattern("8;12", 900)
    scene e02s02-a16-1-f with dissolve
    pause
    mc "And I’m on the edge..."
    mc "Don’t stop."
    scene e02s02-a16-2-f with dissolve
    play voice3 nora_sucking1 noloop
    queue voice3 lissa_sucking
    mh "I’m going to cum soon..."
    pause
    scene e02s02-a16-3-f with dissolve
    pause
    play voice2 mc_scared_oh4 noloop
    mc "Oh shit, fuck, here it comes. Fuck!"
    play voice2 d1s5_orgasm noloop
    play voice3 lissa_moan7 noloop
    stop sound fadeout 1.0
    $ Lovense.stop()
    $ Lovense.vibrate(16)
    scene e02s02-17 mc-mh-cum_c1
    with hpunch
    mh "Ahh!!!!"
    play voice2 d1s5_orgasm2 noloop
    play voice3 dahlia_sex_closedmoan5 noloop
    scene e02s02-16 mc-mh-bj2_c3 with hpunch
    pause
    $ renpy.music.set_volume(0.7, 3.0, "music" )
    $ Lovense.vibrate(3)
    scene e02s02-17 mc-mh-cum_c3 with dissolve
    play voice3 polly_breathing noloop
    mh "So good... my legs are so weak right now."
    play voice2 mc_yes_ugu1 noloop
    mc "Mine too."
    mc "Let’s just take another ski lift down, and ski another time."
    mc "I don’t want you to worry too much on the first day."
    $ Lovense.vibrate(1)
    scene e02s02-17 mc-mh-cum_c1 with dissolve
    play voice3 lissa_mmm1 noloop
    mh "You just want me to suck your dick again, don’t you?"
    play voice2 mc_yes_sure1 noloop
    mc "I mean it sounds like a decent offer."
    $ unlock_gallery_slot("scene", "e02s02")
    mh "One of these days though, we have to ski. We can’t have sex the entire time we’re here."
    mc "Hey, let’s not rule anything out."

    $ Lovense.stop()

    $ renpy.end_replay()
    $ renpy.music.set_volume(0.4, 2.0, "sound2" )
    play sound sfx_snowboard_slide1
    scene e02s02-20 mc-mh-ski1_c1 with Fade(0.5, 0.5, .5)
    stop sound fadeout 3.5
    play voice2 mc_happy_wooh3 noloop
    mc "Why didn't anyone tell me this was going to be so great?"
    scene e02s02-20 mc-mh-ski1_c2 with dissolve
    play voice3 lissa_ha noloop
    mh "You seem to be getting the hang of it."
    scene e02s02-20 mc-mh-ski1_c3 with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Am I?"
    scene e02s02-20 mc-mh-ski1_c2 with dissolve
    play voice3 lissa_aga noloop
    mh "You're not falling like when we first tried it. That's a true mark of success."
    scene e02s02-21 mc-mh-ski2_c1 with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "That's a relief to hear, thank you."
    play voice3 lissa_laugh noloop
    mh "Now who's the one being sarcastic?"
    scene e02s02-22 mc-mh-ski3_c1 with dissolve
    play voice2 d2s9_mchey noloop volume 1.6
    mc "I must have gotten that from you."
    mc "I'm not a sarcastic person in general."
    scene e02s02-22 mc-mh-ski3_c2 with dissolve
    play voice3 lissa_ugu2 noloop
    mh "Nor am I."
    scene e02s02-23 mc-mh-ski4_c1 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "First time?"
    scene e02s02-23 mc-mh-ski4_c2 with dissolve
    play voice3 dahlia_no_simple noloop
    mh "No."
    scene e02s02-24 mc-mh-ski5_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "You go skiing a lot?"
    scene e02s02-24 mc-mh-ski5_c2 with dissolve
    play voice3 dahlia_no_uhuh noloop
    mh "No, not really. In order to go skiing, I would require snow."
    mh "And we don't live in a snowy climate, thus making the occasion special."
    play sound sfx_snowboard_slide1
    scene e02s02-25 mc-mh-ski6_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay, you don’t ski that often. How are you so good at it then?"
    scene e02s02-25 mc-mh-ski6_c2 with dissolve
    play voice3 lissa_haha2 noloop
    mh "It's all about balance."
    mh "You have to warm yourself up and then maintain a center of gravity."
    scene e02s02-26 mc-mh-ski7_c1 with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "Warm up? In this location?"
    scene e02s02-26 mc-mh-ski7_c2 with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    mh "I mean warming up as in stretching."
    scene e02s02-27 mc-mh-ski8_c1 with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Ah gotcha! Good thing we already stretched out the most important part."
    scene e02s02-27 mc-mh-ski8_c2 with dissolve
    play voice3 lissa_laugh2 noloop
    mh "Mmmm. You certainly wouldn't want to pull a muscle there."
    play voice2 mc_scared_huh1 noloop
    play sound sfx_snowboard_stop2
    scene e02s02-31 mc-mh-ski12_c1 with vpunch
    pause
    scene e02s02-30 mc-mh-ski11_c1 with dissolve
    play voice2 mc_happy_oof2 noloop
    mc "Shit, did you see that? I almost fell!"
    mct "This is a nightmare, I'll need inertial dampeners at this rate."
    scene e02s02-31 mc-mh-ski12_c2 with dissolve
    play voice3 dahlia_yes_aga noloop
    mh "Bank left, follow the trail, and avoid crashing into those trees. I'll see you down there."
    play sound sfx_snowboard_slide1
    scene e02s02-32 mc-mh-ski13_c1 with dissolve
    pause

    stop music fadeout 3.5
    stop sound2 fadeout 3.0
    stop sound fadeout 3.0
    jump e02s03

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
