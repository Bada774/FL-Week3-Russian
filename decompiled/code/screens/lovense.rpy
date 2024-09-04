default persistent.lovense_ip = "XXX.XXX.X.XX"
default persistent.lovense_port = "XXXXX"
default persistent.lovense_connected = False

screen lovense_connect():
    tag menu


    use game_menu(_("")):


        add "images/utility/lovense/lovense_bg.webp" xpos -20 ypos -100

        style_prefix "lovense"

        frame:
            vbox:
                style_prefix "lovense_info"
                text _("Please make sure both FL and Lovense Remote app are on the same LAN.")
                text _("Follow the steps to enable Game Mode in Lovense Remote app and connect your toy to FL.")

            hbox:
                style_prefix "lovense_steps"
                vbox:
                    add "images/utility/lovense/lovense_step_1.webp" xalign 0.5
                    null height 20
                    text _("1. Click on the \"Me\" tab")
                    text _("2. Then click on \"Settings\"")
                vbox:
                    add "images/utility/lovense/lovense_step_2.webp" xalign 0.5
                    null height 20
                    text _("3. Click the button to enable \"Game Mode\"")
                vbox:
                    add "images/utility/lovense/lovense_step_3.webp" xalign 0.5
                    null height 20
                    text _("4. Enter the \"Local IP\" and \"Http Port\" shown in the app")

            vbox:
                hbox:
                    hbox:
                        text _("Local IP: ")
                        textbutton _("{}").format(persistent.lovense_ip) action ShowMenu("lovense_input", "ip")
                    null width 100
                    hbox:
                        text _("HTTP Port: ")
                        textbutton _("{}").format(persistent.lovense_port) action ShowMenu("lovense_input", "port")
                textbutton _("Connect") action Function(Lovense.check_connection) xalign 0.5 selected (persistent.lovense_connected) style "lovense_connect_button"

            if config.developer is True:
                textbutton "Test" action ui.callsinnewcontext("lovense_test") xalign 1.0 yalign 1.0 style "lovense_test_button"
                textbutton "Stop" action ui.callsinnewcontext("lovense_stop") xalign 1.0 yalign 0.9 style "lovense_test_button"

    hbox:
        style_prefix "lovense_title"
        text _("Connect")
        imagebutton auto "images/utility/lovense/lovense_big_%s.webp" yalign 0.5 action OpenURL("https://www.lovense.com/r/9qvp6l?t=m1")
        text _("Toy")

screen lovense_sale_screen():
    tag menu


    use game_menu(_("")):

        add "images/utility/lovense/lovense_bg.webp" xpos -20 ypos -100

        add "images/utility/lovense/lovense_banner.webp" xalign 0.5 yalign -0.05

        vbox:
            style_prefix "lovense_sale_title"
            text _("Your favorite toy now works with Fetish Locator!")
        vbox:
            style_prefix "lovense_sale_body"
            text _("Get a Lovense toy and enjoy the best way to experience Fetish Locator!")

        vbox:
            xalign 0.5
            yalign 0.97
            style_prefix "prologue_yta"
            textbutton _("Get a toy now"):
                action OpenURL("https://www.lovense.com/r/9qvp6l?t=m1")

    vbox:
        style_prefix "connect_toy"
        textbutton _("{u}Connect your toy!{/u}") action ShowMenu("lovense_connect")

    imagebutton auto "images/utility/lovense/lovense_big_%s.webp" xpos 75 ypos 60 action OpenURL("https://www.lovense.com/r/9qvp6l?t=m1")


