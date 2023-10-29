



init python:
    for i in ("lang_en", "lang_cn", "lang_pt", "lang_es", "lang_ko", "lang_it", "lang_ms", "lang_ru", "lang_tr"):
        j = i[5:]
        style.button[i].idle_background             = "images/utility/flags/flag_{0}_idle.webp".format(j)
        style.button[i].hover_background            = "images/utility/flags/flag_{0}_hover.webp".format(j)
        style.button[i].selected_background         = "images/utility/flags/flag_{0}_selected.webp".format(j)
        style.button[i].selected_idle_background    = "images/utility/flags/flag_{0}_selected_idle.webp".format(j)
        style.button[i].selected_hover_background   = "images/utility/flags/flag_{0}_hover.webp".format(j)
        style.button[i].hover_sound                 = "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_submenu_hover.mp3"
        style.button[i].activate_sound              = "audio/loudlout/extended/sfx/fl3_ui_sfx/sfx_menu_button_click.mp3"
        style.button[i].xsize                       = 300
        style.button[i].ysize                       = 200
        style.button[i].top_padding                 = 170

screen language_buttons(splash=False):

    grid 3 3:
        style_prefix "language"
        xpos 100
        yalign 0.5
        spacing 100

        button id "lang_en":
            text "English"
            style style.button["lang_en"]
            selected (preferences.language == None)
            if splash is False:
                action Function(language_setter, newlang=None)
            else:
                action (Function(language_setter, newlang=None), Return())

        button id "lang_cn":
            text "{font=fonts/Arial-Unicode.ttf}中文{/font}"
            style style.button["lang_cn"]
            selected (preferences.language == "chinese")
            if splash is False:
                action Function(language_setter, newlang="chinese")
            else:
                action (Function(language_setter, newlang="chinese"), Return())

        button id "lang_pt":
            text "Português"
            style style.button["lang_pt"]
            selected (preferences.language == "portuguese")
            if splash is False:
                action Function(language_setter, newlang="portuguese")
            else:
                action (Function(language_setter, newlang="portuguese"), Return())

        button id "lang_es":
            text "Español"
            style style.button["lang_es"]
            selected (preferences.language == "spanish")
            if splash is False:
                action Function(language_setter, newlang="spanish")
            else:
                action (Function(language_setter, newlang="spanish"), Return())

        button id "lang_tr":
            text "Türkçe"
            style style.button["lang_tr"]
            selected (preferences.language == "turkish")
            if splash is False:
                action Function(language_setter, newlang="turkish")
            else:
                action (Function(language_setter, newlang="turkish"), Return())
        button id "lang_ru":
            text "Русский"
            style style.button["lang_ru"]
            if splash is False:
                action Function(language_setter, newlang="russian")
            else:
                action (Function(language_setter, newlang="russian"), Return())

        if config.developer is True:
            button id "lang_ko":
                text "{font=fonts/Arial-Unicode.ttf}한국어{/font}"
                style style.button["lang_ko"]
                selected (preferences.language == "korean")
                if splash is False:
                    action Function(language_setter, newlang="korean")
                else:
                    action (Function(language_setter, newlang="korean"), Return())

            button id "lang_it":
                text "Italiano"
                style style.button["lang_it"]
                selected (preferences.language == "italian")
                if splash is False:
                    action Function(language_setter, newlang="italian")
                else:
                    action (Function(language_setter, newlang="italian"), Return())

            button id "lang_ms":
                text "Malay"
                style style.button["lang_ms"]
                selected (preferences.language == "malay")
                if splash is False:
                    action Function(language_setter, newlang="malay")
                else:
                    action (Function(language_setter, newlang="malay"), Return())

        else:
            null height 200 width 300
            null height 200 width 300
            null height 200 width 300

screen language_chooser():
    tag menu


    use game_menu(_("Switch Language"), scroll="viewport", yinitial=1.0):

        use language_buttons(False)

screen language_chooser_splash():

    modal True

    add "black"
    add "images/utility/fl-loading-logo.webp" xalign 0.65 yalign 0.5 at image_opacity(0.13)

    label _("Choose Language") xalign 0.5 style "game_menu_label"

    frame:
        style_prefix "language"
        use language_buttons(True)

style language_text:
    selected_color gui.interface_text_color
    idle_color gui.idle_color
    hover_color gui.hover_color
    selected_hover_color gui.hover_color
    xalign 0.5
    yanchor 0.0

