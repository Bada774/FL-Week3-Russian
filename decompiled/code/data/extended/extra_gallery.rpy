init python:













    extra_gallery_slots = []

    main_game_extra_gallery_slots = [
        ("d21s99n01",   _("01. Worst Nightmare"),                       _("Unlock the hidden 19th ending"),                         None),
        ("d19s05n01",   _("02. GG EZ Videogame"),                       _("Get a high score in the minigame"),                      None),
        ("d21s25n01",   _("03. Somebody that I Used to Know"),          _("Unlock Lydia's music video"),                            None),
        ("d21s25n02",   _("04. Full Course"),                           _("Unlock 18 endings"),                                     None),
        ("d21s25n03",   _("05. Front Nine"),                            _("Unlock 9 endings"),                                      None),
        ("d21s25n04",   _("06. What a Wild Ride"),                      _("Complete all 6 base endings"),                           None),
        ("d18s10n01",   _("07. WTF Bro?"),                              _("See everything you never wanted to"),                    None),
        ("d18s10n02",   _("08. Hacker"),                                _("View all the secret door codes"),                        None),
        ("d15s01n01",   _("09. In the Beginning..."),                   _("Make it all the way to Day 15"),                         None),
        ("d16s10n01",   _("10. Release the Kraken"),                    _("Get free from the cage"),                                None),
        ("d18s10n03",   _("11. Sudo Admin"),                            _("Enter the server room"),                                 None),
        ("d20s08n01",   _("12. rm -rf"),                                _("Destroy the app... or not"),                             None),
        ("d21s07n01",   _("13. The People Versus..."),                  _("Go to the court trial"),                                 None),
        ("d21s25n05",   _("14. Cherry Popped"),                         _("Finish your first time"),                                None),
        ("d18s10n04",   _("15. Miss White, with the Candlestick"),      _("Discover who is behind the app on the LC path"),         None),
        ("d18s10n05",   _("16. Keyser Soze"),                           _("Discover who is behind the app on the NTR path"),        None),
        ("d20s04n01",   _("17. Real Genius"),                           _("Finish final exams perfectly"),                          None),
        ("d21s07n02",   _("18. Keep Pounding That Gavel"),              _("Get both scenes with the judge"),                        None),
        ("d20s03n01",   _("19. What Are Friends For"),                  _("Knock up your best friend's gal"),                       None),
        ("d17s06n01",   _("20. Are You Not Entertained"),               _("Play all three scenes at the amusement park"),           None),
        ("d17s05n01",   _("21. Oh, the Humanity!"),                     _("Play all three versions of Lyssa's Wednesday scenes"),   None),
        ("d16s04n01",   _("22. Why Would You Do That"),                 _("Don't remove the cage, even though you could"),          None),
        ("d21s05n01",   _("23. Fantastic Fivesome"),                    _("Maria and some friends are very thankful"),              None),
        ("e06s08n01",   _("24. Craving Pickles and Ice-cream"),         _("Impregnate every possible person in the queen's harem"), None),
        ("e02s05n01",   _("25. I Need Sexual Healing"),                 _("Helped all 3 couples at the ski resort"),                None),
        ("d17s06n02",   _("26. This Magic Moment"),                     _("Went on the ferris wheel with Daisy"),                   None),
        ("d17s06n03",   _("27. May I panic now, Mistress?"),            _("Braved the funhouse with Dahlia"),                       None),
        ("d17s06n04",   _("28. Fifty-Five Foot Club"),                  _("Join Polly and Nora on the ferris wheel"),               None),
        ("d15s04n01",   _("29. That Was Cathartic... for Them"),        _("Fix Dahlia and Samiya's relationship"),                  None),
        ]

    extra_gallery_slots.extend(main_game_extra_gallery_slots)

    dlc_1_extra_gallery_slots =  [
        ("dlc01n01",    _("30. What? You wanted more?"),                _("Finish all 6 Endings from DLC-1"),                       None),
        ("e14s06n01",   _("31. Go Debbie Go"),                          _("Have sex with Debbie"),                                  None),
        ("e07s07n01",   _("32. Fully Cooked"),                          _("Get max points in Lydia's challenges in e07"),           None),
        ("e04s08n01",   _("33. Full House"),                            _("Play with all the characters in e04"),                   None),
        ("dlc01n02",    _("34. Day and Night"),                         _("Finish Ending 4 and Ending 7"),                          None),
        ("dlc01n03",    _("35. A lucky dozen"),                         _("Finish 12 endings"),                                     None),
        ]

    dlc_2_extra_gallery_slots =  [
        ("dlc02n01",    _("36. Don't threaten me with a good time"),    _("Finish all 6 Endings from DLC-2"),                       None),
        ("e09s01n01",   _("37. I saw, I came, I conquered"),            _("Have all Characters in last orgy in Ending 9"),          None),
        ("e15s01n01",   _("38. Golden Pass"),                           _("Have all Characters in Ending 15"),                      None),
        ("e03s01n01",   _("39. She belongs in a museum"),               _("Find golden Lyssa (Ending 3)"),                          None),
        ("e18s01n01",   _("40. Do the Pulp Fiction Thing"),             _("Do the pulp fiction thing (Ending 18)"),                 None),
        ("e16s01n01",   _("41. Backdoor Cat Girl"),                     _("Backdoor Cat Girl (Ending 16)"),                         None),
        ("e15s01n02",   _("42. Pee Bootcamp"),                          _("Begin Olivia's Training"),                               None),
        ("e05s01n01",   _("43. Choo-choo"),                             _("Choo-choo (Ending 5)"),                                  None),
        ("dlc02n02",    _("44. Londyn Twice"),                          _("Meet Londyn in Ending 9 and Ending 18"),                 None),
        ("dlc02n03",    _("45. I've seen all the possible outcomes"),   _("Finish all 18 Endings"),                                 None),
        ]














    extra_gallery = FLGallery()
    extra_gallery.transition = dissolve
    cg_gallery.navigation = True
    extra_gallery.locked_button = "gallery_locked_button"




    extra_gallery.button("d21s99n01")
    extra_gallery.image("sad-kianu")


    extra_gallery.button("d19s05n01")


    extra_gallery.button("d21s25n01")


    extra_gallery.button("d21s25n02")
    extra_gallery.image("sy-goty_c1")
    extra_gallery.image("sy-goty-2_c1")


    extra_gallery.button("d21s25n03")
    extra_gallery.image("front_nine_bonus_meme")


    extra_gallery.button("d21s25n04")


    extra_gallery.button("d18s10n01")
    extra_gallery.image("homer_pete_1")
    extra_gallery.image("homer_pete_2")
    extra_gallery.image("homer_pete_3")


    extra_gallery.button("d18s10n02")
    extra_gallery.image("fl-promo-new-years-arj-4k_c1")
    extra_gallery.image("fl-promo-new-years-mes-4k_c1")


    extra_gallery.button("d15s01n01")
    extra_gallery.image("sy_09_bonus_art")
    extra_gallery.image("sy_09_bonus_art_2")


    extra_gallery.button("d16s10n01")
    extra_gallery.image("arj_10_bonus_art")
    extra_gallery.image("arj_10_bonus_art_2")


    extra_gallery.button("d18s10n03")
    extra_gallery.image("promo-ir-hr-01_c1")
    extra_gallery.image("promo-ir-hr-01_c2")
    extra_gallery.image("promo-ir-hr-01_c3")
    extra_gallery.image("promo-ir-hr-02_c1")
    extra_gallery.image("promo-ir-hr-02_c2")
    extra_gallery.image("promo-ir-hr-02_c3")


    extra_gallery.button("d20s08n01")
    extra_gallery.image("rm_rf_bonus_meme")


    extra_gallery.button("d21s07n01")
    extra_gallery.image("lc-court_c1")


    extra_gallery.button("d21s25n05")
    extra_gallery.image("real_ending_bonus_meme")


    extra_gallery.button("d18s10n04")
    extra_gallery.image("lc_15_bonus_art_1")
    extra_gallery.image("lc_15_bonus_art_2")


    extra_gallery.button("d18s10n05")
    extra_gallery.image("lc_ntr_16_bonus_art_1")
    extra_gallery.image("lc_ntr_16_bonus_art_2")
    extra_gallery.image("lc_ntr_16_bonus_art_3")
    extra_gallery.image("lc_ntr_16_bonus_art_4")
    extra_gallery.image("lc_ntr_16_bonus_art_5")


    extra_gallery.button("d20s04n01")
    extra_gallery.image("mes_17_bonus_art")


    extra_gallery.button("d21s07n02")
    extra_gallery.image("judge_c1")


    extra_gallery.button("d20s03n01")
    extra_gallery.image("chloe-pregnant_c1")


    extra_gallery.button("d17s06n01")
    extra_gallery.image("dd-dw-pw-meme")


    extra_gallery.button("d17s05n01")
    extra_gallery.image("promo-lc-lyssa-01-4k_c1")
    extra_gallery.image("promo-lc-lyssa-01-4k_c2")
    extra_gallery.image("promo-lc-lyssa-01-4k_c3")
    extra_gallery.image("promo-lc-lyssa-01-4k_c4")


    extra_gallery.button("d16s04n01")
    extra_gallery.image("money_mc_meme_art")


    extra_gallery.button("d21s05n01")
    extra_gallery.image("mk_23_bonus_art_1")
    extra_gallery.image("mk_23_bonus_art_2")
    extra_gallery.image("mk_23_bonus_art_3")
    extra_gallery.image("mk_23_bonus_art_4")
    extra_gallery.image("mk_23_bonus_art_5")
    extra_gallery.image("mk_23_bonus_art_6")


    extra_gallery.button("e06s08n01")
    extra_gallery.image("mh_bonus_trade_meme")


    extra_gallery.button("e02s05n01")
    extra_gallery.image("promo-ntr-lyssa-01-4k_c1")
    extra_gallery.image("promo-ntr-lyssa-01_4k_c2")
    extra_gallery.image("promo-ntr-lyssa-01_4k_c3")
    extra_gallery.image("promo-ntr-lyssa-01-4k_c4")


    extra_gallery.button("d17s06n02")
    extra_gallery.image("dd_26_bonus_art")
    extra_gallery.image("dd_26_bonus_art_2")


    extra_gallery.button("d17s06n03")
    extra_gallery.image("promo-stacy-dahlia-02-4k_c1")
    extra_gallery.image("promo-stacy-dahlia-02-4k_c2")
    extra_gallery.image("promo-stacy-dahlia-02-4k_c3")


    extra_gallery.button("d17s06n04")
    extra_gallery.image("nk_28_bonus_art_1")
    extra_gallery.image("nk_28_bonus_art_2")
    extra_gallery.image("nk_28_bonus_art_3")
    extra_gallery.image("nk_28_bonus_art_4")
    extra_gallery.image("nk_28_bonus_art_5")
    extra_gallery.image("nk_28_bonus_art_6")
    extra_gallery.image("pw_28_bonus_art_1")
    extra_gallery.image("pw_28_bonus_art_2")
    extra_gallery.image("pw_28_bonus_art_3")
    extra_gallery.image("pw_28_bonus_art_4")
    extra_gallery.image("pw_28_bonus_art_5")
    extra_gallery.image("pw_28_bonus_art_6")


    extra_gallery.button("d15s04n01")
    extra_gallery.image("promo-stacy-dahlia-01-4k_c1")
    extra_gallery.image("promo-stacy-dahlia-01-4k_c2")
    extra_gallery.image("promo-stacy-dahlia-01-4k_c3")


    extra_gallery.button("dlc01n01")


    extra_gallery.button("e14s06n01")
    extra_gallery.image("sy_christmas_bonus_art_sm")


    extra_gallery.button("e07s07n01")
    extra_gallery.image("lydiaxlydia_promo")


    extra_gallery.button("e04s08n01")
    extra_gallery.image("sy_halloween_bonus_art")


    extra_gallery.button("dlc01n02")
    extra_gallery.image("lydiaxlydia_meme_bonus")


    extra_gallery.button("dlc01n03")
    extra_gallery.image("mh_christmas_bonus_art")


    extra_gallery.button("dlc02n01")


    extra_gallery.button("e09s01n01")
    extra_gallery.image("i_come_in_peace_1")


    extra_gallery.button("e15s01n01")


    extra_gallery.button("e03s01n01")
    extra_gallery.image("i_come_in_peace_2")


    extra_gallery.button("e18s01n01")
    extra_gallery.image("sb_pulp_fiction_meme")


    extra_gallery.button("e16s01n01")


    extra_gallery.button("e15s01n02")


    extra_gallery.button("e05s01n01")


    extra_gallery.button("dlc02n02")


    extra_gallery.button("dlc02n03")
    extra_gallery.image("gigachad_mc_meme")



