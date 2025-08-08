









init -1 style default:
    properties gui.text_properties()
    language gui.language

init -1 style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

init -1 style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

init -1 style gui_text:
    properties gui.text_properties("interface")

init -1 style button:
    properties gui.button_properties("button")

init -1 style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

init -1 style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

init -1 style prompt_text is gui_text:
    properties gui.text_properties("prompt")

init -1 style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

init -1 style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

init -1 style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

init -1 style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

init -1 style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

init -1 style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"

init -1 style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)




















init -501 screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        background Transform(Frame("gui/textbox.png", xalign = 0.5, yalign = 1.0), alpha = persistent.dialogueboxopacity)

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

default -1 persistent.dialogueboxopacity = 1.0

init -1 python:
    config.character_id_prefixes.append('namebox')

init -1 style window is default
init -1 style say_label is default
init -1 style say_dialogue is default
init -1 style say_thought is say_dialogue

init -1 style namebox is default
init -1 style namebox_label is say_label

init -1 style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

init -1 style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

init -1 style say_label:
    properties gui.text_properties("name", accent=True)
    outlines [ (absolute(2), "#000", 0, 0) ]
    xalign gui.name_xalign
    yalign 0.5

init -1 style say_dialogue:
    properties gui.text_properties("dialogue")
    outlines [ (absolute(1), "#000", 0, 0) ]

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

init -1 style fl_text is say_dialogue:
    font "fonts/Oswald-Regular.ttf"











init -501 screen input(prompt):
    style_prefix "input"

    window:

        has vbox
        xpos gui.dialogue_xpos
        xsize gui.dialogue_width
        ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"

init -1 style input_prompt is default

init -1 style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

init -1 style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width










init -501 screen choice(items):

    style_prefix "choice"

    vbox:
        for i in items:

            $ hint = i.kwargs.get("hint", "none")

            hbox:
                xanchor 1.0
                xpos 1250
                spacing 60
                if persistent.menu_hints is True and is_there_a_hint(hint):
                    if renpy.variant("steam_deck"):
                        imagebutton auto "images/Utility/menu/menu_hint_%s.webp" yalign 0.5 action NullAction() hovered Function(show_menu_hint, hint) unhovered (Hide('notify'), Function(restore_notify_timeout))
                    else:
                        imagebutton auto "images/Utility/menu/menu_hint_%s.webp" yalign 0.5 action (Hide('notify'), i.action) hovered Function(show_menu_hint, hint) unhovered (Hide('notify'), Function(restore_notify_timeout))
                else:
                    null height 46 width 46

                textbutton i.caption action i.action

define -1 config.narrator_menu = True

init -1 style choice_vbox is vbox
init -1 style choice_button is button
init -1 style choice_button_text is button_text

init -1 style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5
    spacing gui.choice_spacing

init -1 style choice_button is default:
    properties gui.button_properties("choice_button")

init -1 style choice_button_text is default:
    properties gui.button_text_properties("choice_button")







init -501 screen quick_menu():

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            if persistent.menu_hints is True:
                textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=False) keysym "pad_x_press" alternate_keysym 'shift_K_s'
            else:
                textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True) keysym "pad_x_press"
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


init -1 python:
    config.overlay_screens.append("quick_menu")

default -1 quick_menu = True

init -1 style quick_button is default
init -1 style quick_button_text is button_text

init -1 style quick_button:
    properties gui.button_properties("quick_button")

init -1 style quick_button_text:
    properties gui.button_text_properties("quick_button")











