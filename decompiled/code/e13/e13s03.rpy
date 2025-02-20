image e13_music_clip = Movie(play = "images/E-13/s99/e13e03-a05-03-2x-30fps_2.webm", loop = False, start_image = "e13s03-a05-03 mc-j-nk-bar-transition-anim-05-03-00_i", image = "e13s03-11 mc-n-hospital-wait5_c2")

label e13s03:

    scene black
    show screen scene_transistion(_("A month later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.1, 0.0, "sound2")
    play sound2 sfx_seawaves_ambience1 fadein 1.5
    play sound sfx_cleaning_floor2 loop volume 0.8
    scene e13s03-01 mc-j-nk-bar-entry1_c1
    with Fade(0.5, 0.5, 0.9)
    pause
    scene e13s03-01 mc-j-nk-bar-entry1_c2 with dissolve
    pause
    scene e13s03-01 mc-j-nk-bar-entry1_c3 with dissolve
    pause
    stop sound fadeout 0.7
    play voice3 nora_huh noloop
    scene e13s03-01-4 mc-j-nk-bar-entry4_c2_i with dissolve
    pause
    scene e13s03-01-4 mc-j-nk-bar-entry4_c3_i with dissolve
    $ renpy.music.set_volume(0.7, 1.0, "music")
    play music music_short_panic
    pause
    scene e13s03-01-5 mc-j-nk-bar-entry5_c2_i with dissolve
    nk "[mcname], I think my water broke."
    scene e13s03-01-2 mc-j-nk-bar-entry2_c3 with dissolve
    play voice2 mc_surprised_huh4 noloop
    mc "Shit."
    mc "What is the time?"
    scene e13s03-01-3 mc-j-nk-bar-time_c3 with dissolve
    play voice4 terrell_hmm3 noloop
    "Jim" "It's 12:49."
    scene e13s03-03 mc-j-nk-bar-talk1_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Okay, come on. We need to get to the hospital. Do you feel any con—"
    play voice3 nora_auh noloop
    scene e13s03-03 mc-j-nk-bar-talk1_c2 with dissolve
    pause
    scene e13s03-03 mc-j-nk-bar-talk1_c3 with dissolve
    play voice3 nora_yes noloop
    nk "{i}Yep{/i}. She's coming."
    scene e13s03-04 mc-j-nk-bar-talk2_c3 with dissolve
    play voice2 mc_scared_oh1 noloop
    mc "Alright, let's go."
    scene e13s03-05 mc-j-nk-bar-exit_c3 with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "Jim, close down the cafe and look after it while we're gone. I'll give you a call when I get to the hospital."
    scene e13s03-05 mc-j-nk-bar-exit_c1 with dissolve
    play voice4 terrell_aga2 noloop
    "Jim" "Aye, aye, Captain. Good luck, Nora!"
    scene e13s03-05 mc-j-nk-bar-exit_c2 with dissolve
    play voice3 nora_oh noloop
    nk "Thanks."
    scene e13s03-a05-03 mc-j-nk-bar-transition-anim-05-03-00_i with dissolve
    pause
    if not renpy.seen_image("e13s03-07 mc-n-hospital-wait1_c1"):
        $ _skipping = False
    $ quick_menu = False
    stop music fadeout 1.5
    stop sound2 fadeout 1.5
    play sound sfx_camera_fly1
    scene e13_music_clip
    show screen cutscene_skip("e13s03_after_clip")
    $ renpy.pause(65.0, hard=True)

label e13s03_after_clip:

    $ persistent.seen_lc_song_p1 = True
    $ _skipping = True
    $ quick_menu = True
    hide screen cutscene_skip
    scene e13s03-07 mc-n-hospital-wait1_c1 with dissolve
    $ renpy.music.set_volume(0.2, 0.0, "sound2")
    play sound2 classroom fadein 1.5
    pause
    scene e13s03-12 mc-n-d-hospital-doctor1_c1 with dissolve
    play voice4 lissa_thinking noloop
    "Doctor" "Mr. Young? [mcname] Young?"
    scene e13s03-12 mc-n-d-hospital-doctor1_c2 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yes?"
    scene e13s03-13 mc-nk-d-baby1_c2 with dissolve
    play voice4 lissa_ugu noloop
    "Doctor" "Congratulations, you have one healthy baby boy!"
    stop sound2 fadeout 1.3
    play music light_casual_piano fadein 1.5
    scene e13s03-14 mc-nk-d-baby2_c1 with Dissolve(0.7)
    pause
    play voice2 mc_scared_huuuh1 noloop
    scene e13s03-14 mc-nk-d-baby2_c2 with dissolve
    pause
    scene e13s03-15 mc-nk-d-baby3_c1 with dissolve
    pause
    play sound sfx_baby_moan1
    scene e13s03-16 mc-nk-d-baby4_c1 with dissolve
    pause
    play voice2 mc_happy_a1 noloop
    scene e13s03-16 mc-nk-d-baby4_c2 with dissolve
    pause
    play sound maria_kiss1
    scene e13s03-17 mc-nk-d-end_c1 with dissolve
    play voice3 nora_pleasure noloop
    pause
    play sound maria_kiss2
    scene e13s03-17 mc-nk-d-end_c2 with dissolve
    pause
    $ renpy.music.set_volume(1.0, 1.0, "sound2")
    stop music fadeout 4.0

    jump e13s04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
