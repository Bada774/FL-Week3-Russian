default persistent.d17s06_dd = False
default persistent.d17s06_dw = False
default persistent.d17s06_pn = False

label d17s06:

    $ d17s06_dd_preg = False
    $ d17s06_pn_thruple = False
    $ d17s06_teddy_name = ""
    $ d17s06_points = 0
    $ d17s06_choice_study = False
    $ d17s06_choice_dd = False
    $ d17s06_choice_dw = False
    $ d17s06_choice_pn = False

    scene black
    show screen scene_transistion(_("Back at the dorm"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene d17s06-01 mc-coming_c1
    with Fade(0.5, 0.5, 0.9)
    play voice2 d1s5b_ehhh noloop volume 1.5
    mc "Alright - time to get some studying done."
    if persistent.d17s05_mh is True and persistent.d17s05_mh_sy is True and persistent.d17s05_mh_op is True:
        $ fl_achievement_unlock("d17s05n01")
        $ unlock_gallery_slot("extra", "d17s05n01")

    if date_dd is False and date_dw is False and date_pw is False:
        jump d17s06_study

    scene d17s06-10 mc-phone-sit-study_c1 with Fade(0.5, 1.5, 0.5)
    play music thinking_music_4 volume 1.6
    $ renpy.music.set_volume(1.0, 4.0, "music")
    play voice2 mc_thinking_hmm1 noloop
    mct "Alright, time for a break."
    scene d17s06-03 mc-phone-sit_c1 with dissolve
    mct "Let's check my phone... oh, I got a few messages."
    mct "Blah blah blah, I need a better spam filter."
    scene d17s06-04 mc-phone-sit-curious_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mct "Oh, this looks interesting."
    scene d17s06-04 mc-phone-sit-curious_c2 with dissolve
    if date_dw is True:
        mct "Dahlia is at the amusement park and expects me to meet her there."
    if date_dd is True:
        mct "Daisy is going to the amusement park and wants to know if I can join her."

    if date_pw is True:
        if date_dw is True or date_dd is True:
            mct "Hmm. Polly also says that she & Nora are going to the amusement park... and they're horny as hell?!"
        elif True:
            mct "Hmm. Polly says that she & Nora are going to the amusement park... and they're horny as hell?!"
    scene d17s06-05 mc-phone-sit-thinking_c1 with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.6
    mct "I really should keep studying, but I could use a break."

    menu:
        "Respond to Daisy"(hint="d17s06m01c01") if date_dd is True:
            $ d17s06_choice_dd = True

            stop music fadeout 3.0
            jump d17s06dd

        "Respond to Dahlia"(hint="d17s06m01c02") if date_dw is True:
            $ d17s06_choice_dw = True

            stop music fadeout 3.0
            jump d17s06dw

        "Respond to Polly and Nora"(hint="d17s06m01c03") if date_pw is True and d06s07_creampie is False:
            $ d17s06_choice_pn = True

            stop music fadeout 3.0
            jump d17s06pn
        "Go back to studying"(hint="d17s06m01c04") if True:


            $ d17s06_choice_study = True

            scene d17s06-05 mc-phone-sit-thinking_c2 with dissolve
            play voice2 mc_no_nah2 noloop
            mct "Nah. I really need to hit the books."

            jump d17s06_study

label d17s06_study:

    $ study_points += 1
    play sound sfx_paper_rustl1
    scene d17s06-10 mc-phone-sit-study_c1 with fade
    pause
    play sound sfx_keyboard_typing2
    scene d17s06-10 mc-phone-sit-study_c2 with fade
    stop sound fadeout 1.0
    pause
    scene d17s06-10 mc-phone-sit-study_c1 with fade
    play voice2 mc_angry_huh2 noloop
    mct "Well, that's enough of that."
    mct "Damn. Why is studying always so boring?"
    scene d17s06-02 mc-phone_c1 with dissolve
    mct "Maybe I can take a little nap before dinner."

    stop music fadeout 3.0
    jump d17s07
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
