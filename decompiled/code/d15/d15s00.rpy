screen prologue_recap_choice():

    frame:
        style_prefix "prologue"
        has vbox:
            xalign 0.5
            yalign 0.3
            style_prefix "prologue_fetishes"
        vbox:
            xalign 0.5
            null height 10
            text _("Do you want to watch the recap of previous weeks?") text_align 0.5
            null height 150
        vbox:
            xalign 0.5
            spacing 30
            hbox:
                xalign 0.5
                spacing 200
                vbox:
                    xsize 300
                    spacing 10
                    imagebutton:
                        idle "images/utility/prologue/watch_recap_idle.webp"
                        hover "images/utility/prologue/watch_recap_hover.webp"
                        action Jump("week_1_recap")
                    text _("Watch the Recap") style_prefix "name" xalign 0.5 text_align 0.5
                vbox:
                    xsize 300
                    spacing 10
                    imagebutton:
                        idle "images/utility/prologue/play_week3_idle.webp"
                        hover "images/utility/prologue/play_week3_hover.webp"
                        action Jump("d15s01")
                    text _("Play Week-3") style_prefix "name" xalign 0.5 text_align 0.5

label d15s00:

    $ fl_day = 15
    $ fl_release = 11
    $ quick_menu = True

    $ fl_points = 0

    $ _preferences.show_empty_window = False

    call update_ending_variables from _call_update_ending_variables_8
    call screen prologue_recap_choice

    jump week_1_recap

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
