init:
    transform gallery_tr_vertical:
        subpixel True
        yalign 1.0
        linear 5.0 yalign 0.0

init python:













    cg_gallery_slots = []

    main_game_cg_slots = [
        ( "d15s01"    , _("Day 15: AmRose"               ), _(""                                         ) ),
        ( "d15s04dw"  , _("Day 15: Dahlia & Samiya"      ), _(""                                         ) ),
        ( "d15s04dd"  , _("Day 15: Daisy"                ), _(""                                         ) ),
        ( "d15s06"    , _("Day 15: Lyssa"                ), _("Express your love"                        ) ),
        ( "d15s08"    , _("Day 15: Girls"                ), _(""                                         ) ),

        ( "d16s02"    , _("Day 16: AmRose"               ), _(""                                         ) ),
        ( "d16s03"    , _("Day 16: Lydia"                ), _(""                                         ) ),
        ( "d16s05"    , _("Day 16: Stacy"                ), _(""                                         ) ),
        ( "d16s05p"   , _("Day 16: Stacy Washroom"       ), _("Ask for photos"                           ) ),
        ( "d16s06"    , _("Day 16: Allison"              ), _("Don't remove cock cage before this scene" ) ),
        ( "d16s07"    , _("Day 16: Jessie & Kanya"       ), _(""                                         ) ),

        ( "d17s02"    , _("Day 17: Vanessa"              ), _(""                                         ) ),
        ( "d17s03"    , _("Day 17: Iona"                 ), _(""                                         ) ),
        ( "d17s05"    , _("Day 17: Lyssa"                ), _("Bring Stacy with you"                     ) ),
        ( "d17s06dd"  , _("Day 17: Daisy"                ), _(""                                         ) ),
        ( "d17s06dw"  , _("Day 17: Dahlia & Samiya"      ), _(""                                         ) ),
        ( "d17s06pn"  , _("Day 17: Polly & Nora"         ), _(""                                         ) ),
        ( "d17s07"    , _("Day 17: Jessie"               ), _(""                                         ) ),

        ( "d18s05"    , _("Day 18: Dahlia & Samiya"      ), _(""                                         ) ),
        ( "d18s08"    , _("Day 18: Cynthia"              ), _(""                                         ) ),

        ( "d19s01ntr" , _("Day 19: Lydia's Dungeon"      ), _(""                                         ) ),
        ( "d19s03"    , _("Day 19: Stacy & Lyssa"        ), _(""                                         ) ),
        ( "d19s04dd"  , _("Day 19: Daisy"                ), _("You need to date Dahlia"                  ) ),
        ( "d19s04dw"  , _("Day 19: Dahlia"               ), _("You need to date Daisy"                   ) ),
        ( "d19s08sy"  , _("Day 19: Stacy"                ), _(""                                         ) ),
        ( "d19s08mh"  , _("Day 19: Lyssa"                ), _(""                                         ) ),

        ( "d20s01"    , _("Day 20: Stacy & AmRose"       ), _(""                                         ) ),
        ( "d20s05"    , _("Day 20: Min"                  ), _(""                                         ) ),

        ( "d21s02"    , _("Day 21: Stacy"                ), _("Bring Stacy with you"                     ) ),
        ( "d21s04"    , _("Day 21: Lyssa"                ), _(""                                         ) ),
        ( "d21s06"    , _("Day 21: Min"                  ), _("Unlock Waterfall Ending"                  ) ),
        ]

    cg_gallery_slots.extend(main_game_cg_slots)

    ending_01_cg_slots = [
        ( "e01s02"    , _("Ending 01: Stacy"             ), _(""                                         ) ),
        ]

    ending_02_cg_slots = [
        ( "e02s04"    , _("Ending 02: Lyssa"             ), _(""                                         ) ),
        ( "e02s05"    , _("Ending 02: Lyssa"             ), _("Spend time with everyone"                 ) ),
        ( "e02s09"    , _("Ending 02: Lyssa"             ), _(""                                         ) ),
        ]

    ending_06_cg_slots = [
        ( "e06s01"    , _("Ending 06: Lydia"             ), _(""                                         ) ),
        ( "e06s04"    , _("Ending 06: Harem"             ), _(""                                         ) ),
        ( "e06s07"    , _("Ending 06: Marriage"          ), _(""                                         ) ),
        ]

    ending_08_cg_slots = [
        ( "e08s01"    , _("Ending 08: AmRose"            ), _(""                                         ) ),
        ( "e08s07"    , _("Ending 08: AmRose & Stacy"    ), _(""                                         ) ),
        ]

    ending_10_cg_slots = [
        ( "e10s03"    , _("Ending 10: Min"               ), _(""                                         ) ),
        ( "e10s04"    , _("Ending 10: Min"               ), _(""                                         ) ),
        ]

    ending_11_cg_slots = [
        ]

    ending_12_cg_slots = [
        ( "e12s01"    , _("Ending 12: Vanessa & Allison" ), _(""                                         ) ),
        ]

    ending_13_cg_slots = [
        ( "e13s01"    , _("Ending 13: Nora"              ), _(""                                         ) ),
        ( "e13s02"    , _("Ending 13: Pregnant Nora"     ), _(""                                         ) ),
        ]

    ending_14_cg_slots = [
        ( "e14s01"    , _("Ending 14: Polly & Nora"      ), _(""                                         ) ),
        ]

    ending_17_cg_slots = [
        ]














    cg_gallery = FLGallery()
    cg_gallery.transition = dissolve
    cg_gallery.navigation = True
    cg_gallery.locked_button = "gallery_locked_button"


    cg_gallery.button("d15s01")
    cg_gallery.unlock_image("d15s01-99-26 shower-2-arj-enters_c2")
    cg_gallery.unlock_image("d15s01-99-28 shower-4-talk-1_c3")
    cg_gallery.unlock_image("d15s01-99-31 shower-4-talk-4_c2")

    cg_gallery.button("d15s04dw")
    cg_gallery.unlock_image("d15s04a-03 mc-dw-come-in_c2")
    cg_gallery.image("d15s04a-09 mc-dw-sb-samiya-surprise_c1")

    cg_gallery.button("d15s04dd")
    cg_gallery.unlock_image("d15s04-71-mc-looking-at-dd")
    cg_gallery.unlock_image("d15s04-73-dd-talking-with-mc")

    cg_gallery.button("d15s06")
    cg_gallery.image("d15s06-10_mc_mh_montage")
    cg_gallery.unlock_image("d15s06-15_mc_mh_cookingmontage")

    cg_gallery.button("d15s08")
    cg_gallery.unlock_image("d15s08-03 mc-hr-sy-arj-talking")
    cg_gallery.unlock_image("d15s08-13 mc-hr-sy-arj-talking")
    cg_gallery.unlock_image("d15s08-19 mc-hr-sy-arj-talking")

    cg_gallery.button("d16s02")
    cg_gallery.unlock_image("d16s02-07-02 mc-arj-entrance-talk2_c2")
    cg_gallery.unlock_image("d16s02-07-03 mc-arj-entrance-talk3_c2")

    cg_gallery.button("d16s03")
    cg_gallery.unlock_image("d16s03-97 mc-lc-sit-up-talk-alt-pose-5-c1")

    cg_gallery.button("d16s05")
    cg_gallery.unlock_image("d16s05-07-2 mc-sy-talk5_c1")
    cg_gallery.unlock_image("d16s05-08-2 mc-sy-toilet2_c2")

    cg_gallery.button("d16s05p")
    cg_gallery.unlock_image("d16s05-62 sy-toilet1_c1")
    cg_gallery.unlock_image("d16s05-62 sy-toilet1_c2")

    cg_gallery.button("d16s06")
    cg_gallery.unlock_image("d16s06-05 mc-aw-alisson-dorm_c1")
    cg_gallery.unlock_image("d16s06-06 mc-aw-closing-laptop_c1")
    cg_gallery.unlock_image("d16s06-48 mc-aw-preping-stream_c1")
    cg_gallery.unlock_image("d16s06-07 mc-aw-greeting_c1")

    cg_gallery.button("d16s07")
    cg_gallery.unlock_image("d16s07-14 mc_jf_kv_zebra_sex_with_jessie")
    cg_gallery.unlock_image("d16s07-68 mc_jf_kv_zebra_sex_with_jessie")
    cg_gallery.unlock_image("d16s07-79 mc_jf_kv_zebra_sex_with_jessie")
    cg_gallery.unlock_image("d16s07-83 mc_jf_kv_zebra_sex_with_jessie")
    cg_gallery.unlock_image("d16s07-106 mc_jf_kv_zebra_sex_with_jessie")
    cg_gallery.unlock_image("d16s07-110-2 mc_jf_kv_zebra_sex_with_jessie")

    cg_gallery.button("d17s02")
    cg_gallery.unlock_image("d17s02-05 vw-photo-02")
    cg_gallery.unlock_image("d17s02-04 vw-photo-01-alt-opening")

    cg_gallery.button("d17s03")
    cg_gallery.unlock_image("d17s03-03-ir-talk-mc")
    cg_gallery.unlock_image("d17s03-12-ir-talk-mc")
    cg_gallery.unlock_image("d17s03-20-ir-talk-mc")
    cg_gallery.unlock_image("d17s03-24-ir-talk-mc")
    cg_gallery.unlock_image("d17s03-56-ir-talk-mc")

    cg_gallery.button("d17s05")
    cg_gallery.unlock_image("d17s05-01-lh-on-phone")
    cg_gallery.unlock_image("d17s05-02-lh-on-phone-close-up")
    cg_gallery.unlock_image("d17s05-03-lh-on-phone-alt-angle")
    cg_gallery.unlock_image("d17s05-15-sy-mh-stacy-lyssa")
    cg_gallery.unlock_image("d17s05-23-sy-mh-stacy-lyssa")

    cg_gallery.button("d17s06dd")
    cg_gallery.unlock_image("d17s06a-03-dd-smiles")
    cg_gallery.unlock_image("d17s06a-14-dd-talking-with-mc")
    cg_gallery.unlock_image("d17s06a-17-dd-talking-with-mc")
    cg_gallery.unlock_image("d17s06a-32-dd-talking-with-mc")
    cg_gallery.unlock_image("d17s06a-57-dd-talking-with-mc")
    cg_gallery.unlock_image("d17s06a-63-dd-talking-with-mc")

    cg_gallery.button("d17s06dw")
    cg_gallery.unlock_image("d17s06-09 mc-sd-dw-dialog-amusement-park_c5")
    cg_gallery.unlock_image("d17s06-11 mc-sd-dw-dialog-amusement-park_c6")
    cg_gallery.unlock_image("d17s06-15 mc-sd-dw-dialog-amusement-park_c4")
    cg_gallery.unlock_image("d17s06-20 mc-sd-dw-dialog-amusement-park_c4")

    cg_gallery.button("d17s06pn")
    cg_gallery.unlock_image("d17s06-07 pw-nk-heroine-poses_c1")
    cg_gallery.unlock_image("d17s06-09 pw-heroine-pose_c1")
    cg_gallery.unlock_image("d17s06-08 nk-heroine-pose_c1")

    cg_gallery.button("d17s07")
    cg_gallery.unlock_image("d17s07-06 mc_jf_breeding_ponies")
    cg_gallery.unlock_image("d17s07-09 mc_jf_breeding_ponies")

    cg_gallery.button("d18s05")
    cg_gallery.unlock_image("d18s05-12-sb-sits-talk-pb")
    cg_gallery.unlock_image("d18s05-29-sb-talk-mc")
    cg_gallery.unlock_image("d18s05-60-dw-talk-mc-sb")
    cg_gallery.unlock_image("d18s05-70-dw-talk-mc")

    cg_gallery.button("d18s08")
    cg_gallery.unlock_image("d18s08-08 tl-slaps-cl-again_c1")
    cg_gallery.unlock_image("d18s08-07 slap-noise-tl-screams-at-cl_c1")
    cg_gallery.unlock_image("d18s08-09-1 tl-asks-whos-there_c1")
    cg_gallery.unlock_image("d18s08-12 cl-covering-ass_c1")
    cg_gallery.unlock_image("d18s08_slap_1")
    cg_gallery.unlock_image("d18s08_slap_2")

    cg_gallery.button("d19s01ntr")
    cg_gallery.unlock_image("d19s01ntr-a11-2 glambot-11-2-00_i")
    cg_gallery.unlock_image("d19s01ntr-17 mc_lc_pd_ntr_lydias_dungeon")
    cg_gallery.unlock_image("d19s01ntr-22 mc_lc_pd_ntr_lydias_dungeon")
    cg_gallery.unlock_image("d19s01ntr-31 mc_lc_pd_ntr_lydias_dungeon")
    cg_gallery.unlock_image("d19s01ntr-32 mc_lc_pd_ntr_lydias_dungeon")

    cg_gallery.button("d19s03")
    cg_gallery.unlock_image("d19s03-03 sy-asks-who-knocks-mh-answers_c1")
    cg_gallery.unlock_image("d19s03-05 sy-opens-door-mh-other-side_c1")
    cg_gallery.unlock_image("d19s03-06 sy-mh-cheek-kiss_c1")

    cg_gallery.button("d19s04dd")
    cg_gallery.unlock_image("d19s04-12 dd-take-off-pants-daisy-close-up")
    cg_gallery.unlock_image("d19s04-27 dd-can-i-join")
    cg_gallery.unlock_image("d19s04-73 dd-after-fade-daisy-resting-eyes")

    cg_gallery.button("d19s04dw")
    cg_gallery.unlock_image("d19s04-dd-66 dw-talk-dd-mc")
    cg_gallery.unlock_image("d19s04-dd-69 dw-talk-mc")
    cg_gallery.unlock_image("d19s04-dd-124 dw-smirk-mc")

    cg_gallery.button("d19s08sy")
    cg_gallery.unlock_image("d19s08-06 sy-taking-shower-startled_c1")
    cg_gallery.unlock_image("d19s08-08 sy-not-happy-mc-walked-in-apartment_c1")
    cg_gallery.unlock_image("d19s09-01 sy-out-of-shower_c1")
    cg_gallery.unlock_image("d19s09-05 sy-tongue-out_c1")
    cg_gallery.unlock_image("d19s09-05-01 sy-dims-lights_c1")

    cg_gallery.button("d19s08mh")
    cg_gallery.image("d19s08-17 mh-lounge-eating-fruit_c1")
    cg_gallery.image("d19s08-19 mh-talking-smiling_c1")
    cg_gallery.image("d19s08-23 mh-turns-sideways-hand-between-thighs_c1")
    cg_gallery.image("d19s08-30 mh-agrees-to-send-later_c1")
    cg_gallery.image("d19s08-33 mh-talking-phone-looking-nails_c1")
    cg_gallery.image("d19s09-mh-anim")

    cg_gallery.button("d20s01")
    cg_gallery.unlock_image("d20s1-01 mc-arj-sy-room-walkup1_c1_i")
    cg_gallery.unlock_image("d20s1-07 sy-bathroom1_c1_i")
    cg_gallery.unlock_image("d20s1-12 mc-sy-arj-bathroom-entry_c3_i")
    cg_gallery.unlock_image("d20s1-13 mc-sy-arj-bathroom-entry2_c4_i")

    cg_gallery.button("d20s05")
    cg_gallery.unlock_image("d20s05-02 mc-mes-talking")
    cg_gallery.unlock_image("d20s05-17 mes-sexy-outfit")
    cg_gallery.unlock_image("d20s05-20 mc-mes-shush")
    cg_gallery.unlock_image("d20s05-21 mes-dancing")
    cg_gallery.unlock_image("d20s05-24 mc-mes-stripping")
    cg_gallery.unlock_image("d20s05-24-02 mes-stripping")
    cg_gallery.unlock_image("d20s05-24-04 mes-stripping")
    cg_gallery.unlock_image("d20s05-24-06 mc-mes-stripping")

    cg_gallery.button("d21s02")
    cg_gallery.unlock_image("d21s02-24 sy-talking")
    cg_gallery.unlock_image("d21s02-75-07 mc-sy-ly-talking-lc")
    cg_gallery.unlock_image("d21s02-75-08 mc-sy-ly-talking-lc")

    cg_gallery.button("d21s04")
    cg_gallery.unlock_image("d21s04-02-mh-close-up")
    cg_gallery.unlock_image("d21s04-05-mh-talk-mc")
    cg_gallery.unlock_image("d21s04-46-mh-talk-mc")
    cg_gallery.unlock_image("d21s04-70-mh-talk-mc")

    cg_gallery.button("d21s06")
    cg_gallery.unlock_image("d21s06-75 min-waterfall2_c1")
    cg_gallery.unlock_image("d21s06-76 min-waterfall3_c1")
    cg_gallery.unlock_image("d21s06-77 min-waterfall6_c1")
    cg_gallery.unlock_image("d21s06-78 min-waterfall4_c1")
    cg_gallery.unlock_image("d21s06-79 min-waterfall5_c1")
    cg_gallery.unlock_image("d21s06-82 min-waterfall8_c1")

    cg_gallery.button("e01s02")
    cg_gallery.unlock_image("e01s02-29 mc-sy-talking")
    cg_gallery.unlock_image("e01s02-41 mc-sy-talking")
    cg_gallery.unlock_image("e01s02-47 mc-sy-talking")

    cg_gallery.button("e02s04")
    cg_gallery.unlock_image("e02s04-50 mc-mh-sleep1_c1")
    cg_gallery.unlock_image("e02s04-50 mc-mh-sleep1_c2")
    cg_gallery.unlock_image("e02s04-59 mc-mh-kiss_c2")
    cg_gallery.unlock_image("e02s04-59 mc-mh-kiss_c3")
    cg_gallery.unlock_image("e02s04-59-2 mc-mh-getup_c2")

    cg_gallery.button("e02s05")
    cg_gallery.unlock_image("e02s05-01 mc-mh-sex1_c1")
    cg_gallery.unlock_image("e02s05-01 mc-mh-sex1_c2")
    cg_gallery.unlock_image("e02s05-01 mc-mh-sex1_c3")
    cg_gallery.unlock_image("e02s05-02 mc-mh-getup_c1")
    cg_gallery.unlock_image("e02s05-02-2 mc-mh-getup2_c1")
    cg_gallery.unlock_image("e02s05-24 mc-mh-bed1_c2")
    cg_gallery.unlock_image("e02s05-24-2 mc-mh-bed2_c1")
    cg_gallery.unlock_image("e02s05-30 mc-mh-tub1_c3")
    cg_gallery.unlock_image("e02s05-31 mc-mh-tub2_c3")

    cg_gallery.button("e02s09")
    cg_gallery.unlock_image("e02s09-47 later-bedroom-mh-enters-mc-chilling-bed_c1")
    cg_gallery.unlock_image("e02s09-49 mh-undress_c1")
    cg_gallery.unlock_image("e02s09-50 mh-waited-all-day-climbs-bed_c1")
    cg_gallery.image("e02s09-51 mh-hesitant-mc-thinks-not-sounding-like-mh_c1")
    cg_gallery.unlock_image("e02s09-53 mh-mc-kiss_c1")
    cg_gallery.unlock_image("e02s09-54 mc-surprised-mh-feels-embarrassed_c1")
    cg_gallery.unlock_image("e02s09-55 mc-lays-mh-down-wants-speak-him-she-sniffs_c1")
    cg_gallery.unlock_image("e02s09-57 mh-tells-mc-been-patient-mc-not-about-change_c1")
    cg_gallery.unlock_image("e02s09-64 mc-mh-sleep-cuddled_c1")

    cg_gallery.button("e06s01")
    cg_gallery.unlock_image("e06s01-14-2 mc-lc-talk12_c2")
    cg_gallery.unlock_image("e06s01-15 mc-lc-reentry1_c2")
    cg_gallery.image("e06s01-28 mc-lc-front4_c2")

    cg_gallery.button("e06s04")
    cg_gallery.unlock_image("e06s04-01-lc-phone")
    cg_gallery.unlock_image("e06s04-03-lc-talk-mc")
    cg_gallery.unlock_image("e06s04-23-mes-pool")
    cg_gallery.unlock_image("e06s04-24-mes-talk-mc")
    cg_gallery.unlock_image("e06s04-25-mes-pool")
    cg_gallery.unlock_image("e06s04-44-mes-notice-arj-sy")
    cg_gallery.unlock_image("e06s04-46-arj-talk-sy")
    cg_gallery.unlock_image("e06s04-47-sy-talks")
    cg_gallery.unlock_image("e06s04-49-mes-talk-arj")
    cg_gallery.unlock_image("e06s04-121-mes-talk-lc")

    cg_gallery.button("e06s07")
    cg_gallery.unlock_image("e06s07-13 sy-at-door-asks-mc-last-regrets-pov_c1")
    cg_gallery.unlock_image("e06s07-22 mes-listens-lc-vow_c1")
    cg_gallery.unlock_image("e06s07-23 arj-listens-lc-vow_c1")
    cg_gallery.unlock_image("e06s07-24 dd-listens-to-vows_c1")
    cg_gallery.unlock_image("e06s07-25 sy-listens-lc-vow_c1")
    cg_gallery.unlock_image("e06s07-52 mh-agrees-as-well_c1")
    cg_gallery.unlock_image("e06s07-62 lc-mh-hold-hands-as-mh-forgot-detail_c1")

    cg_gallery.button("e08s01")
    cg_gallery.unlock_image("e8s01-07-02 amr-look-up")
    cg_gallery.unlock_image("e8s01-76 amr-mc-rmy-change-clothes-table")
    cg_gallery.unlock_image("e8s01-84 amr-rmy-come-back")
    cg_gallery.unlock_image("e8s01-95 amr-talk-alt-amr")

    cg_gallery.button("e08s07")
    cg_gallery.unlock_image("e08s07-04 arj-enters-livingroom-joins-mc_c1")
    cg_gallery.image("e08s07-11 sy-waiting-outside-door_c1")
    cg_gallery.image("e08s07-12 sy-says-hey-she-is-happy_c1")
    cg_gallery.unlock_image("e08s07-20 arj-leans-puts-arm-sy-shoulder_c1")
    cg_gallery.unlock_image("e08s07-43 mc-arj-showing-sy-farm-three_c1")
    cg_gallery.unlock_image("e08s07-44 sy-mc-arj-selfie_c1")
    cg_gallery.unlock_image("e08s07-49 sy-leans-over-produce_c1")

    cg_gallery.button("e10s03")
    cg_gallery.unlock_image("e10s03-21 mc-mes-getting-dressed_c2")
    cg_gallery.unlock_image("e10s03-20 mc-wake-up-couch-naked_c1")
    cg_gallery.unlock_image("e10s03-29-12 mc-mes-min-door-talk_c1")

    cg_gallery.button("e10s04")
    cg_gallery.unlock_image("e10s04-06 mes-not-sure-why-thats-con_c1")
    cg_gallery.unlock_image("e10s04-14 mes-asking-mc-if-he-wants-abandon-studies_c1")
    cg_gallery.unlock_image("e10s04-34 mes-asking-what-mc-doing_c1")
    cg_gallery.unlock_image("e10s04-52 mc-mes-both-laugh_c1")
    cg_gallery.unlock_image("e10s04-54 mc-kisses-mes_c1")

    cg_gallery.button("e12s01")
    cg_gallery.unlock_image("e12s03-24 aw-shows-pool_c1")
    cg_gallery.unlock_image("e12s03-42 vw-plenty-time-teach-mc-ask-that-bad_c1")
    cg_gallery.unlock_image("e12s03-59 mc-vw-stand-next-aw-mc-agrees-vw-confirms_c1")
    cg_gallery.unlock_image("e12s06-68 aw-thanking-vanessa")
    cg_gallery.image("e12s06-87 vw-undress-full-shot")
    cg_gallery.unlock_image("e12s07-105-mc-aw-vw-on-the-swing")

    cg_gallery.button("e13s01")
    cg_gallery.image("e13s01-26 nk-construction-window_c22")
    cg_gallery.unlock_image("e13s01-46 mc-nk-construction-rest_c10")

    cg_gallery.button("e13s02")
    cg_gallery.unlock_image("e13s02-03-nk-cleaning")
    cg_gallery.unlock_image("e13s02-06-nk-look-jim")
    cg_gallery.unlock_image("e13s02-15-nk-talk-mc")
    cg_gallery.unlock_image("e13s02-17-nk-talk-mc")

    cg_gallery.button("e14s01")
    cg_gallery.unlock_image("e13s01-03 mc-pw-nk-construction_c5")
    cg_gallery.unlock_image("e14s02-60 pw-ask-remember-time-fuck-pussy-mc-struggles-answers_c1")
    cg_gallery.unlock_image("e14s02-63 nk-gets-hot-wants-calm-down-pw-good-mc-ugh_c1")
    cg_gallery.unlock_image("e14s02-65 new-customer-walks-in_c1")
    cg_gallery.unlock_image("e14s07-115 all-do-yoga-end-scene_c1")

    for i in cg_gallery_slots:
        renpy.image("gallery_tncg_" + i[0], Image("images/extended/cg/" + i[0] + ".webp"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