screen bonus_high_score():
    tag menu


    add "images/extended/bonus/sp-mike.webp"

    text _("HIGH SCORE :\n[persistent.minigame_max_score]") style "bonus_high_score_text"

    button:
        action ShowMenu("extra")

style bonus_high_score_text:
    font "fonts/impact.ttf"
    color "#fff"
    size 60
    outlines [(3, "#000", 0, 0)]
    text_align 0.5
    xpos 1440
    ypos 380



label lc_video_full:

    $ renpy.movie_cutscene("images/extended/bonus/lc_videoc_lip_full.webm")
    $ renpy.end_replay()

    return



screen bonus_front_nine():
    tag menu


    add "black"
    add "images/extended/bonus/rookie-numbers.webp" xalign 0.5

    text _("HOW MANY ENDINGS HAVE YOU UNLOCKED?") ypos 310 style "bonus_front_nine_text"
    text _("9 ENDINGS") ypos 670 style "bonus_front_nine_text"
    text _("YOU GOTTA PUMP THOSE NUMBERS UP.\nTHOSE ARE ROOKIE NUMBERS!") ypos 990 style "bonus_front_nine_text"

    button:
        action ShowMenu("extra")

style bonus_front_nine_text:
    font "fonts/impact.ttf"
    color "#fff"
    outlines [(1, "#000", 0, 0)]
    size 30
    xalign 0.5
    text_align 0.5
    kerning 1



