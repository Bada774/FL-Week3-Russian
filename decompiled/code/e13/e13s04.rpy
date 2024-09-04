image e13s04-a13-1-f = Movie(play = "images/E-13/s04/anim/e13s04-a13-1-2x-50fps_vp9.webm", start_image = "e13s04-a13-1 mc-nk-kiss-fingering-anim1-01_i")
image e13s04-a13-1 = Movie(play = "images/E-13/s04/anim/e13s04-a13-1-4x-60fps_vp9.webm", start_image = "e13s04-a13-1 mc-nk-kiss-fingering-anim1-01_i")
image e13s04-a13-2-f = Movie(play = "images/E-13/s04/anim/e13s04-a13-2-2x-50fps_vp9.webm", start_image = "e13s04-a13-2 mc-nk-kiss-fingering-anim2-01_i")
image e13s04-a13-2 = Movie(play = "images/E-13/s04/anim/e13s04-a13-2-4x-60fps_vp9.webm", start_image = "e13s04-a13-2 mc-nk-kiss-fingering-anim2-01_i")

image e13s04-a14-1-f = Movie(play = "images/E-13/s04/anim/e13s04-a14-1-2x-50fps_vp9.webm", start_image = "e13s04-a14-1 mc-nk-rimming-anim1-01_i")
image e13s04-a14-1 = Movie(play = "images/E-13/s04/anim/e13s04-a14-1-4x-60fps_vp9.webm", start_image = "e13s04-a14-1 mc-nk-rimming-anim1-01_i")
image e13s04-a14-2-f = Movie(play = "images/E-13/s04/anim/e13s04-a14-2-2x-50fps.webm", start_image = "e13s04-a14-2 mc-nk-rimming-anim2-01_i")
image e13s04-a14-3-f = Movie(play = "images/E-13/s04/anim/e13s04-a14-3-2x-50fps.webm", start_image = "e13s04-a14-3 mc-nk-rimming-anim3-01_i")

image e13s04-a15-1-f = Movie(play = "images/E-13/s04/anim/e13s04-a15-1-2x-50fps.webm", start_image = "e13s04-a15-1 mc-nk-rimming-fingering-anim1-01_i")
image e13s04-a15-2-f = Movie(play = "images/E-13/s04/anim/e13s04-a15-2-2x-50fps.webm", start_image = "e13s04-a15-2 mc-nk-rimming-fingering-anim2-01_i")
image e13s04-a15-3-f = Movie(play = "images/E-13/s04/anim/e13s04-a15-3-2x-50fps.webm", start_image = "e13s04-a15-3 mc-nk-rimming-fingering-anim3-01_i")

image e13s04-a21-1 = Movie(play = "images/E-13/s04/anim/e13s04-a21-1-2x-50fps.webm", start_image = "e13s04-a21-1 mc-nk-sex2-anim1-01")
image e13s04-a21-1-f = Movie(play = "images/E-13/s04/anim/e13s04-a21-1-2x-60fps.webm", start_image = "e13s04-a21-1 mc-nk-sex2-anim1-01")
image e13s04-a21-2 = Movie(play = "images/E-13/s04/anim/e13s04-a21-2-2x-50fps.webm", start_image = "e13s04-a21-2 mc-nk-sex2-anim2-01_i")
image e13s04-a21-2-f = Movie(play = "images/E-13/s04/anim/e13s04-a21-2-2x-60fps.webm", start_image = "e13s04-a21-2 mc-nk-sex2-anim2-01_i")
image e13s04-a21-3 = Movie(play = "images/E-13/s04/anim/e13s04-a21-3-2x-50fps.webm", start_image = "e13s04-a21-3 mc-nk-sex2-anim3-01_i")
image e13s04-a21-3-f = Movie(play = "images/E-13/s04/anim/e13s04-a21-3-2x-60fps.webm", start_image = "e13s04-a21-3 mc-nk-sex2-anim3-01_i")

