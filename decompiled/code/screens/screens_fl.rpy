





init -1:
    image fl_title = Text(" Fetish Locator", size=130, font="fonts/new/KaushanScript-Regular.ttf", color="#f4426b", outlines=[(4, "#611a2b", 4, 4)])
    image fl_subtitle = Text("Week-3", size=45, font="fonts/new/KaushanScript-Regular.ttf", color="#f4426b", outlines=[(2, "#611a2b", 2, 2)])
    image ee_subtitle = Text("Week-3 Extended Edition", size=45, font="fonts/new/KaushanScript-Regular.ttf", color="#f4426b", outlines=[(2, "#611a2b", 2, 2)])
    image hints_dlc = Text("+ Walkthough DLC", size=45, font="fonts/new/KaushanScript-Regular.ttf", color="#f4426b", outlines=[(2, "#611a2b", 2, 2)])






init -1 python:
    for i in ("even", "odd"):
        style.button["menu_load_mp_" + i].hover_background  = "images/utility/menu/hover/load.webp"
        style.button["menu_load_mp_" + i].hover_background  = "images/utility/menu/hover/load.webp"
        style.button["menu_load_mp_" + i].xsize             = 36
        style.button["menu_load_mp_" + i].ysize             = 36
    style.button["menu_load_mp_odd" ].idle_background   = "images/utility/menu/idle/load.webp"
    style.button["menu_load_mp_even"].idle_background   = "images/utility/menu/selected/load.webp"
    style.button["menu_load_mp_odd" ].padding           = (0,0,0,0)
    style.button["menu_load_mp_even"].margin            = (0,0,0,0)

init -501 screen load_mp():
    tag menu
    $ prev_week_saves = FLSS.previous_mp_saves



    use game_menu(_("Continue from week [FLSS.week.prev]"), scroll="viewport", yinitial=1.0):

        vbox:
            spacing 10
            xsize 1380

            if (len(prev_week_saves) > 0):
                $ j = 0

                hbox:
                    ysize 50
                    xsize 1370
                    style_prefix "mph"
                    vbox:
                        style_prefix "mph_large"
                        text _("NAME")

                    null width 100

                    vbox:
                        style_prefix "mph_large"
                        text _("DATE")

                for i in prev_week_saves:
                    $ text_style = "odd" if (j%2 == 1) else "even"
                    $ j += 1
                    hbox:
                        style_prefix "mpb"
                        vbox:
                            style_prefix "mpb_large"
                            button:
                                text (
                                    _("Unnamed End Game Save") if (i["savename"]=="") else i["savename"]
                                ) style "mpb_large_"+text_style+"_text"
                                action FLLoadMp(i["slot"])
                                idle_background "images/utility/menu/selected/load.webp"
                                hover_background "images/utility/menu/hover/load.webp"
                                hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_submenu_hover.mp3"
                                activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"
                                left_padding 50
                        vbox:
                            style_prefix "mpb_large"
                            button:
                                text _strftime(
                                    renpy.translation.translate_string(_("{#file_time}%A, %B %d %Y, %H:%M")),
                                    time.localtime(i["timestamp"])
                                ) style "mpb_large_"+text_style+"_text"
                                action FLLoadMp(i["slot"])
                                xalign 1.0
                                hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_submenu_hover.mp3"
                                activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"
                        vbox:
                            xalign 1.0
                            style_prefix "mpb_delete"
                            imagebutton:
                                if text_style == "odd":
                                    idle "images/utility/menu/delete_idle_odd.webp"
                                else:
                                    idle "images/utility/menu/delete_idle.webp"
                                hover "images/utility/menu/delete_hover_accent.webp"
                                focus_mask "images/utility/menu/delete_mask.webp"
                                action FLDeleteMp(i["slot"])
                                hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_submenu_hover.mp3"
                                activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"

            else:
                hbox:
                    xsize 1380
                    vbox:
                        xalign 0.5
                        spacing 20
                        style_prefix "android_mp"
                        if renpy.android is False:
                            vbox:
                                style_prefix "no_mp_title"
                                xalign 0.5
                                text _("No end game save from week [FLSS.week.prev] has been detected")
                            null height 5
                            vbox:
                                style_prefix "no_mp_subtitle"
                                xalign 0.5
                                text _("Please open Fetish Locator week [FLSS.week.prev] and SAVE at the end game save screen")
                            add "images/week-2/week-2-save-screen.webp" xalign 0.5
                        else:
                            vbox:
                                text _("Due to some new changes in Android OS, to import your save from Week 2 you need to follow these instructions.")
                            vbox:
                                text _("1. Close the game and find the Week save file named \"FetishLocator\" in - \"InternalStorage/RenPy/persistent/\"")
                            vbox:
                                text _("2. Copy the \"FetishLocator\" file to the following folder (replace existing files if any) -")
                            vbox:
                                text _("\"Internal storage/Android/data/com.patreon.fetishlocator.week3/files/saves/\".")
                            null height 5
                            vbox:
                                text _("Contact us on {a=https://discord.gg/efmQRNtFks}Discord{/a} if you need help.")

                        null height 5
                        add "gui/horizontal_devider.png" xalign 0.5
                        null height 5
                        text _("Or"):
                            color "#fff"
                            xalign 0.5
                            size 40
                        button:
                            text _("{u}Fill the questionnaire to play week [FLSS.week.cur] without loading a save{/u}"):
                                size 40
                                idle_color "#ffffff"
                                hover_color "#f05172"
                            xalign 0.5
                            action Start()
                            hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_submenu_hover.mp3"
                            activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"