screen bonus_change_my_mind():
    tag menu


    add "black"
    add "images/extended/bonus/sy-change-my-mind.webp" xalign 0.5

    text _("6 endings\naren't enough.\nI need all 18 now!!!") style "bonus_change_mind_text_1" at rotate(-10)
    text _("{b}CHANGE MY MIND{/b}") style "bonus_change_mind_text_2" at rotate(-11)

    button:
        action ShowMenu("extra")

style bonus_change_mind_text_1:
    font "fonts/Andika-Regular.ttf"
    color "#000"
    size 70
    text_align 0.5
    xpos 820
    ypos 410

style bonus_change_mind_text_2:
    font "fonts/Andika-Regular.ttf"
    color "#000"
    size 60
    text_align 0.5
    xpos 875
    ypos 650



image sy_09_bonus_art = Composite(
    (1920, 1080),
    (0, 0), "black",
    (564, 0), "sy_3_6_sfw"
    )

image sy_09_bonus_art_2 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (564, 0), "sy_3_6"
    )



image arj_10_bonus_art = Composite(
    (1920, 1080),
    (0, 0), "black",
    (564, 0), "arj_2_4_sfw"
    )

image arj_10_bonus_art_2 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (564, 0), "arj_2_4"
    )



screen bonus_rm_rf():
    tag menu


    add "black"
    add "images/extended/bonus/ana-pad.webp" xalign 0.5

    text _("I WANT TO KEEP\nFETISH LOCATOR") style "bonus_rm_rf_text_1"
    if is_steam_edition is True or is_gog_edition is True:
        text _("TO MAKE SURE NO ONE\nWILL BE BLACKMAILED") style "bonus_rm_rf_text_2"
    else:
        text _("YOU'RE GOING TO USE\nIT FOR GOOD, RIGHT?") style "bonus_rm_rf_text_2"
    text _("RIGHT?") style "bonus_rm_rf_text_3"

    button:
        action ShowMenu("extra", 2)