init -501 screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:
            if (FLSS.week.cur > 1) and (len(FLSS.previous_mp_saves) > 0):
                button id "menu_loadmp":
                    text _("Continue from week [FLSS.week.prev]")
                    style style.button["menu_load_mp"]
                    action ShowMenu("load_mp")
            button id "menu_start":
                text _("Start")
                style style.button["menu_start"]
                action Start()
        else:
            if not main_menu:
                button id "menu_mainmenu":
                    text _("Main Menu")
                    style style.button["menu_mainmenu"]
                    action (Function(stop_all_sound), MainMenu())
            button id "menu_history":
                text _("History")
                style style.button["menu_history"]
                action ShowMenu("history")
            button id "menu_save":
                text _("Save")
                style style.button["menu_save"]
                action ShowMenu("save")
        button id "menu_load":
            text _("Load")
            style style.button["menu_load"]
            action ShowMenu("load")
        if (FLSS.week.cur > 1) and not (main_menu and (len(FLSS.previous_mp_saves) > 0) ):
            button id "menu_loadmp":
                text _("Continue from week [FLSS.week.prev]")
                style style.button["menu_load_mp"]
                action ShowMenu("load_mp")
        button id "menu_preferences":
            text _("Preferences")
            style style.button["menu_preferences"]
            action ShowMenu("preferences")
        if is_steam_edition is False and is_gog_edition is False:
            button id "menu_patreon":
                text _("Support on Patreon")
                style style.button["menu_patreon"]
                action OpenURL("https://www.patreon.com/fetishlocator")
        button id "menu_discord":
            text _("Join Discord")
            style style.button["menu_discord"]
            action OpenURL("https://discord.gg/efmQRNtFks")
        button id "menu_language_chooser":
            text _("Switch Language")
            style style.button["menu_language_chooser"]
            action ShowMenu("language_chooser")
        if main_menu:
            button id "menu_endings":
                text _("Endings")
                style style.button["menu_endings"]
                action ShowMenu("fl_endings")
        if is_extended_edition:
            button id "menu_cg_gallery":
                text _("CG Gallery")
                style style.button["menu_cg_gallery"]
                action ShowMenu("cg_gallery")
            if not _in_replay:
                button id "menu_replay_room":
                    text _("Replay Room")
                    style style.button["menu_replay_room"]
                    action ShowMenu("replay_room")
            else:
                button id "menu_end_replay":
                    text _("End Replay")
                    style style.button["menu_end_replay"]
                    action (Function(stop_all_sound), EndReplay(confirm=True))
            button id "menu_extra":
                text _("Bonus Content")
                style style.button["menu_extra"]
                action ShowMenu("extra")
        if preferences.language == "chinese":
            if main_menu:
                button id "menu_about":
                    text _("About")
                    style style.button["menu_about"]
                    action ShowMenu("about")
        else:
            button id "menu_about":
                text _("About")
                style style.button["menu_about"]
                action ShowMenu("about")
        if renpy.variant("pc"):
            button id "menu_help":
                text _("Help")
                style style.button["menu_help"]
                if renpy.variant("steam_deck"):
                    action ShowMenu("steam_deck_layout", False)
                else:
                    action ShowMenu("help")
            button id "menu_quit":
                text _("Quit")
                style style.button["menu_quit"]
                action Quit(confirm=not main_menu)

init -1 style navigation_button is gui_button
init -1 style navigation_button_text is gui_button_text

init -1 style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

init -1 style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

init -1 style navigation_text:
    selected_color gui.interface_text_color
    idle_color gui.idle_color
    hover_color gui.hover_color
    selected_hover_color gui.hover_color
    xsize 350







init -501 screen main_menu():
    tag menu


    if not persistent.hide_tu_trailer_ad:
        on "show" action Show("tu_trailer_ad")

    $ renpy.music.set_volume(volume=0.8, delay=1, channel='music')

    style_prefix "main_menu"

    if is_extended_edition:

        use main_menu_extended()

    else:
        add gui.main_menu_background

        frame


        use navigation

        vbox:
            text "v. [config.version][persistent.mp_info]":
                style "main_menu_version"
                at title_effect(0.3)

init -1:
    transform title_effect(pause):
        alpha 0.0
        pause pause
        linear 0.5 alpha 1.0

init -1 style main_menu_frame is empty
init -1 style main_menu_vbox is vbox
init -1 style main_menu_text is gui_text
init -1 style main_menu_title is main_menu_text
init -1 style main_menu_version is main_menu_text

init -1 style mainmenu_button is gui_button
init -1 style mainmenu_button_text is gui_button_text

init -1 style mainmenu_button:
    properties gui.button_properties("navigation_button")

init -1 style mainmenu_button_text:
    properties gui.button_text_properties("navigation_button")

init -1 style mainmenu_text:
    idle_color "#ffffff"
    hover_color "#ff486e"
    size gui.mainmenu_text_size

init -1 style main_menu_frame:
    xsize 420
    yfill True
    background "gui/overlay/main_menu.png"

init -1 style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

