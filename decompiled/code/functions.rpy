init python:





    def set_has_ending(ending, status):
        persistent.__setattr__("has_e" + ending, status)

    def get_has_ending(ending):
        return persistent.__getattribute__("has_e" + ending)

    def get_ending_status(ending):
        global ending_status
        for i in endings_list:
            if ending == i[0]:
                ending_status = i[4]

    def check_ending_lock(ending):
        for i in endings_list:
            if ending == i[0]:
                if persistent.__getattribute__(i[3]) == True:
                    return True
        return False

    def unlock_ending(ending):
        if persistent.__getattribute__("reached_e" + ending) is False:
            persistent.__setattr__(("reached_e" + ending), True)
            renpy.notify(_("You have unlocked Ending #{}").format(ending))
            
            number_of_unlocked_endings = 0
            for i in endings_list:
                if persistent.__getattribute__("reached_e" + i[0][-2:]) is True:
                    number_of_unlocked_endings += 1
                    fl_achievement_unlock("e" + i[0][-2:] + "_unlock")
            if (number_of_unlocked_endings == 9):
                fl_achievement_unlock("d21s25n03")
                unlock_gallery_slot("extra", "d21s25n03")
            if (number_of_unlocked_endings == 18):
                fl_achievement_unlock("d21s25n02")
                unlock_gallery_slot("extra", "d21s25n02")

    def check_finished_endings():
        
        if persistent.finished_e01 and persistent.finished_e02 and persistent.finished_e06 and persistent.finished_e08 and persistent.finished_e10 and persistent.finished_e13:
            fl_achievement_unlock("d21s25n04")
            unlock_gallery_slot("extra", "d21s25n04")
        
        if persistent.finished_e04 and persistent.finished_e07 and persistent.finished_e11 and persistent.finished_e12 and persistent.finished_e14 and persistent.finished_e17:
            fl_achievement_unlock("dlc01n01")
            unlock_gallery_slot("extra", "dlc01n01")
        
        if persistent.finished_e04 is True and persistent.finished_e07 is True:
            fl_achievement_unlock("dlc01n02")
            unlock_gallery_slot("extra", "dlc01n02")
        
        number_of_finished_endings = 0
        for i in endings_list:
            if persistent.__getattribute__("finished_e" + i[0][-2:]) is True:
                number_of_finished_endings += 1
        
        if number_of_finished_endings == 1:
            fl_achievement_unlock("d21s25n05")
            unlock_gallery_slot("extra", "d21s25n05")
        
        if number_of_finished_endings == 12:
            fl_achievement_unlock("dlc01n03")
            unlock_gallery_slot("extra", "dlc01n03")





    import math

    class Shaker(object):
        
        anchors = {'top' : 0.0, 'center' : 0.5, 'bottom' : 1.0, 'left' : 0.0, 'right' : 1.0}
        
        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            
            self.start = [ self.anchors.get(i, i) for i in start ]  
            self.dist = dist    
            self.child = child
        
        def __call__(self, t, sizes):
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x
            
            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]
            
            xpos = xpos - xanchor
            ypos = ypos - yanchor
            
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            
            return (int(nx), int(ny), 0, 0)

    def _Shake(start, time, child=None, dist=100.0, **properties):
        
        move = Shaker(start, child, dist=dist)
        
        return renpy.display.layout.Motion(move, time, child, add_sizes=True, **properties)

    Shake = renpy.curry(_Shake)





    def restore_notify_timeout():
        setattr(renpy.store, "notify_timeout", True)

    def set_menu_hints( status = True ):
        persistent.menu_hints = status



    def show_hover_notify(what):
        setattr(renpy.store, "notify_timeout", False)
        renpy.notify(what)

    def hide_hover_notify():
        setattr(renpy.store, "notify_timeout", True)
        renpy.hide_screen("notify")



    def stop_all_sound():
        renpy.music.stop('music')
        renpy.music.stop('music2')
        renpy.music.stop('music3')
        renpy.music.stop('sound')
        renpy.music.stop('sound2')
        renpy.music.stop('sound3')
        renpy.music.stop('sound4')
        renpy.music.stop('sound5')
        renpy.music.stop('sound6')
        renpy.music.stop('voice')
        renpy.music.stop('voice2')
        renpy.music.stop('voice3')
        renpy.music.stop('voice4')
        renpy.music.stop('voice5')
        renpy.music.stop('voice6')
        renpy.music.stop('voice7')
        renpy.music.stop('voice8')



    def makeimagelist(imagename, start, to, postfix, step = 1):
        imagelist = []
        for x in range(start, to+step, step):
            if (to > 9 or start > 9) and x < 10:
                num = "0" + str(x)
            else:
                num = str(x)
            imagelist.append(imagename + num + postfix)
        return imagelist



    def set_variable(var, status):
        setattr(renpy.store, var, status)

    def has_persistent(var):
        if var in persistent.__dict__:
            return True
        else:
            return False



    def set_special( status = True ):
        persistent.is_special = status



    def language_setter(newlang):
        persistent.chose_lang = True
        if(preferences.language != newlang):
            renpy.change_language(newlang)
        return



    def mp_manage(what, slot_num):
        pager = Pager()
        slot = "{0}-{1}".format(pager.str, slot_num)
        if (what == "del"):
            if (pager.int > 0):
                FLSS.mp_del(slot)
        elif (what == "save"):
            FLSS.set_savename()
            if (pager.int > 0):
                FLSS.mp_write(slot)
        elif (what == "load"):
            FLSS.savename_temp = str(renpy.slot_json(slot)["_save_name"]).strip()





    def get_gallery_page_count(what):
        return (len(renpy.store.__getattribute__(what + "_gallery_slots")) + 5) // 6

    def get_gallery_page(what, page):
        gallery_slots = renpy.store.__getattribute__(what + "_gallery_slots")
        slots = []
        first_index = (page - 1) * 6
        for i in range(first_index, first_index + 6):
            if i < len(gallery_slots):
                slots.append(gallery_slots[i])
            else:
                slots.append((None, None, None))
        return slots

    def unlock_gallery_slot(what, slot):
        if not _in_replay and is_extended_edition is True:
            if not persistent.__getattribute__(what)[slot]:
                persistent.__getattribute__(what)[slot] = True
                warning = {
                    "cg":       _("You've unlocked a new CG Gallery"                ),
                    "scene":    _("You can watch the scene again in the Replay Room"),
                    "extra":    _("You've unlocked a new bonus content"             ),
                }
                renpy.notify(warning[what])
                if what == "cg":
                    renpy.play("audio/loudlout/extended/sfx/cg_gallery_unlock.ogg", channel="sound5")
                elif what == "scene":
                    renpy.play("audio/loudlout/extended/sfx/replay_room_unlock.ogg", channel="sound5")
                else:
                    renpy.play("audio/loudlout/extended/sfx/extra_content_unlock.ogg", channel="sound5")

    def lock_gallery_slot(what, slot):
        persistent.__getattribute__(what)[slot] = False

    def unlock_gallery_in_replay(what, slot):
        if is_extended_edition is True:
            if not persistent.__getattribute__(what)[slot]:
                persistent.__getattribute__(what)[slot] = True
                warning = {
                    "cg":       _("You've unlocked a new CG Gallery"                ),
                    "scene":    _("You can watch the scene again in the Replay Room"),
                    "extra":    _("You've unlocked a new bonus content"             ),
                }
                renpy.notify(warning[what])
                if what == "cg":
                    renpy.play("audio/loudlout/extended/sfx/cg_gallery_unlock.ogg", channel="sound5")
                elif what == "scene":
                    renpy.play("audio/loudlout/extended/sfx/replay_room_unlock.ogg", channel="sound5")
                else:
                    renpy.play("audio/loudlout/extended/sfx/extra_content_unlock.ogg", channel="sound5")

    def is_gallery_slot_unlocked(what, slot):
        return persistent.__getattribute__(what)[slot]

    def set_replay_scope(slot, main_menu):
        scene_gallery[slot]["option"]["mcname" ] = __(persistent.mcname)
        scene_gallery[slot]["option"]["mclogin"] = __(persistent.mclogin)
        if main_menu:
            for i in scene_gallery[slot]["option"]:
                scene_gallery[slot]["scope"][i] = scene_gallery[slot]["option"][i]
        else:
            for i in scene_gallery[slot]["option"]:
                scene_gallery[slot]["scope"][i] = getattr(renpy.store, i, scene_gallery[slot]["option"][i])

    def  get_replay_warning(what, main_menu):
        replay_warning = ""
        if what == "scene":
            if main_menu:
                replay_warning = _("The game will replay the scene according to a default playthrough")
            else:
                replay_warning = _("The game will try to replay the scene according to your current playthrough")
        return replay_warning

    def create_persistent_gallery_if_non_existent():
        if not "gallery_hint" in persistent.__dict__:
            persistent.__setattr__("gallery_hint", False)
        for what in ["scene", "cg", "extra"]:
            if not what in persistent.__dict__:
                persistent.__setattr__(what, {})
            conds = renpy.store.__getattribute__(what + "_gallery_unlock_conditions_for_old_players")
            for slot in conds:
                if not slot in persistent.__getattribute__(what):
                    persistent.__getattribute__(what)[slot] = renpy.seen_image(conds[slot]) if (what is not "extra") else False





    def get_ext_audio(sound):
        if is_extended_edition:
            return audiofiles[sound]
        else:
            return "audio/renpy/common/_silence.ogg"





    def fl_achievement_unlock(name):
        if is_steam_edition is True:
            if not achievement.has(fl_achievements[name]):
                achievement.grant(fl_achievements[name])
                achievement.sync()

    def fl_achievements_clear():
        if is_steam_edition is True:
            achievement.clear_all()
            achievement.sync()





    def prologue_get_girls(step):
        range = (
            (0,3),
            (6,8),
            (8,13) if is_extended_edition else (8,12),
            (13,18) if is_extended_edition else (13,17),
            (3,6),
        )[step]
        return prologue_girls[range[0] : range[1]]

    def prologue_get_fetishes():
        return prologue_fetishes

    def prologue_set_girls(step, girl, connection):
        if step > 1:
            setattr(renpy.store, girl, not getattr(renpy.store, girl))
        elif getattr(renpy.store, girl):
            setattr(renpy.store, girl, False)
            if step == 0:
                setattr(renpy.store, connection, False)
        else:
            girls = prologue_get_girls(step)
            already_active = 0
            max_already_active = len(girls) - 1
            for g in girls:
                already_active += int(getattr(renpy.store, g[0]))
            if already_active < max_already_active:
                setattr(renpy.store, girl, True)
            else:
                renpy.music.play(audio.error, "sound5", loop=False)
                if step == 0:
                    renpy.notify(_("You can only select two out of Min, Lyssa and Maria"))
                elif step == 1:
                    renpy.notify(_("You can only select one out of Daisy and Dahlia"))

    def prologue_check_girls():
        if is_extended_edition is True:
            if date_sy and date_pw and date_vw and date_aw and date_cb and date_ir and date_hr and date_nr and date_jf and date_jdg:
                return True
            else:
                return False
        else:
            if date_sy and date_pw and date_vw and date_aw and date_cb and date_ir and date_hr and date_nr:
                return True
            else:
                return False

    def prologue_set_fetishes(fetish, value):
        setattr(renpy.store, fetish, value)

    def prologue_set_all_fetishes(value):
        for i in prologue_fetishes:
            setattr(renpy.store, i[0], value)

    def prologue_check_fetishes():
        for i in prologue_fetishes:
            if fl_enema and fl_watersports and fl_footfetish and fl_cumgarnish and fl_fisting and temp_pegging and fl_trans:
                return True
            else:
                return False

    def prologue_set_all_girls(step, value):
        girls = prologue_get_girls(step)
        for i in girls:
            setattr(renpy.store, i[0], value)

    def prologue_set_variables():
        for i in prologue_events:
            setattr(renpy.store, i[0], eval(i[2]))


    def prologue_import():
        for what in ("girls", "fetishes", "screen", "events"):
            for entry in getattr(renpy.store, "prologue_" + what):
                if entry[0] in vars_from_prev_week:
                    setattr(    renpy.store,    entry[0],   vars_from_prev_week[entry[0]]   )
                elif (entry[1] is not None) and (entry[1] in vars_from_prev_week):
                    setattr(    renpy.store,    entry[0],   vars_from_prev_week[entry[1]]   )
                else:
                    setattr(    renpy.store,    entry[0],   eval(entry[2])                  )





    def fl_renamer(what, value):
        if what == "save":
            setattr(renpy.store, "save_name", value)
        elif what == "ip":
            persistent.lovense_ip = value
        elif what == "port":
            persistent.lovense_port = value
        else:
            FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves")).set_text(value)

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
