screen e09_char_choice():

    frame:
        style_prefix "prologue"
        vbox:
            xalign 0.5
            yalign 0.3
            style_prefix "prologue_fetishes"
            vbox:
                xalign 0.5
                null height 10
                text _("Do you want to have the Judge in this ending?")
                null height 150
            vbox:
                xalign 0.5
                xsize 300
                imagebutton:
                    idle "images/utility/prologue/girls/idle/jdg.webp"
                    hover "images/utility/prologue/girls/hover/jdg.webp"
                    selected_idle "images/utility/prologue/girls/selected/jdg.webp"
                    selected_hover "images/utility/prologue/girls/hover/jdg.webp"
                    action ToggleVariable("date_jdg")
                    selected date_jdg
                text _("Judge") style_prefix "name" xalign 0.5

        vbox:
            xalign 0.5
            yalign 0.9
            style_prefix "prologue_yta"
            textbutton _("Continue"):
                action Jump("e09s01")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
