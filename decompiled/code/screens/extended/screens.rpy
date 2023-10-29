

default vu_ad_hover = False
default persistent.seen_lc_song_p1 = False
default persistent.seen_lc_song_p2 = False
default main_menu_bg = "main"
default sm_play_bg = "idle"
default sm_bonus_bg = "idle"

image vu_ad_patreon_wc_emblem = ConditionSwitch(
    "vu_ad_hover == False", "images/extended/ui/buttons/vu_ad_patreon_wc_idle.webp",
    "vu_ad_hover == True", "images/extended/ui/buttons/vu_ad_patreon_wc_hover.webp",
    predict_all = True,
    )

image vu_ad_patreon_tf_emblem = ConditionSwitch(
    "vu_ad_hover == False", "images/extended/ui/buttons/vu_ad_patreon_tf_idle.webp",
    "vu_ad_hover == True", "images/extended/ui/buttons/vu_ad_patreon_tf_hover.webp",
    predict_all = True,
    )

image vu_ad_patreon_cn_emblem = ConditionSwitch(
    "vu_ad_hover == False", "images/extended/ui/buttons/vu_ad_patreon_cn_idle.webp",
    "vu_ad_hover == True", "images/extended/ui/buttons/vu_ad_patreon_cn_hover.webp",
    predict_all = True,
    )

image vu_ad_patreon_anim:
    subpixel True
    "vu_ad_patreon_wc_emblem" with Dissolve (0.5, alpha=True)
    linear 1.0 zoom 0.95
    linear 1.0 zoom 1.0
    "vu_ad_patreon_tf_emblem" with Dissolve (0.5, alpha=True)
    linear 1.0 zoom 0.95
    linear 1.0 zoom 1.0
    "vu_ad_patreon_cn_emblem" with Dissolve (0.5, alpha=True)
    linear 1.0 zoom 0.95
    linear 1.0 zoom 1.0
    repeat

image vu_ad_wc_emblem = ConditionSwitch(
    "vu_ad_hover == False", "images/extended/ui/buttons/vu_ad_wc_idle.webp",
    "vu_ad_hover == True", "images/extended/ui/buttons/vu_ad_wc_hover.webp",
    predict_all = True,
    )

image vu_ad_tf_emblem = ConditionSwitch(
    "vu_ad_hover == False", "images/extended/ui/buttons/vu_ad_tf_idle.webp",
    "vu_ad_hover == True", "images/extended/ui/buttons/vu_ad_tf_hover.webp",
    predict_all = True,
    )

image vu_ad_cn_emblem = ConditionSwitch(
    "vu_ad_hover == False", "images/extended/ui/buttons/vu_ad_cn_idle.webp",
    "vu_ad_hover == True", "images/extended/ui/buttons/vu_ad_cn_hover.webp",
    predict_all = True,
    )

image vu_ad_anim:
    subpixel True
    "vu_ad_wc_emblem" with Dissolve (0.5, alpha=True)
    linear 1.0 zoom 0.95
    linear 1.0 zoom 1.0
    "vu_ad_tf_emblem" with Dissolve (0.5, alpha=True)
    linear 1.0 zoom 0.95
    linear 1.0 zoom 1.0
    "vu_ad_cn_emblem" with Dissolve (0.5, alpha=True)
    linear 1.0 zoom 0.95
    linear 1.0 zoom 1.0
    repeat

image main_menu_background = ConditionSwitch(
    "main_menu_bg == 'main'", "images/extended/ui/mm_bg_main.webp",
    "main_menu_bg == 'play'", "images/extended/ui/mm_bg_play.webp",
    "main_menu_bg == 'load'", "images/extended/ui/mm_bg_load.webp",
    "main_menu_bg == 'bonus'", "images/extended/ui/mm_bg_bonus.webp",
    "main_menu_bg == 'settings'", "images/extended/ui/mm_bg_settings.webp",
    "main_menu_bg == 'translate'", "images/extended/ui/mm_bg_translate.webp",
    "main_menu_bg == 'info'", "images/extended/ui/mm_bg_info.webp",
    "main_menu_bg == 'lc'", "images/extended/ui/mm_bg_lc.webp",
    predict_all = True,
    )

image sub_menu_play_bg = ConditionSwitch(
    "sm_play_bg == 'idle'", "images/extended/ui/sm_play_idle.webp",
    "sm_play_bg == 'one'", "images/extended/ui/sm_play_one.webp",
    "sm_play_bg == 'two'", "images/extended/ui/sm_play_two.webp",
    predict_all = True,
    )

