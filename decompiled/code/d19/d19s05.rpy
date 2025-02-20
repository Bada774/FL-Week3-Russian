image d19s05-a1 = Movie(play = "images/Day-19/s05/anim/d19s05-a26-03-1-2x-50fps.webm", start_image = "d19s05-a26-03-1 mc-jerk-off-anim-01")
image d19s05-a2 = Movie(play = "images/Day-19/s05/anim/d19s05-a26-03-2-2x-50fps.webm", start_image = "d19s05-a26-03-2 mc-jerk-off-anim-01")

image minigame_icon_0 = "images/Day-19/s05/minigame/minigame_icon_0.webp"
image minigame_icon_1 = "images/Day-19/s05/minigame/minigame_icon_1.webp"
image minigame_icon_2 = "images/Day-19/s05/minigame/minigame_icon_2.webp"
image minigame_icon_3 = "images/Day-19/s05/minigame/minigame_icon_3.webp"
image minigame_icon_4 = "images/Day-19/s05/minigame/minigame_icon_4.webp"
image minigame_icon_5 = "images/Day-19/s05/minigame/minigame_icon_5.webp"
image minigame_icon_6 = "images/Day-19/s05/minigame/minigame_icon_6.webp"
image minigame_icon_7 = "images/Day-19/s05/minigame/minigame_icon_7.webp"
image minigame_icon_8 = "images/Day-19/s05/minigame/minigame_icon_8.webp"

image d19s05_minigame_mc_expression_change:
    "d19s05-17 mc-minigame-main_c1"
    pause 5.45
    "d19s05-17-01 expression_01_c1"
    pause 5.45
    "d19s05-17-02 expression_02_c1"
    pause 5.45
    "d19s05-17-03 expression_03_c1"
    pause 5.45
    "d19s05-17-04 expression_04_c1"
    pause 5.45
    "d19s05-17-05 expression_05_c1"
    pause 5.45
    "d19s05-17-06 expression_06_c1"
    pause 5.45
    "d19s05-17-07 expression_07_c1"
    pause 5.45
    "d19s05-17-08 expression_08_c1"
    pause 5.45
    "d19s05-17-09 expression_09_c1"
    pause 5.45
    "d19s05-17-10 expression_09b_c1"
    pause 5.45

