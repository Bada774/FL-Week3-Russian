init 1 python:

    flash = Fade(.25, 0, .75, color="#fff")

    config.overlay_screens.append('fl_points_screen')
    renpy.hide_screen("fl_points_screen")

    renpy.music.register_channel("music2", "music")
    renpy.music.register_channel("music3", "music")
    renpy.music.register_channel("sound2", "sfx")
    renpy.music.register_channel("sound3", "sfx")
    renpy.music.register_channel("sound4", "sfx")
    renpy.music.register_channel("sound5", "sfx")
    renpy.music.register_channel("sound6", "sfx")
    renpy.music.register_channel("voice2", "voice")
    renpy.music.register_channel("voice3", "voice")
    renpy.music.register_channel("voice4", "voice")
    renpy.music.register_channel("voice5", "voice")
    renpy.music.register_channel("voice6", "voice")
    renpy.music.register_channel("voice7", "voice")
    renpy.music.register_channel("voice8", "voice")

    set_menu_hints(False)
    set_has_ending("03", False)
    set_has_ending("04", False)
    set_has_ending("05", False)
    set_has_ending("07", False)
    set_has_ending("09", False)
    set_has_ending("11", False)
    set_has_ending("12", False)
    set_has_ending("14", False)
    set_has_ending("15", False)
    set_has_ending("16", False)
    set_has_ending("17", False)
    set_has_ending("18", False)

    if not "is_special" in persistent.__dict__:
        persistent.__setattr__("is_special", is_steam_edition)

    if is_steam_edition:
        achievement.sync()

    if config.developer is True:
        config.keymap['screenshot'].remove('noshift_K_s')
        config.keymap['fast_skip'].append('noshift_K_s')
        config.keymap['screenshot'].append('noshift_K_q')

init 999 python:

    if is_antagonist_mode is False:
        flr_name = "Fetish Master"
    else:
        flr_name = "Fetish Locator Retention"

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
