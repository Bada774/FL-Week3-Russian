label d21s99:

    $ persistent.reached_e99 = True

    $ renpy.music.set_volume(1.0, 3.0, "sound2" )
    $ renpy.music.set_volume(1.0, 3.0, "sound3" )
    play sound3 sfx_weather_rainfall1 fadein 10.0
    call end_game_text (_("Not reaching an ending is also an ending...")) from _call_end_game_text_6
    call end_game_text (_("Just not a good one")) from _call_end_game_text_7

    $ renpy.music.set_volume(0.9, 3.0, "music" )
    play sound2 sfx_thunder_1 noloop
    play music music_bad_is_bad fadein 10.0
    with Fade(0.8, 1.0, 0.8)
    scene d21s99-01 mc-sitting with dissolve
    pause
    scene d21s99-02 mc-sitting with dissolve
    pause
    scene d21s99-03 mc-car-incoming with dissolve
    pause
    play sound sfx_motobike_stop
    play sound2 sfx_water_out1 volume 5.0 noloop
    scene d21s99-04 mc-car-incoming with dissolve
    pause
    play voice2 mc_pain_argh1 noloop
    scene d21s99-05 mc-splashed-with-mud with dissolve
    pause
    play voice2 d9s5_auch2 noloop
    scene d21s99-07 mc-getting-mad-at-the-car with dissolve
    pause
    play voice2 mc_pain_mff4 noloop
    scene d21s99-07-02 mc-sad-again with dissolve
    $ fl_achievement_unlock("d21s99n01")
    $ unlock_gallery_slot("extra", "d21s99n01")
    pause

    stop sound fadeout 3.0
    stop sound2 fadeout 3.0
    stop sound3 fadeout 3.0
    stop music fadeout 4.0
    jump end

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