label replay_d19s05:
label d19s05:

    $ d19s05_use_panty = False
    $ d19s05_skip_minigame = False
    $ d19s05_win = False

    if not _in_replay:
        scene black
        show screen scene_transistion(_("1 hour later"))
        with Fade(0.9, 0.5, 0.5)
        pause
        hide screen scene_transistion
    scene d19s05-01 mc-walks-into-arj-apartment_c1
    with Fade(0.5, 0.5, 0.9)
    queue music music_relaxed_at_home
    $ renpy.music.set_volume(0.7, 5.5, "music")
    pause
    play sound sfx_cloth_rustling4
    scene d19s05-02 mc-puts-books-couch-sits-down_c1 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.5
    mct "*Sigh* This place is so much nicer than the dorm."
    mct "I never noticed how quiet it is here."
    scene d19s05-03 mc-sighs_c1 with dissolve
    play voice2 d1s1_mmm noloop volume 1.4
    mct "I'm really fucking glad I asked AmRose if I could study here."
    if cage_ntr is True:
        scene d19s05-04 mc-angry-cant-go-back-dorm_c1 with dissolve
        play voice2 mc_disappointed_ehh4 noloop
        mct "I can't spend a second longer in that fucking dorm anyway."
        mct "If that dickless bastard had come in while I was getting my books, one of us would've died today."
    scene d19s05-05 mc-stands-up_c1 with dissolve
    if cage_ntr is True:
        mct "No point worrying about that now. I have to focus on this."
    mct "I need something to wake me up. AmRose has a bath here, doesn't she...?"

    play sound shower fadein 1.5
    scene d19s05-20 mc-gets-out-shower_c1 with Fade(0.5, 0.5, 0.5)
    stop sound fadeout 1.0
    $ renpy.music.set_volume(1.0, 0.0, "sound4")
    play sound4 sfx_shower_off1 noloop
    play voice2 mc_happy_oof3 noloop
    pause
    scene d19s05-22 mc-enters-arj-room_looking_towel_c1 with dissolve
    pause
    play sound sfx_door_creak4
    scene d19s05-23 mc-searching-drawers_c1 with dissolve
    pause
    play sound sfx_door_slide2
    scene d19s05-24 mc-finds-panties_c1 with dissolve
    pause
    scene d19s05-25 mc-panties-choice_c1 with dissolve
    play voice2 mc_happy_hah2 noloop
    mct "Well, what do we have here..."
    menu:
        "Peruse her wears"(hint="d19s05m01c01"):

            $ d19s05_use_panty = True

            $ Lovense.stop()

            play voice2 d14s16_smell noloop
            scene d19s05-26-01 mc-smells-panties_c1 with dissolve
            $ Lovense.vibrate(1)
            pause
            scene d19s05-26-02 mc-gets-hard_c1 with dissolve
            play voice2 mc_thinking_mmm2 noloop
            mct "...I've been studying hard enough, a slight break wouldn't hurt."
            scene d19s05-a26-03-1 mc-jerk-off-anim-01 with dissolve
            pause
            play voice2 d7s4_mcbreathing fadein 4.0
            play sound sfx_handjob_cream1 loop
            $ Lovense.vibrate(5)
            scene d19s05-a1
            pause
            scene d19s05-a2 with dissolve
            pause
            $ Lovense.vibrate(12)
            play voice2 d1s5_orgasm2 noloop
            stop sound fadeout 0.5
            scene d19s05-26-04 mc-cums-in-panties_c1 with hpunch
            pause
            $ Lovense.vibrate(1)
            scene d19s05-26-05 mc-leaves-arj-bedroom_c1 with dissolve
            pause
            play sound sfx_handjob_cream1 loop
            $ Lovense.vibrate(5)
            scene d19s05-26-06 mc-jerk-study-montage-one_c1 with dissolve
            play voice2 mc_thinking_mmm1 noloop
            pause
            stop sound fadeout 0.5
            play sound4 sfx_paper_rustl1 noloop
            $ Lovense.vibrate(1)
            scene d19s05-26-07 mc-jerk-study-montage-two_c1 with dissolve
            pause
            play sound sfx_handjob_cream1 loop
            $ Lovense.vibrate(5)
            scene d19s05-26-08 mc-jerk-study-montage-three_c1 with dissolve
            play voice2 mc_angry_huh2 noloop
            pause
            stop sound fadeout 0.5
            play sound4 sfx_paper_slide1 noloop
            $ Lovense.vibrate(1)
            scene d19s05-26-09 mc-jerk-study-montage-four_c1 with dissolve
            pause
            play sound sfx_handjob_cream1 loop
            $ Lovense.vibrate(5)
            scene d19s05-26-10 mc-jerk-study-montage-five_c1 with dissolve
            play voice2 d14s16_smell noloop
            pause
            stop sound fadeout 0.5
            play voice2 mc_angry_errr4 noloop
            $ Lovense.vibrate(15)
            scene d19s05-26-11 mc-cums-last-time_c1 with vpunch
            pause
            queue voice2 d7s6_snoring noloop
            $ Lovense.vibrate(1)
            scene d19s05-26-12 mc-cant-go-anymore_c1 with dissolve
            pause
            scene d19s05-26-13 mc-looks-around-spent_c1 with dissolve
            play voice2 mc_arrogant_heh2 noloop
            mct "I better clean this mess up and get serious."
            play sound sfx_door_slide1 volume 1.7
            scene d19s05-27-01 mc-puts-panties-back_c1 with dissolve
            pause

            $ Lovense.stop()

            $ renpy.music.set_volume(0.3, 3.5, "music")
            play sound ["<silence 0.3>", sfx_door_closed7]
            scene d19s05-27-02 mc-focused-ready-to-study_c1 with fade
            pause
            scene d19s05-05 mc-stands-up_c1 with dissolve
            pause
            $ renpy.end_replay()
            $ unlock_gallery_slot("scene", "d19s05")

            jump d19s05_minigame
        "Don't"(hint="d19s05m01c02"):

            play voice2 mc_arrogant_nah1 noloop
            scene d19s05-27-01 mc-puts-panties-back_c1 with dissolve
            mc "Nah, I need to focus on studying."
            $ renpy.music.set_volume(1.0, 3.5, "music")
            play sound sfx_door_slide1 volume 1.7
            scene d19s05-27-02 mc-focused-ready-to-study_c1 with Fade(0.4, 0.4, 0.4)
            pause
            play sound sfx_paper_rustl1
            scene d19s05-07 mc-study-montage-one_c1 with dissolve
            pause
            play sound sfx_keyboard_typing2
            scene d19s05-08 mc-study-montage-two_c1 with dissolve
            pause
            stop sound fadeout 1.0
            scene d19s05-09 mc-study-montage-three_c1 with dissolve
            pause
            play sound sfx_keyboard_typing1
            scene d19s05-10 mc-study-montage-four_c1 with dissolve
            pause
            play sound sfx_paper_slide1
            scene d19s05-11 mc-study-montage-five_c1 with dissolve
            pause
            play sound sfx_keyboard_typing2
            scene d19s05-12 mc-study-montage-six_c1 with dissolve
            pause
            play sound sfx_paper_rustl1
            scene d19s05-13 mc-study-montage-seven_c1 with dissolve
            pause
            scene d19s05-14 mc-study-montage-eight_c1 with dissolve
            pause
            scene d19s05-15 mc-study-montage-nine_c1 with dissolve
            pause
            play sound sfx_keyboard_typing2
            scene d19s05-16 mc-study-montage-ten_c1 with dissolve
            pause
            stop sound fadeout 1.0
            scene d19s05-05 mc-stands-up_c1 with dissolve
            pause
            $ renpy.end_replay()

            jump d19s05_minigame