style language_frame:
    background None
    xalign 0.4
    yalign 0.75



translate chinese style default:
    font "fonts/Arial-Unicode.ttf"

translate chinese style mainmenu_text:
    font "fonts/Arial-Unicode.ttf"
    size 35

translate chinese style navigation_text:
    font "fonts/Arial-Unicode.ttf"
    size 28
    ypos -5

translate chinese style slot_button_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style fl_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style say_label:
    font "fonts/MaShanZheng-Regular.ttf"

translate chinese style choice_button_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style confirm_prompt_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style confirm_button_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style history_name_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style history_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style history_label_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style help_button_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style help_label_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style help_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style pref_label_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style radio_button_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style check_button_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style slider_button_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style about_label_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style about_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style quick_button_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style notify_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style skip_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style gui_label_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style overlay_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style fl_points_button_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style sex_counter_button_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style pool_button_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style renamer_text:
    font "fonts/Arial-Unicode.ttf"
    ypos -5

translate chinese style renamer_button_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style free_roam_button_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style prologue_button_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style prologue_yta_button_text:
    font "fonts/Arial-Unicode.ttf"
    size 36

translate chinese style disclaimer:
    font "fonts/Arial-Unicode.ttf"
    size 50

translate chinese style skip_recap_button_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style sub_menu_bonus_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style sub_menu_play_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style ext_mm_text:
    font "fonts/Arial-Unicode.ttf"
    size 35

translate chinese style skip_recap_button:
    top_padding 10

translate chinese style scene_transistion_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style game_end_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style connect_toy_button_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style lovense_connect_button_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style lovense_pref_button_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style lovense_test_button_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style prologue_yes_button_text:
    font "fonts/Arial-Unicode.ttf"
    size 30

translate chinese style prologue_no_button_text:
    font "fonts/Arial-Unicode.ttf"
    size 30

translate chinese style prologue_no_sp_button_text:
    font "fonts/Arial-Unicode.ttf"
    size 30
    xpos -30

translate chinese style prologue_yes_button:
    left_padding 16
    right_padding 18
    top_padding 8
    bottom_padding 10

translate chinese style prologue_no_button:
    left_padding 16
    right_padding 18
    top_padding 8
    bottom_padding 10

translate chinese style prologue_no_sp_button:
    xsize 95
    ysize 60
    top_padding 8
    bottom_padding 10

translate chinese style prologue_yta_button:
    top_padding 6

translate chinese style lovense_connect_button:
    top_padding 6

translate chinese style prologue_name_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style prologue_fetishes_text:
    font "fonts/Arial-Unicode.ttf"
    size 50

translate chinese style ending_menu_label_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style about_button_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style ending_screen_start_text:
    ypos -4

translate chinese style ending_screen_return_text:
    ypos -4

translate chinese style hint_text:
    ypos -10

translate spanish style no_mp_title_text:
    size 40

translate spanish style no_mp_subtitle_text:
    size 27

translate chinese style fetish_selection_button_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style thank_you_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style credits_roll_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style credit_start_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style ending_start_screen_label_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style dark_character:
    font "fonts/MaShanZheng-Regular.ttf"
    kerning 0

translate chinese style mpb_large_odd_text:
    ypos -8

translate chinese style mpb_large_even_text:
    ypos -8

translate chinese style bonus_high_score_text:
    font "fonts/Arial-Unicode.ttf"
    xpos 1500

translate chinese style bonus_front_nine_text:
    font "fonts/Arial-Unicode.ttf"

translate chinese style bonus_change_mind_text_1:
    font "fonts/Arial-Unicode.ttf"
    size 60

translate chinese style bonus_change_mind_text_2:
    font "fonts/Arial-Unicode.ttf"
    xpos 1050
    ypos 830

translate chinese style bonus_rm_rf_text_1:
    font "fonts/Arial-Unicode.ttf"

translate chinese style bonus_rm_rf_text_2:
    font "fonts/Arial-Unicode.ttf"

translate chinese style bonus_rm_rf_text_3:
    font "fonts/Arial-Unicode.ttf"

translate chinese style bonus_cherry_popped_text_big:
    font "fonts/Arial-Unicode.ttf"

translate chinese style bonus_cherry_popped_text_small:
    font "fonts/Arial-Unicode.ttf"