image sub_menu_bonus_bg_left = ConditionSwitch(
    "sm_bonus_bg == 'idle'", "images/extended/ui/sm_bonus_idle_left.webp",
    "sm_bonus_bg == 'one'", "images/extended/ui/sm_bonus_one_left.webp",
    "sm_bonus_bg == 'two'", "images/extended/ui/sm_bonus_two_left.webp",
    "sm_bonus_bg == 'three'", "images/extended/ui/sm_bonus_three_left.webp",
    "sm_bonus_bg == 'four'", "images/extended/ui/sm_bonus_four_left.webp",
    predict_all = True,
    )

image sub_menu_bonus_bg_right = ConditionSwitch(
    "sm_bonus_bg == 'idle'", "images/extended/ui/sm_bonus_idle_right.webp",
    "sm_bonus_bg == 'one'", "images/extended/ui/sm_bonus_one_right.webp",
    "sm_bonus_bg == 'two'", "images/extended/ui/sm_bonus_two_right.webp",
    "sm_bonus_bg == 'three'", "images/extended/ui/sm_bonus_three_right.webp",
    "sm_bonus_bg == 'four'", "images/extended/ui/sm_bonus_four_right.webp",
    predict_all = True,
    )

screen main_menu_extended():

    add "main_menu_background"

    frame:
        style_prefix "ext_mm"
        button:
            frame:
                xpos 332
                ypos 255
                at rotate(-2.5)
                text _("PLAY")
            focus_mask "images/extended/ui/mm_bg_play_mask.webp"
            action (SetVariable("main_menu_bg", "main"), ShowMenu("sub_menu_play"))
            hovered SetVariable("main_menu_bg", "play")
            unhovered SetVariable("main_menu_bg", "main")
            activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_cube_click_bonus.mp3"

        button:
            frame:
                xpos 770
                ypos 395
                text _("LOAD")
            focus_mask "images/extended/ui/mm_bg_load_mask.webp"
            action (SetVariable("main_menu_bg", "main"), ShowMenu("load"))
            hovered SetVariable("main_menu_bg", "load")
            unhovered SetVariable("main_menu_bg", "main")

        button:
            frame:
                xpos 1502
                ypos 238
                text _("BONUS")
            focus_mask "images/extended/ui/mm_bg_bonus_mask.webp"
            action (SetVariable("main_menu_bg", "main"), ShowMenu("sub_menu_bonus"))
            hovered SetVariable("main_menu_bg", "bonus")
            unhovered SetVariable("main_menu_bg", "main")
            activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_cube_click_bonus.mp3"

        button:
            frame:
                xpos 197
                ypos 872
                text _("SETTINGS")
            focus_mask "images/extended/ui/mm_bg_settings_mask.webp"
            action (SetVariable("main_menu_bg", "main"), ShowMenu("preferences"))
            hovered SetVariable("main_menu_bg", "settings")
            unhovered SetVariable("main_menu_bg", "main")

        button:
            frame:
                xpos 846
                ypos 892
                text _("LANGUAGE")
            focus_mask "images/extended/ui/mm_bg_translate_mask.webp"
            action (SetVariable("main_menu_bg", "main"), ShowMenu("language_chooser"))
            hovered SetVariable("main_menu_bg", "translate")
            unhovered SetVariable("main_menu_bg", "main")

        button:
            frame:
                xpos 1482
                ypos 893
                text _("INFO")
            focus_mask "images/extended/ui/mm_bg_info_mask.webp"
            action (SetVariable("main_menu_bg", "main"), ShowMenu("sub_menu_info"))
            hovered SetVariable("main_menu_bg", "info")
            unhovered SetVariable("main_menu_bg", "main")
            activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_cube_click_bonus.mp3"

    if persistent.seen_lc_song_p1 is True and persistent.seen_lc_song_p2 is True:
        button:
            focus_mask "images/extended/ui/mm_bg_lc_mask.webp"
            action (SetVariable("main_menu_bg", "main"), Function(fl_achievement_unlock, "d21s25n01"), Function(unlock_gallery_slot, "extra", "d21s25n01"), ShowMenu("jump_replay"))
            hovered SetVariable("main_menu_bg", "lc")
            unhovered (SetVariable("main_menu_bg", "main"), Play("sound", "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_lydia_zip_out.mp3"))
            hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_lydia_zip_in.mp3"

    if preferences.get_volume("music") != 0.0:
        add "fl_logo_eq_effect" xpos 640 ypos 83 at image_opacity(0.6)

    vbox:
        xalign 0.995
        yalign 0.999
        yanchor 1.0
        spacing -10
        if not is_steam_edition:
            imagebutton auto "images/extended/ui/buttons/mm_patreon_%s.webp" focus_mask "images/extended/ui/buttons/mm_patreon_mask.webp" action OpenURL("https://www.patreon.com/fetishlocator") hovered Function(show_hover_notify, (_("Support us on Patreon"))) unhovered Function(hide_hover_notify) style "ext_mm_side"
        imagebutton auto "images/extended/ui/buttons/mm_discord_%s.webp" focus_mask "images/extended/ui/buttons/mm_quit_mask.webp" action OpenURL("https://discord.gg/efmQRNtFks") hovered Function(show_hover_notify, (_("Join us on Discord"))) unhovered Function(hide_hover_notify) style "ext_mm_side"
        imagebutton auto "images/extended/ui/buttons/mm_quit_%s.webp" focus_mask "images/extended/ui/buttons/mm_quit_mask.webp" action Quit() hovered Function(show_hover_notify, (_("Quit Game"))) unhovered Function(hide_hover_notify) style "ext_mm_side"

    vbox:
        xalign 0.015
        yalign 0.985
        style_prefix "ext_mm_version"
        if persistent.menu_hints is True:
            text "v. [config.version][persistent.mp_info] + Walkthrough DLC" at image_opacity(0.7)
        else:
            text "v. [config.version][persistent.mp_info]" at image_opacity(0.7)

    imagebutton:
        idle "images/extended/ui/lovense/lovense_max2_button_idle.webp"
        hover "images/extended/ui/lovense/lovense_max2_button_hover.webp"
        xalign 0.955
        yalign 0.23
        focus_mask True
        action (Function(hide_hover_notify), ShowMenu("lovense_sale_screen"))
        hovered Function(show_hover_notify, (_("Get a Lovense toy")))
        unhovered Function(hide_hover_notify)
        at shake_effect

    imagebutton:
        if is_steam_edition is True:
            idle "vu_ad_anim"
        else:
            idle "vu_ad_patreon_anim"
        focus_mask "images/extended/ui/buttons/vu_ad_focus_mask.webp"
        xcenter 0.07
        ycenter 0.12
        if is_steam_edition is True:
            action OpenURL("steam://openurl/https://store.steampowered.com/app/2459350/Taboo_University_Book_One/")
            hovered (ToggleVariable("vu_ad_hover"), Notify(_("Wishlist Taboo University in Steam")))
        else:
            action OpenURL("https://www.patreon.com/VinovellaGames")
            hovered (ToggleVariable("vu_ad_hover"), Notify(_("Try our new game Taboo University")))
        unhovered (ToggleVariable("vu_ad_hover"), Function(hide_hover_notify))