image e13s04-a22-1 = Movie(play = "images/E-13/s04/anim/e13s04-a22-1-2x-50fps.webm", start_image = "e13s04-a22-1 mc-nk-sex3-anim1-01_i")
image e13s04-a22-1-f = Movie(play = "images/E-13/s04/anim/e13s04-a22-1-2x-60fps.webm", start_image = "e13s04-a22-1 mc-nk-sex3-anim1-01_i")
image e13s04-a22-2 = Movie(play = "images/E-13/s04/anim/e13s04-a22-2-2x-50fps.webm", start_image = "e13s04-a22-2 mc-nk-sex3-anim2-01_i")
image e13s04-a22-2-f = Movie(play = "images/E-13/s04/anim/e13s04-a22-2-2x-60fps.webm", start_image = "e13s04-a22-2 mc-nk-sex3-anim2-01_i")
image e13s04-a22-3 = Movie(play = "images/E-13/s04/anim/e13s04-a22-3-2x-50fps.webm", start_image = "e13s04-a22-3 mc-nk-sex3-anim3-01_i")
image e13s04-a22-3-f = Movie(play = "images/E-13/s04/anim/e13s04-a22-3-2x-60fps.webm", start_image = "e13s04-a22-3 mc-nk-sex3-anim3-01_i")