translate chinese style bonus_trade_text_title:
    font "fonts/Arial-Unicode.ttf"

translate chinese style bonus_trade_text_body:
    font "fonts/Arial-Unicode.ttf"



translate korean style default:
    font "fonts/Arial-Unicode.ttf"

translate korean style mainmenu_text:
    font "fonts/Arial-Unicode.ttf"
    size 35

translate korean style navigation_text:
    font "fonts/Arial-Unicode.ttf"
    size 28
    ypos -5

translate korean style slot_button_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style fl_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style say_label:
    font "fonts/Arial-Unicode.ttf"

translate korean style choice_button_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style confirm_prompt_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style confirm_button_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style history_name_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style history_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style history_label_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style help_button_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style help_label_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style help_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style pref_label_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style radio_button_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style check_button_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style slider_button_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style about_label_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style about_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style quick_button_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style notify_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style skip_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style gui_label_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style overlay_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style fl_points_button_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style sex_counter_button_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style pool_button_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style renamer_text:
    font "fonts/Arial-Unicode.ttf"
    ypos -5

translate korean style renamer_button_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style free_roam_button_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style prologue_button_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style prologue_yta_button_text:
    font "fonts/Arial-Unicode.ttf"
    size 36

translate korean style disclaimer:
    font "fonts/Arial-Unicode.ttf"
    size 50

translate korean style skip_recap_button_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style sub_menu_bonus_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style sub_menu_play_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style ext_mm_text:
    font "fonts/Arial-Unicode.ttf"
    size 35

translate korean style skip_recap_button:
    top_padding 10

translate korean style scene_transistion_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style game_end_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style connect_toy_button_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style lovense_connect_button_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style lovense_pref_button_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style lovense_test_button_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style prologue_yes_button_text:
    font "fonts/Arial-Unicode.ttf"
    size 30

translate korean style prologue_no_button_text:
    font "fonts/Arial-Unicode.ttf"
    size 30

translate korean style prologue_no_sp_button_text:
    font "fonts/Arial-Unicode.ttf"
    size 30
    xpos -30

translate korean style prologue_yes_button:
    left_padding 16
    right_padding 18
    top_padding 8
    bottom_padding 10

translate korean style prologue_no_button:
    left_padding 16
    right_padding 18
    top_padding 8
    bottom_padding 10

translate korean style prologue_no_sp_button:
    xsize 95
    ysize 60
    top_padding 8
    bottom_padding 10

translate korean style prologue_yta_button:
    top_padding 6

translate korean style lovense_connect_button:
    top_padding 6

translate korean style prologue_name_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style prologue_fetishes_text:
    font "fonts/Arial-Unicode.ttf"
    size 50

translate korean style ending_menu_label_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style about_button_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style ending_screen_start_text:
    ypos -4

translate korean style ending_screen_return_text:
    ypos -4

translate korean style hint_text:
    ypos -10

translate spanish style no_mp_title_text:
    size 40

translate spanish style no_mp_subtitle_text:
    size 27

translate korean style fetish_selection_button_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style thank_you_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style credits_roll_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style credit_start_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style ending_start_screen_label_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style dark_character:
    font "fonts/MaShanZheng-Regular.ttf"
    kerning 0

translate korean style mpb_large_odd_text:
    ypos -8

translate korean style mpb_large_even_text:
    ypos -8

translate korean style bonus_high_score_text:
    font "fonts/Arial-Unicode.ttf"
    xpos 1500

translate korean style bonus_front_nine_text:
    font "fonts/Arial-Unicode.ttf"

translate korean style bonus_change_mind_text_1:
    font "fonts/Arial-Unicode.ttf"
    size 60

translate korean style bonus_change_mind_text_2:
    font "fonts/Arial-Unicode.ttf"
    xpos 1050
    ypos 830

translate korean style bonus_rm_rf_text_1:
    font "fonts/Arial-Unicode.ttf"

translate korean style bonus_rm_rf_text_2:
    font "fonts/Arial-Unicode.ttf"

translate korean style bonus_rm_rf_text_3:
    font "fonts/Arial-Unicode.ttf"

translate korean style bonus_cherry_popped_text_big:
    font "fonts/Arial-Unicode.ttf"

translate korean style bonus_cherry_popped_text_small:
    font "fonts/Arial-Unicode.ttf"

translate korean style bonus_trade_text_title:
    font "fonts/Arial-Unicode.ttf"