init -501 screen mp_fail():

    add "black"

    style_prefix "mp_fail"
    vbox:
        if renpy.android is True:
            text _("Your device can't save the game progress through different weeks. Please, allow FL App to write on the external storage.")
            null height 20
            text _("On most devices you can set the permissions on the Setting app.")
            text _("1. Go to - Settings -> Apps -> Fetish Locator Week [FLSS.week.cur] -> Permissions -> Storage.")
            text _("2. Set the permission to -> \"Allow management of all files\".")
            null height 20
            text _("Now the game should work.")
        else:
            text _("Your device cannot save the game progress through different weeks. Please, follow these instructions to fix this issue.")
            null height 20
            text _("1. Enable \"Show hidden items\" option in Windows Explorer.")
            text _("2. Go to - \"C:/Users/username/AppData/Roaming/RenPy/persistent/\" folder.")
            text _("3. Create a backup of the file \"FetishLocator\" and delete it.")
            null height 20
            text _("4. After launching the game once, you can put the backed up \"FetishLocator\" file back to it's location to get your Previous Week's saves back.")
        null height 20
        text _("Contact us on {a=https://discord.gg/efmQRNtFks}Discord{/a} if you need help.")
        null height 20
        vbox:
            spacing 30
            hbox:
                style_prefix "prologue_yta"
                xalign 0.5
                textbutton _("Continue playing") action Confirm(_("If you decide to continue, you might not be able to load saves from Week-2. You won't be notified again. Are you sure?"), (SetVariable("persistent.ignore_mp_fail", True), SetVariable("persistent.mp_info", " MP"), MainMenu(confirm=False)))
            hbox:
                style_prefix "prologue_yta"
                xalign 0.5
                textbutton _("Close the game") action Quit(confirm=False)

init -1 style mp_fail_vbox:
    xsize 1850
    xalign 0.5
    yalign 0.5
    spacing 20

init -1 style mp_fail_text:
    xalign 0.5
    text_align 0.5
    font gui.text_font
    size 50
    color "#ffffff"
    line_spacing 10

init -1 style android_mp_vbox:
    xalign 0.5
    xsize 1250
    spacing 40

init -1 style android_mp_text:
    xalign 0.5
    text_align 0.5
    size 40
    line_spacing 10

init -1 style no_mp_title_text:
    color "#fff"
    size 45

init -1 style no_mp_subtitle_text:
    color "#fff"
    size 35

init -1 style mph_vbox:
    ysize 50

init -1 style mpb_vbox:
    ysize 50

init -1 style mpb_hbox:
    xsize 1370

init -1 style mph_small_vbox:
    xsize 100

init -1 style mph_large_vbox:
    xsize 600

init -1 style mph_small_text:
    xalign 0.5
    color gui.accent_color
    bold True

init -1 style mph_large_text:
    xalign 0.5
    color gui.accent_color
    bold True

init -1 style mpb_small_vbox:
    xsize 100

init -1 style mpb_large_vbox:
    xsize 640

init -1 style mpb_delete_vbox:
    xsize 40

init -1 style mpb_small_odd_text:
    xalign 0.5
    color gui.idle_color

init -1 style mpb_large_odd_text:
    xalign 0.1
    idle_color gui.idle_color
    hover_color "#f05172"
    size 37

init -1 style mpb_small_even_text:
    xalign 0.5
    color "#fff"

init -1 style mpb_large_even_text:
    xalign 0.1
    idle_color "#fff"
    hover_color "#f05172"
    size 37



init -501 screen steam_deck_layout(splash=False):
    tag menu


    style_prefix "steam_deck_help"

    key "pad_b_press" action Return()

    add "images/utility/steam_deck/steam_deck_control_layout.webp"

    text _("Touch input supported") xalign 0.5 yalign 0.41
    text _("Navigation") xalign 0.5 ypos 70
    text _("Pause Menu") xanchor 0.5 xpos 1445 ypos 70
    text _("Quick Save") xanchor 0.5 xpos 480 ypos 70

    text _("Roll Back") xanchor 1.0 xpos 280 ypos 730
    text _("Navigation") xanchor 1.0 xpos 280 ypos 155

    text _("{b}A{/b} - Select") xpos 1650 ypos 175
    text _("{b}B{/b} - Go Back") xpos 1650 ypos 285
    text _("{b}X{/b} - Skip") xpos 1650 ypos 395
    text _("{b}Y{/b} - Hide UI") xpos 1650 ypos 505
    text _("Roll Forward") xpos 1650 ypos 730

    if splash is True:
        text _("You can find this layout in the {b}Help{/b} menu") xalign 0.5 ypos 1000
    else:
        textbutton _("CLOSE") xalign 0.99 yalign 0.99 action Return() keysym ('K_ESCAPE', 'mousedown_3')

init -1 style steam_deck_help_button_text:
    idle_color "#fff"
    hover_color gui.hover_color
    outlines [ (absolute(1), "#000", 0, 0) ]



init -501 screen end_screen():

    vbox:
        style_prefix "end_screen"

        text _("Save your game now") at text_appear(0.5)

        textbutton _("{u}Done{/u}") action Jump("end") at text_appear(0.5)

transform -1 text_appear(pause):
    alpha 0.0
    pause pause
    linear 0.5 alpha 1.0

init -1 style end_screen_vbox:
    xsize 1920
    ysize 750
    yalign 0.9

