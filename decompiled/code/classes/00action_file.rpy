init -2 python:

    class FLFileSave(FileSave, Action, DictEquality):
        def __call__(self):
            if not self.get_sensitive():
                return
            fn = _m1_00action_file__slotname(self.name, self.page, self.slot)
            if renpy.scan_saved_game(fn):
                if self.confirm:
                    layout.yesno_screen(layout.OVERWRITE_SAVE, FLFileSave(self.name, False, False, self.page, cycle=self.cycle, slot=self.slot))
                    return
            if self.cycle:
                renpy.renpy.loadsave.cycle_saves(self.page + "-", config.quicksave_slots)
            renpy.save(fn, extra_info=save_name)
            mp_manage("save", self.name)
            renpy.restart_interaction()



    class FLFileLoad(FileLoad, Action, DictEquality):
        def __call__(self):
            if not self.get_sensitive():
                return
            fn = _m1_00action_file__slotname(self.name, self.page, self.slot)
            if not main_menu:
                if self.confirm:
                    if config.autosave_on_quit and not fn.startswith("auto-"):
                        renpy.loadsave.force_autosave()
                    layout.yesno_screen(layout.LOADING, FLFileLoad(self.name, False, self.page, slot=self.slot))
                    return
            mp_manage("load", self.name)
            renpy.load(fn)



    @renpy.pure
    class FLFileDelete(FileDelete, Action, DictEquality):
        def __call__(self):
            if not self.get_sensitive():
                return
            fn = _m1_00action_file__slotname(self.name, self.page, self.slot)
            if self.confirm:
                layout.yesno_screen(layout.DELETE_SAVE, FLFileDelete(self.name, False, self.page, self.slot))
                return
            renpy.unlink_save(fn)
            mp_manage("del", self.name)



    def FLFileAction(name, page=None, **kwargs):
        if renpy.current_screen().screen_name[0] == "load":
            return FLFileLoad(name, page=page, **kwargs)
        else:
            return FLFileSave(name, page=page, **kwargs)



    class FLLoadMp(Action, DictEquality):
        alt = _("Load multipersistent save [slot]")
        slot = None
        def __init__(self, name, confirm=True, page=None, slot=False):
            self.name = name
            self.confirm = confirm
            self.page = page
            self.slot = slot
        def __call__(self):
            if not self.get_sensitive():
                return
            if not main_menu:
                if self.confirm:
                    if config.autosave_on_quit:
                        renpy.force_autosave()
                    layout.yesno_screen(layout.LOADING, FLLoadMp(self.name, False, self.page, slot=self.slot))
                    return
            persistent.mp_slot = self.name
            renpy.full_restart(transition=config.game_main_transition, target="continue_from_previous_week")
        def get_sensitive(self):
            if _in_replay:
                return False
            return (self.name in FLSS.mp.__getattribute__(FLSS.week.str_prev))



    class FLDeleteMp(Action, DictEquality):
        slot = None
        
        def __init__(self, name, confirm=True, page=None, slot=False):
            self.name = name
            self.confirm = confirm
            self.page = page
            self.slot = slot
        
        def __call__(self):
            if self.confirm:
                layout.yesno_screen(layout.DELETE_SAVE, FLDeleteMp(self.name, False, self.page, slot=self.slot))
                return
            FLSS.mp_del_prev(self.name)
            FLSS.mp.save()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
