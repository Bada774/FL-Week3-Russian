









init -2 python:
    gui.init(1920, 1080)








define -2 config.default_text_cps = 75






define -2 gui.accent_color = '#e34364'


define -2 gui.idle_color = '#888888'



define -2 gui.idle_small_color = '#aaaaaa'


define -2 gui.hover_color = '#f05172'



define -2 gui.selected_color = '#ffffff'


define -2 gui.insensitive_color = '#8888887f'



define -2 gui.muted_color = '#610e1f'
define -2 gui.hover_muted_color = '#80001a'


define -2 gui.text_color = '#ffffff'
define -2 gui.interface_text_color = '#ffffff'






define -2 gui.text_font = "fonts/Andika-Regular.ttf"



define -2 gui.name_text_font = "fonts/new/KaushanScript-Regular.ttf"



define -2 gui.interface_text_font = "fonts/Andika-Regular.ttf"


define -2 gui.text_size = 33


define -2 gui.name_text_size = 45


define -2 gui.interface_text_size = 33

define -2 gui.mainmenu_text_size = 45


define -2 gui.label_text_size = 36


define -2 gui.notify_text_size = 24


define -2 gui.title_text_size = 75
define -2 gui.title_text_font = gui.name_text_font
define -2 gui.title_text_outlines = [ (absolute(6), "#0006", 3, 3) ]
define -2 gui.version_text_outlines = [ (absolute(1), "#0006", 1, 1) ]





init 1 python:
    for i in ("menu_about", "menu_endings", "menu_cg_gallery", "menu_discord", "menu_edit", "menu_end_replay", "menu_extra", "menu_help", "menu_history", "menu_hint", "menu_language_chooser", "menu_load_mp", "menu_load", "menu_mainmenu", "menu_patreon", "menu_preferences", "menu_return", "menu_quit", "menu_replay_room", "menu_save", "menu_start"):
        j = i[5:]
        style.button[i].idle_background             = "images/utility/menu/idle/{0}.webp".format(j)
        style.button[i].hover_background            = "images/utility/menu/hover/{0}.webp".format(j)
        style.button[i].selected_background         = "images/utility/menu/selected/{0}.webp".format(j)
        style.button[i].selected_idle_background    = "images/utility/menu/selected/{0}.webp".format(j)
        style.button[i].selected_hover_background   = "images/utility/menu/hover/{0}.webp".format(j)
        style.button[i].insensitive_background      = "images/utility/menu/selected/{0}.webp".format(j)
        style.button[i].left_padding                = 50
        style.button[i].hover_sound                 = "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_submenu_hover.mp3"
        style.button[i].activate_sound              = "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"
    style.button["menu_return"].xpos                = gui.navigation_xpos
    style.button["menu_return"].yalign              = 1.0
    style.button["menu_return"].yoffset             = -45
    style.button["menu_hint"].left_padding          = 0



    if is_extended_edition:
        gui.main_menu_background = "images/extended/ui/mm_bg_main.webp"
    else:
        gui.main_menu_background = "gui/main_menu.png"

    gui.game_menu_background = gui.main_menu_background



define -2 gui.mm_bg_borders = Borders(60, 10, 25, 10)







define -2 gui.textbox_height = 278



define -2 gui.textbox_yalign = 1.0




define -2 gui.name_xpos = 360
define -2 gui.name_ypos = -3



define -2 gui.name_xalign = 0.0



define -2 gui.namebox_width = None
define -2 gui.namebox_height = None



define -2 gui.namebox_borders = Borders(5, 5, 5, 5)



define -2 gui.namebox_tile = False





define -2 gui.dialogue_xpos = 402
define -2 gui.dialogue_ypos = 75


define -2 gui.dialogue_width = 1116



define -2 gui.dialogue_text_xalign = 0.0








define -2 gui.button_width = None
define -2 gui.button_height = None


define -2 gui.button_borders = Borders(6, 6, 6, 6)



define -2 gui.button_tile = False


define -2 gui.button_text_font = gui.interface_text_font


define -2 gui.button_text_size = gui.interface_text_size


define -2 gui.button_text_idle_color = gui.idle_color
define -2 gui.button_text_hover_color = gui.hover_color
define -2 gui.button_text_selected_color = gui.selected_color
define -2 gui.button_text_insensitive_color = gui.insensitive_color



define -2 gui.button_text_xalign = 0.0








define -2 gui.radio_button_borders = Borders(27, 6, 6, 6)

define -2 gui.check_button_borders = Borders(27, 6, 6, 6)

define -2 gui.confirm_button_text_xalign = 0.5

