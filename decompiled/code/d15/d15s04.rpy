label d15s04:


    $ d15s04_study = False
    $ d15s04_doubletrouble = False
    $ d15s04_dd_doctor = False


    $ d15s04_quartet_prep = False
    $ d15s04_resolve_part1 = False
    $ d15s04_resolve_part2 = False
    $ d15s04dw_points = 0


    $ d15s04_dd_kiss = False
    $ d15s04dd_points = 0

    scene black
    show screen scene_transistion(_("20 minutes later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    queue music slow_love
    hide screen scene_transistion
    scene d15s04-02 mc-study-put-down-phone_c1
    with Fade(0.5, 0.5, 0.9)
    play voice2 d1s1_mmm noloop
    mct "Hm. I got some time to kill. Wonder what I should do?"
    if date_mk_tr is True:
        call buzz from _call_buzz_3
        scene d15s04-05 mc-study-dahlia_c1 with dissolve
        mk "Hey can you meet me today? The place you and AmRose sent me to."
        play voice2 mc_thinking_hmm3 noloop
        mct "Maria? What does she want?"
        scene d15s04-01 mc-study_c1 with dissolve
        play sound [sfx_phone_tapping1, sfx_message_out1]
        mct "Alright. I'll be there."
        scene d15s04-04 mc-study-dahlia_c1 with dissolve
        pause
    if date_mes is True and date_mh is False:
        call buzz from _call_buzz_4
        scene d15s04-05 mc-study-dahlia_c1 with dissolve
        play voice2 d1s5_mchappy noloop
        mct "Now what?"
        mes "Hey can you come to Lydia's place a bit later?"
        scene d15s04-07 mc-study-daisy-surprise_c1 with dissolve
        play voice2 mc_yes_sure1 noloop
        mc "Sure I guess. What's up?"
        mes "I'll tell you there."
        scene d15s04-10 mc-study-daisy-texting-confused_c1 with dissolve
        play voice2 mc_yes_okay2 noloop
        mc "Okay..."
        scene d15s04-04 mc-study-dahlia_c1 with dissolve

    menu:
        mc "What should I do now?"
        "Continue Studying for Exams"(hint="d15s04m01c01") if True:
            mct "Study is what I need to fucking do now."
            scene d15s04-03 mc-study-get-up_c1 with dissolve
            play voice2 mc_angry_huh2 noloop
            if study_points > 0:
                mct "I was doing pretty well, I need to get started again if I'm gonna pass this exam."
            elif True:
                mct "I'm way behind. I need to get on this stat or I'm gonna flunk hard."

            $ d15s04_study = True
            $ study_points += 1

            jump d15s04_studying

        "Invite Dahlia and Samiya here to talk"(hint="d15s04m01c02") if date_dw is True:

            $ d15s04_doubletrouble = True
            $ d15s04dw_points = 6

            scene d15s04-04 mc-study-dahlia_c1 with dissolve
            mct "Hm... This is either a great idea or a terrible mistake."
            mct "Not sure which it's gonna be, but it can't just go on like this either."
            scene d15s04-06 mc-study-daisy_c1 with dissolve
            play voice2 mc_angry_hm1 noloop
            play sound sfx_phone_tapping1 loop
            mct "If those two don't figure out whatever the hell their problem is, it's all gonna blow up—and I'm gonna be smack-dab in the middle of it."
            mct "Might as well get it over with now."
            scene d15s04-05 mc-study-dahlia_c1 with dissolve
            play sound sfx_message_out1
            play voice2 mc_disappointed_ehh2 noloop
            mct "*Sigh* Here goes nothing."
            mct "Hm... I wonder if I have enough time to write a will?"

            jump d15s04dw

        "Spend time with Daisy"(hint="d15s04m01c03") if date_dd is True:

            $ d15s04_dd_doctor = True
            $ d15s04dd_points = 6

            scene d15s04-06 mc-study-daisy_c1 with dissolve
            mct "Hm... I wonder if Daisy—"
            scene d15s04-07 mc-study-daisy-surprise_c1 with dissolve
            play voice2 mc_arrogant_huh2 noloop
            mct "Huh?"
            mct "Oh, speak of the devil."
            scene d15s04-08 mc-study-daisy-texting_c1 with dissolve
            play sound sfx_message_in1
            dd "Hey you free?"
            play sound [sfx_phone_tapping1, sfx_message_out1]
            mct "Yeah, I was just gonna message you."
            scene d15s04-06 mc-study-daisy_c1 with dissolve
            play sound sfx_message_in1
            dd "Haha perfect timing. I was wondering if you could pick me up?"
            play sound sfx_message_in1
            dd "I got another appointment at the docs."
            scene d15s04-09 mc-study-daisy-texting_c1 with dissolve
            play sound [sfx_phone_tapping1, sfx_message_out1]
            mct "When? Is everything alright?"
            play sound sfx_message_in1
            dd "Everything's fine. I just wanted you there."
            play sound sfx_message_in1
            dd "Uhh... in like 30 minutes give or take."
            scene d15s04-06 mc-study-daisy_c1 with dissolve
            play sound [sfx_phone_tapping1, sfx_message_out1]
            mct "Alright sure. I'll come pick you up."
            play sound sfx_message_out1
            mct "Dorm?"
            play sound sfx_message_in1
            dd "Yep."
            scene d15s04-08 mc-study-daisy-texting_c1 with dissolve
            play sound [sfx_phone_tapping1, sfx_message_out1]
            mct "Cool. I'll be there."
            dd "..."
            scene d15s04-10 mc-study-daisy-texting-confused_c1 with dissolve
            play sound sfx_message_out1
            mct "Hm?"
            play sound sfx_message_in1
            dd "Great! I'll be waiting."
            play voice2 mc_thinking_hmm5 noloop
            mct "She was writing something and then it seemed like she deleted it."
            scene d15s04-11 mc-study-daisy-mc-leaving_c1 with dissolve
            mct "Eh, probably nothing. I should get going."
            stop music fadeout 3.0

            jump d15s04dd

label d15s04_studying:

    scene d15s04-12 mc-study-studying_c1 with dissolve
    pause
    mct "Huh, apparently something like 70 small businesses went bankrupt every hour back in '09."
    mct "I'm not sure how that information helps me in the present, but alright."
    play sound sfx_paper_rustl1
    scene d15s04-13 mc-study-studying_c1 with dissolve
    play voice2 mc_disappointed_meh1 noloop
    mct "Business, business, business. I need to get my hands on whatever Unikitty's on."
    scene d15s04-14 mc-study-studying_c1 with dissolve
    mct "They warn you that masturbation will make you go blind, but really it's textbooks that do it."
    play sound sfx_keyboard_enter1
    play sound2 sfx_youtube_catsong fadein 1.0
    scene d15s04-15 mc-study-studying_c1 with dissolve
    pause
    stop sound2 fadeout 3.5

    jump d15s05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