init -1 style end_screen_text:
    font "fonts/new/KaushanScript-Regular.ttf"
    size 120
    outlines [(2, "#000000", 0, 0)]
    kerning 1
    xalign 0.5
    text_align 0.5

init -1 style end_screen_button:
    xalign 0.5
    hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_submenu_hover.mp3"
    activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"

init -1 style end_screen_button_text:
    idle_color gui.idle_color
    hover_color gui.accent_color
    size 60
    outlines [(2, "#000000", 0, 0)]
    kerning 1



init -501 screen scene_transistion(message):

    vbox:
        style_prefix "scene_transistion"

        text message

init -1 style scene_transistion_vbox:
    xalign 0.5
    yalign 0.5

init -1 style scene_transistion_text:
    font "fonts/new/KaushanScript-Regular.ttf"
    text_align 0.5
    size 120
    xsize 1250
    color "#ffffff"
    outlines [(4, "#555555", 3, 3)]

init -501 screen game_end_text(txt):

    vbox:
        style_prefix "game_end"

        text txt

init -1 style game_end_vbox:
    xalign 0.5
    yalign 0.5

init -1 style game_end_text:
    font "fonts/new/KaushanScript-Regular.ttf"
    text_align 0.5
    size 70
    xsize 1800
    color "#ffffff"
    outlines [(2, "#444444", 2, 2)]



default -1 trying_skip_cutscene = False

init -501 screen cutscene_skip(jump_label):

    key "mouseup_1" action SetVariable("trying_skip_cutscene", True)
    key "mouseup_3" action SetVariable("trying_skip_cutscene", True)
    key "K_ESCAPE" action SetVariable("trying_skip_cutscene", True)
    key "K_MENU" action SetVariable("trying_skip_cutscene", True)
    key "K_RETURN" action SetVariable("trying_skip_cutscene", True)
    key "K_KP_ENTER" action SetVariable("trying_skip_cutscene", True)
    key "K_PAUSE" action SetVariable("trying_skip_cutscene", True)
    key "K_SPACE" action SetVariable("trying_skip_cutscene", True)

    if trying_skip_cutscene is True:
        hbox:
            style_prefix "skip_cutscene"

            textbutton _("SKIP") action (Hide("cutscene_skip"), Jump(jump_label))

        timer 3.0 action SetVariable("trying_skip_cutscene", False)

init -1 style skip_cutscene_hbox:
    yalign 0.952
    xalign 0.971

init -1 style skip_cutscene_button:
    idle_background Frame("images/utility/menu/skip_idle.webp", 8, 7, 7, 7)
    hover_background Frame("images/utility/menu/skip_hover.webp", 8, 7, 7, 7)
    left_padding 15
    right_padding 15
    top_padding 15
    bottom_padding 10

init -1 style skip_cutscene_button_text:
    size 40
    hover_color gui.accent_color





init -501 screen fl_points_screen(points=0, is_enabled=True):

    if is_enabled and not _in_replay:
        frame:
            xpadding 12
            ypadding 12
            xpos 0.995 ypos 0.01
            xanchor 1.0 yanchor 0.0
            background Color((61, 23, 31, 90))
            style_prefix "fl_points"

            has vbox
            spacing -10
            textbutton "Fetish Locator"
            hbox:
                spacing -15

                at transform:
                    linear 0.5 alpha 1.0
                textbutton _("points: ")
                textbutton "[points]"
            null height 30
            hbox:
                xalign 0.5
                spacing 10
                if fl_goldstars == 0:
                    add "utility/menu/no_gold_star.webp"
                else:
                    if fl_goldstars >= 1:
                        add "utility/menu/gold_star.webp"
                    if fl_goldstars >= 2:
                        add "utility/menu/gold_star.webp"
                    if fl_goldstars >= 3:
                        add "utility/menu/gold_star.webp"
                    if fl_goldstars >= 4:
                        add "utility/menu/gold_star.webp"
                    if fl_goldstars >= 5:
                        add "utility/menu/gold_star.webp"

init -1 style fl_points_button_text is text:
    idle_color gui.accent_color
    insensitive_color gui.accent_color
    font "fonts/new/KaushanScript-Regular.ttf"





init -1 python:

    for i in ( "mes", "mh", "mk", "cl", "op", "ah", "dd", "dw", "sy", "pw", "vw", "aw", "jf", "cb", "ir", "hr", "nr", "jdg"):
        style.button["prologue_" + i].idle_background             = "images/utility/prologue/girls/idle/{0}.webp".format(i)
        style.button["prologue_" + i].hover_background            = "images/utility/prologue/girls/hover/{0}.webp".format(i)
        style.button["prologue_" + i].selected_background         = "images/utility/prologue/girls/selected/{0}.webp".format(i)
        style.button["prologue_" + i].selected_idle_background    = "images/utility/prologue/girls/selected/{0}.webp".format(i)
        style.button["prologue_" + i].selected_hover_background   = "images/utility/prologue/girls/hover/{0}.webp".format(i)
        style.button["prologue_" + i].activate_sound              = "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_questionnaire_choice.mp3"
        style.button["prologue_" + i].xsize                       = 300
        style.button["prologue_" + i].ysize                       = 360
    style.button["prologue_mes_in"].idle_background            = "images/utility/prologue/girls/idle/mes.webp".format(i)
    style.button["prologue_mes_in"].hover_background           = "images/utility/prologue/girls/idle/mes.webp".format(i)
    style.button["prologue_mes_in"].xsize                      = 300
    style.button["prologue_mes_in"].ysize                      = 360
    style.button["prologue_mh_in"].idle_background             = "images/utility/prologue/girls/idle/mh.webp".format(i)
    style.button["prologue_mh_in"].hover_background            = "images/utility/prologue/girls/idle/mh.webp".format(i)
    style.button["prologue_mh_in"].xsize                       = 300
    style.button["prologue_mh_in"].ysize                       = 360