label e13s04:

    scene black
    show screen scene_transistion(_("One year later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene e13s04-01 mc-baby1_c1
    with Fade(0.5, 0.5, 0.9)
    $ renpy.music.set_volume(0.6, 0.0, "music2")
    play music2 music_e13_sunny_future_intro
    queue music2 music_e13_sunny_future
    pause
    play sound sfx_door_slide4
    scene e13s04-02 mc-baby2_c1 with dissolve
    pause
    scene e13s04-03 mc-baby3_c1 with dissolve
    play voice2 d2s9_mchey noloop
    mc "You gave your mother a lot of trouble today, didn't you?"
    scene e13s04-03 mc-baby3_c2 with dissolve
    pause
    scene e13s04-04 mc-baby4_c1 with dissolve
    play voice3 aaleyah_disappointed_mff2 noloop
    nk "Did he finally settle down?"
    scene e13s04-04 mc-baby4_c2 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Mm. He is an {i}extremely{/i} opinionated young gentleman."
    mc "Told me all about how unfairly you were treating him."
    scene e13s04-04 mc-baby4_c1 with dissolve
    play voice3 nora_heh noloop
    nk "*Laughs* Unfairly!? Well, I never!"
    play sound sfx_door_slide2
    scene e13s04-05 mc-exit1_c1 with dissolve
    pause

label replay_e13s04:

    if _in_replay:
        $ renpy.music.set_volume(0.6, 1.0, "music")
        play music music_e13_sunny_future

    scene e13s04-06 mc-bar1_c2 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Did you close up shop already?"
    scene e13s04-06 mc-bar1_c1 with dissolve
    play voice3 aaleyah_yes_yep noloop
    nk "Yep. Thought we could share a drink and relax tonight."
    scene e13s04-06 mc-bar1_c2 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "I like the sound of that."
    scene e13s04-07 mc-bar2_c1 with dissolve
    play voice3 aaleyah_thinking_hmm2 noloop
    nk "What are you—"
    play sound sfx_coffee_pouring
    scene e13s04-08 mc-blindfold_c1 with dissolve
    play voice2 shhh noloop
    mc "Shh, keep looking forward and keep your hands flat on the counter."
    scene e13s04-08 mc-blindfold_c2 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "You didn't think I forgot what today was, did you?"
    play sound sfx_cloth_rustling3
    scene e13s04-09 mc-blindfold2_c1 with dissolve
    play voice3 nora_auh noloop
    nk "Well, I wasn't {i}completely{/i} sure."
    scene e13s04-09 mc-blindfold2_c2 with dissolve
    play voice2 d4s4_mclaugh noloop volume 1.5
    mc "*Chuckles* You really need to give me more credit."
    scene e13s04-10 mc-nk-talk3_c2 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Happy Anniversary, Nora."
    play sound maria_kiss2
    scene e13s04-11 mc-nk-kiss_c1 with dissolve
    pause
    scene e13s04-10 mc-nk-talk3_c1 with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "Now scoot back a bit and spread your legs for me."

    $ Lovense.stop()

    scene e13s04-12 mc-nk-fingering_c1 with dissolve
    play voice3 nora_pleasure noloop
    nk "*Soft moans* This really brings back memories."
    scene e13s04-12 mc-nk-fingering_c2 with dissolve
    play voice3 aaleyah_happy_laugh2 noloop
    nk "The final not-so-blind date *Soft laugh*."
    play voice2 mc_arrogant_hm1 noloop
    mc "Well, it's a long ways away from being final anything if I have a say in it."
    scene e13s04-11 mc-nk-kiss_c2 with dissolve
    play voice3 nora_moan1 noloop
    nk "Kiss me."
    play sound maria_kiss1
    $ Lovense.vibrate(1)
    scene e13s04-13 mc-nk-kiss-fingering_c1 with dissolve
    pause
    scene e13s04-a13-1 mc-nk-kiss-fingering-anim1-01_i with dissolve
    play voice3 nora_mmm noloop
    queue voice3 nora_sucks_mouth
    $ Lovense.vibrate(2)
    scene e13s04-a13-1
    nk "*Muffled moans* Just like that. Please keep going."
    pause
    scene e13s04-a13-2 with dissolve
    pause
    $ Lovense.vibrate(3)
    scene e13s04-a13-1-f with dissolve
    pause
    scene e13s04-a13-2-f with dissolve
    pause
    nk "Mmm, I love the way your fingers feel inside of me."
    scene e13s04-a14-1 with dissolve
    play voice3 nora_orgasm3 noloop
    queue voice3 nora_moans1
    play voice2 [d2s12_flicking, d2s12_licking]
    $ Lovense.vibrate(4)
    pause
    scene e13s04-a14-2-f with dissolve
    pause
    scene e13s04-a14-3-f with dissolve
    pause
    scene e13s04-a14-1-f with dissolve
    pause
    stop voice2 fadeout 1.0
    scene e13s04-a15-1 mc-nk-rimming-fingering-anim1-01_i with dissolve
    play voice3 nora_huh noloop
    nk "Hm? [mcname]? Why did—"
    play voice2 [d2s12_flicking, d2s12_licking]
    scene e13s04-a15-1-f
    play voice3 nora_orgasm1 noloop
    queue voice3 "<silence 0.6>" noloop
    queue voice3 aaleyah_open_moans1
    $ Lovense.vibrate(5)
    nk "Oh! Oh God. Fuck. *Moans*"
    scene e13s04-a15-2-f with dissolve
    pause
    scene e13s04-a15-3-f with dissolve
    pause
    play voice3 nora_yes noloop
    nk "Yes! Fuck, God yes. That feels {i}so{/i} good."
    scene e13s04-16 mc-nk-cum_c1 with dissolve
    play voice3 aaleyah_open_moans2
    nk "Oh my God! Fuck! *Loader and loader moans*"
    nk "Yes, yes! I'm close! [mcname], I'm gonna—!"
    play voice3 aaleyah_orgasm_shortmoan1 noloop
    play voice2 mc_scared_huuuh3 noloop
    $ Lovense.vibrate(6)
    scene e13s04-16 mc-nk-cum2_c2 with hpunch
    pause
    $ Lovense.vibrate(2)
    scene e13s04-16 mc-nk-cum_c1 with dissolve
    play voice3 aaleyah_closed_moan4 noloop
    nk "God... That was amazing…"
    play sound maria_kiss1
    scene e13s04-17 mc-nk-kiss2_c1 with dissolve
    pause
    play sound maria_kiss2
    scene e13s04-17 mc-nk-kiss2_c2 with dissolve
    pause
    play sound sfx_bandage_off1
    scene e13s04-18 mc-nk-exit-store_c1 with dissolve
    play voice2 mc_scared_huh1 noloop
    mc "Where are we going?"
    play voice3 aaleyah_closed_moan3 noloop
    nk "I want you to fuck me outside."
    scene e13s04-18 mc-nk-exit-store_c2 with dissolve
    pause
    $ renpy.music.set_volume(1.0, 0.0, "sound3")
    play sound3 sfx_seawaves_ambience1 fadein 1.0
    play sound2 "<silence 1.0>" noloop
    queue sound2 sfx_barefoot_run1 volume 0.3
    play sound sfx_barefoot_run1 loop fadein 1.0
    scene e13s04-19 mc-nk-exit-store2_c1 with dissolve
    play voice3 aaleyah_angry_grrr1 noloop
    nk "Fuck me. Fuck me as hard as you can. I don't care who sees or hears."
    scene e13s04-19 mc-nk-exit-store2_c2 with dissolve
    pause
    play sound2 sfx_sand_run1 fadein 1.0
    play voice3 aaleyah_happy_laugh1 noloop
    scene e13s04-20 mc-nk-exit-store3_c2 with dissolve
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    play voice2 d7s4_mcbreathing
    play voice3 aaleyah_open_moans1
    $ Lovense.pattern("7;12", 1700)
    scene e13s04-a21-1 with dissolve
    nk "*Loud moans* Yes, fuck… Yes! I love you, [mcname]."
    scene e13s04-a21-2 with dissolve
    pause
    scene e13s04-a21-3 with dissolve
    pause
    $ Lovense.pattern("7;12", 900)
    scene e13s04-a21-1-f with dissolve
    pause
    scene e13s04-a21-2-f with dissolve
    nk "Give me another baby! Make me pregnant again!"
    pause
    scene e13s04-a21-3-f with dissolve
    pause
    play voice3 aaleyah_open_moans2
    $ Lovense.pattern("7;12", 1700)
    scene e13s04-a22-1 with dissolve
    pause
    scene e13s04-a22-2 with dissolve
    pause
    scene e13s04-a22-3 with dissolve
    pause
    nk "*Staggered moans* I—I'm gonna cum. Cum with me, [mcname]."
    $ Lovense.pattern("7;12", 900)
    scene e13s04-a22-1-f with dissolve
    pause
    scene e13s04-a22-2-f with dissolve
    pause
    scene e13s04-a22-3-f with dissolve
    pause
    play voice2 d1s5_orgasm2 noloop
    play voice3 aaleyah_orgasm_shortmoan1 noloop
    $ Lovense.stop()
    $ Lovense.vibrate(19)
    scene e13s04-23 mc-nk-cum_c1 with hpunch
    pause
    stop voice3 fadeout 0.5
    play sound maria_kiss1
    scene e13s04-24 mc-nk-kiss_c2 with dissolve
    $ Lovense.vibrate(2)
    pause
    scene e13s04-25 mc-nk-beach_c1 with dissolve
    play voice3 aaleyah_closed_moan1 noloop
    nk "*Breathy laugh* Think that might've done it."
    nk "You wanna go again?"
    scene e13s04-25 mc-nk-beach_c2 with dissolve
    play voice2 mc_scared_oh1 noloop
    mc "You're fucking insatiable."
    mc "I love you."

    $ Lovense.stop()

    $ renpy.music.set_volume(1.0, 3.0, "music2")
    play sound sfx_sea_guls_1
    $ renpy.end_replay()

    play sound2 ["<silence 2.0>", sfx_acoustic_guitar1] noloop volume 0.55
    scene ending_13_art_2 with Fade(1.25, 1.0, 1.75, color="#fff")
    pause
    call end_game_text (_("You have finished playing ending number 13!")) from _call_end_game_text_1
    $ persistent.finished_e13 = True
    $ fl_achievement_unlock("e13_finish")
    $ unlock_gallery_slot("scene", "e13s04")
    stop sound fadeout 3.0
    stop sound3 fadeout 3.0
    stop sound2 fadeout 1.0
    stop music2 fadeout 3.0

    jump end

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
