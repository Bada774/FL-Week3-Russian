label d20s00:

    $ renpy.suspend_rollback(False)

    if not hasattr(renpy.store, "d19s01lc_kiss"):
        $ d19s01lc_kiss = False
    if not hasattr(renpy.store, "d19s01lc_talk_nice"):
        $ d19s01lc_talk_nice = False
    if not hasattr(renpy.store, "d19s01lc_was_fun"):
        $ d19s01lc_was_fun = False

    if not hasattr(renpy.store, "d19s01ntr_q1"):
        $ d19s01ntr_q1 = False
    if not hasattr(renpy.store, "d19s01ntr_q2"):
        $ d19s01ntr_q2 = False
    if not hasattr(renpy.store, "d19s01ntr_q3"):
        $ d19s01ntr_q3 = False
    if not hasattr(renpy.store, "d19s01ntr_q4"):
        $ d19s01ntr_q4 = False
    if not hasattr(renpy.store, "d19s01ntr_no_ques"):
        $ d19s01ntr_no_ques = False
    if not hasattr(renpy.store, "d19s01ntr_slave"):
        $ d19s01ntr_slave = False

    jump d20s01

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