init -501 screen prologue_intro():

    vbox:
        xalign 0.5
        yalign 0.3
        vbox:
            xalign 0.5
            style_prefix "prologue_fetishes"
            vbox:
                xalign 0.5
                null height 10
                text _("Welcome to")
                at title_effect(0.3)
        vbox:
            xalign 0.5
            spacing -35
            add "fl_title" xalign 0.5
            if is_extended_edition is True:
                add "ee_subtitle" xalign 0.5
            else:
                add "fl_subtitle" xalign 0.5
            at title_effect(0.6)

        null height 50

        vbox:
            xalign 0.5
            style_prefix "prologue_name"
            vbox:
                xalign 0.5
                null height 10
                text _("Please enter your name here")
                null height 40
            frame:
                xsize 800
                ysize 100
                xalign 0.5
                top_padding 30
                background "gui/frame2.png"
                input default "Mike":
                    xfill True
                    value VariableInputValue("mcname")
                    pixel_width 500
                    size 42
                    xalign 0.5
                    color "#ffffff"
            at title_effect(0.9)

    hbox:
        xalign 0.5
        yalign 0.85
        style_prefix "prologue_yta"
        textbutton _("Done") action [Jump("prologue_fl_name"), Hide("prologue_intro")] keysym ("K_RETURN", "K_KP_ENTER")
        at title_effect(1.2)

init -501 screen prologue_fl_name():

    vbox:
        xalign 0.5
        yalign 0.35
        vbox:
            xalign 0.5
            add "images/utility/fl-loading-logo_only.webp"
            at title_effect(0.3)

        null height 50

        vbox:
            xalign 0.5
            style_prefix "prologue_name"
            vbox:
                xalign 0.5
                null height 10
                text _("Please enter your Fetish Locator username here")
                null height 40
            frame:
                xsize 800
                ysize 100
                xalign 0.5
                top_padding 30
                background "gui/frame2.png"
                input default "Not_Mike":
                    xfill True
                    value VariableInputValue("mclogin")
                    pixel_width 500
                    size 42
                    xalign 0.5
                    color "#ffffff"
            at title_effect(0.3)

        null height 50

    hbox:
        xalign 0.986
        yalign 0.975
        style_prefix "prologue_yta"
        textbutton _("Done") action [Jump("prologue_intro_done"), Hide("prologue_fl_name")] keysym ("K_RETURN", "K_KP_ENTER")
        at title_effect(0.3)

    hbox:
        xalign 0.014
        yalign 0.975
        style_prefix "prologue_yta"
        textbutton _("Back") action Rollback()
        at title_effect(0.3)

init -501 screen prologue_fetishes():

    $ fetishes = prologue_get_fetishes()

    frame:
        style_prefix "prologue"
        has vbox
        xalign 0.5
        yalign 0.4
        style_prefix "prologue_fetishes"
        vbox:
            xalign 0.5
            text _("Please choose your preferences")
            null height 100
        vbox:
            xalign 0.5
            spacing 30
            for i in fetishes:
                hbox:
                    vbox:
                        xsize 480
                        yalign 0.5
                        text i[4] style_prefix "name"
                    hbox:
                        spacing 0
                        textbutton _("Yes"):
                            style_prefix "prologue_yes"
                            selected getattr(renpy.store, i[0])
                            action Function(prologue_set_fetishes, i[0], True)

                        textbutton _("No"):
                            style_prefix "prologue_no"
                            selected not getattr(renpy.store, i[0])
                            action Function(prologue_set_fetishes, i[0], False)

        vbox:
            style_prefix "prologue_yta"
            xalign 0.5

            null height 70
            textbutton _("Yes to all"):
                action Function(prologue_set_all_fetishes, True)
                selected prologue_check_fetishes()

    use prologue_done("prologue_fetishes_choose", "prologue_girls_1")

init -501 screen prologue_done(what_scren, next_label):

    hbox:
        xalign 0.986
        yalign 0.975
        style_prefix "prologue_yta"
        textbutton _("Done") action [Hide(what_scren), Jump(next_label)] keysym ("K_RETURN", "K_KP_ENTER")

    hbox:
        xalign 0.014
        yalign 0.975
        style_prefix "prologue_yta"
        textbutton _("Back") action Rollback()

init -501 screen prologue_fetishes_show():
    tag prologue


    style_prefix "prologue"
    modal False
    use prologue_fetishes(False)

init -501 screen prologue_fetishes_choose():
    tag prologue


    style_prefix "prologue"
    modal True
    use prologue_fetishes()