init -1 style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

init -1 style main_menu_title:
    properties gui.text_properties("title")

init -1 style main_menu_version:
    properties gui.text_properties("version")










init -501 screen game_menu(title, scroll=None, yinitial=0.0):

    if notify_timeout is False:
        on 'show' action Function(hide_hover_notify)

    if persistent.chose_lang is True:
        on 'show' action PauseAudio('music', True)
        on 'show' action PauseAudio('music2', True)
        on 'show' action PauseAudio('music3', True)
        on 'show' action PauseAudio('sound', True)
        on 'show' action PauseAudio('sound2', True)
        on 'show' action PauseAudio('sound3', True)
        on 'show' action PauseAudio('sound4', True)
        on 'show' action PauseAudio('sound5', True)
        on 'show' action PauseAudio('sound6', True)
        on 'show' action PauseAudio('voice2', True)
        on 'show' action PauseAudio('voice3', True)
        on 'show' action PauseAudio('voice4', True)
        on 'show' action PauseAudio('voice5', True)
        on 'show' action PauseAudio('voice6', True)
        on 'show' action PauseAudio('voice7', True)
        on 'show' action PauseAudio('voice8', True)
        on 'show' action Function(Lovense.stop)

    style_prefix "game_menu"

    if main_menu and is_extended_edition:
        if title == "Load":
            add "mm_load_crush_effect"
        elif title == "Preferences":
            add "mm_settings_crush_effect"
        elif title == "Switch Language":
            add "mm_translate_crush_effect"
        else:
            add gui.main_menu_background

        if preferences.get_volume("music") != 0.0:
            add "fl_logo_eq_effect" xpos 640 ypos 83
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        has hbox

        frame:
            style "game_menu_navigation_frame"

        frame:

            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial yinitial

                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation

    button id "menu_return":
        text _("Return") style "navigation_text"
        style style.button["menu_return"]
        action Return()
        keysym "pad_b_press"

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


init -1 style game_menu_outer_frame is empty
init -1 style game_menu_navigation_frame is empty
init -1 style game_menu_content_frame is empty
init -1 style game_menu_viewport is gui_viewport
init -1 style game_menu_side is gui_side
init -1 style game_menu_scrollbar is gui_vscrollbar

init -1 style game_menu_label is gui_label
init -1 style game_menu_label_text is gui_label_text

init -1 style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

init -1 style game_menu_navigation_frame:
    xsize 420
    yfill True

init -1 style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

init -1 style game_menu_viewport:
    xsize 1380

init -1 style game_menu_vscrollbar:
    unscrollable gui.unscrollable

init -1 style game_menu_side:
    spacing 15

init -1 style game_menu_label:
    xpos 75
    ysize 180

init -1 style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5








init -501 screen about():
    tag menu
    default about_page = "game"



    predict False

    use game_menu(_("About")):

        vbox:
            hbox:
                style_prefix "about"
                xsize 1380

                textbutton _("Game") action SetScreenVariable("about_page", "game") xalign 0.5
                if is_extended_edition is False:
                    textbutton _("Sound Effects") action SetScreenVariable("about_page", "sound") xalign 0.5
                else:
                    textbutton _("Soundtracks") action SetScreenVariable("about_page", "music") xalign 0.5
                    textbutton _("Sound Effects") action SetScreenVariable("about_page", "sound_ext") xalign 0.5
                    textbutton _("Other Sounds") action SetScreenVariable("about_page", "sound_ext2") xalign 0.5
                textbutton _("Others") action SetScreenVariable("about_page", "others") xalign 0.5

            null height 50

            if about_page == "game":
                use about_game
            elif about_page == "sound":
                use about_sound
            elif about_page == "music":
                use about_music
            elif about_page == "sound_ext":
                use about_sound_ext
            elif about_page == "sound_ext2":
                use about_sound_ext2
            elif about_page == "others":
                use about_others

init -501 screen about_game():

    vbox:
        style_prefix "about"

        vbox:
            xpos -50
            spacing -40
            add "fl_title"
            if is_extended_edition is True:
                hbox:
                    xsize 780
                    add "ee_subtitle" xpos 45
                    text "v. [config.version]":
                        style "main_menu_version"
                        xalign 1.0
                        yalign 0.7
            else:
                hbox:
                    xsize 780
                    add "fl_subtitle" xpos 45
                    text "v. [config.version]":
                        style "main_menu_version"
                        xalign 1.0
                        yalign 0.7

        null height 50

        if gui.about:
            text "[gui.about!t]\n"

        null height 50

        text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]\n")

