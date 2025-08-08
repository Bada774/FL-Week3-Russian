init -2 python:

    import math
    import time
    import copy



    class FetishLocatorSaveSystem:
        """
        A class used to import and export Fetish Locator saves from and to different weeks

        Attributes
        ----------
        week : Week
            A Week object.
        gamestate : GameState
            A GameState object.
        mp : MultiPersistent
            A MultiPersistent object.
            Saves at the end of the week are stored in dictionaries, one per week.
            In each dictionary saves are indexed by slot.
            E.g.: when saving the 2nd week in the 3rd slot of page 7,
            the game stores the data in FLSS.mp.week2.7-3
        savename : string
            The current save name
        is_inited : bool
            Bool for is game was inited sucessfully
        savename_temp : string
            A temporary save name. Used to store the name of a save the player has only inspected, without fully loading it
        previous_mp_saves : [dict]
            A list of dictionaries: each one is a previous multipersistent save.
            Each entry has a slot, the save name and the UNIX timestamp of the last modification.

        Methods
        -------
        init() : None
            It initializes the instance: set the objects and add a slot to the mp object
            ("week1", "week2", ...) if it doesn't exist yet.
            Also, it creates vars_from_prev_week which is a dictionary holding the values imported from the previous week.
            vars_from_prev_week is intended to be a read-only copy: it retains the original names and values of the variables.
            Only some of them are later renamed and copied into the store object (an external function will do this).
            vars_from_prev_week can be useful in case the importing process turned out to be incomplete
        set_previous_mp_saves() : None
            It lists the multipersistent saves from the previous week
            and store their most important stats into self.previous_mp_saves.
        mp_write(slot) : None
            When saving the game, it stores the current progress if the week has already ended.
            If it hasn't, it eventually removes a previous multipersistent save in the corresponding slot.
        mp_read(slot) : bool
            When loading a game from a multipersistent slot, initialized the variables and jumps to the loading label.
        is_inited_read() : boll
            return is game inited
        mp_del(slot) : bool
            When deleting a game, it eventually removes a previous multipersistent save in the corresponding slot.
        """
        def __init__(self, week, landing_label):
            self.week               = Week(week, landing_label)
            self.gamestate          = GameState()
            self.mp                 = None
            self.is_inited          = False
            self.previous_mp_saves  = []
            self.savename           = ""
            self.savename_temp      = ""
            try:
                self.mp                 = MultiPersistent("FetishLocator")
                if not self.week.str_cur in self.mp.__dict__:
                    self.mp.__setattr__(self.week.str_cur, {})
                    self.mp.save()
                self.previous_mp_saves  = self.get_previous_mp_saves()
                self.sort_previous_mp_saves("timestamp", True)
                self.is_inited          = True
            except:
                pass
            if self.week.cur > 1:
                setattr(renpy.store, "vars_from_prev_week", {})
        
        def set_savename(self):
            self.savename = renpy.store.save_name.strip()
        
        def get_previous_mp_saves(self):
            tmp = []
            if self.week.str_prev in self.mp.__dict__:
                for slot, data in self.mp.__getattribute__(self.week.str_prev).items():
                    tmp.append({
                        "slot"          : str(  slot                ),
                        "savename"      : str(  data["savename" ]   ),
                        "timestamp"     : float(data["timestamp"]   )
                    })
            return tmp
        
        def sort_previous_mp_saves(self, field, is_reverse):
            self.previous_mp_saves = sorted(self.previous_mp_saves, key = lambda i: i[field], reverse=is_reverse)
        
        def mp_write(self, slot):
            if self.week.is_over:
                self.gamestate.update(self.savename)
                self.mp.__getattribute__(self.week.str_cur).__setitem__(slot, vars(copy.deepcopy(self.gamestate)))
            else:
                self.mp_del(slot)
            self.mp.save()
        
        def mp_load(self, slot):
            if slot in self.mp.__getattribute__(self.week.str_prev):
                tmp = self.mp.__getattribute__(self.week.str_prev)[slot]
                setattr(renpy.store, "vars_from_prev_week", dict(tmp["store"]))
                self.savename = tmp["savename"]
                renpy.jump_out_of_context(self.week.landing_label)
            else:
                pass
        
        def mp_del(self, slot):
            if slot in self.mp.__getattribute__(self.week.str_cur):
                del self.mp.__getattribute__(self.week.str_cur)[slot]
            self.mp.save()
        
        def mp_del_prev(self, slot):
            if slot in self.mp.__getattribute__(self.week.str_prev):
                del self.mp.__getattribute__(self.week.str_prev)[slot]
            self.mp.save()
            self.previous_mp_saves  = self.get_previous_mp_saves()
            self.sort_previous_mp_saves("timestamp", True)



    class Week:
        """
        A class storing time data

        Attributes
        ----------
        cur : int
            The number of the current week
        prev : int
            The number of the previous week
        str_cur : str
            A string starting by "week" and ending by cur (the current week number).
            E.g.: "week1", "week2", ...).
        str_prev : str
            Same as str_cur but it ends by cur-1 (the next number week)
        landing_label : str
            Label where the game jumps, when a multipersistent save is loaded.

        Methods
        -------
        init() : None
            It initializes the instance.
        """
        
        def __init__(self, week, landing_label):
            self.cur            = int(week)
            self.prev           = week - 1
            self.str_cur        = "week" + str(week)
            self.str_prev       = "week" + str(week-1)
            self.landing_label  = str(landing_label)
        
        @property
        def is_over(self):
            return is_chapter_over



    class GameState:
        """
        A class storing data to be exported

        Attributes
        ----------
        savename : str
            The name of the current save.
        timestamp : fload
            The UNIX timestamp of the last modification.
        store : list
            A list of tuples (key, value). They are all the vars displayed by the dev console.
            For instance, variables created through the "define" statement are ignored.
        Methods
        -------
        init() : None
            It initializes the instance.
        update(savename) : None
            It makes a snapshot of the game.
        get_store() : [()]
            It returns a list of tuples (key, value) corresponding to the in-game variables.
        """
        
        def __init__(self):
            self.savename   = None
            self.timestamp  = None
            self.store      = []
        
        def update(self, savename=""):
            self.savename   = savename
            self.timestamp  = time.time()
            self.store      = self.get_store()
        
        def get_store(self):
            temp = []
            for sn, d in renpy.python.store_dicts.items():
                if sn.startswith("store._"):
                    continue
                for vn in d.ever_been_changed:
                    if vn.startswith("_m1_classes__00"):
                        continue
                    if vn.startswith("_") and not vn.startswith("__"):
                        continue
                    if vn in ["nvl_list", "save_name"]:
                        continue
                    if vn in d:
                        temp.append((vn, d[vn]))
            return temp



    class Pager:
        """
        A class used to browse regular saves

        Attributes
        ----------
        str : str
            The page number (as a string) or "auto" for automatic saves or "quick" for quick saves
        int : int
            The page number (as an integer) or zero for automatic and quick saves
        rng : [int]
            A list of page numbers to be displayed
        """
        
        def __init__(self):
            self.str    = FileCurrentPage()
            self.int    = 0 if (self.str in ["auto", "quick"]) else int(self.str)
            self.rng    = range(1,10) if (self.int < 6) else range(self.int - 4, self.int + 5)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