init -501 screen prologue_girls_1(step):

    $ girls = prologue_get_girls(0)
    $ second_choices = prologue_get_girls(4)

    frame:
        style_prefix "prologue"
        ypos 60
        ysize 980
        has vbox
        xalign 0.5
        style_prefix "prologue_fetishes"
        vbox:
            xalign 0.5
            null height 10
            text _("Please select whom you like")
            null height 20
        vbox:
            xalign 0.5
            hbox:
                xalign 0.5
                spacing 50
                for i in girls:
                    vbox:
                        xsize 300
                        spacing 10
                        if getattr(renpy.store, i[6]):
                            button id ("prologue_" + i[0][5:]):
                                style style.button["prologue_" + i[0][5:]]
                                selected getattr(renpy.store, i[0])
                                action Function(prologue_set_girls, (step-1), i[0], i[5])
                            text i[4] style_prefix "name" xalign 0.5
                        else:
                            button id ("prologue_" + i[0][5:] + "_in"):
                                style style.button["prologue_" + i[0][5:] + "_in"]
                                action ToggleVariable(i[0] + "_info")
                                activate_sound audio.error
                            text i[4] style_prefix "name_in" xalign 0.5
        null height 20
        vbox:
            xalign 0.5
            hbox:
                xalign 0.5
                spacing 50
                for i in second_choices:
                    vbox:
                        xsize 300
                        spacing 10
                        if getattr(renpy.store, i[5]):
                            button id ("prologue_" + i[0][5:]):
                                style style.button["prologue_" + i[0][5:]]
                                selected getattr(renpy.store, i[0])
                                action Function(prologue_set_girls, (step+3), i[0], i[5])
                            text i[4] style_prefix "name" xalign 0.5
                        else:
                            null height 360
    hbox:
        xalign 0.5
        ypos 591
        spacing 50
        frame:
            xsize 300
            ysize 360
            background None
            if date_mes_info:
                text _("Go back and enable {b}Watersports{/b} fetish to be able to select Min") style_prefix "name" xalign 0.5 yalign 0.5 line_spacing 15

        frame:
            xsize 300
            ysize 360
            background None
            if date_mh_info:
                text _("Go back and enable {b}Trans Content{/b} to be able to select Lyssa") style_prefix "name" xalign 0.5 yalign 0.5 line_spacing 15

        vbox:
            xsize 300
            null height 360

    use prologue_done("prologue_girls_1", "prologue_questions_1")

init -501 screen prologue_questions_1():

    frame:
        style_prefix "prologue"
        has vbox
        xalign 0.5
        yalign 0.3
        style_prefix "prologue_fetishes"
        vbox:
            xalign 0.5
            text _("Please answer the questions")
            null height 50

        hbox:
            xalign 0.5
            spacing 100
            vbox:
                xalign 0.5
                xsize 300
                ysize 700
                add "images/utility/prologue/extra/arj.webp" xalign 0.5
                text _("AmRose Romance or Slave route?") style_prefix "name" xalign 0.5
                hbox:
                    xalign 0.5
                    textbutton _("Romance"):
                        style_prefix "prologue_yes"
                        action (SetVariable("date_arj_romance", True), SetVariable("date_arj_sexslave", False))
                    textbutton _("Slave"):
                        style_prefix "prologue_no_sp"
                        action (SetVariable("date_arj_sexslave", True), SetVariable("date_arj_romance", False))
                        left_padding 45
                        right_padding 46

                null height 5

                text _("Did you kiss AmRose?") style_prefix "name" xalign 0.5
                hbox:
                    xalign 0.5
                    textbutton _("Yes"):
                        style_prefix "prologue_yes"
                        action SetVariable("d14s03_arj_kiss", True)
                    textbutton _("No"):
                        style_prefix "prologue_no"
                        action SetVariable("d14s03_arj_kiss", False)

            if date_mh:
                vbox:
                    xalign 0.5
                    xsize 300
                    ysize 700
                    add "images/utility/prologue/girls/hover/mh.webp" xalign 0.5
                    text _("Do you want to dominate Lyssa?") style_prefix "name" xalign 0.5
                    hbox:
                        xalign 0.5
                        textbutton _("Yes"):
                            style_prefix "prologue_yes"
                            action SetVariable("date_mh_bdsm", True)
                        textbutton _("No"):
                            style_prefix "prologue_no"
                            action SetVariable("date_mh_bdsm", False)

            vbox:
                xalign 0.5
                xsize 300
                ysize 650
                spacing 20
                add "images/utility/prologue/extra/lc.webp"
                text _("Did you say that you love Lydia?") style_prefix "name" xalign 0.5
                hbox:
                    xalign 0.5
                    yalign 1.0
                    textbutton _("Yes"):
                        style_prefix "prologue_yes"
                        action SetVariable("d14s16_love_lc", True)
                    textbutton _("No"):
                        style_prefix "prologue_no"
                        action SetVariable("d14s16_love_lc", False)

    use prologue_done("prologue_questions_1", "prologue_girls_2")

init -501 screen prologue_girls_2(step):

    $ girls = prologue_get_girls(1)

    frame:
        style_prefix "prologue"
        has vbox
        xalign 0.5
        yalign 0.3
        style_prefix "prologue_fetishes"
        vbox:
            xalign 0.5
            null height 10
            text _("Please select whom you like")
            null height 150
        vbox:
            xalign 0.5
            spacing 30
            hbox:
                xalign 0.5
                spacing 50
                for i in girls:
                    vbox:
                        xsize 300
                        spacing 10
                        button id ("prologue_" + i[0][5:]):
                            style style.button["prologue_" + i[0][5:]]
                            selected getattr(renpy.store, i[0])
                            action Function(prologue_set_girls, (step-1), i[0], i[5])
                        text i[4] style_prefix "name" xalign 0.5

    use prologue_done("prologue_girls_2", "prologue_girls_3")