translate korean style bonus_trade_text_body:
    font "fonts/Arial-Unicode.ttf"



translate portuguese style lovense_info_vbox:
    spacing 10

translate portuguese style lovense_info_text:
    size 29

translate portuguese style hint_text:
    ypos -4

translate portuguese style bonus_change_mind_text_1:
    ypos 480
    xpos 900
    size 60

translate portuguese style bonus_change_mind_text_2:
    size 50
    xpos 870
    ypos 650

translate portuguese style bonus_high_score_text:
    ypos 350



translate spanish style lovense_info_vbox:
    spacing 10

translate spanish style lovense_info_text:
    size 25

translate spanish style hint_text:
    ypos -10
    size 25

translate spanish style sub_menu_play_text:
    line_spacing -20

translate spanish style sub_menu_bonus_text:
    size 65

translate spanish style prologue_yes_button:
    left_padding 25
    right_padding 20

translate spanish style bonus_high_score_text:
    ypos 350

translate spanish style bonus_change_mind_text_1:
    ypos 430
    xpos 830
    size 60

translate spanish style bonus_change_mind_text_2:
    size 50
    xpos 870
    ypos 650



translate italian style lovense_info_vbox:
    spacing 10

translate italian style lovense_info_text:
    size 28

translate italian style sub_menu_play_text:
    line_spacing -20

translate italian style hint_text:
    ypos -10
    size 25

translate italian style bonus_high_score_text:
    ypos 350

translate italian style bonus_change_mind_text_1:
    ypos 445
    xpos 850
    size 60

translate italian style bonus_change_mind_text_2:
    size 55
    xpos 870
    ypos 650



translate malay style lovense_info_vbox:
    spacing 10

translate malay style lovense_info_text:
    size 25

translate malay style sub_menu_play_text:
    line_spacing -20

translate malay style hint_text:
    ypos -10
    size 25

translate malay style sub_menu_bonus_text:
    size 65

translate malay style prologue_yes_button:
    left_padding 25
    right_padding 25



translate turkish style prologue_yes_button:
    left_padding 25
    right_padding 20

translate turkish style lovense_info_vbox:
    spacing 10

translate turkish style lovense_info_text:
    size 26

translate turkish style sub_menu_play_text:
    line_spacing -22

translate turkish style bonus_high_score_text:
    xpos 1500
    ypos 325

translate turkish style bonus_rm_rf_text_2:
    ypos 340

translate turkish style bonus_change_mind_text_1:
    xpos 875
    ypos 465
    size 60

translate turkish style bonus_change_mind_text_2:
    size 55
    xpos 885
    ypos 655
    


translate russian style default:
    font "fonts/Andika-Regular.ttf"

translate russian style mainmenu_text:
    font "fonts/Andika-Regular.ttf"

translate russian style navigation_text:
    font "fonts/Andika-Regular.ttf"

translate russian style slot_button_text:
    font "fonts/Andika-Regular.ttf"

translate russian style fl_text:
    font "fonts/Andika-Regular.ttf"

translate russian style say_label:
    font "fonts/Andika-Regular.ttf"

translate russian style choice_button_text:
    font "fonts/Andika-Regular.ttf"

translate russian style confirm_prompt_text:
    font "fonts/Andika-Regular.ttf"

translate russian style confirm_button_text:
    font "fonts/Andika-Regular.ttf"

translate russian style history_name_text:
    font "fonts/Andika-Regular.ttf"

translate russian style history_text:
    font "fonts/Andika-Regular.ttf"

translate russian style history_label_text:
    font "fonts/Andika-Regular.ttf"

translate russian style help_button_text:
    font "fonts/Andika-Regular.ttf"

translate russian style help_label_text:
    font "fonts/Andika-Regular.ttf"

translate russian style help_text:
    font "fonts/Andika-Regular.ttf"

translate russian style pref_label_text:
    font "fonts/Andika-Regular.ttf"

translate russian style radio_button_text:
    font "fonts/Andika-Regular.ttf"

translate russian style check_button_text:
    font "fonts/Andika-Regular.ttf"

translate russian style slider_button_text:
    font "fonts/Andika-Regular.ttf"

translate russian style about_label_text:
    font "fonts/Andika-Regular.ttf"

translate russian style about_text:
    font "fonts/Andika-Regular.ttf"