style bonus_rm_rf_text_1:
    size 55
    font "fonts/impact.ttf"
    color "#fff"
    outlines [(3, "#000", 0, 0)]
    text_align 0.5
    xanchor 0.5
    xpos 640
    ypos 380

style bonus_rm_rf_text_2:
    size 50
    font "fonts/impact.ttf"
    color "#fff"
    outlines [(3, "#000", 0, 0)]
    text_align 0.5
    xanchor 0.5
    xpos 1280
    ypos 390

style bonus_rm_rf_text_3:
    size 80
    font "fonts/impact.ttf"
    color "#fff"
    outlines [(3, "#000", 0, 0)]
    text_align 0.5
    xanchor 0.5
    xpos 1280
    ypos 980



screen bonus_cherry_popped():
    tag menu


    add "images/extended/bonus/arj-meme.webp"

    text _("THE FIRST ENDING\nFROM 18 TOTAL ENDINGS") style "bonus_cherry_popped_text_small"
    text _("IS THAT A REAL ENDING?") style "bonus_cherry_popped_text_big"

    button:
        action ShowMenu("extra", 3)

style bonus_cherry_popped_text_big:
    size 75
    font "fonts/impact.ttf"
    color "#fff"
    outlines [(3, "#000", 0, 0)]
    text_align 0.5
    xalign 0.5
    ypos 970

