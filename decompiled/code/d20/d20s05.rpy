image d20s05-pole-a1 = Movie(play = "images/Day-20/s05/anim/d20s05-a24-04-01-2x-50fps.webm", start_image = "d20s05-a24-04-01 mes-stripping-anim-24-04-01-00_i")
image d20s05-pole-a2 = Movie(play = "images/Day-20/s05/anim/d20s05-a24-05-01-2x-50fps.webm", start_image = "d20s05-a24-05-01 mc-mes-stripping-anim-24-05-01-00_i")
image d20s05-pole-a3 = Movie(play = "images/Day-20/s05/anim/d20s05-a24-05-02-2x-50fps.webm", start_image = "d20s05-a24-05-02 mc-mes-stripping-anim-24-05-02-00_i")

image d20s05-a1-f = Movie(play = "images/Day-20/s05/anim/d20s05-a37-1-2x-50fps.webm", start_image = "d20s05-a37-1 mc-mes-more-cuddles-01")
image d20s05-a1 = Movie(play = "images/Day-20/s05/anim/d20s05-a37-1-3x-60fps.webm", start_image = "d20s05-a37-1 mc-mes-more-cuddles-01")
image d20s05-a2-f = Movie(play = "images/Day-20/s05/anim/d20s05-a37-2-2x-50fps.webm", start_image = "d20s05-a37-2 mc-mes-more-cuddles-01")
image d20s05-a2 = Movie(play = "images/Day-20/s05/anim/d20s05-a37-2-3x-60fps.webm", start_image = "d20s05-a37-2 mc-mes-more-cuddles-01")
image d20s05-a3-f = Movie(play = "images/Day-20/s05/anim/d20s05-a37-3-2x-50fps.webm", start_image = "d20s05-a37-3 mc-mes-more-cuddles-01")
image d20s05-a3 = Movie(play = "images/Day-20/s05/anim/d20s05-a37-3-3x-60fps.webm", start_image = "d20s05-a37-3 mc-mes-more-cuddles-01")
image d20s05-a4-f = Movie(play = "images/Day-20/s05/anim/d20s05-a39-1-2x-50fps.webm", start_image = "d20s05-a39-1 mc-mes-underwater-fuck-01")
image d20s05-a4 = Movie(play = "images/Day-20/s05/anim/d20s05-a39-1-3x-60fps.webm", start_image = "d20s05-a39-1 mc-mes-underwater-fuck-01")
image d20s05-a5-f = Movie(play = "images/Day-20/s05/anim/d20s05-a39-2-2x-50fps.webm", start_image = "d20s05-a39-2 mc-mes-underwater-fuck-01")
image d20s05-a5 = Movie(play = "images/Day-20/s05/anim/d20s05-a39-2-3x-60fps.webm", start_image = "d20s05-a39-2 mc-mes-underwater-fuck-01")
image d20s05-a6-f = Movie(play = "images/Day-20/s05/anim/d20s05-a39-3-2x-50fps.webm", start_image = "d20s05-a39-3 mc-mes-underwater-fuck-01")
image d20s05-a6 = Movie(play = "images/Day-20/s05/anim/d20s05-a39-3-3x-60fps.webm", start_image = "d20s05-a39-3 mc-mes-underwater-fuck-01")

image d20s05-a7 = Movie(play = "images/Day-20/s05/anim/d20s05-a41-02-01-2x-50fps.webm", start_image = "d20s05-a41-02-01 mc-mes-above-the-water-anim-41-02-01-01")
image d20s05-a8 = Movie(play = "images/Day-20/s05/anim/d20s05-a41-02-02-2x-50fps.webm", start_image = "d20s05-a41-02-02 mc-mes-above-the-water-anim-41-02-02-01")
image d20s05-a9 = Movie(play = "images/Day-20/s05/anim/d20s05-a42-01-01-2x-50fps.webm", start_image = "d20s05-a42-01-01 mc-mes-above-the-water-anim-42-01-01-01")
image d20s05-a10 = Movie(play = "images/Day-20/s05/anim/d20s05-a42-02-02-2x-50fps.webm", start_image = "d20s05-a42-02-02 mc-mes-above-the-water-anim-42-02-02-00")
image d20s05-a11 = Movie(play = "images/Day-20/s05/anim/d20s05-a43-02-2x-50fps.webm", start_image = "d20s05-a43-02 mc-mes-head underwater-anim-43-02-01")
image d20s05-a12 = Movie(play = "images/Day-20/s05/anim/d20s05-a43-01-2x-50fps.webm", start_image = "d20s05-a43-01 mc-mes-head underwater-anim-43-01-01")