define -2 gui.page_button_borders = Borders(15, 6, 15, 6)

define -2 gui.quick_button_borders = Borders(15, 6, 15, 0)
define -2 gui.quick_button_text_size = 21
define -2 gui.quick_button_text_idle_color = gui.idle_small_color
define -2 gui.quick_button_text_selected_color = gui.accent_color












define -2 gui.choice_button_width = 1185
define -2 gui.choice_button_height = None
define -2 gui.choice_button_tile = False
define -2 gui.choice_button_borders = Borders(150, 8, 150, 8)
define -2 gui.choice_button_text_font = gui.text_font
define -2 gui.choice_button_text_size = gui.text_size
define -2 gui.choice_button_text_xalign = 0.5
define -2 gui.choice_button_text_idle_color = "#cccccc"
define -2 gui.choice_button_text_hover_color = "#ffffff"
define -2 gui.choice_button_text_insensitive_color = "#444444"









define -2 gui.slot_button_width = 414
define -2 gui.slot_button_height = 309
define -2 gui.slot_button_borders = Borders(15, 15, 15, 15)
define -2 gui.slot_button_text_size = 21
define -2 gui.slot_button_text_xalign = 0.5
define -2 gui.slot_button_text_idle_color = gui.idle_small_color
define -2 gui.slot_button_text_selected_idle_color = gui.selected_color
define -2 gui.slot_button_text_selected_hover_color = gui.hover_color


define -2 config.thumbnail_width = 384
define -2 config.thumbnail_height = 216


define -2 gui.file_slot_cols = 3
define -2 gui.file_slot_rows = 2









define -2 gui.navigation_xpos = 20


define -2 gui.skip_ypos = 105





define -2 gui.choice_spacing = 33


define -2 gui.navigation_spacing = 6


define -2 gui.pref_spacing = 15


define -2 gui.pref_button_spacing = 0


define -2 gui.page_spacing = 0


define -2 gui.slot_spacing = 15


define -2 gui.main_menu_text_xalign = 1.0








define -2 gui.frame_borders = Borders(6, 6, 6, 6)


define -2 gui.confirm_frame_borders = Borders(60, 60, 60, 60)


define -2 gui.skip_frame_borders = Borders(24, 8, 75, 8)


define -2 gui.notify_frame_borders = Borders(15, 10, 15, 10)


define -2 gui.frame_tile = False











define -2 gui.bar_size = 38
define -2 gui.scrollbar_size = 18
define -2 gui.slider_size = 38


define -2 gui.bar_tile = False
define -2 gui.scrollbar_tile = False
define -2 gui.slider_tile = False


define -2 gui.bar_borders = Borders(6, 6, 6, 6)
define -2 gui.scrollbar_borders = Borders(6, 6, 6, 6)
define -2 gui.slider_borders = Borders(6, 6, 6, 6)


define -2 gui.vbar_borders = Borders(6, 6, 6, 6)
define -2 gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define -2 gui.vslider_borders = Borders(6, 6, 6, 6)



define -2 gui.unscrollable = "hide"







define -2 config.history_length = 250



define -2 gui.history_height = 210



define -2 gui.history_name_xpos = 233
define -2 gui.history_name_ypos = 0
define -2 gui.history_name_width = 233
define -2 gui.history_name_xalign = 1.0


define -2 gui.history_text_xpos = 255
define -2 gui.history_text_ypos = 3
define -2 gui.history_text_width = 1110
define -2 gui.history_text_xalign = 0.0







define -2 gui.nvl_borders = Borders(0, 15, 0, 30)



define -2 gui.nvl_list_length = 6



define -2 gui.nvl_height = 173



define -2 gui.nvl_spacing = 15



define -2 gui.nvl_name_xpos = 645
define -2 gui.nvl_name_ypos = 0
define -2 gui.nvl_name_width = 225
define -2 gui.nvl_name_xalign = 1.0


define -2 gui.nvl_text_xpos = 675
define -2 gui.nvl_text_ypos = 12
define -2 gui.nvl_text_width = 885
define -2 gui.nvl_text_xalign = 0.0



define -2 gui.nvl_thought_xpos = 360
define -2 gui.nvl_thought_ypos = 0
define -2 gui.nvl_thought_width = 1170
define -2 gui.nvl_thought_xalign = 0.0


define -2 gui.nvl_button_xpos = 675
define -2 gui.nvl_button_xalign = 0.0







define -2 gui.language = "unicode"





init -2 python:

    if renpy.variant("touch"):
        gui.quick_button_borders = Borders(60, 21, 60, 0)

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
