label prologue_fresh_start:


    $ mcname                    = __("Mike")
    $ mclogin                   = __("Not_Mike")


    $ date_arj                  = True
    $ date_sy                   = False
    $ date_pw                   = False
    $ date_vw                   = False
    $ date_cb                   = False
    $ date_jf                   = False
    $ date_mes                  = False
    $ date_mh                   = False
    $ date_op                   = False
    $ date_mk                   = False
    $ date_dd                   = False
    $ date_dw                   = False
    $ date_ir                   = False
    $ date_hr                   = False
    $ date_nr                   = False
    $ date_cl                   = False
    $ date_ah                   = False
    $ date_aw                   = False
    $ date_jdg                  = False


    $ fl_cumshot                = False
    $ fl_creampie               = False
    $ fl_enema                  = False
    $ fl_watersports            = False
    $ fl_footfetish             = False
    $ fl_cumgarnish             = False
    $ fl_fisting                = False
    $ temp_anal                 = False
    $ temp_pegging              = False
    $ temp_scat                 = False
    $ fl_trans                  = False


    $ date_arj_romance          = True
    $ date_arj_sexslave         = False
    $ date_mh_bdsm              = False
    $ date_nk_preg              = False
    $ pete_ntr                  = False
    $ d12s02_gavepass           = False
    $ d13s08_keep_shoe_cum      = False
    $ d14s03_arj_kiss           = False
    $ d14s16_love_lc            = False
    $ d14s19_everything         = False

    $ quick_menu                = False
    $ date_mes_info             = False
    $ date_mh_info              = False

    call hide_fl_points_overlay from _call_hide_fl_points_overlay

    jump prologue_intro

label prologue_intro:

    scene black
    queue music fl_w3_questionnaire_soundtrack
    call screen prologue_intro()

    jump prologue_fl_name

label prologue_fl_name:

    scene black
    call screen prologue_fl_name()

    jump prologue_intro_done

label prologue_intro_done:

    $ mcname = mcname.strip().title()
    $ mclogin = mclogin.strip().title()

    if not mcname:
        $ mcname="Mike"

    if not mclogin:
        $ mclogin = __("Not_") + mcname

    jump prologue_fetishes

label prologue_fetishes:

    scene black
    call screen prologue_fetishes_choose()

    jump prologue_girls_1

label prologue_girls_1:

    scene black
    call screen prologue_girls_1(1)

    jump prologue_questions_1

label prologue_questions_1:

    if not date_mes:
        $ date_cl = False

    if not date_mk:
        $ date_ah = False

    if not date_mh:
        $ date_op = False

    scene black
    call screen prologue_questions_1()

    jump prologue_girls_2

label prologue_girls_2:

    scene black
    call screen prologue_girls_2(2)

    jump prologue_girls_3

label prologue_girls_3:

    scene black
    call screen prologue_girls_3(3)

    jump prologue_questions_2

label prologue_questions_2:

    if date_sy or date_vw or date_pw or date_dw or date_hr:
        scene black
        call screen prologue_questions_2()

    jump prologue_finalize

label prologue_finalize:

    $ prologue_set_variables()
    stop music fadeout 3.0

    jump d15s00



label prologue_from_week_2:

    call hide_fl_points_overlay from _call_hide_fl_points_overlay_1

    $ prologue_import()

    if is_debug:
        $ debug_mp_importing()
    stop music fadeout 3.0

    jump d15s00

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
