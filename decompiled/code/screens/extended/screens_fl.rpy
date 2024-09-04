





init -498 screen fl_extra():
    tag menu


    use game_menu("Bonus Content")

    use coming_soon

init -498 screen cg_gallery():
    tag menu
    default gallery_page = 1

    use gallery(_("CG Gallery" ), "cg"  , gallery_page)

init -498 screen replay_room():
    tag menu
    default gallery_page = 1

    use gallery(_("Replay Room"), "scene", gallery_page)

init -498 screen extra():
    tag menu
    default gallery_page = 1

    use gallery(_("Bonus Content" ), "extra", gallery_page)

init -498 screen gallery(title, what, page):

    default total_pages = get_gallery_page_count(what)
    $ replay_warning = get_replay_warning(what, main_menu)
    $ data = get_gallery_page(what, page)
    $ hint_label = _("Hints on") if persistent.gallery_hint else _("Hints off")

    use game_menu(title):

        fixed:
            hbox:
                style_prefix "renamer"
                xanchor 1.0
                xpos 1335
                text __("Page [page]") color gui.interface_text_color

            button:
                style style.button["menu_hint"]
                xanchor 0.0
                xpos 80
                yalign 0.0
                left_padding 50
                action ToggleVariable("persistent.gallery_hint", True, False)
                selected (persistent.gallery_hint)
                text hint_label style "hint_text"

            grid 3 2:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing

                for (slot, title, hint) in data:
                    if slot:
                        if is_gallery_slot_unlocked(what, slot):
                            button:
                                vbox:
                                    add "images/extended/{}/{}.webp".format(what, slot) xalign 0.5
                                    text title style "slot_name_text" color gui.interface_text_color hover_color gui.hover_color
                                    if persistent.gallery_hint:
                                        text hint style "slot_time_text"
                                if what == "cg":
                                    action cg_gallery.Action(slot)
                                elif what == "extra":
                                    if slot == "d21s25n01":
                                        action [Function(set_replay_scope, "lc_video", main_menu), Replay(scene_gallery["lc_video"]["label"], scene_gallery["lc_video"]["scope"], False)]
                                    elif slot == "d19s05n01":
                                        action ShowMenu("bonus_high_score")
                                    elif slot == "d21s25n03":
                                        action ShowMenu("bonus_front_nine")
                                    elif slot == "d21s25n04":
                                        action ShowMenu("bonus_change_my_mind")
                                    elif slot == "d20s08n01":
                                        action ShowMenu("bonus_rm_rf")
                                    elif slot == "e06s08n01":
                                        action ShowMenu("bonus_trade_meme")
                                    elif slot == "d21s25n05":
                                        action ShowMenu("bonus_cherry_popped")
                                    elif slot == "dlc01n01":
                                        action ShowMenu("bonus_horny_meme")
                                    else:
                                        action extra_gallery.Action(slot)
                                else:
                                    action [Function(set_replay_scope, slot, main_menu), Replay(scene_gallery[slot]["label"], scene_gallery[slot]["scope"], False)]
                        else:
                            button:
                                vbox:
                                    add "gallery_locked_button" xalign 0.5
                                    text title style "slot_name_text" color gui.interface_text_color hover_color gui.hover_color
                                    if persistent.gallery_hint:
                                        text hint style "slot_time_text"
                                action NullAction()
                    else:
                        null height 0

            hbox:
                style_prefix "renamer"
                xalign 0.5
                yalign 0.94
                text replay_warning color gui.idle_color text_align 0.5

            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0
                spacing gui.page_spacing

                if page > 1:
                    textbutton _("<") action SetScreenVariable("gallery_page", page - 1 )
                else:
                    textbutton _("<") action NullAction()

                for i in range(1, total_pages + 1):
                    textbutton "[i]" action SetScreenVariable("gallery_page", i        )

                if page < total_pages:
                    textbutton _(">") action SetScreenVariable("gallery_page", page + 1 )
                else:
                    textbutton _(">") action NullAction()

init 2 style hint_text:
    selected_color gui.interface_text_color
    idle_color gui.idle_color
    hover_color gui.hover_color
    selected_hover_color gui.hover_color

init -498 screen coming_soon():

    vbox:
        style_prefix "coming_soon"

        text (_("Coming Soon"))

init 2 style coming_soon_vbox:
    xalign 0.7
    yalign 0.5

init 2 style coming_soon_text:
    size 150
    color gui.accent_color
    font gui.interface_text_font



init -498 screen jump_replay():

    timer 0.001 action (Hide("jump_replay"), Replay(scene_gallery["lc_video"]["label"]))

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
