label e13_menu_jump:

    stop music fadeout 2.0
    call start_ending_from_menu from _call_start_ending_from_menu_3
    $ cockcage_released = True
    $ mcname = persistent.mcname
    $ mclogin = persistent.mclogin
    $ fl_watersports = persistent.fl_watersports
    $ stop_all_sound()
    call hide_fl_points_overlay from _call_hide_fl_points_overlay_11

    jump d16s09_nk_end

label e13s01:

    call hide_fl_points_overlay from _call_hide_fl_points_overlay_3
    scene black
    show screen scene_transistion(_("Ending #13\nPregnant Nora"))
    with Fade(0.9, 0.9, 0.9)
    pause
    hide screen scene_transistion
    play music deep_blue fadein 2.2
    scene e13s01-31 construction_c5
    with Fade(0.9, 0.9, 0.9)
    pause 4.0
    scene e13s01-32 mc-nk-construction_c1 with Fade(0.9,0.2,0.9)
    pause 4.0
    scene e13s01-33 mc-nk-construction_c2 with Fade(0.9,0.2,0.9)
    pause 4.0
    scene e13s01-34 mc-nk-construction_c5 with Fade(0.9,0.2,0.9)
    pause 3.0
    scene e13s01-35 mc-nk-construction-start_c4 with Fade(0.8,0.1,0.6)
    pause 2.0
    scene e13s01-36 mc-nk-construction-start-ladder_c5 with dissolve
    pause 2.0
    scene e13s01-37 mc-nk-construction_c6 with dissolve
    pause 2.0
    scene e13s01-38 mc-nk-construction_c8 with dissolve
    pause 2.0
    scene e13s01-39 mc-construction-roof_c9 with dissolve
    pause 2.0
    scene e13s01-40 mc-nk-construction_c17 with dissolve
    pause 2.0
    scene e13s01-41 mc-nk-construction_c4 with dissolve
    pause 2.0
    scene e13s01-42 mc-nk-construction_c6 with dissolve
    pause 1.5
    scene e13s01-43 mc-nk-construction_c7 with dissolve
    pause 1.5
    scene e13s01-44 mc-nk-construction_c11 with dissolve
    pause 2.0
    scene e13s01-45 mc-construction-roof_c16 with dissolve
    pause 2.0
    scene e13s01-46 mc-nk-construction-rest_c10 with dissolve
    pause 2.0
    scene e13s01-47 mc-nk-construction_c6 with dissolve
    pause 2.0
    scene e13s01-48 mc-nk-construction_c10 with dissolve
    pause 2.0
    scene e13s01-49 mc-nk-construction-chair_c20 with dissolve
    pause 2.0
    scene e13s01-50 mc-nk-construction-window_c22 with dissolve
    pause 2.0
    scene e13s01-51 mc-nk-construction-window_c22 with dissolve
    pause 3.5
    scene e13s01-52 mc-nk-construction-completion_c10 with dissolve
    pause 3.5
    scene e13s01-53 construction_c5 with Fade(0.8,0.1,0.6)
    pause 5.0
    $ unlock_gallery_slot("cg", "e13s01")

    jump e13s02

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