screen lovense_input(what):

    modal True

    if what == "ip":
        default title = _("Please enter your Local IP number:")
        default dummy = persistent.lovense_ip
    elif what == "port":
        default title = _("Please enter your HTTP Port number:")
        default dummy = persistent.lovense_port

    add "gui/overlay/confirm.png"

    frame:
        xsize 1000
        ysize 250
        xalign 0.5
        yalign 0.5
        xpadding 25
        ypadding 25

        has vbox:
            order_reverse False
            spacing 25

        frame:
            xsize 950
            background None
            text title xalign 0.5

        frame:
            xsize 620
            ysize 60
            xalign 0.5

            input:
                xalign 0.5
                yalign 0.5
                xfill True
                value ScreenVariableInputValue("dummy", True, False)
                pixel_width 300
                allow ("0123456789.")

        frame:
            xsize 950
            ysize 55
            background None

            has fixed
            button:
                xalign 0.0
                left_padding 50
                top_padding 3
                idle_background "images/utility/menu/selected/back.webp"
                hover_background "images/utility/menu/hover/back.webp"
                text _("Back") style "renamer_text"
                selected True
                action Hide("lovense_input")
                keysym ("K_ESCAPE", "mouseup_3")
                hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_submenu_hover.mp3"
                activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"

            button:
                xanchor 1.0
                xalign 1.0
                left_padding 50
                top_padding 3
                idle_background "images/utility/menu/selected/edit.webp"
                hover_background "images/utility/menu/hover/edit.webp"
                text _("Save") style "renamer_text"
                selected True
                if what == "ip":
                    action [Function(fl_renamer, "ip", dummy), Hide("lovense_input")]
                elif what == "port":
                    action [Function(fl_renamer, "port", dummy), Hide("lovense_input")]
                keysym ("K_RETURN", "K_KP_ENTER")
                hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_submenu_hover.mp3"
                activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"

label lovense_test:

    $ Lovense.vibrate(2)
    "Test 1 (2)"
    $ Lovense.vibrate(20)
    "Test 2 (20)"
    $ Lovense.vibrate(0,0,1)
    "vibrate Test 0"
    $ Lovense.vibrate(10)
    $ Lovense.pump(1,0,0)
    "Pump Test LOW"
    $ Lovense.vibrate(5,0,1)
    $ Lovense.pump(3,0,0)
    "Pump Test MAX"
    $ Lovense.pattern("1;20",0,2000)
    "Pattern Test"
    $ Lovense.vibrot()
    "Vibration + Rotation test"
    $ Lovense.stop()
    "Stop test"
    return

label lovense_stop:
    $ Lovense.stop()
    return

style lovense_steps_hbox:
    xalign 0.5
    yalign 0.28

style lovense_steps_vbox:
    xsize 400

style lovense_steps_text:
    xalign 0.5
    size 26
    text_align 0.5
    line_spacing 20

style lovense_frame:
    background None
    xfill True
    yfill True

style lovense_info_vbox:
    xalign 0.5
    yalign -0.05

style lovense_info_text:
    xalign 0.5

style lovense_vbox:
    xalign 0.5
    yalign 1.01
    spacing 40

style lovense_text:
    xalign 0.5
    yalign 0.5
    size 35

style lovense_button:
    xalign 0.5
    yalign 0.5
    xsize 355
    idle_background Frame("gui/frame_idle.png", 10, 10, 10, 10)
    hover_background Frame("gui/frame.png", 10, 10, 10, 10)

style lovense_button_text:
    xalign 0.5
    size 35

style lovense_connect_button_text:
    size 38
    idle_color "#ffffff"
    hover_color "#ffffff"
    selected_idle_color "#ffffff"
    selected_hover_color "#ffffff"

style lovense_connect_button:
    idle_background Frame("images/utility/prologue/yta_r_hover.webp", 15, 15, 15, 15)
    hover_background Frame("images/utility/prologue/yta_hover.webp", 15, 15, 15, 15)
    selected_background Frame("images/utility/prologue/yta_hover.webp", 15, 15, 15, 15)
    hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_submenu_hover.mp3"
    activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"
    left_padding 15
    right_padding 18
    top_padding 13
    bottom_padding 10

style lovense_title_hbox:
    xpos 75
    ypos 50
    spacing 25

style lovense_title_text:
    size 75
    color gui.accent_color

style lovense_sale_title_vbox:
    xalign 0.5
    yalign 0.55

style lovense_sale_title_text:
    color "#ff2d89"
    size 60
    text_align 0.5

style lovense_sale_body_vbox:
    spacing 50
    xalign 0.5
    yalign 0.72

style lovense_sale_body_text:
    size 34
    text_align 0.5

style connect_toy_vbox:
    xanchor 1.0
    xpos 1875
    ypos 90

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
