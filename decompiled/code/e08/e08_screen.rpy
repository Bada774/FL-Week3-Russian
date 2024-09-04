screen e08_char_choice():

    frame:
        style_prefix "prologue"
        vbox:
            xalign 0.5
            yalign 0.3
            style_prefix "prologue_fetishes"
            vbox:
                xalign 0.5
                null height 10
                text _("Do you want to have Stacy this ending?")
                null height 150
            vbox:
                xalign 0.5
                xsize 300
                imagebutton:
                    idle "images/utility/prologue/girls/idle/sy.webp"
                    hover "images/utility/prologue/girls/hover/sy.webp"
                    selected_idle "images/utility/prologue/girls/selected/sy.webp"
                    selected_hover "images/utility/prologue/girls/hover/sy.webp"
                    action ToggleVariable("date_sy")
                    selected date_sy
                text _("Stacy") style_prefix "name" xalign 0.5

        vbox:
            xalign 0.5
            yalign 0.9
            style_prefix "prologue_yta"
            textbutton _("Continue"):
                action Jump("e08s01")

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