label d20s05:

    $ d20s05_joke = False
    $ d20s05_mes_solo = False

    if date_mes is False:
        jump d20s06

    if d20s04_pass_exam is False:
        $ renpy.music.set_volume(0.25, 5.0, "music")
        queue music music_melancholy_forever
    if d20s04_pass_exam is True:
        $ renpy.music.set_volume(0.5, 4.0, "music")
        queue music music_mission_completed
    play sound ["<silence 0.3>", sfx_door_open1]
    scene d20s05-01 mc-mes-waiting with Fade(0.5, 0.5, 0.5)
    pause
    scene d20s05-02 mc-mes-talking with dissolve
    play voice3 min_arrogant_huh2 noloop
    mes "So... Tell me about your exams!!!{w} How did you do?!"
    menu:
        "Tell Her You Passed (Truth)"(hint="d20s05m01c01") if d20s04_pass_exam is True:
            play sound sfx_door_closed2
            scene d20s05-03 mc-mes-talking with dissolve
            play voice2 mc_happy_yay1 noloop
            mc "I passed!"
            scene d20s05-04 mc-mes-talking with dissolve
            play voice3 min_happy_mmm noloop
            mes "Of course you did. I had complete faith in you."
            scene d20s05-05 mc-mes-pretending-to-fail with dissolve
            play voice2 mc_disgust_pfe1 noloop
            mc "I wish I had been so confident. My legs are still a little shaky."
            scene d20s05-06 mc-mes-caught with dissolve
            play voice3 min_surprised_oh noloop
            mes "Oh really?"
            scene d20s05-07 mc-talking with dissolve
            play voice2 d9s3_no noloop volume 1.7
            mc "Not literally...{w} Why? What do you have planned?"

            jump d20s05_celebrate

        "Pretend You Failed"(hint="d20s05m01c02") if d20s04_pass_exam is True:
            $ d20s05_joke = True

            play sound sfx_door_closed2
            scene d20s05-05 mc-mes-pretending-to-fail with dissolve
            play voice2 mc_disappointed_ah1 noloop
            mc "Well, I hate to admit it, but-"
            scene d20s05-06 mc-mes-caught with dissolve
            play voice3 min_disappointed_ehh3 noloop
            mes "You can cut the bullshit. I can tell that you passed."
            scene d20s05-07 mc-talking with dissolve
            play voice2 mc_arrogant_huh2 noloop
            mc "How did you know?"
            scene d20s05-04 mc-mes-talking with dissolve
            play voice3 min_no_uhuh noloop
            mes "I'll never reveal my secrets."
            scene d20s05-03 mc-mes-talking with dissolve
            play voice2 mc_disappointed_off1 noloop
            mc "You know, Min.{w} You're the best kind of scary."

            jump d20s05_celebrate

        "Tell Her You Failed (Truth)"(hint="d20s05m01c03") if d20s04_pass_exam is False:
            play sound sfx_door_closed2
            scene d20s05-08 mc-mes-failure with dissolve
            play voice2 mc_disappointed_ah1 noloop
            mc "Fuck, Min... I failed."
            scene d20s05-09 mc-mes-talking with dissolve
            play voice3 min_thinking_mhh noloop
            mes "Shit."
            scene d20s05-10 mc-mes-talking with dissolve
            play voice2 mc_yes_yeah1 noloop
            mc "Yeah. I feel like I got punched in the gut."
            scene d20s05-11 mc-mes-talking with dissolve
            play voice3 min_arrogant_hm noloop
            mes "Damn. How is that possible? I thought you were doing well."
            scene d20s05-08 mc-mes-failure with dissolve
            play voice2 mc_thinking_mmm5 noloop
            mc "I don't know. What can I say?{w} I fucked up."
            scene d20s05-09 mc-mes-talking with dissolve
            play voice3 min_surprised_ehh1 noloop
            mes "I'm sorry.{w} I mean, I'm disappointed, but mostly I feel bad for you."
            scene d20s05-10 mc-mes-talking with dissolve
            play voice2 mc_arrogant_hm3 noloop
            mc "You're not particularly comforting, you know that?"
            scene d20s05-11 mc-mes-talking with dissolve
            play voice3 min_yes_yeah1 noloop
            mes "Yeah, my bad. What are you going to do?"
            scene d20s05-05 mc-mes-pretending-to-fail with dissolve
            play voice2 mc_angry_huh2 noloop
            mc "I think I'm just going to go for a walk."
            scene d20s05-04 mc-mes-talking with dissolve
            play voice3 min_thinking_hmm3 noloop
            mes "Oh. That makes sense.{w} Do you want some company?"
            scene d20s05-08 mc-mes-failure with dissolve
            play voice2 mc_no_no5 noloop
            mc "No thanks.{w} I'll see you around later."
            scene d20s05-09 mc-mes-talking with dissolve
            play voice3 min_thinking_hmm1 noloop
            mes "Okay... if you're sure..."
            scene d20s05-07 mc-talking with dissolve
            play voice2 mc_hey_hey2 noloop
            mc "Don't get me wrong. I love spending time with you. I just want to be alone right now."
            scene d20s05-12 mc-mes-leaving with dissolve
            play voice2 mc_angry_hm2 noloop
            mct "I'm better off without her around to remind me how bad I failed today."

            $ renpy.music.set_volume(0.6, 3.0, "music")
            jump d20s05_end

label replay_d20s05:
label d20s05_celebrate:

    if _in_replay:
        $ renpy.music.set_volume(0.5, 4.0, "music")
        play music music_mission_completed
    scene d20s05-13 mc-mes-talking with dissolve
    play voice3 min_arrogant_huh1 noloop
    mes "So, if you have a little free time right now I'd suggest we celebrate."
    scene d20s05-14 mc-mes-talking with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "I assume you passed your exams as well?"
    scene d20s05-11 mc-mes-talking with dissolve
    play voice3 min_arrogant_pff noloop
    mes "Did you ever have any doubts?"
    scene d20s05-07 mc-talking with dissolve
    play voice2 mc_no_nope2 noloop
    mc "Of course not. So we'll be celebrating our mutual successes."
    scene d20s05-13 mc-mes-talking with dissolve
    play voice3 min_happy_yeah noloop volume 0.7
    mes "Back at my place. I've got a special sexy outfit there that I can't wait to take off for you."
    scene d20s05-14 mc-mes-talking with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "I can definitely make time for that."
    scene d20s05-15 mc-mes-going with dissolve
    play voice3 min_thinking_hmm2 noloop
    mes "Alright!{w} Come with me."
    scene d20s05-16 mes-rearshot with dissolve
    play voice2 d1s1_mmm noloop
    mct "I'd follow that ass anywhere."

    jump d20s05_mes_house