style ext_mm_button:
    hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_cube_hover.mp3"
    activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_cube_click_v2.mp3"

style ext_mm_frame:
    background None
    xsize 170
    ysize 70

style ext_mm_text:
    xalign 0.45
    yalign 0.6
    text_align 0.5
    size 42
    line_spacing 5
    idle_color "#FFFFFF"
    hover_color gui.accent_color
    font "fonts/new/Teko-SemiBold.ttf"

style ext_mm_version_text:
    size 30
    color "#FFFFFF"
    font gui.text_font

style ext_mm_side:
    hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_socials_hover.mp3"
    activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_socials_click.mp3"

transform rotate(rotation):
    rotate rotation

transform shake_effect:
    subpixel True xanchor 0.5 yanchor 1.0 rotate -20 zoom 0.85
    easein 0.05 rotate -25
    easein 0.1 rotate -15
    easein 0.1 rotate -25
    easein 0.1 rotate -15
    easein 0.1 rotate -25
    easein 0.1 rotate -15
    easein 0.1 rotate -25
    easein 0.1 rotate -15
    easein 0.05 rotate -20
    pause 3.0
    repeat



screen sub_menu_play():

    modal True

    add "mm_play_crush_effect"

    add "gui/overlay/confirm.png"

    fixed:
        at wait_effect

        button focus_mask "images/extended/ui/sm_play_idle_mask.webp" action (SetVariable("sm_play_bg", "idle"), Hide("sub_menu_play")) keysym ("mouseup_3", "K_ESCAPE", "K_MENU", "K_PAUSE") style "sm_return_button"

        fixed:
            style_prefix "sub_menu_play"

            at from_bottom

            add "sub_menu_play_bg"

            button:
                frame:
                    xpos 318
                    ypos 303
                    text _("ANSWER THE QUESTIONNAIRE AND START A NEW GAME")
                focus_mask "images/extended/ui/sm_play_one_mask.webp"
                action (Start(), SetVariable("sm_play_bg", "idle"), Hide("sub_menu_play"))
                hovered SetVariable("sm_play_bg", "one")
                unhovered SetVariable("sm_play_bg", "idle")

            button:
                frame:
                    xpos 1288
                    ypos 303
                    text _("LOAD A SAVE FROM WEEK 2")
                focus_mask "images/extended/ui/sm_play_two_mask.webp"
                action (ShowMenu("load_mp"), SetVariable("sm_play_bg", "idle"), Hide("sub_menu_play"))
                hovered SetVariable("sm_play_bg", "two")
                unhovered SetVariable("sm_play_bg", "idle")



