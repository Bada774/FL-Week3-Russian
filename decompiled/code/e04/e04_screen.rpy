screen e04_char_choice():

    frame:
        style_prefix "prologue"
        vbox:
            xalign 0.5
            yalign 0.3
            style_prefix "prologue_fetishes"
            vbox:
                xalign 0.5
                null height 10
                text _("Please choose optional characters for this ending.")
                null height 150
            hbox:
                xalign 0.5
                spacing 250
                vbox:
                    xsize 300
                    imagebutton:
                        idle "images/utility/prologue/girls/idle/mh.webp"
                        hover "images/utility/prologue/girls/hover/mh.webp"
                        selected_idle "images/utility/prologue/girls/selected/mh.webp"
                        selected_hover "images/utility/prologue/girls/hover/mh.webp"
                        action ToggleVariable("date_mh")
                        selected date_mh
                    text _("Lyssa") style_prefix "name" xalign 0.5
                vbox:
                    xsize 300
                    imagebutton:
                        idle "images/utility/prologue/girls/idle/mk.webp"
                        hover "images/utility/prologue/girls/hover/mk.webp"
                        selected_idle "images/utility/prologue/girls/selected/mk.webp"
                        selected_hover "images/utility/prologue/girls/hover/mk.webp"
                        action ToggleVariable("e04s06_mk_available")
                        selected e04s06_mk_available
                    text _("Maria") style_prefix "name" xalign 0.5

        vbox:
            xalign 0.5
            yalign 0.9
            style_prefix "prologue_yta"
            textbutton _("Continue"):
                action Jump("d21s07_closing")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