init -501 screen prologue_girls_3(step):

    $ girls_set_3 = prologue_get_girls(2)
    $ girls_set_4 = prologue_get_girls(3)

    frame:
        style_prefix "prologue"
        has vbox
        xalign 0.5
        style_prefix "prologue_fetishes"
        vbox:
            xalign 0.5
            null height 10
            text _("Please select whom you like")
            null height 20
        vbox:
            xalign 0.5
            spacing 30
            hbox:
                xalign 0.5
                spacing 50
                for i in girls_set_3:
                    vbox:
                        xsize 300
                        spacing 10
                        button id ("prologue_" + i[0][5:]):
                            style style.button["prologue_" + i[0][5:]]
                            selected getattr(renpy.store, i[0])
                            action Function(prologue_set_girls, (step-1), i[0], i[5])
                        text i[4] style_prefix "name" xalign 0.5
            hbox:
                xalign 0.5
                spacing 50
                for i in girls_set_4:
                    vbox:
                        xsize 300
                        spacing 10
                        button id ("prologue_" + i[0][5:]):
                            style style.button["prologue_" + i[0][5:]]
                            selected getattr(renpy.store, i[0])
                            action Function(prologue_set_girls, (step), i[0], i[5])
                        text i[4] style_prefix "name" xalign 0.5

        vbox at image_zoom(0.9):
            style_prefix "prologue_yta"
            xalign 0.5
            textbutton _("Select all"):
                action (Function(prologue_set_all_girls, 2, True), Function(prologue_set_all_girls, 3, True))
                selected prologue_check_girls()

    use prologue_done("prologue_girls_3", "prologue_questions_2")

init -501 screen prologue_questions_2():

    frame:
        style_prefix "prologue"
        has vbox
        xalign 0.5
        yalign 0.3
        style_prefix "prologue_fetishes"
        vbox:
            xalign 0.5
            text _("Please answer the questions")
            null height 50

        hbox:
            xalign 0.5
            spacing 30
            if date_sy:
                vbox:
                    xalign 0.5
                    xsize 300
                    ysize 650
                    spacing 20
                    add "images/utility/prologue/girls/hover/sy.webp"
                    text _("Did you agree to have kids with Stacy?") style_prefix "name" xalign 0.5
                    hbox:
                        xalign 0.5
                        yalign 1.0
                        textbutton _("Yes"):
                            style_prefix "prologue_yes"
                            action SetVariable("d14s19_everything", True)
                        textbutton _("No"):
                            style_prefix "prologue_no"
                            action SetVariable("d14s19_everything", False)
            if date_pw:
                vbox:
                    xalign 0.5
                    xsize 300
                    ysize 650
                    spacing 20
                    add "images/utility/prologue/extra/nk.webp"
                    text _("Did you creampie Nora and agree to be the father?") style_prefix "name" xalign 0.5
                    hbox:
                        xalign 0.5
                        yalign 1.0
                        textbutton _("Yes"):
                            style_prefix "prologue_yes"
                            action SetVariable("date_nk_preg", True)
                        textbutton _("No"):
                            style_prefix "prologue_no"
                            action SetVariable("date_nk_preg", False)
            if date_vw:
                vbox:
                    xalign 0.5
                    xsize 300
                    ysize 650
                    spacing 20
                    add "images/utility/prologue/girls/hover/vw.webp"
                    text _("Did you ask Vanessa to wear shoes with cum?") style_prefix "name" xalign 0.5
                    hbox:
                        xalign 0.5
                        yalign 1.0
                        textbutton _("Yes"):
                            style_prefix "prologue_yes"
                            action SetVariable("d13s08_keep_shoe_cum", True)
                        textbutton _("No"):
                            style_prefix "prologue_no"
                            action SetVariable("d13s08_keep_shoe_cum", False)
            if date_hr:
                vbox:
                    xalign 0.5
                    xsize 300
                    ysize 650
                    spacing 20
                    add "images/utility/prologue/girls/hover/hr.webp"
                    text _("Did you give the password to Hana?") style_prefix "name" xalign 0.5
                    hbox:
                        xalign 0.5
                        yalign 1.0
                        textbutton _("Yes"):
                            style_prefix "prologue_yes"
                            action SetVariable("d12s02_gavepass", True)
                        textbutton _("No"):
                            style_prefix "prologue_no"
                            action SetVariable("d12s02_gavepass", False)

            if date_dw:
                vbox:
                    xalign 0.5
                    xsize 300
                    ysize 650
                    spacing 20
                    add "images/utility/prologue/extra/pb_ntr.webp"
                    text _("Did you let Pete hit on Samiya?") style_prefix "name" xalign 0.5
                    hbox:
                        xalign 0.5
                        yalign 1.0
                        textbutton _("Yes"):
                            style_prefix "prologue_yes"
                            action SetVariable("pete_ntr", True)
                        textbutton _("No"):
                            style_prefix "prologue_no"
                            action SetVariable("pete_ntr", False)

    use prologue_done("prologue_questions_2", "prologue_finalize")

init -1 style prologue_name_text:
    size 55
    font "fonts/Andika-Regular.ttf"
    color "#ffffff"

init -1 style prologue_yes_button_text:
    size 35
    idle_color "#ffffff"
    hover_color "#ffffff"
    selected_idle_color "#ffffff"
    selected_hover_color "#ffffff"

init -1 style prologue_no_button_text:
    size 35
    idle_color "#ffffff"
    hover_color "#ffffff"
    selected_idle_color "#ffffff"
    selected_hover_color "#ffffff"

init -1 style prologue_no_sp_button_text:
    size 35
    idle_color "#ffffff"
    hover_color "#ffffff"
    selected_idle_color "#ffffff"
    selected_hover_color "#ffffff"

