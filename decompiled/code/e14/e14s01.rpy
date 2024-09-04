label e14_menu_jump:

    stop music fadeout 2.0
    call start_ending_from_menu from _call_start_ending_from_menu_5
    $ mcname = persistent.mcname
    $ mclogin = persistent.mclogin
    $ stop_all_sound()
    call hide_fl_points_overlay from _call_hide_fl_points_overlay_18
    $ d20s07_go_with_pn = True
    $ d15s05b_pegged = persistent.nk_pegged

    jump d20s07_end

label e14s01:

    call hide_fl_points_overlay from _call_hide_fl_points_overlay_19
    scene black
    show screen scene_transistion(_("Ending #14\nPolly & Nora"))
    with Fade(0.9, 0.9, 0.9)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(1.0, 1.0, "music")
    play music deep_blue fadein 2.2
    scene e13s01-31 construction_c5
    with Fade(0.9, 0.9, 0.9)
    pause 4.0
    scene e13s01-01 mc-pw-nk-construction_c1 with Fade(0.9,0.2,0.9)
    pause 4.0
    scene e13s01-02 mc-pw-nk-construction_c2 with Fade(0.9,0.2,0.9)
    pause 4.0
    scene e13s01-03 mc-pw-nk-construction_c5 with Fade(0.9,0.2,0.9)
    pause 3.0
    scene e13s01-04 mc-pw-nk-construction-start_c4 with Fade(0.8,0.1,0.6)
    pause 2.0
    scene e13s01-05 mc-pw-nk-construction-start-ladder_c5 with dissolve
    pause 2.0
    scene e13s01-06 mc-pw-nk-construction_c6 with dissolve
    pause 2.0
    scene e13s01-07 mc-pw-nk-construction-roof-ladder_c5 with dissolve
    pause 2.0
    scene e13s01-08 pw-nk-construction_c8 with dissolve
    pause 2.0
    scene e13s01-09 mc-construction-roof_c9 with dissolve
    pause 2.0
    scene e13s01-10 mc-pw-nk-construction_c17 with dissolve
    pause 2.0
    scene e13s01-11 mc-pw-nk-construction_c4 with dissolve
    pause 1.0
    scene e13s01-12 mc-pw-nk-construction_c6 with dissolve
    pause 1.0
    scene e13s01-13 mc-pw-nk-construction_c7 with dissolve
    pause 1.0
    scene e13s01-14 mc-pw-nk-construction_c11 with dissolve
    pause 1.0
    scene e13s01-15 mc-construction-roof_c16 with dissolve
    pause 1.5
    scene e13s01-16 pw-nk-construction_c9 with dissolve
    pause 1.5
    scene e13s01-17 mc-pw-nk-construction-rest_c10 with dissolve
    pause 1.5
    scene e13s01-18 mc-pw-nk-construction_c6 with dissolve
    pause 2.0
    scene e13s01-19 pw-construction-window_c2 with dissolve
    pause 2.0
    scene e13s01-20 nk-construction-umbrella_c3 with dissolve
    pause 2.0
    scene e13s01-21 mc-pw-nk-construction_c8 with dissolve
    pause 2.0
    scene e13s01-22 mc-pw-nk-construction_c10 with dissolve
    pause 2.0
    scene e13s01-23 pw-construction-window_c9 with dissolve
    pause 2.0
    scene e13s01-24 nk-construction-chair_c20 with dissolve
    pause 2.0
    scene e13s01-25 mc-pw-nk-construction-rest_c21 with dissolve
    pause 2.0
    scene e13s01-26 nk-construction-window_c22 with dissolve
    pause 2.0
    scene e13s01-27 nk-construction-window_c23 with dissolve
    pause 2.0
    scene e13s01-28 mc-pw-nk-construction-window_c24 with dissolve
    pause 3.5
    scene e13s01-29 mc-pw-nk-construction-completion_c10 with dissolve
    pause 3.5
    scene e13s01-30 mc-pw-nk-construction-completion_c10 with dissolve
    pause 3.5
    scene e13s01-53 construction_c5 with Fade(0.8,0.1,0.6)
    pause 5.0
    stop music fadeout 3.0

    jump e14s02

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
