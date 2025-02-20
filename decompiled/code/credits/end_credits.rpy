default persistent.seen_credits = False
default dlc_2_postcredits = False



label end_credits:

    call hide_fl_points_overlay from _call_hide_fl_points_overlay_2
    $ _skipping = False
    $ renpy.checkpoint()
    $ renpy.free_memory()


    scene black with dissolve
    $ renpy.music.set_volume(1.0, delay=1, channel='music')
    play music audio.game_titles3
    $ renpy.pause(0.8)
    show team-logo with dissolve
    $ renpy.pause(3.0)
    scene black with dissolve
    show thank_you:
        xalign 0.5 yalign 0.35 alpha 0.0
        linear 1.0 alpha 1.0
    show week_three:
        xalign 0.5 yalign 0.55 alpha 0.0
        pause 2.0
        linear 1.0 alpha 1.0
    $ renpy.pause(5.0)
    scene black with dissolve
    $ renpy.pause(0.8)
    show freelanceTranslatorIntroduce:
        xalign 0.5 yalign 0.35 alpha 0.0
        linear 1.0 alpha 1.0
    show freelanceTranslatorSteam:
        xalign 0.5 yalign 0.55 alpha 0.0
        linear 1.0 alpha 1.0
    $ renpy.pause(7.0)
    scene black with dissolve



    scene credit_anim_bg
    show screen credits_roll()
    with dissolve
    $ renpy.pause(66.5, hard=True)

    hide screen credits_roll
    $ persistent.seen_credits = True

    jump end_credits_end

label end_credits_end:
    $ _skipping = True
    jump after_credits
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