translate russian style quick_button_text:
    font "fonts/Andika-Regular.ttf"

translate russian style notify_text:
    font "fonts/Andika-Regular.ttf"

translate russian style skip_text:
    font "fonts/Andika-Regular.ttf"

translate russian style gui_label_text:
    font "fonts/Andika-Regular.ttf"

translate russian style overlay_text:
    font "fonts/Andika-Regular.ttf"

translate russian style fl_points_button_text:
    font "fonts/Andika-Regular.ttf"

translate russian style sex_counter_button_text:
    font "fonts/Andika-Regular.ttf"

translate russian style pool_button_text:
    font "fonts/Andika-Regular.ttf"

translate russian style renamer_text:
    font "fonts/Andika-Regular.ttf"

translate russian style renamer_button_text:
    font "fonts/Andika-Regular.ttf"

translate russian style free_roam_button_text:
    font "fonts/Andika-Regular.ttf"

translate russian style prologue_button_text:
    font "fonts/Andika-Regular.ttf"

translate russian style prologue_yta_button_text:
    font "fonts/Andika-Regular.ttf"
    size 36

translate russian style disclaimer:
    font "fonts/Andika-Regular.ttf"

translate russian style skip_recap_button_text:
    font "fonts/Andika-Regular.ttf"

translate russian style sub_menu_bonus_text:
    font "fonts/Andika-Regular.ttf"
    size 55

translate russian style sub_menu_play_text:
    font "fonts/Andika-Regular.ttf"
    size 40

translate russian style ext_mm_text:
    font "fonts/Andika-Regular.ttf"
    size 30

translate russian style scene_transistion_text:
    font "fonts/Andika-Regular.ttf"

translate russian style game_end_text:
    font "fonts/Andika-Regular.ttf"

translate russian style connect_toy_button_text:
    font "fonts/Andika-Regular.ttf"

translate russian style lovense_connect_button_text:
    font "fonts/Andika-Regular.ttf"

translate russian style lovense_pref_button_text:
    font "fonts/Andika-Regular.ttf"

translate russian style lovense_test_button_text:
    font "fonts/Andika-Regular.ttf"

translate russian style prologue_yes_button_text:
    font "fonts/Andika-Regular.ttf"

translate russian style prologue_no_button_text:
    font "fonts/Andika-Regular.ttf"

translate russian style prologue_no_sp_button_text:
    font "fonts/Andika-Regular.ttf"

translate russian style prologue_name_text:
    font "fonts/Andika-Regular.ttf"

translate russian style prologue_fetishes_text:
    font "fonts/Andika-Regular.ttf"

translate russian style ending_menu_label_text:
    font "fonts/Andika-Regular.ttf"

translate russian style about_button_text:
    font "fonts/Andika-Regular.ttf"

translate russian style fetish_selection_button_text:
    font "fonts/Andika-Regular.ttf"

translate russian style thank_you_text:
    font "fonts/Andika-Regular.ttf"

translate russian style credits_roll_text:
    font "fonts/Andika-Regular.ttf"

translate russian style credit_start_text:
    font "fonts/Andika-Regular.ttf"

translate russian style ending_start_screen_label_text:
    font "fonts/Andika-Regular.ttf"

translate russian style dark_character:
    font "fonts/Andika-Regular.ttf"

translate russian style bonus_high_score_text:
    font "fonts/Andika-Regular.ttf"

translate russian style bonus_front_nine_text:
    font "fonts/Andika-Regular.ttf"

translate russian style bonus_change_mind_text_1:
    font "fonts/Andika-Regular.ttf"

translate russian style bonus_change_mind_text_2:
    font "fonts/Andika-Regular.ttf"

translate russian style bonus_rm_rf_text_1:
    font "fonts/Andika-Regular.ttf"

translate russian style bonus_rm_rf_text_2:
    font "fonts/Andika-Regular.ttf"

translate russian style bonus_rm_rf_text_3:
    font "fonts/Andika-Regular.ttf"

translate russian style bonus_cherry_popped_text_big:
    font "fonts/Andika-Regular.ttf"

translate russian style bonus_cherry_popped_text_small:
    font "fonts/Andika-Regular.ttf"

translate russian style bonus_trade_text_title:
    font "fonts/Andika-Regular.ttf"

translate russian style bonus_trade_text_body:
    font "fonts/Andika-Regular.ttf"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
