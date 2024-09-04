label d19s01:


    if not hasattr(renpy.store, "d16s07_points"):
        if d16s07_jf_sex is True:
            $ d16s07_points = 12
            call add_points (d16s07_points) from _call_add_points_25


    $ study_points += 1


    $ d19s01lc_kiss = False
    $ d19s01lc_talk_nice = False
    $ d19s01lc_was_fun = False


    $ d19s01ntr_q1 = False
    $ d19s01ntr_q2 = False
    $ d19s01ntr_q3 = False
    $ d19s01ntr_q4 = False
    $ d19s01ntr_no_ques = False
    $ d19s01ntr_slave = False

    if cage_ntr is False:
        jump d19s01lc
    elif True:
        jump d19s01ntr

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