init -501 screen about_music():

    viewport:
        yinitial 0.0
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True

        has vbox
        style_prefix "about"

        text "[gui.credits_audio_ext!t]"

init -501 screen about_sound():

    viewport:
        yinitial 0.0
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True

        has vbox
        style_prefix "about"

        text "[gui.credits_sounds_incipit!t]"
        text "[gui.credits_audio!t]"

init -501 screen about_sound_ext():

    viewport:
        yinitial 0.0
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True

        has vbox
        style_prefix "about"

        text "[gui.credits_audio_ext_effects!t]"

init -501 screen about_sound_ext2():

    viewport:
        yinitial 0.0
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True

        has vbox
        style_prefix "about"

        text "[gui.credits_audio_ext_ambient!t]"
        text "[gui.credits_sounds_incipit!t]"
        text "[gui.credits_audio!t]"

init -501 screen about_others():

    vbox:
        style_prefix "about"

        text "[gui.credits_more!t]"

init -1 style about_button:
    idle_background Frame("images/utility/menu/skip_idle.webp", 5, 5, 5, 5)
    hover_background Frame("images/utility/menu/skip_hover.webp", 5, 5, 5, 5)
    selected_background Frame("images/utility/menu/skip_selected.webp", 5, 5, 5, 5)
    selected_hover_background Frame("images/utility/menu/skip_hover.webp", 5, 5, 5, 5)
    hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_submenu_hover.mp3"
    activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"
    left_padding 15
    right_padding 15
    top_padding 15
    bottom_padding 10

init -1 style about_button_text:
    selected_hover_color gui.hover_color

init -1 style about_label is gui_label
init -1 style about_label_text is gui_label_text
init -1 style about_text is gui_text

init -1 style about_label_text:
    size gui.label_text_size








default -1 persistent.save_name_prompt = True

init -501 screen save():
    tag menu


    use file_slots(_("Save"), "save")


init -501 screen load():
    tag menu


    use file_slots(_("Load"), "load")

init -501 screen file_slots(title, what):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"), default=False)
    $ pager = Pager()

    use game_menu(title):

        fixed:

            hbox:
                style_prefix "renamer"
                xsize 1250
                xpos 84
                ypos 0
                hbox:
                    if pager.int > 0:
                        button:
                            text page_name_value.get_text()
                            style style.button["menu_edit"]
                            selected True
                            action Show("renamer", None, "page")
                    else:
                        text page_name_value.get_text():
                            xalign 0.0
                            color gui.interface_text_color

                    null width 50

                if CurrentScreenName() == "save":
                    hbox:
                        xalign 1.0
                        text _("Naming save file:"):
                            xalign 1.0
                            color gui.idle_color
                        null width 15
                        textbutton _("Enabled" ) selected (    persistent.save_name_prompt) action SetVariable("persistent.save_name_prompt", True)
                        null width 5
                        text "/"
                        null width 5
                        textbutton _("Disabled") selected (not persistent.save_name_prompt) action [SetVariable("persistent.save_name_prompt", False), SetVariable("save_name", "")]

                else:
                    if config.has_sync:
                        hbox:
                            xalign 1.0
                            textbutton _("Ren'Py Save Sync") action ShowMenu("save_sync_menu")

            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        if what == "load":
                            action FLFileAction(slot)
                        else:
                            if persistent.save_name_prompt is True and pager.int > 0:
                                action [SetVariable("slot_name", slot), ShowMenu("save_name_input")]
                            else:
                                action FLFileAction(slot)

                        vbox:

                            add FileScreenshot(slot) xalign 0.5

                            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                style "slot_time_text"

                            text FileSaveName(slot):
                                style "slot_name_text"

                            if FileLoadable(slot):
                                imagebutton auto "images/utility/menu/delete_%s.webp" action FLFileDelete(slot) focus_mask "images/utility/menu/delete_mask.webp" xalign 0.03 ypos -250

                            key "save_delete" action FLFileDelete(slot)

            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                if pager.int > 10:
                    textbutton _("«") action FilePage(pager.int - 10)

                if pager.int > 1:
                    textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                for page in pager.rng:
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()

                textbutton _("»") action FilePage(pager.int + 10)