init -1 style prologue_yes_button:
    idle_background Frame("images/utility/prologue/left_idle.webp", 15, 15, 15, 15)
    hover_background Frame("images/utility/prologue/left_hover.webp", 15, 15, 15, 15)
    selected_background Frame("images/utility/prologue/left_hover.webp", 15, 15, 15, 15)
    activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_questionnaire_choice.mp3"
    left_padding 12
    right_padding 11
    top_padding 13
    bottom_padding 10

init -1 style prologue_no_button:
    idle_background Frame("images/utility/prologue/right_idle.webp", 15, 15, 15, 15)
    hover_background Frame("images/utility/prologue/right_hover.webp", 15, 15, 15, 15)
    selected_background Frame("images/utility/prologue/right_hover.webp", 15, 15, 15, 15)
    activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_questionnaire_choice.mp3"
    left_padding 15
    right_padding 18
    top_padding 13
    bottom_padding 10

init -1 style prologue_no_sp_button:
    idle_background Frame("images/utility/prologue/right_idle.webp", 15, 15, 15, 15)
    hover_background Frame("images/utility/prologue/right_hover.webp", 15, 15, 15, 15)
    selected_background Frame("images/utility/prologue/right_hover.webp", 15, 15, 15, 15)
    activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_questionnaire_choice.mp3"
    left_padding 15
    right_padding 18
    top_padding 13
    bottom_padding 10

init -1 style prologue_fetishes_vbox:
    spacing 10

init -1 style prologue_fetishes_text:
    size 70
    font "fonts/Andika-Regular.ttf"
    color "#f4426b"
    outlines [(2, "#61192b", 2, 2)]

init -1 style prologue_yta_button_text:
    size 45
    idle_color "#ffffff"
    hover_color "#ffffff"
    selected_idle_color "#ffffff"
    selected_hover_color "#ffffff"

init -1 style prologue_yta_button:
    idle_background Frame("images/utility/prologue/yta_r_hover.webp", 15, 15, 15, 15)
    hover_background Frame("images/utility/prologue/yta_hover.webp", 15, 15, 15, 15)
    selected_background Frame("images/utility/prologue/yta_hover.webp", 15, 15, 15, 15)
    hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_submenu_hover.mp3"
    activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"
    left_padding 15
    right_padding 18
    top_padding 13
    bottom_padding 10

init -1 style prologue_frame:
    background None
    xsize 1920
    ysize 1080

init -1 style name_in_text:
    color "#ffffff"
    size 35

init -1 style name_text:
    color gui.hover_color
    size 35

init -1 style description_text:
    color gui.interface_text_color



default -1 slot_name = None

init -501 screen save_name_input():

    modal True

    default title = _("How do you want to name your save?")
    default dummy = str(save_name)

    add "gui/overlay/confirm.png"

    frame:
        xsize 1000
        ysize 250
        xalign 0.5
        yalign 0.5
        xpadding 25
        ypadding 25

        has vbox
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
                pixel_width 580
                allow ("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz1234567890!@#$&-_+?.,\'\":)(;*/")

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
                action Hide("save_name_input")
                keysym ("K_ESCAPE", "mouseup_3")
                hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_submenu_hover.mp3"
                activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"

            button:
                xalign 1.0
                left_padding 50
                top_padding 3
                idle_background "images/utility/menu/selected/edit.webp"
                hover_background "images/utility/menu/hover/edit.webp"
                text _("Save") style "renamer_text"
                selected True
                action [Function(fl_renamer, "save", dummy), FLFileAction(slot_name), Hide("save_name_input")]
                keysym ("K_RETURN", "K_KP_ENTER")
                hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_submenu_hover.mp3"
                activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"





init -501 screen renamer(what):

    modal True
    zorder 100
    default title = _("How do you want to name your save?") if (what == "save") else _("How do you want to rename this page?")
    default dummy = str(save_name) if (what == "save") else str(FilePageNameInputValue(pattern=_("Page {}")).get_text())

    frame:
        xsize 1000
        ysize 200
        xpos 670
        ypos 200
        xpadding 25
        ypadding 25
        has vbox

        order_reverse False

        spacing 25
        text title
        input:
            xalign 0.0
            xfill True
            value ScreenVariableInputValue("dummy", True, False)
            pixel_width 400
            allow ("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz1234567890!@#$&-_+?.,\'\":)(;*/")
        hbox:
            spacing 250
            button:
                xsize 250
                text _("Save") style "renamer_text"
                style style.button["menu_edit"]
                selected True
                action [Function(fl_renamer, what, dummy), Hide("renamer")]
                keysym ("K_RETURN", "K_KP_ENTER")

            button:
                xsize 250
                text _("Undo") style "renamer_text"
                style style.button["menu_return"] xpos 0 yalign 0 yoffset 0
                selected True
                action Hide("renamer")
                keysym "K_ESCAPE"





init -501 screen disclaimer():

    modal False

    $ disclaimer = _("Fetish Locator is intended for a mature audience\nof 18 years or older. Please abide by your local laws.\nAll characters are 18 years or older. No exceptions.\nThe characters in Fetish Locator explore relationships and their sexuality in both healthy and unhealthy ways. Some of these may be offensive to some players. Viewer discretion is advised. To that end, much of the content is optional and often there are alternative paths available. This is necessary to the story. The content explored should not be treated as an endorsement of particular fetishes, kinks, or patterns of behaviour. Please explore your own relationships and sexuality responsibly.\n\nEnjoy!")
    frame:
        xsize 1920
        ysize 1080
        xpos 0
        ypos 0
        xpadding 50
        ypadding 50
        background Solid("#000")
        text disclaimer style "disclaimer"