style bonus_cherry_popped_text_small:
    size 45
    font "fonts/impact.ttf"
    color "#fff"
    outlines [(1, "#000", 0, 0)]
    text_align 0.5
    kerning 1
    xanchor 0.5
    xpos 1535
    ypos 400



image lc_15_bonus_art_1 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (420, 0), "lc-canvas-3_c1"
    )

image lc_15_bonus_art_2 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (420, 0), "lc-canvas-3_c2"
    )



image lc_ntr_16_bonus_art_1 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (420, 0), "lc-canvas-1_c1"
    )

image lc_ntr_16_bonus_art_2 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (420, 0), "lc-canvas-1_c2"
    )

image lc_ntr_16_bonus_art_3 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (420, 0), "lc-canvas-1_c3"
    )

image lc_ntr_16_bonus_art_4 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (420, 0), "lc-canvas-2_c2"
    )

image lc_ntr_16_bonus_art_5 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (420, 0), "lc-canvas-2_c3"
    )



image mes_17_bonus_art = Composite(
    (1920, 1080),
    (0, 0), "black",
    (424, 0), "min_2a"
    )



image money_mc_meme_art = Composite(
    (1920, 1080),
    (0, 0), "black",
    (231, 0), "money_with_mike_2"
    )



image mk_23_bonus_art_1 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (420, 0), "mk-canvas-1_c1"
    )

image mk_23_bonus_art_2 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (420, 0), "mk-canvas-1_c2"
    )

image mk_23_bonus_art_3 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (420, 0), "mk-canvas-1_c3"
    )

image mk_23_bonus_art_4 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (420, 0), "mk-canvas-2_c1"
    )

image mk_23_bonus_art_5 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (420, 0), "mk-canvas-3_c1"
    )