label replay_d19s05m:
    $ study_points = 0
label d19s05_minigame:

    $ preferences.gl_powersave = False
    $ renpy.free_memory()
    $ d19s05_minigame_score = 0
    $ d19s05_minigame_timer = 60.0
    $ d19s05_score_multiplier = 1.0
    $ d19s05_difficulty = 0.5
    $ d19s05_player_hp = 3
    $ d19s05_speed_multiplier = [8.0, 6.0, 5.5, 5.0, 4.5, 4.0, 3.0, 2.5, 2.0, 2.0, 1.5, 1.5]
    $ d19s05_step = 0
    $ d19s05_icons_list = [
            clicker_projectile("minigame_icon_0", 1.0),
            clicker_projectile("minigame_icon_1", 1.0),
            clicker_projectile("minigame_icon_2", 1.0),
            clicker_projectile("minigame_icon_3", 1.0),
            clicker_projectile("minigame_icon_4", 1.0),
            clicker_projectile("minigame_icon_5", 1.0),
            clicker_projectile("minigame_icon_6", 1.0),
            clicker_projectile("minigame_icon_7", 1.0),
            clicker_projectile("minigame_icon_8", 1.0),
            ]

    $ quick_menu = False
    call hide_fl_points_overlay () from _call_hide_fl_points_overlay_4

    $ renpy.music.set_volume(0.3, 3.5, "music")
    scene d19s05-06 mc-looks-at-books-time-to-study_c1 with dissolve
    play voice2 d1s5_mchappy noloop
    mct "I should focus on the study materials and keep my brain away from the boobs and asses."
    $ renpy.music.set_volume(0.1, 7.5, "music")
    scene d19s05-17 mc-minigame-main_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    "Super focused study stars in 3... 2... 1..."
    $ renpy.music.set_volume(0.0, 0.6, "music")
    $ renpy.music.set_volume(1.0, 0.0, "music2")

    $ renpy.block_rollback()
    play music2 blitz_soundtrack_warmup
    scene d19s05_minigame_mc_expression_change
    call screen minigame_screen()

    jump d19s05_after_minigame

label d19s05_skip_minigame:
    $ d19s05_player_hp = 0
    $ d19s05_skip_minigame = True

    jump d19s05_after_minigame

label d19s05_after_minigame:

    $ quick_menu = True
    $ preferences.gl_powersave = True
    call show_fl_points_overlay () from _call_show_fl_points_overlay_2

    $ d19s05_minigame_score = d19s05_minigame_score * d19s05_score_multiplier
    $ d19s05_minigame_score = int(d19s05_minigame_score)
    stop music2 fadeout 1.4
    if d19s05_player_hp > 0:
        $ d19s05_win = True
    if d19s05_skip_minigame is False:
        $ renpy.notify(_("Your total score is {}").format(d19s05_minigame_score))
        if persistent.minigame_max_score < d19s05_minigame_score:
            $ persistent.minigame_max_score = d19s05_minigame_score

    if d19s05_win is True:
        play sound sfx_d19s05_minigame_win
        scene d19s05-18 mc-headache-from-study_c1 with fade
        $ renpy.block_rollback()
        pause
        $ study_points += 1
        play voice2 mc_thinking_mmm3 noloop
        mct "For the first time in weeks, I actually feel like I learned something. I might actually have a chance here!"
        $ renpy.music.set_volume(0.5, 3.5, "music")
        scene d19s05-27-04 mc-smiles-happy-he-finished_c1 with dissolve
        play voice2 d3s11b_mcheh noloop
        mct "That...actually went better than I thought it would."
        mct "Now if I can just get the judges on my side, I'm sure I can ace this!"
        $ unlock_gallery_slot("scene", "d19s05m")
    else:
        play sound sfx_d19s05_minigame_lose
        scene d19s05-19 mc-splays-couch_c1 with fade
        $ renpy.block_rollback()
        pause
        play voice2 d1s1_mmm noloop
        mct "All that work just to end up back on square one. I've learned jack shit!"
        mct "If I want to pass, I need to think about getting the judges on my side."
        $ renpy.music.set_volume(0.5, 3.5, "music")
    scene d19s05-27-03 mc-puts-down-laptop-books_c1 with dissolve
    if d19s05_minigame_score >= 250:
        $ fl_achievement_unlock("d19s05n01")
        $ unlock_gallery_in_replay("extra", "d19s05n01")
    pause
    $ renpy.end_replay()

    jump d19s06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