screen sub_menu_info():

    modal True

    add "mm_info_crush_effect"

    add "gui/overlay/confirm.png"

    fixed:
        at wait_effect

        button focus_mask "images/extended/ui/sm_play_idle_mask.webp" action (SetVariable("sm_play_bg", "idle"), Hide("sub_menu_info")) keysym ("mouseup_3", "K_ESCAPE", "K_MENU", "K_PAUSE") style "sm_return_button"

        fixed:
            style_prefix "sub_menu_play"

            at from_bottom

            add "sub_menu_play_bg"

            button:
                frame:
                    xpos 318
                    ypos 303
                    text _("ABOUT")
                focus_mask "images/extended/ui/sm_play_one_mask.webp"
                action (ShowMenu("about"), SetVariable("sm_play_bg", "idle"), Hide("sub_menu_info"))
                hovered SetVariable("sm_play_bg", "one")
                unhovered SetVariable("sm_play_bg", "idle")

            button:
                frame:
                    xpos 1288
                    ypos 303
                    text _("HELP")
                focus_mask "images/extended/ui/sm_play_two_mask.webp"
                action (ShowMenu("help"), SetVariable("sm_play_bg", "idle"), Hide("sub_menu_info"))
                hovered SetVariable("sm_play_bg", "two")
                unhovered SetVariable("sm_play_bg", "idle")

transform from_bottom:
    subpixel True
    yalign 1.0 yanchor 0.0
    pause 0.3
    easein 0.3 yalign 0.5 yanchor 0.5
    on hide:
        easein 0.3 yalign 1.0 yanchor 0.0

style sub_menu_play_frame:
    background None
    xsize 360
    ysize 360

style sub_menu_play_text:
    xalign 0.5
    yalign 0.5
    text_align 0.5
    size 65
    idle_color "#FFFFFF"
    hover_color gui.accent_color
    font "fonts/new/Teko-SemiBold.ttf"



screen sub_menu_bonus():

    modal True

    add "mm_bonus_crush_effect"

    add "gui/overlay/confirm.png"

    fixed:
        at wait_effect

        button focus_mask "images/extended/ui/sm_bonus_idle_mask.webp" action (SetVariable("sm_bonus_bg", "idle"), Hide("sub_menu_bonus")) keysym ("mouseup_3", "K_ESCAPE", "K_MENU", "K_PAUSE") style "sm_return_button"

        fixed:
            style_prefix "sub_menu_bonus"

            at from_left

            add "sub_menu_bonus_bg_left"

            button:
                frame:
                    xpos 360
                    ypos 52
                    text _("CG\nGALLERY")
                focus_mask "images/extended/ui/sm_bonus_one_mask.webp"
                action (ShowMenu("cg_gallery"), SetVariable("sm_bonus_bg", "idle"), Hide("sub_menu_bonus"))
                hovered SetVariable("sm_bonus_bg", "one")
                unhovered SetVariable("sm_bonus_bg", "idle")

            button:
                frame:
                    xpos 360
                    ypos 625
                    text _("REPLAY ROOM")
                focus_mask "images/extended/ui/sm_bonus_two_mask.webp"
                action (ShowMenu("replay_room"), SetVariable("sm_bonus_bg", "idle"), Hide("sub_menu_bonus"))
                hovered SetVariable("sm_bonus_bg", "two")
                unhovered SetVariable("sm_bonus_bg", "idle")

        fixed:
            style_prefix "sub_menu_bonus"

            at from_right

            add "sub_menu_bonus_bg_right"

            button:
                frame:
                    xpos 1202
                    ypos 52
                    text _("BONUS CONTENT")
                focus_mask "images/extended/ui/sm_bonus_three_mask.webp"
                action (ShowMenu("extra"), SetVariable("sm_bonus_bg", "idle"), Hide("sub_menu_bonus"))
                hovered SetVariable("sm_bonus_bg", "three")
                unhovered SetVariable("sm_bonus_bg", "idle")

            button:
                frame:
                    xpos 1202
                    ypos 625
                    text _("ENDINGS")
                focus_mask "images/extended/ui/sm_bonus_four_mask.webp"
                action (ShowMenu("fl_endings"), SetVariable("sm_bonus_bg", "idle"), Hide("sub_menu_bonus"))
                hovered SetVariable("sm_bonus_bg", "four")
                unhovered SetVariable("sm_bonus_bg", "idle")

