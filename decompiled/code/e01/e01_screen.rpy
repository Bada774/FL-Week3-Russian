screen e01s01_fetish_selection():

    style_prefix "fetish_selection"

    add "e01s01-40 laptop-pov_c1"

    frame:
        vbox:
            hbox:
                textbutton _("BDSM - Dominant"):
                    action ToggleVariable("e01s01_bdsm_dom")
                    if persistent.menu_hints is False:
                        xpos 180
                if persistent.menu_hints is True:
                    imagebutton:
                        idle "images/utility/menu/menu_hint_idle_2.webp"
                        hover "images/utility/menu/menu_hint_hover.webp"
                        xalign 1.0
                        yalign 0.5
                        action NullAction()
                        hovered Function(show_menu_hint, "e01s01m04c01")
                        unhovered (Hide('notify'), Function(restore_notify_timeout))

            hbox:
                textbutton _("BDSM - Submissive"):
                    action ToggleVariable("e01s01_bdsm_sub")
                    if persistent.menu_hints is False:
                        xpos 180
                if persistent.menu_hints is True:
                    imagebutton:
                        idle "images/utility/menu/menu_hint_idle_2.webp"
                        hover "images/utility/menu/menu_hint_hover.webp"
                        xalign 1.0
                        yalign 0.5
                        action NullAction()
                        hovered Function(show_menu_hint, "e01s01m04c02")
                        unhovered (Hide('notify'), Function(restore_notify_timeout))

            hbox:
                textbutton _("Watersports"):
                    action ToggleVariable("e01s01_piss")
                    if persistent.menu_hints is False:
                        xpos 180
                if persistent.menu_hints is True:
                    imagebutton:
                        idle "images/utility/menu/menu_hint_idle_2.webp"
                        hover "images/utility/menu/menu_hint_hover.webp"
                        xalign 1.0
                        yalign 0.5
                        action NullAction()
                        hovered Function(show_menu_hint, "e01s01m04c03")
                        unhovered (Hide('notify'), Function(restore_notify_timeout))

            hbox:
                textbutton _("Footfetish"):
                    action ToggleVariable("e01s01_footfet")
                    if persistent.menu_hints is False:
                        xpos 180
                if persistent.menu_hints is True:
                    imagebutton:
                        idle "images/utility/menu/menu_hint_idle_2.webp"
                        hover "images/utility/menu/menu_hint_hover.webp"
                        xalign 1.0
                        yalign 0.5
                        action NullAction()
                        hovered Function(show_menu_hint, "e01s01m04c04")
                        unhovered (Hide('notify'), Function(restore_notify_timeout))

            hbox:
                textbutton _("Rimming"):
                    action ToggleVariable("e01s01_rimming")
                    if persistent.menu_hints is False:
                        xpos 180
                if persistent.menu_hints is True:
                    imagebutton:
                        idle "images/utility/menu/menu_hint_idle_2.webp"
                        hover "images/utility/menu/menu_hint_hover.webp"
                        xalign 1.0
                        yalign 0.5
                        action NullAction()
                        hovered Function(show_menu_hint, "e01s01m04c05")
                        unhovered (Hide('notify'), Function(restore_notify_timeout))

        vbox:
            xalign 0.5
            yalign 0.95
            style_prefix "prologue_yta"
            textbutton _("Done") action (Hide("e01s01_fetish_selection"), Jump("e01s01_choice_done")) keysym ("K_RETURN", "K_KP_ENTER")


style fetish_selection_frame:
    xsize 1275
    ysize 777
    xalign 0.5
    yalign 0.46
    background None

style fetish_selection_vbox:
    xalign 0.5
    yalign 0.35
    spacing 50

style fetish_selection_hbox:
    xsize 700

style fetish_selection_button:
    idle_background "images/E-01/s01/buttons/tick_empty_idle.webp"
    hover_background "images/E-01/s01/buttons/tick_empty_hover.webp"
    selected_background "images/E-01/s01/buttons/tick_select_idle.webp"
    selected_idle_background "images/E-01/s01/buttons/tick_select_idle.webp"
    selected_hover_background "images/E-01/s01/buttons/tick_select_hover.webp"
    left_padding 100
    hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_submenu_hover.mp3"
    activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"

style fetish_selection_button_text:
    idle_color "#000000"
    hover_color gui.accent_color

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