label d20s05_mes_house:

    scene black
    show screen scene_transistion(_("Some time later\nAt Min's house"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound sfx_bed_slide3 volume 0.6
    scene d20s05-17 mes-sexy-outfit
    with Fade(0.5, 0.5, 0.5)
    pause
    play voice3 min_old_hmm noloop
    mes "Have a seat. I have something special to show you."
    scene d20s05-18 mc-mes-talking with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "I'm puddy in your hands."
    play voice3 min_no_nah noloop
    mes "Not yet.{w} This will be a feast for your eyes."
    scene d20s05-19 mc-mes-sitting with dissolve
    play voice2 mc_scared_huuuh3 noloop
    mc "You don't mean...?"
    play voice3 min_old_laugh noloop
    mes "Did you think I just had this pole here for decoration...{w} or maybe for parties?"
    play voice2 d2s12_emmm noloop
    mc "I didn't..."


    $ Lovense.stop()

    scene d20s05-20 mc-mes-shush with dissolve
    play voice3 fshhh noloop
    mes "Shhh.{w} Just enjoy the show."
    $ renpy.music.set_volume(0.7, 4.0, "music")
    $ Lovense.vibrate(1)
    scene d20s05-21 mes-dancing with dissolve
    pause
    scene d20s05-22 mes-dancing with dissolve
    play voice2 mc_scared_oh1 noloop
    mct "Oh my."
    scene d20s05-23 mes-stripping with dissolve
    pause
    $ Lovense.vibrate(2)
    scene d20s05-24 mc-mes-stripping with dissolve
    play voice3 min_thinking_hmm3 noloop
    mes "You gotta gamble if you're gonna win..."
    scene d20s05-24-02 mes-stripping with dissolve
    play voice3 min_happy_yeah noloop
    mes "I'm betting on myself..."
    play sound sfx_clothes_undress1 volume 2.5
    scene d20s05-24-03 mc-mes-stripping with dissolve
    mes "And I'm gonna win!"
    play sound sfx_shoes_off1 volume 2.0
    scene d20s05-24-04 mes-stripping with dissolve
    pause
    $ renpy.music.set_volume(1.0, 1.0, "sound2")
    play sound2 sfx_stripper_pole_spin1
    scene d20s05-pole-a1 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    $ Lovense.vibrate(3)
    mct "Where on earth did she learn to dance like that?"
    pause
    stop sound2 fadeout 1.0
    play sound sfx_underpants_off1 volume 3.5
    scene d20s05-24-05 mc-mes-stripping with dissolve
    pause
    play sound2 sfx_stripper_pole_spin1
    scene d20s05-pole-a2 with dissolve
    mct "Did she come up with this herself? I need to get her some lessons somewhere."
    pause
    scene d20s05-pole-a3 with dissolve
    mct "Doesn't matter. Min is hot even if her dancing is shit."
    pause
    stop sound2 fadeout 1.0
    scene d20s05-24-06 mc-mes-stripping with dissolve
    pause
    play voice3 dahlia_sex_closedmoan1 noloop
    $ Lovense.vibrate(4)
    scene d20s05-24-07 mc-mes-stripping with dissolve
    pause
    $ renpy.music.set_volume(0.45, 2.0, "music")
    scene d20s05-24-08 mc-mes-stripping with dissolve
    play voice2 d1s5_orgasm noloop
    mct "God damn.{w} I can't wait to fuck her senseless."
    play voice2 mc_scared_huh1 noloop
    play sound sfx_bed_slide2
    play sound2 sfx_kick4 noloop
    scene d20s05-24-09 mc-mes-pushing back with hpunch
    pause
    scene d20s05-25 mc-mes-talking with dissolve
    play voice3 min_disappointed_ehh1 noloop
    mes "Honey, you could never handle me..."
    scene d20s05-26 mc-mes-lapdance with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "All the blood has rushed from my head."
    scene d20s05-27 mc-mes-talking with dissolve
    play voice3 min_yes_simple noloop
    mes "That means I'm doing my job right."
    scene d20s05-28 mc-mes-lapdance with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "I can barely think. I just want to fuck her."
    mes "I'm all pelvic thrust...{w} and I'm on the prowl for you!"
    play sound sfx_cloth_rustling4 volume 2.0
    scene d20s05-29 mc-mes-lapdance with dissolve
    play voice2 mc_surprised_what1 noloop
    mct "... What{w} the fuck did she say?"
    mct "Doesn't matter.{w} My whole being is focused on shoving my dick deep inside her."
    scene d20s05-30 mc-mes-lapdance with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    mes "This is only the beginning. Follow me."
    $ unlock_gallery_slot("cg", "d20s05")
    $ Lovense.vibrate(2)
    scene d20s05-31 mc-mes-walking to the pool with dissolve
    play voice2 d3s11b_mcheh noloop
    mct "I'd follow that ass anywhere."

    jump d20s05_pool

label d20s05_pool:

    $ renpy.music.set_volume(1.0, 4.0, "sound2")
    $ renpy.music.set_volume(1.0, 1.0, "sound3")
    play sound2 sfx_pool_ambience1 fadein 2.5
    scene d20s05-32 mc-mes-at the pool with Fade(0.5, 0.5, 0.5)
    pause
    scene d20s05-33 mc-mes-at the pool talking with dissolve
    play voice3 min_angry_breath noloop
    mes "I'm going to fuck you like there's no tomorrow."
    play voice2 d1s2_hmm noloop volume 1.6
    mc "Shouldn't I be the one fucking you?"
    play sound sfx_fall_mud1
    $ renpy.music.set_volume(0.5, 4.0, "music")
    play voice2 mc_scared_huuuh1 noloop
    scene d20s05-34 mc-mes-pulling mc underwater with dissolve
    pause
    play sound sfx_water_splash2 volume 3.0
    play sound2 sfx_underwater_loop1
    scene d20s05-35 mc-mes-splash with dissolve
    stop sound fadeout 1.0
    pause
    scene d20s05-36 mc-mes-underwater cuddles with dissolve
    pause
    play sound min_kiss_underwater1
    $ Lovense.vibrate(3)
    scene d20s05-36-02 mc-mes-underwater cuddles with dissolve
    pause
    scene d20s05-a37-1 mc-mes-more-cuddles-01 with dissolve
    pause
    play sound3 sfx_underwater_fingering1
    play sound [sfx_water_bubbles1, "<silence 2.3>", sfx_water_bubbles2] loop
    play voice3 min_sex_underwater_moans1
    $ Lovense.pattern("5;8", 1700)
    scene d20s05-a1
    pause
    scene d20s05-a2 with dissolve
    pause
    scene d20s05-a3 with dissolve
    pause
    play sound3 sfx_underwater_fingering_fast1
    $ Lovense.pattern("5;8", 900)
    scene d20s05-a1-f with dissolve
    pause
    scene d20s05-a2-f with dissolve
    pause
    scene d20s05-a3-f with dissolve
    pause
    play sound3 sfx_underwater_fingering1
    $ Lovense.pattern("5;8", 1700)
    scene d20s05-a4 with dissolve
    pause
    scene d20s05-a5 with dissolve
    pause
    scene d20s05-a6 with dissolve
    pause
    play sound3 sfx_underwater_fingering_fast1
    $ Lovense.pattern("5;8", 900)
    scene d20s05-a4-f with dissolve
    pause
    scene d20s05-a5-f with dissolve
    pause
    scene d20s05-a6-f with dissolve
    pause
    play sound2 sfx_pool_ambience1 fadein 2.5
    play sound sfx_water_floatup1
    play voice3 min_old_breathing noloop
    scene d20s05-41 mc-mes-above the water with fade
    $ Lovense.pattern("5;8", 1700)
    mes "I've always wanted to do this."
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "You've never had sex in this pool?"
    mes "There's a first time for everything."
    scene d20s05-a41-02-01 mc-mes-above-the-water-anim-41-02-01-01 with fade
    pause
    play sound [sfx_water_run1, sfx_water_swim1] loop
    play voice2 d7s4_mcbreathing
    play voice3 min_old_moans
    $ Lovense.pattern("6;9", 600)
    scene d20s05-a7
    pause
    play sound sfx_water_bubbles1
    play sound2 sfx_underwater_loop1
    play sound3 sfx_underwater_fingering_fast1
    scene d20s05-a8 with dissolve
    pause
    stop sound3 fadeout 1.0




    stop voice3 fadeout 1.0
    play sound2 sfx_pool_ambience1 fadein 2.5
    play sound sfx_water_floatup1
    $ Lovense.stop()
    $ Lovense.vibrate(4)
    scene d20s05-a43-02 mc-mes-head underwater-anim-43-02-01 with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "Let's change things up a bit."
    play sound [sfx_water_run1, sfx_water_swim1] loop
    play voice3 min_old_longmoan2
    play voice2 d7s4_mcbreathing
    $ Lovense.pattern("6;9", 600)
    scene d20s05-a11 with dissolve
    pause
    scene d20s05-a12 with dissolve
    pause
    play sound sfx_water_splash2 volume 3.5
    play voice2 mc_angry_errr4 noloop
    play voice3 min_sex_underwater_moans2 noloop
    $ Lovense.stop()
    $ Lovense.vibrate(6)
    scene d20s05-43-02 mc-mes-head underwater with vpunch
    pause
    mc "I'm going to fucking cum so deep in you!"
    scene d20s05-43-2 mc-mes-head underwater with dissolve
    pause
    play sound2 sfx_underwater_loop1
    play sound3 sfx_underwater_fingering_fast1
    play sound [sfx_water_bubbles1, "<silence 2.3>", sfx_water_bubbles2] loop
    play voice3 min_sex_underwater_moans3
    $ Lovense.pattern("8;12", 600)
    scene d20s05-a10 with dissolve
    pause
    play sound2 sfx_pool_ambience1
    play voice2 d7s4_mcbreathing
    scene d20s05-a9 with dissolve
    pause
    mc "I'm gonna cum! I'm going to fucking cum!!!"
    stop sound fadeout 0.5
    play voice3 min_old_orgasm2 noloop
    play voice2 d9s5_auch2 noloop
    stop sound3 fadeout 1.0
    $ Lovense.stop()
    $ Lovense.vibrate(17)
    scene d20s05-44 mc-mes-head above water with vpunch
    mes "I'MMMMMmm CUMMMMmmminnnggg!!!!"
    play voice2 mc_pain_argh1 noloop
    play sound2 sfx_underwater_loop1
    $ Lovense.vibrate(18)
    scene d20s05-44-02 mc-mes-cumming with hpunch
    mc "FUUUUuuCCCKkkkk YEEEAAaaahhhh!!!"
    scene d20s05-46 mc-mes-talking with fade
    $ Lovense.vibrate(1)
    play sound2 sfx_pool_ambience1
    play voice2 mc_surprised_wow2 noloop
    mc "*panting* Wow. That was something else."
    play voice3 min_old_moan1 noloop
    mes "You're telling me."
    play voice2 mc_hey_hey3 noloop
    mc "Really?{w} ...what the fuck was that???"
    scene d20s05-47 mc-mes-talking with dissolve
    play voice3 min_thinking_mhh noloop
    mes "I've always wanted to try it."
    play voice2 mc_disappointed_off2 noloop
    mc "Well...{w} at least for me, it was worth it."
    scene d20s05-48 mc-mes-talking with dissolve
    play voice3 min_thinking_oh noloop
    mes "It felt ridiculous, but also hot...{w} and I came like a demon possessed."
    play voice2 mc_arrogant_hm1 noloop
    mc "Would that be a person possessed by a demon, or-"
    scene d20s05-47 mc-mes-talking with dissolve
    play voice3 min_disappointed_ehh2 noloop
    mes "Like a demon possessed by another demon."
    play voice2 mc_surprised_wow1 noloop
    mc "Wow."
    mes "You said it."
    mc "I didn't know you had that in you."
    scene d20s05-49 mc-mes-facing away with dissolve
    play voice3 min_yes_ugu noloop
    mes "There's a lot you don't know about me.{w}.. yet."
    play voice2 mc_yes_yeah1 noloop
    mc "I look forward to-"
    mes "I know you do. Just enjoy this moment while we can."


    $ Lovense.stop()

    $ renpy.end_replay()
    $ unlock_gallery_slot("scene", "d20s05")

    stop sound2 fadeout 1.5
    jump d20s05_pool_talk

label d20s05_pool_talk:

    $ renpy.music.set_volume(0.2, 4.0, "music")
    scene d20s05-50 mes-post fuck talk with Fade(0.5, 0.5, 0.5)
    play voice3 min_surprised_huh2 noloop
    mes "How many points do you think we'll get for that?"
    scene d20s05-51 mc-mes-post fuck talk with dissolve
    play voice2 mc_no_nah2 noloop
    mc "I don't think Fetish Locator is giving out points anymore."
    scene d20s05-52 mc-mes-post fuck talk with dissolve
    play voice3 min_arrogant_heh1 noloop
    mes "The app is still working. It doesn't say anything about points being suspended. What makes you say that?"
    scene d20s05-53 mc-mes-post fuck talk with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Well, I mean, Lydia...{w} You don't know?"
    scene d20s05-55 mc-mes-post fuck talk with dissolve
    play voice3 min_surprised_huh1 noloop
    mes "What about Lydia? What are you talking about?"
    scene d20s05-54 mc-post fuck talk with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "Lydia was the one behind Fetish Locator."
    scene d20s05-75 mes-talking with dissolve
    play voice3 min_surprised_what noloop
    mes "What? No. Lydia?{w} You're kidding me."
    scene d20s05-73 mc-talking with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah, I'm serious.{w} I mean, Jerome created the app, but he did it for her."
    scene d20s05-56 mes-post fuck talk with dissolve
    play voice3 min_disappointed_off noloop
    mes "That doesn't make any sense.{w} I better call her and find out what is really going on."
    scene d20s05-57 mc-mes-post fuck talk with dissolve
    play voice2 mc_no_uhuh1 noloop
    mc "Um... She can't answer the phone right now."
    scene d20s05-76 mes-talking with dissolve
    play voice3 min_happy_relief noloop
    mes "Why not?"
    scene d20s05-69 mc-talking with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "Lydia is in jail."
    play sound rewind
    stop music fadeout 0.5
    scene d20s05-58 mes-shock with dissolve
    play music music_melancholy_forever
    play voice3 jessie_what noloop
    mes "WHAT?!?!?!"
    scene d20s05-59 mc-mes-explaining with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Let me explain..."
    scene d20s05-58 mes-shock with dissolve
    play voice3 min_yes_serious noloop
    mes "You better fucking explain!"
    scene d20s05-60 mc-explaining with dissolve
    play voice2 mc_no_no5 noloop
    mc "No, there is too much. Let me sum up."
    if cage_ntr is True:
        mc "Lydia is actually a huge slut. She has a sex dungeon for slaves and everything."
        mc "Jerome is one of her sex slaves. He created Fetish Locator to make her happy."
        scene d20s05-60-02 mc-explaining-antagonist with dissolve
        play voice2 mc_disappointed_ehh4 noloop
        if is_antagonist_mode is True:
            mc "The whole app's purpose was to scout for new sex slaves...{w} so they could blackmail them."
        elif True:
            mc "The whole app's purpose was really just to scout for new sex slaves."
            scene d20s05-61 mc-mes-explaining with dissolve
            mc "The $1kk goal and VIP program and everything was a lie."
            mc "She just wanted more slaves to play with, tortment, and fuck."
    elif True:
        mc "You know Lydia's fetish... that she's a voyeur."
        mc "Jerome created Fetish Locator based on her fantasy - an unending source of fresh, new, sexy pics and videos that Lydia could enjoy."
        scene d20s05-60-02 mc-explaining-antagonist with dissolve
        play voice2 mc_disappointed_ehh4 noloop
        mc "The whole thing runs from some sort of Artificial Intelligence."
        mc "I guess he wanted to impress her and get her to fall in love with him, or have sex with him, or something."
        mc "It didn't work."
        scene d20s05-61 mc-mes-explaining with dissolve
        play voice2 d2s9_confused noloop volume 1.7
        mc "Well, I mean, the A.I. worked. The app worked.{w} But Lydia didn't fall for Jerome or whatever he wanted to get out of it.."
        if is_antagonist_mode is True:
            mc "The A.I. even started blackmailing people to get more content."
        elif True:
            mc "The A.I. even started a $1kk competition and a VIP program to get more content."
        scene d20s05-61-02 mc-mes-explaining-antagonist with dissolve
        play voice2 mc_thinking_mmm3 noloop
        mc "Although I'm not sure if that was an accident or part of Jerome's design."
        if is_antagonist_mode is False:
            mc "Of course, there isn't any $1kk prize. All of that was a lie."
    scene d20s05-62 mes-collpasing back to chair with dissolve
    play voice3 min_old_disgusted noloop
    mes "I need to sit down."
    scene d20s05-63 mc-talking with dissolve
    play voice2 mc_arrogant_hm2 noloop
    mc "Crazy, right?{w} I know it's a lot to take in, but-"
    scene d20s05-64 mes-collpasing back to chair with dissolve
    play voice3 min_no_simple noloop
    mes "No, no. It makes sense."
    scene d20s05-65 mc-talking with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "Really?"
    scene d20s05-68 mes-talking with dissolve
    play voice3 min_yes_active noloop
    mes "I should have realized...{w} but wait, why is she in jail?"
    scene d20s05-66 mc-talking with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    if cage_ntr is True:
        mc "Well, she abducted me... sorta."
        mc "Also, she kinda held Terrell & his girlfriend in her sex dungeon..."
        if is_antagonist_mode is False:
            mc "... although it seemed like they enjoyed that."
        scene d20s05-67 mc-mes-talking with dissolve
        play voice2 mc_thinking_mmm4 noloop
        mc "The cops caught her trying to abduct AmRose, but AmRose wasn't there, so..."
        if is_antagonist_mode is True:
            mc "Hmm.{w} I guess it's all the blackmail."
        elif True:
            mc "Hmm.{w} I guess it's fraud over the $1kk prize."
    elif True:
        mc "Well, she turned herself in to the police and confessed."
        if is_antagonist_mode is True:
            mc "She felt really bad about the coercion and blackmail."
        elif True:
            mc "She felt really bad about the fraud and fake $1kk prize."
    scene d20s05-69 mc-talking with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.5
    mc "Although, now that I think about it... I'm really not sure what she's been charged with..."
    mc "I imagine any halfway decent lawyer could get her out, but it's the weekend... they probably need to wait until Monday for her arraignment."
    scene d20s05-70 mes-talking with dissolve
    play voice3 min_angry_argh1 noloop
    mes "She gets a phone call. Why didn't she call me?"
    scene d20s05-73 mc-talking with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "It's only one call, right? Maybe she called her parents or a lawyer?"
    scene d20s05-71 mes-talking with dissolve
    play voice3 min_no_angry noloop
    mes "No, she could have called me.{w} There must be some reason she didn't."
    scene d20s05-85 mc-talking with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "Maybe she's feeling guilty because you got so involved in playing the app?"
    scene d20s05-79 mes-talking with dissolve
    play voice3 min_happy_mmm noloop
    mes "Probably..."
    if cage_ntr is True:
        mes "Why didn't she try to abduct me?"
        if is_antagonist_mode is True:
            scene d20s05-75 mes-talking with dissolve
            play voice3 min_disappointed_ehh3 noloop
            mes "She didn't even try to blackmail me."
            scene d20s05-73 mc-talking with dissolve
            play voice2 mc_yes_ugu1 noloop
            mc "I think she figured that blackmail wouldn't work on you."
        elif True:
            scene d20s05-73 mc-talking with dissolve
        play voice2 mc_thinking_hmm4 noloop
        mc "She did tell me that you weren't \"ripe\" yet. She didn't want to \"pluck\" you until you were completely her sex slave."
        scene d20s05-79 mes-talking with dissolve
        play voice3 min_arrogant_pff noloop
        mes "Wow."
    mes "That little slitch...{w} I can't believe I didn't see this coming."
    scene d20s05-70 mes-talking with dissolve
    play voice3 min_pain_sobs2 noloop
    mes "I've been so blind."

    jump d20s05_plans

label d20s05_plans:

    scene d20s05-74 mes-talking with Fade(0.5, 0.5, 0.5)
    mes "..."
    scene d20s05-73 mc-talking with dissolve
    mct "Lydia's betrayal must have really affected her."
    mct "She's been silent for way too long...{w} I need to say something to distract her."
    play voice2 mc_arrogant_hm3 noloop
    mc "So..."
    scene d20s05-82 mes-talking with dissolve
    play voice3 min_old_huh noloop
    mes "Huh?{w} Oh, what were you saying?"

    jump d20s05_from_end_menu

label d20s05_from_end_menu hide:

    if from_ending_menu is True:
        $ renpy.music.set_volume(0.2, 4.0, "music")
        play music music_melancholy_forever
    scene d20s05-81 mc-talking with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "I was just wondering...{w} Are you planning to work for your father this summer?"
    scene d20s05-83 mes-talking with dissolve
    play voice3 min_thinking_oh noloop
    mes "*sigh* Oh, that. Probably not."
    mes "Although I'll probably end up working with my brother after I graduate, I would like to do something else."
    mes "I wish I could do something more significant, but ya'know...{w} family."
    scene d20s05-78 mc-talking with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah. But not this summer?"
    scene d20s05-84 mes-talking with dissolve
    play voice3 min_no_nah noloop
    mes "Nah. I'm not sure what I'm going to do. Maybe just stay here."
    mes "Just enjoy a month or two with nothing to do."
    scene d20s05-80 mc-talking with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.6
    mc "You talked about high frequency trading. Is that still something you're interested in?"
    scene d20s05-75 mes-talking with dissolve
    play voice3 min_old_hmm noloop volume 1.2
    mes "I mean, it's the most reliable source of income these days. You can't trust anything else in the market - but you can game the market itself."
    scene d20s05-69 mc-talking with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Still. I imagine it takes millions of dollars to make a profit, and you need to be geographically close to the stock markets to maximize return."
    scene d20s05-68 mes-talking with dissolve
    play voice3 min_yes_aga noloop
    mes "Optimally, sure.{w} But there's plenty of money to be made anywhere in the world with a decent system."
    mes "It's really all about the math...{w} the algorithms."
    scene d20s05-66 mc-talking with dissolve
    play voice2 d1s5_mchappy noloop volume 1.5
    mc "So, while you're bumming here this summer you could create something like that?"
label ending_10_return hide:
    scene d20s05-75 mes-talking with dissolve
    play voice3 min_thinking_emm noloop
    mes "Maybe...{w} It's really just a fantasy."
    mes "Anyway, what about you? Any plans for this summer?"
    if from_ending_menu is True:
        jump d20s05_mes_end
    scene d20s05-80 mc-talking with dissolve
    $ unlock_ending("10")
    call update_ending_variables from _call_update_ending_variables_6
    menu:
        "Leave Town With Min"(hint="d20s05m02c01") if True:
            $ d20s05_mes_solo = True
            jump d20s05_mes_end
        "Talk About Your Summer Plans"(hint="d20s05m02c02") if True:

            jump d20s05_continue

label d20s05_mes_end hide:

    scene d20s05-60-02 mc-explaining-antagonist with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "Well, I was thinking about disrupting your plans."
    scene d20s05-64 mes-collpasing back to chair with dissolve
    play voice3 min_disappointed_ehh2 noloop
    mes "Oh?"
    scene d20s05-65 mc-talking with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "Why don't the two of us get the hell out of here. Like right now."
    scene d20s05-84 mes-talking with dissolve
    play voice3 min_arrogant_hm noloop
    mes "Sure, what do you have in mind?"
    scene d20s05-63 mc-talking with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "You. Me. The open road.{w} Just disappear for a couple months."
    scene d20s05-79 mes-talking with dissolve
    play voice3 min_disappointed_mph noloop
    mes "Just like that? Forget about everyone and everything?"
    scene d20s05-78 mc-talking with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Exactly. Just like that."
    scene d20s05-52 mc-mes-post fuck talk with dissolve
    play voice3 min_surprised_ehh1 noloop
    mes "Wait...{w} are you joking?"
    scene d20s05-57 mc-mes-post fuck talk with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "I've never been more serious in my life."
    scene d20s05-74 mes-talking with dissolve
    play voice3 min_thinking_hmm1 noloop
    mes "I don't understand."
    scene d20s05-73 mc-talking with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "All this Fetish Locator bullshit and Lydia and everything else that's happened the past few weeks?"
    mc "I just don't feel like going home, getting some summer job, living some pretend life."
    mc "Right now I've got one good thing in my life - and that's you."
    scene d20s05-75 mes-talking with dissolve
    play voice3 min_thinking_hmm2 noloop
    mes "We'll be together again in the Autumn-"
    scene d20s05-67 mc-mes-talking with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah, that's true.{w} Maybe."
    scene d20s05-82 mes-talking with dissolve
    play voice3 min_thinking_mhh noloop
    mes "What do you mean?"
    scene d20s05-85 mc-talking with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Look, I'm about 5 minutes from just jumping on a bus and getting the fuck out of here."
    mc "Except I don't want to lose you."
    scene d20s05-84 mes-talking with dissolve
    play voice3 min_scared_off noloop
    mes "Well, fuck me.{w} That's almost the most romantic thing I've ever heard."
    scene d20s05-81 mc-talking with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Yeah?"
    scene d20s05-62 mes-collpasing back to chair with dissolve
    play voice3 min_thinking_hmm3 noloop
    mes "You really want to go somewhere with me for the summer?"
    scene d20s05-65 mc-talking with dissolve
    play voice2 d9s2_mcyes noloop volume 2.3
    mc "Hell yes.{w} As long as we leave immediately."
    scene d20s05-83 mes-talking with dissolve
    play voice3 min_happy_yay noloop
    mes "Alright. I'll call the airport.{w} Have you ever flown a private charter?"
    scene d20s05-65 mc-talking with dissolve
    play voice2 mc_no_no2 noloop
    mc "No... I've never had the opportunity."
    scene d20s05-56 mes-post fuck talk with dissolve
    play voice3 min_old_laugh noloop
    mes "Let's see what he can arrange.{w} Where do you want to go?"
    scene d20s05-66 mc-talking with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "Anywhere that isn't here."
    scene d20s05-55 mc-mes-post fuck talk with dissolve
    play voice3 min_hey_simple noloop
    mes "Your choice. Anywhere in the world."
    scene d20s05-73 mc-talking with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "Where did she say her family was? Japan? South Korea? Something like that."
    mc "Well...{w} I've never been to South Korea."
    scene d20s05-84 mes-talking with dissolve
    play voice3 min_arrogant_huh2 noloop
    mes "Really?"
    scene d20s05-78 mc-talking with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "I mean, I really don't know much about South Korea except that they have fast internet and a lot of people with video game addictions."
    scene d20s05-75 mes-talking with dissolve
    play voice3 min_arrogant_heh2 noloop
    mes "There's a little more than that. I can show you around."
    scene d20s05-85 mc-talking with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "I'd like that."
    stop sound2 fadeout 3.0

    jump ending_10

label d20s05_continue hide:

    scene d20s05-60-02 mc-explaining-antagonist with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "My own plans are...{w} different now."
    scene d20s05-64 mes-collpasing back to chair with dissolve
    play voice3 min_disappointed_ehh2 noloop
    mes "Oh? How so?"
    scene d20s05-65 mc-talking with dissolve
    play voice2 mc_disappointed_ehh2 noloop
    mc "I don't know. After this week...{w} after these weeks...{w} I don't know."
    scene d20s05-84 mes-talking with dissolve
    play voice3 min_arrogant_hm noloop
    mes "What do you mean?"
    scene d20s05-63 mc-talking with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Have you ever experienced one of those life altering experiences - where everything you planned suddenly got turned on it's head?"
    scene d20s05-79 mes-talking with dissolve
    play voice3 min_disappointed_mph noloop
    mes "You mean like when Antony broke up with me?"
    play voice2 mc_yes_yeah3 noloop
    scene d20s05-78 mc-talking with dissolve
    mc "Maybe.{w} Three weeks ago I was going along with the plan."
    mc "My life was straightforward and boring."
    mc "I'd find another girlfriend. Maybe she'd be the one. I'd spend the rest of my life with her."
    scene d20s05-85 mc-talking with dissolve
    play voice2 d3s11b_mcheh noloop
    mc "I'd finish my degree. Get a job at some multinational multibillion-dollar corporation."
    mc "Run my way up the ranks, then either build my own company or jump ship to a start-up."
    mc "Turn that start-up into an established corporation..."
    scene d20s05-65 mc-talking with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "Then probably get kicked out by the stockholders for someone else. Then start another corporation."
    mc "Later, rinse, repeat.{w} Have a nice McMansion and a few million in my bank account."
    scene d20s05-66 mc-talking with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "Wait for my wife to divorce me and take the kids. Then remarry someone half my age."
    mc "So on and so on and scooby-dooby-doo."
    scene d20s05-84 mes-talking with dissolve
    play voice3 min_disgust_off noloop
    mes "Doesn't sound like a great plan, but could be worse."
    scene d20s05-69 mc-talking with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yeah. That's not my path anymore. The past three weeks changed that."
    mc "Fetish Locator changed that."
    scene d20s05-75 mes-talking with dissolve
    play voice3 min_happy_relief noloop
    mes "So, what do you want to do?"
    scene d20s05-73 mc-talking with dissolve
    play voice2 mc_arrogant_hm2 noloop
    mc "I'm not sure.{w} But I'll tell you what I won't do. I'm not going back to my Mom's house and getting some ordinary summer job."
    scene d20s05-84 mes-talking with dissolve
    play voice3 min_thinking_hmm2 noloop
    mes "Something different..."
    scene d20s05-60-02 mc-explaining-antagonist with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yep. I feel like I'm finding myself and carving out a new path."
    scene d20s05-64 mes-collpasing back to chair with dissolve
    play voice3 min_surprised_ehh1 noloop
    mes "I...{w} I like the sound of that."
    scene d20s05-69 mc-talking with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Yeah?"
    scene d20s05-55 mc-mes-post fuck talk with dissolve
    play voice3 min_yes_yeah2 noloop
    mes "Yeah.{w} Let me know how I can help."
    scene d20s05-57 mc-mes-post fuck talk with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Will do."
    $ renpy.music.set_volume(0.5, 3.0, "music")
    stop sound2 fadeout 3.0

    jump d20s05_end

label d20s05_end:

    jump d20s06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