style sub_menu_play_button:
    hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_cube_hover2.mp3"
    activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"

style sub_menu_bonus_button:
    hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_cube_hover2.mp3"
    activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"

style sm_return_button:
    activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"

style sub_menu_bonus_frame:
    background None
    xsize 370
    ysize 370

style sub_menu_bonus_text:
    xalign 0.5
    yalign 0.5
    text_align 0.5
    size 80
    line_spacing 20
    idle_color "#FFFFFF"
    hover_color gui.accent_color
    font "fonts/new/Teko-SemiBold.ttf"

transform wait_effect:
    alpha 0.0
    pause 0.1
    linear 0.1 alpha 1.0

transform from_left:
    subpixel True
    xalign 0.0 xanchor 1.0
    pause 0.3
    easein 0.3 xalign 0.5 xanchor 0.5
    on hide:
        easein 0.3 xalign 0.0 xanchor 1.0

transform from_right:
    subpixel True
    xalign 1.0 xanchor 0.0
    pause 0.3
    easein 0.3 xalign 0.5 xanchor 0.5
    on hide:
        easein 0.3 xalign 1.0 xanchor 0.0

image fl_logo_eq_effect:
    "images/extended/ui/effect/fl_logo_eq_eff_1.webp"
    pause 0.1
    "images/extended/ui/effect/fl_logo_eq_eff_2.webp"
    pause 0.1
    "images/extended/ui/effect/fl_logo_eq_eff_3.webp"
    pause 0.1
    "images/extended/ui/effect/fl_logo_eq_eff_4.webp"
    pause 0.1
    "images/extended/ui/effect/fl_logo_eq_eff_5.webp"
    pause 0.1
    "images/extended/ui/effect/fl_logo_eq_eff_6.webp"
    pause 0.1
    "images/extended/ui/effect/fl_logo_eq_eff_7.webp"
    pause 0.1
    "images/extended/ui/effect/fl_logo_eq_eff_8.webp"
    pause 0.1
    "images/extended/ui/effect/fl_logo_eq_eff_9.webp"
    pause 0.1
    "images/extended/ui/effect/fl_logo_eq_eff_10.webp"
    pause 0.1
    "images/extended/ui/effect/fl_logo_eq_eff_11.webp"
    pause 0.1
    "images/extended/ui/effect/fl_logo_eq_eff_12.webp"
    pause 0.1
    "images/extended/ui/effect/fl_logo_eq_eff_13.webp"
    pause 0.1
    "images/extended/ui/effect/fl_logo_eq_eff_14.webp"
    pause 0.1
    "images/extended/ui/effect/fl_logo_eq_eff_15.webp"
    pause 0.1
    "images/extended/ui/effect/fl_logo_eq_eff_16.webp"
    pause 0.1
    "images/extended/ui/effect/fl_logo_eq_eff_17.webp"
    pause 0.1
    "images/extended/ui/effect/fl_logo_eq_eff_18.webp"
    pause 0.1
    repeat

image mm_play_crush_effect:
    "images/extended/ui/effect/mm_play_crush_1.webp"
    pause 0.1
    "images/extended/ui/effect/mm_play_crush_2.webp"

image mm_load_crush_effect:
    "images/extended/ui/effect/mm_load_crush_1.webp"
    pause 0.1
    "images/extended/ui/effect/mm_load_crush_2.webp"

image mm_bonus_crush_effect:
    "images/extended/ui/effect/mm_bonus_crush_1.webp"
    pause 0.1
    "images/extended/ui/effect/mm_bonus_crush_2.webp"

image mm_settings_crush_effect:
    "images/extended/ui/effect/mm_settings_crush_1.webp"
    pause 0.1
    "images/extended/ui/effect/mm_settings_crush_2.webp"

image mm_translate_crush_effect:
    "images/extended/ui/effect/mm_translate_crush_1.webp"
    pause 0.1
    "images/extended/ui/effect/mm_translate_crush_2.webp"

image mm_info_crush_effect:
    "images/extended/ui/effect/mm_info_crush_1.webp"
    pause 0.1
    "images/extended/ui/effect/mm_info_crush_2.webp"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