init -1 style renamer_text:
    yalign 0.5
    selected_color gui.interface_text_color
    idle_color gui.idle_color
    hover_color gui.hover_color
    selected_hover_color gui.hover_color

init -1 style renamer_hbox:
    ysize 50

init -1 style renamer_button is gui_button
init -1 style renamer_button_text is gui_button_text

init -1 style page_label is gui_label
init -1 style page_label_text is gui_label_text
init -1 style page_button is gui_button
init -1 style page_button_text is gui_button_text

init -1 style slot_button is gui_button
init -1 style slot_button_text is gui_button_text
init -1 style slot_time_text is slot_button_text
init -1 style slot_name_text is slot_button_text

init -1 style renamer_button:
    hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_submenu_hover.mp3"
    activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"

init -1 style page_button:
    hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_submenu_hover.mp3"
    activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"

init -1 style slot_button:
    properties gui.button_properties("slot_button")
    hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_submenu_hover.mp3"
    activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"

init -1 style slot_button_text:
    properties gui.button_text_properties("slot_button")









init -501 screen preferences():
    tag menu


    use game_menu(_("Preferences"), scroll="viewport"):
        vbox:
            hbox:
                box_wrap True
                if is_steam_edition is False and is_gog_edition is False:
                    spacing 80
                if renpy.variant("pc"):
                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")
                        textbutton "1920 x 1080" action Preference("display", 1.0)
                        textbutton "1600 x 900" action Preference("display", 0.83333333333)
                        textbutton "1280 x 720" action Preference("display", 0.666666666667)
                        textbutton "960 × 540" action Preference("display", 0.5)

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                if is_antagonist_mode is True:
                    vbox:
                        style_prefix "radio"
                        label _("Taboo Mode")
                        textbutton _("Enabled" ) selected (    persistent.is_special) action SetVariable("persistent.is_special", True )
                        textbutton _("Disabled") selected (not persistent.is_special) action SetVariable("persistent.is_special", False)

            null height gui.pref_spacing

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                    label _("Dialogue Box Opacity")

                    bar value FieldValue(persistent, "dialogueboxopacity", range = 1.0, style = "slider")

                    null height 50

                    textbutton _("Connect Your Toy"):
                        action ShowMenu("lovense_connect")
                        idle_background "images/utility/lovense/lovense_logo_idle.webp"
                        hover_background "images/utility/lovense/lovense_logo_hover.webp"
                        focus_mask "images/utility/lovense/lovense_button_mask.webp"
                        style "lovense_pref_button"

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice and is_extended_edition:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

                    if not is_extended_edition:
                        null height 20
                        frame:
                            xsize 525
                            background None
                            text _("Music, Voice and Sound Effects are only implemented in the Extended Edition of the game")

init -1 style pref_label is gui_label
init -1 style pref_label_text is gui_label_text
init -1 style pref_vbox is vbox

init -1 style radio_label is pref_label
init -1 style radio_label_text is pref_label_text
init -1 style radio_button is gui_button
init -1 style radio_button_text is gui_button_text
init -1 style radio_vbox is pref_vbox

init -1 style check_label is pref_label
init -1 style check_label_text is pref_label_text
init -1 style check_button is gui_button
init -1 style check_button_text is gui_button_text
init -1 style check_vbox is pref_vbox

init -1 style slider_label is pref_label
init -1 style slider_label_text is pref_label_text
init -1 style slider_slider is gui_slider
init -1 style slider_button is gui_button
init -1 style slider_button_text is gui_button_text
init -1 style slider_pref_vbox is pref_vbox

init -1 style mute_all_button is check_button
init -1 style mute_all_button_text is check_button_text

init -1 style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

init -1 style pref_label_text:
    yalign 1.0

init -1 style pref_vbox:
    xsize 338

init -1 style radio_vbox:
    spacing gui.pref_button_spacing

init -1 style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"
    hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_submenu_hover.mp3"
    activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"

init -1 style radio_button_text:
    properties gui.button_text_properties("radio_button")

init -1 style check_vbox:
    spacing gui.pref_button_spacing