image mk_23_bonus_art_6 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (420, 0), "mk-canvas-3_c2"
    )



screen bonus_trade_meme():
    tag menu


    add "black"
    add "images/extended/bonus/lyssa-trade-offer-1.webp" xalign 0.5

    frame:
        style_prefix "bonus_trade"
        text _("TRADE OFFER")

    text _("I receive:") xpos 730 style "bonus_trade_text_title"
    text _("Cum in every pussy\nat the wedding") xpos 730 style "bonus_trade_text_body"
    text _("You receive:") xpos 1190 style "bonus_trade_text_title"
    text _("The whole\nharem pregnant") xpos 1190 style "bonus_trade_text_body"

    button:
        action ShowMenu("extra", 4)

style bonus_trade_frame:
    background Frame("images/extended/bonus/lyssa-trade-offer-title-bg.webp", 55, 5, 55, 5)
    left_padding 60
    right_padding 60
    xalign 0.5
    ypos 30

style bonus_trade_text:
    size 40
    font "fonts/Arial-Unicode.ttf"
    color "#fff"
    ypos -3

style bonus_trade_text_title:
    size 40
    font "fonts/impact.ttf"
    color "#fff"
    outlines [(1, "#000", 0, 0)]
    text_align 0.5
    kerning 1
    xanchor 0.5
    ypos 150

style bonus_trade_text_body:
    size 30
    font "fonts/impact.ttf"
    color "#fff"
    outlines [(1, "#000", 0, 0)]
    text_align 0.5
    kerning 1
    xanchor 0.5
    ypos 200



image dd_26_bonus_art = Composite(
    (1920, 1080),
    (0, 0), "black",
    (564, 0), "dd_1_5_sfw"
    )

image dd_26_bonus_art_2 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (564, 0), "dd_1_5"
    )



image nk_28_bonus_art_1 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (420, 0), "nk-canvas-1_c1"
    )

image nk_28_bonus_art_2 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (420, 0), "nk-canvas-2_c1"
    )

image nk_28_bonus_art_3 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (420, 0), "nk-canvas-2_c2"
    )

image nk_28_bonus_art_4 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (420, 0), "nk-canvas-3_c1"
    )

image nk_28_bonus_art_5 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (420, 0), "nk-canvas-3_c2"
    )

image nk_28_bonus_art_6 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (420, 0), "nk-canvas-3_c3"
    )

image pw_28_bonus_art_1 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (420, 0), "pw-canvas-1_c1"
    )

image pw_28_bonus_art_2 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (420, 0), "pw-canvas-1_c2"
    )

image pw_28_bonus_art_3 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (420, 0), "pw-canvas-1_c3"
    )

image pw_28_bonus_art_4 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (420, 0), "pw-canvas-2_c1"
    )

image pw_28_bonus_art_5 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (420, 0), "pw-canvas-2_c2"
    )

image pw_28_bonus_art_6 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (420, 0), "pw-canvas-2_c3"
    )



screen bonus_horny_meme():
    tag menu


    add "black"
    add "images/extended/dlc-1-bonus/meme_2_square_bg.webp" xalign 0.5

    text _("ORNY") xanchor 0.5 xpos 970 yalign 0.2 style "bonus_horny_meme_text"
    text _("H") xanchor 0.5 xpos 1230 yalign 0.24 style "bonus_horny_meme_text"
    text _("UNGRY") xanchor 0.5 xpos 680 yalign 0.36 style "bonus_horny_meme_text"
    text _("APPY") xalign 0.505 yalign 0.73 style "bonus_horny_meme_text"

    button:
        action ShowMenu("extra", 5)

style bonus_horny_meme_text:
    size 60
    font "fonts/impact.ttf"
    color "#fff"
    outlines [(3, "#000", 0, 0)]
    text_align 0.5



