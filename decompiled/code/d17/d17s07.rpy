label d17s07:

    $ d17s07_jf_luvutoo = False
    $ d17s07_jf_ending = False
    $ d17s07_points = 0

    if persistent.d17s06_dd is True and persistent.d17s06_dw is True and persistent.d17s06_pn is True:
        $ fl_achievement_unlock("d17s06n01")
        $ unlock_gallery_slot("extra", "d17s06n01")

    if is_extended_edition is True:
        jump d17s07_ext
    elif True:
        jump d17s08

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