init -1 style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"
    hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_submenu_hover.mp3"
    activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"

init -1 style check_button_text:
    properties gui.button_text_properties("check_button")

init -1 style slider_slider:
    xsize 525

init -1 style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

init -1 style slider_button_text:
    properties gui.button_text_properties("slider_button")

init -1 style slider_vbox:
    xsize 675

init -1 style lovense_pref_button_text:
    idle_color "#ff2d89"
    hover_color "#ffffff"
    size 38
    yoffset 45










init -501 screen history():
    tag menu


    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                has fixed
                yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


define -1 gui.history_allow_tags = set()

init -1 style history_window is empty

init -1 style history_name is gui_label
init -1 style history_name_text is gui_label_text
init -1 style history_text is gui_text

init -1 style history_text is gui_text

init -1 style history_label is gui_label
init -1 style history_label_text is gui_label_text

init -1 style history_window:
    xfill True
    ysize gui.history_height

init -1 style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

init -1 style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

init -1 style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

init -1 style history_label:
    xfill True

init -1 style history_label_text:
    xalign 0.5







init -501 screen help():
    tag menu


    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


init -501 screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


init -501 screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


init -501 screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


init -1 style help_button is gui_button
init -1 style help_button_text is gui_button_text
init -1 style help_label is gui_label
init -1 style help_label_text is gui_label_text
init -1 style help_text is gui_text

init -1 style help_button:
    properties gui.button_properties("help_button")
    xmargin 12
    hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_submenu_hover.mp3"
    activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"

init -1 style help_button_text:
    properties gui.button_text_properties("help_button")

init -1 style help_label:
    xsize 375
    right_padding 30

init -1 style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0














init -501 screen confirm(message, yes_action, no_action):

    on 'show' action Play("sound", "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_submenu_delete_save.mp3", loop = False)

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox
        xalign .5
        yalign .5
        spacing 45

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 150

            textbutton _("Yes") action (Function(Lovense.stop), yes_action) keysym ("K_RETURN", "K_KP_ENTER")
            textbutton _("No") action no_action

    key "game_menu" action no_action


init -1 style confirm_frame is gui_frame
init -1 style confirm_prompt is gui_prompt
init -1 style confirm_prompt_text is gui_prompt_text
init -1 style confirm_button is gui_medium_button
init -1 style confirm_button_text is gui_medium_button_text

init -1 style confirm_frame:
    background Frame(["gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

init -1 style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

init -1 style confirm_button:
    properties gui.button_properties("confirm_button")
    hover_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_submenu_hover.mp3"
    activate_sound "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"

init -1 style confirm_button_text:
    properties gui.button_text_properties("confirm_button")









init -501 screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox
        spacing 9

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


transform -1 delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


init -1 style skip_frame is empty
init -1 style skip_text is gui_text
init -1 style skip_triangle is skip_text

init -1 style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

init -1 style skip_text:
    size gui.notify_text_size

init -1 style skip_triangle:
    font "DejaVuSans.ttf"









default -1 notify_timeout = True

init -501 screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!t]"

    if notify_timeout is True:
        timer 3 action Hide('notify')


transform -1 notify_appear:
    on show:
        ypos -100
        easein 0.25 ypos 20
    on hide:
        easein 0.25 ypos -100


init -1 style notify_frame is empty
init -1 style notify_text is gui_text

init -1 style notify_frame:
    xalign 0.5

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

init -1 style notify_text:
    properties gui.text_properties("notify")









init -501 screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox
        spacing gui.nvl_spacing

        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


init -501 screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed
            yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id


define -1 config.nvl_list_length = gui.nvl_list_length

init -1 style nvl_window is default
init -1 style nvl_entry is default

init -1 style nvl_label is say_label
init -1 style nvl_dialogue is say_dialogue

init -1 style nvl_button is button
init -1 style nvl_button_text is button_text

init -1 style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

init -1 style nvl_entry:
    xfill True
    ysize gui.nvl_height

init -1 style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

init -1 style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init -1 style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init -1 style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

init -1 style nvl_button_text:
    properties gui.button_text_properties("nvl_button")





init -501 screen quick_menu():

    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()

init -1 style quick_button_text:
    variant "small"
    size 28
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