image sy_christmas_bonus_art_sm = Composite(
    (1920, 1080),
    (0, 0), "black",
    (403, 0), "cristmas_sy_sm_bonus_4"
    )



image sy_halloween_bonus_art = Composite(
    (1920, 1080),
    (0, 0), "black",
    (283, 0), "halloween_sy_bonus_5"
    )



image mh_christmas_bonus_art = Composite(
    (1920, 1080),
    (0, 0), "black",
    (208, 0), "cristmas_mh_bonus_2"
    )



screen spit_on_that_thang_meme():
    tag menu


    add "images/extended/bonus-DLC-2/hawk_tuah_meme.webp"

    text _("SPIT ON THAT THANG!") xalign 0.5 yalign 0.99 style "bonus_cherry_popped_text_big"

    button:
        action ShowMenu("extra", 6)



image i_come_in_peace_1 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (626, 0), "i_come_in_peace_mc_sy"
    )



screen mes_leo_meme():
    tag menu


    add "images/extended/bonus-DLC-2/mes_leo_meme.webp"

    text _("WHEN HE MANAGES TO GET EVERYONE TO COME TO YOUR FANCY NEW SPA") xalign 0.5 yalign 0.99 style "bonus_rm_rf_text_1"

    button:
        action ShowMenu("extra", 7)



image i_come_in_peace_2 = Composite(
    (1920, 1080),
    (0, 0), "black",
    (626, 0), "i_come_in_peace_mc_sy_mh"
    )



screen mc_drake_meme():
    tag menu


    add "black"
    add "images/extended/bonus-DLC-2/mc_drake_meme.webp" xalign 0.5

    text _("Fucking\na girl") xcenter 1233 ycenter 270 style "hard_to_swallow_pills_large_text"

    text _("Fucking\na catgirl") xcenter 1250 ycenter 810 style "hard_to_swallow_pills_large_text"

    button:
        action ShowMenu("extra", 7)



screen hard_to_swallow_pills_meme():
    tag menu


    add "black"
    add "images/extended/bonus-DLC-2/hard_to_swallow_pills.webp" xalign 0.5

    text _("Hard to\nswallow\npills") xalign 0.48 yalign 0.23 style "hard_to_swallow_pills_text"

    text _("He will never\nrun out of pee") xalign 0.5 yalign 0.78 style "hard_to_swallow_pills_large_text"

    button:
        action ShowMenu("extra", 7)

style hard_to_swallow_pills_text:
    size 50
    font "fonts/Oswald-Regular.ttf"
    color "#000"
    outlines [(2, "#fff", 0, 0)]
    text_align 0.5
    line_spacing -15
    kerning 1
    xanchor 0.5
    xpos 1535
    ypos 400

style hard_to_swallow_pills_large_text:
    size 70
    font "fonts/Oswald-Regular.ttf"
    color "#000"
    outlines [(2, "#fff", 0, 0)]
    text_align 0.5
    line_spacing -15
    kerning 1
    xanchor 0.5
    xpos 1535
    ypos 400



screen choo_choo_meme():
    tag menu


    add "black"
    add "images/extended/bonus-DLC-2/choo_choo_meme.webp" xalign 0.5

    text _("NEXT STOP") xalign 0.5 yalign 0.47 style "bonus_cherry_popped_text_big"

    text _("PENETRATION STATION") xalign 0.5 yalign 0.999 style "bonus_cherry_popped_text_big"

    button:
        action ShowMenu("extra", 8)



screen londyn_twice_meme():
    tag menu


    add "black"
    add "images/extended/bonus-DLC-2/londyn_twice_meme.webp" xalign 0.5

    text _("They don't know that\nI appear in two endings") xcenter 1050 yalign 0.07 style "hard_to_swallow_pills_text"

    button:
        action ShowMenu("extra", 8)



image gigachad_mc_meme = Composite(
    (1920, 1080),
    (0, 0), "black",
    (478, 0), "gigachad_mc"
    )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