init -1 style disclaimer is text:
    yalign 0.5
    text_align 0.5
    font gui.text_font
    size 60
    color gui.accent_color
    outlines [ (absolute(2), "#e3436466", 2, 2) ]



init -501 screen skip_recap(jump_label, week):

    zorder 300

    if week == 1:
        hbox:
            style_prefix "skip_recap"
            ypos 845
            xalign 0.98
            textbutton _("Skip Recap\nof Week-1") action [Hide("skip_recap"), Jump(jump_label)]
    elif week == 2:
        hbox:
            style_prefix "skip_recap"
            ypos 845
            xalign 0.98
            textbutton _("Skip Recap\nof Week-2") action [Hide("skip_recap"), Jump(jump_label)]

init -1 style skip_recap_button:
    idle_background Frame("images/utility/menu/skip_idle.webp", 5, 5, 5, 5)
    hover_background Frame("images/utility/menu/skip_hover.webp", 5, 5, 5, 5)
    left_padding 15
    right_padding 15
    top_padding 15
    bottom_padding 10

init -1 style skip_recap_button_text:
    size 35
    line_spacing 5



init -501 screen patch_info():

    modal True

    add "images/utility/patch_info.webp"

    button id "menu_quit":
        text _("Quit"):
            idle_color gui.idle_color
            hover_color gui.hover_color
        style style.button["menu_quit"]
        action Quit(confirm=False)
        xalign 0.99
        yalign 0.99



init -501 screen save_sync_menu():

    modal True

    add "gui/overlay/confirm.png"

    frame:
        style_prefix "save_sync_menu"
        has vbox
        text _("Sync your saves using Ren'Py Sync server")
        null height 5
        textbutton _("Upload Saves") action UploadSync()
        textbutton _("Download Saves") action DownloadSync()
        textbutton _("Back") action Hide("save_sync_menu")

    key "game_menu" action Hide()

init -1 style save_sync_menu_frame:
    top_padding 50
    bottom_padding 40
    left_padding 50
    right_padding 50
    xalign 0.5
    yalign 0.5

init -1 style save_sync_menu_vbox:
    xalign 0.5
    spacing 20

init -1 style save_sync_menu_text is gui_label_text

init -1 style save_sync_menu_text:
    size 40
    xalign 0.5

init -1 style save_sync_menu_button:
    xalign 0.5



init 499 image tu_book1_steam_video_ad = Movie(play = "images/utility/tu_ad/tu-book1-steam-video-ad.webm", start_image = "black", image = "tu-book1-steam-video-ad_last_frame", loop = False)
init 499 image sm_trailer_ad = Movie(play = "images/utility/sm_ad/sm_trailer_video.webm", start_image = "black", image = "sm_trailer_last_frame", loop = False)

init -501 screen tu_trailer_ad():

    on "show" action PauseAudio('music', True)
    on "hide" action PauseAudio('music', False)

    modal True

    add "black" at image_opacity(0.8)

    imagebutton auto "images/utility/tu_ad/close_ad-button_%s.webp" action (SetVariable("persistent.hide_tu_trailer_ad", True), Hide()) xalign 0.95 yalign 0.06 at image_zoom(0.5)

    style_prefix "tu_trailer_ad"

    frame:
        modal True

        add "tu_book1_steam_video_ad" xsize 1344 ysize 756

    if is_gog_edition is True:
        textbutton _("{u}Get Taboo University Book 1 on GOG{/u}") action OpenURL("https://www.gog.com/en/game/taboo_university_book_one")
    else:
        textbutton _("{u}Get Taboo University Book 1 on Steam{/u}") action OpenURL("steam://openurl/https://store.steampowered.com/app/2459350/Taboo_University_Book_One/")

    key "game_menu" action (SetVariable("persistent.hide_tu_trailer_ad", True), Hide())

init -501 screen sm_trailer_ad():

    on "show" action PauseAudio('music', True)
    on "hide" action PauseAudio('music', False)

    modal True

    add "black" at image_opacity(0.8)

    imagebutton auto "images/utility/tu_ad/close_ad-button_%s.webp" action (SetVariable("persistent.hide_tu_trailer_ad", True), Hide()) xalign 0.95 yalign 0.06 at image_zoom(0.5)

    style_prefix "tu_trailer_ad"

    frame:
        modal True

        yalign 0.5

        add "sm_trailer_ad" xsize 1344 ysize 756

    if current_year == 2025:
        textbutton _("Wishlist Fetish Locator: S&M Studio on GOG") action OpenURL("https://www.gog.com/en/game/fetish_locator_sm_studio") text_size 55 xalign 0.5 yalign 0.96
    else:
        textbutton _("Get Fetish Locator: S&M Studio on GOG") action OpenURL("https://www.gog.com/en/game/fetish_locator_sm_studio") text_size 55 xalign 0.5 yalign 0.96

    key "game_menu" action (SetVariable("persistent.hide_tu_trailer_ad", True), Hide())

init -1 style tu_trailer_ad_frame:
    xalign 0.5
    yalign 0.25

init -1 style tu_trailer_ad_button:
    xalign 0.5
    yalign 0.92

init -1 style tu_trailer_ad_button_text:
    size 70
    idle_color "#FFFFFF"
    hover_color gui.accent_color
    outlines [(5, "#000000", 0, 0)]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
