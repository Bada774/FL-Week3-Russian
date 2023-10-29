

screen fl_endings():



    style_prefix "ending_menu" tag menu

    add "black"
    add "images/utility/fl-loading-logo_only.webp" xalign 0.5 yalign 0.5 at image_opacity(0.25)

    label _("ENDINGS")

    frame:
        has grid 6 3:
            style_prefix "ending_grid"
            spacing 30

        for e in endings_list:
            if check_ending_lock(e[0]) is True:
                frame:
                    has vbox
                    imagebutton auto "images/utility/endings/ending_" + e[0][1:] + "_%s.webp" action ShowMenu("ending_start_screen", e[0]) style "ending_grid_button"
                    text e[0] + " - " + e[1]
            else:
                frame:
                    has vbox
                    imagebutton auto "images/utility/endings/locked_ending_%s.webp" action NullAction() hovered Function(show_hover_notify, (_("You haven't unlocked this ending"))) unhovered Function(hide_hover_notify) style "ending_grid_button"
                    text e[0] + " - Locked"

    button id "menu_return":
        text _("Return") style "navigation_text"
        style style.button["menu_return"]
        action Return()
        keysym "pad_b_press"
        xalign 0.98
        yalign 1.02

screen ending_start_screen(ending):



    style_prefix "ending_start_screen" tag menu

    add "images/ending-arts/ending_" + ending[-2:] + "_art.webp"

    for e in endings_list:
        if ending == e[0]:
            frame:
                has vbox
                label e[1]
                if not get_has_ending(e[0][-2:]) or not renpy.has_label(e[2]):
                    if e[4] == 2:
                        text _("This ending will be included in a future FREE DLC")
                    elif e[4] == 3:
                        text _("This ending will be included in a future DLC")

            frame:
                style_prefix "ending_start_button"
                has hbox
                if get_has_ending(e[0][-2:]) and renpy.has_label(e[2]):
                    textbutton _("Play") action Start(e[2]) style "ending_screen_start"
                textbutton _("Return") action ShowMenu("fl_endings") keysym "pad_b_press" style "ending_screen_return"
                null height 0

screen ending_unavailable(ending):

    add "images/ending-arts/ending_" + ending[-2:] + "_art.webp"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 50

        style_prefix "prologue_yta"
        textbutton _("Return to the Main Story"):
            action Jump("ending_" + ending[-2:] + "_return")
            xalign 0.5

        textbutton _("Exit to Mainmenu"):
            action MainMenu()
            xalign 0.5

style ending_start_screen_frame:
    xalign 0.0
    yalign 1.0
    background Frame("gui/frame3.png", 10, 50, 50, 10)
    right_padding 45
    left_padding 30
    bottom_padding 30

style ending_start_screen_vbox:
    spacing 15

style ending_start_button_frame:
    xalign 1.0
    yalign 1.0
    background Frame("gui/frame4.png", 50, 50, 10, 10)
    left_padding 30
    top_padding 20
    bottom_padding 20

style ending_start_button_hbox:
    spacing 30

style ending_start_screen_label_text:
    font "fonts/new/KaushanScript-Regular.ttf"
    size 80
    color "#f4426b"
    outlines [(3, "#611a2b", 3, 3)]
    kerning 2

style ending_start_screen_text:
    size 35
    color "#FFF"
    first_indent 15

style ending_screen_start:
    idle_background "images/utility/menu/selected/ending_play.webp"
    hover_background "images/utility/menu/hover/ending_play.webp"
    left_padding 50
    hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_submenu_hover.mp3"
    activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"

style ending_screen_start_text:
    idle_color "#FFF"
    hover_color gui.hover_color

style ending_screen_return:
    idle_background "images/utility/menu/selected/return.webp"
    hover_background "images/utility/menu/hover/return.webp"
    left_padding 50
    hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_submenu_hover.mp3"
    activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"

style ending_screen_return_text:
    idle_color "#FFF"
    hover_color gui.hover_color

style ending_menu_label:
    xalign 0.5
    yalign 0.01

style ending_menu_label_text:
    font "fonts/new/KaushanScript-Regular.ttf"
    size 110
    color gui.accent_color
    outlines [(2, "#611a2b", 2, 2)]

style ending_menu_frame:
    xalign 0.5
    yalign 0.6
    background None

style ending_grid_frame:
    xsize 283
    ysize 235
    background None

style ending_grid_button:
    hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_submenu_hover.mp3"
    activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"

style ending_grid_vbox:
    spacing 5

style ending_grid_text:
    xalign 0.5
    text_align 0.5
    size 22
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
