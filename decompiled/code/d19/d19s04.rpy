label d19s04:


    $ d19s04_dd_black = False
    $ d19s04_dd_odd = False
    $ d19s04_dd_dozen = False
    $ d19s04_dd_corner = False
    $ d19s04_dd_single = False
    $ d19s04_dd_end = False
    $ d19s04_dd_spot_plushie = False


    $ d19s04_dw_cum = False
    $ d19s04_dw_end = False

    if date_dd is True and d19s02_go_to_dd is True:
        jump d19s04dd
    elif date_dw is True and d19s02_go_to_dw is True:
        jump d19s04dw
    elif True:
        jump d19s05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
