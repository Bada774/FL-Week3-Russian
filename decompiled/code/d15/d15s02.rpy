label d15s02:

    $ d15s02_nk_settledown = False
    $ d15s02_goldstar = False

    if date_nk_preg is False:
        jump d15s03

    scene black
    show screen scene_transistion(_("10 minutes of walking later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    queue music caffee_theme_2_slowed
    play sound ["<silence 0.5>", sfx_door_closed8 ]
    hide screen scene_transistion
    scene d15s02-01 mc-nk-cafe-entry1_c2
    with Fade(0.5, 0.5, 0.9)
    $ renpy.music.set_volume(0.8, 3.0, "music")
    pause
    scene d15s02-02 mc-nk-cafe-entry2_c1 with dissolve
    play voice3 nora_hey noloop
    nk "Hey. That was quick."
    scene d15s02-02 mc-nk-cafe-entry2_c2 with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "I thought it was something urgent."
    scene d15s02-03 mc-nk-cafe-entry3_c1 with dissolve
    play voice3 nora_angrymoan noloop
    nk "Heard you fucked 20 women over the weekend."
    scene d15s02-03 mc-nk-cafe-entry3_c2 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Tried to, more like. That was the assignment, but I didn't manage it."
    scene d15s02-04 mc-nk-cafe-entry4_c1 with dissolve
    play voice3 nora_oh noloop
    nk "Man, school is getting crazier and crazier these days."
    nk "What did you lose—if anything?"
    scene d15s02-04 mc-nk-cafe-entry4_c2 with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "My dick."
    scene d15s02-05 mc-nk-cafe-entry5_c1 with dissolve
    play voice3 nora_huuuh noloop
    nk "Your what now?"
    scene d15s02-05 mc-nk-cafe-entry5_c2 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "I should've probably given more context."
    scene d15s02-06 mc-nk-cafe-entry6_c1 with dissolve
    play voice3 nora_aga noloop
    nk "Yeah, I would've appreciated it."
    scene d15s02-06 mc-nk-cafe-entry6_c2 with dissolve
    play voice2 mc_disappointed_ehh2 noloop
    mc "I got put in a cock cage for a bit."
    scene d15s02-07 mc-nk-cafe-entry7_c1 with dissolve
    play voice3 nora_hmm noloop
    nk "Huh..."
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah."
    play voice3 nora_mmm noloop
    nk "Well, compared to the alternative, it sounds like you got off easy."
    scene d15s02-02 mc-nk-cafe-entry2_c1 with dissolve
    nk "And who knows, it might be good for you."
    nk "How do you feel?"
    scene d15s02-02 mc-nk-cafe-entry2_c2 with dissolve
    menu:
        "Itching to Break Free"(hint="d15s02m01c01") if True:

            $ d15s02_nk_settledown = False

            scene d15s02-07 mc-nk-cafe-entry7_c2 with dissolve
            play voice2 mc_yes_yeah3 noloop
            mc "Yeah... I could use the break."
            mc "But I can't wait to get out of this thing either. It's a pain in the ass, well, dick in this case I guess."
            scene d15s02-08 mc-nk-cafe-entry8_c1 with dissolve
            play voice3 min_happy_mmm noloop
            nk "Raring to go for another 20?"
            scene d15s02-08 mc-nk-cafe-entry8_c2 with dissolve
            play voice2 mc_thinking_mmm5 noloop
            mc "Well... I wouldn't mind just one either. If it's someone special."
            play voice3 dahlia_happy_hmm2 noloop
            nk "*Snickers* Mm-hm."
        "Had Enough Fun for Now"(hint="d15s02m01c02") if True:


            $ d15s02_nk_settledown = True

            scene d15s02-07 mc-nk-cafe-entry7_c2 with dissolve
            play voice2 d3s11b_mcheh noloop
            mc "*Chuckles* Maybe you're right."
            mc "I think I've had enough of that kind of fun for a while."
            scene d15s02-08 mc-nk-cafe-entry8_c1 with dissolve
            play voice3 min_happy_mmm noloop
            nk "Was 20, one-after-the-other, too much?"
            scene d15s02-08 mc-nk-cafe-entry8_c2 with dissolve
            play voice2 mc_arrogant_hm2 noloop
            mc "I've been thinking about it since even before that actually."
            nk "Hm."

    play sound sfx_paper_slide1
    scene d15s02-09 mc-nk-cafe-entry9_c2 with dissolve
    play voice2 d2s9_mchey noloop
    mc "What's up with those?"
    scene d15s02-09 mc-nk-cafe-entry9_c1 with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    nk "I got an offer I couldn't refuse."
    scene d15s02-10 mc-nk-cafe-entry10_c1 with dissolve
    play voice2 mc_surprised_huh4 noloop
    mc "What, you in with the mafia now?"
    play voice3 nora_heh noloop
    nk "*Chuckles* Might as well be."
    scene d15s02-09 mc-nk-cafe-entry9_c2 with dissolve
    play voice2 mc_surprised_wow2 noloop
    mc "Wow. That's a hell of a lot of money."
    scene d15s02-11 mc-nk-cafe-entry11_c1 with dissolve
    play voice3 nora_aga noloop
    nk "Yep. I got it a bit back."
    nk "I'm thankful I guess. They could've just swung their big dick around and ran me out of business, but they're asking to buy me out instead."
    nk "Unexpected from a multi-billion dollar multinational megacorp all things considered."
    scene d15s02-11 mc-nk-cafe-entry11_c2 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "This is..."
    scene d15s02-16 mc-nk-cafe-entry16_c1 with dissolve
    play voice3 nora_angrymoan noloop
    nk "I'm thinking about taking it."
    scene d15s02-14 mc-nk-cafe-entry14_c1 with dissolve
    nk "I'm gonna need money to raise this kid of ours."
    nk "Thinking about going somewhere nice and sunny. And hopefully a lot cheaper."
    scene d15s02-14 mc-nk-cafe-entry14_c2 with dissolve
    play voice2 d1s5_mchappy noloop
    mc "...So it's certain then?"
    scene d15s02-12 mc-nk-cafe-entry12_c1 with dissolve
    play voice3 min_thinking_hmm1 noloop
    nk "Mm-hm. I'm pregnant, [mcname]."
    scene d15s02-21 mc-nk-cafe-silence_c1 with dissolve
    "..."
    scene d15s02-12 mc-nk-cafe-entry12_c2 with dissolve
    play voice2 d2s9_confused noloop
    mc "I... After I get out of...the cage. I want to go with you."
    scene d15s02-13 mc-nk-cafe-entry13_c1 with dissolve
    play voice3 nora_huuuh noloop
    nk "What?"
    scene d15s02-13 mc-nk-cafe-entry13_c2 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "That kid in your belly is my child as much as it is yours. I want to be there for him."
    scene d15s02-14 mc-nk-cafe-entry14_c1 with dissolve
    play voice3 nora_hmm noloop
    nk "Or her."
    scene d15s02-15 mc-nk-cafe-entry15_c2 with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "Or her."
    scene d15s02-21 mc-nk-cafe-silence_c1 with dissolve
    "..."
    scene d15s02-17 mc-nk-cafe-entry17_c2 with dissolve
    play voice2 d1s5b_ehhh noloop
    mc "I don't want you to be forced to take this whole thing on by yourself."
    mc "...I made my choice that day. No amount of apologizing is gonna take back what I did."
    scene d15s02-18 mc-nk-cafe-entry18_c2 with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "So I want to own up to it. If this is happening, I want to be there...with you."
    scene d15s02-11 mc-nk-cafe-entry11_c1 with dissolve
    play voice3 nora_oh noloop
    nk "Well aren't you the real responsible type."
    scene d15s02-15 mc-nk-cafe-entry15_c1 with dissolve
    nk "...I need to sleep on it."
    scene d15s02-16 mc-nk-cafe-entry16_c1 with dissolve
    nk "And I suggest you do that as well.{w} This isn't something you just \"decide.\""
    scene d15s02-17 mc-nk-cafe-entry17_c1 with dissolve
    play voice3 nora_arghh noloop
    nk "I don't want to be left alone in the middle of nowhere because you realize that you can't settle down and need to fuck someone else to get your kicks."
    scene d15s02-15 mc-nk-cafe-entry15_c1 with dissolve
    "..."
    scene d15s02-16 mc-nk-cafe-entry16_c1 with dissolve
    play voice3 nora_huh noloop
    nk "I...I'm sorry. That was... I didn't—"
    scene d15s02-16 mc-nk-cafe-entry16_c2 with dissolve
    play voice2 mc_disappointed_ehh2 noloop
    mc "It's alright. I deserved that."
    mc "I {i}have{/i} been a real prick."
    scene d15s02-14 mc-nk-cafe-entry14_c1 with dissolve
    play voice3 nora_heh noloop
    nk "You have."
    scene d15s02-17 mc-nk-cafe-entry17_c1 with dissolve
    play voice3 nora_angrymoan noloop
    nk "If...if this is real. If you really want to do this. Be here tomorrow."
    nk "If not, I'll be in touch. You'll be a part of the child's life, but I can't promise much more than that."
    scene d15s02-11 mc-nk-cafe-entry11_c2 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Alright."
    "..."
    scene d15s02-18 mc-nk-cafe-entry18_c1 with dissolve
    play voice3 nora_hey noloop
    nk "Hey, I'm sorry I blew up at you."
    nk "I'm just... It's a lot."
    scene d15s02-19 mc-nk-cafe-exit1_c2 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "I understand. It's alright."
    scene d15s02-19 mc-nk-cafe-exit1_c1 with dissolve
    play voice3 nora_mmm noloop
    nk "I think I wanna be alone for a bit."
    scene d15s02-19-2 mc-nk-cafe-exit1-2_c1 with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "Right."
    play voice3 nora_hmm noloop
    nk "I have a lot to think about."
    scene d15s02-19-2 mc-nk-cafe-exit1-2_c2 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "It's alright. I get it."
    scene d15s02-20 mc-nk-cafe-exit2_c2 with dissolve
    play voice2 d2s9_confused noloop
    mc "I'll uh... I'll see you later."
    scene d15s02-20 mc-nk-cafe-exit2_c1 with dissolve
    play voice3 nora_aga noloop
    nk "Bye, [mcname]."
    scene d15s02-22 mc-nk-cafe-exit3_c1 with dissolve
    pause
    scene d15s02-22 mc-nk-cafe-exit3-2_c2 with dissolve
    call buzz from _call_buzz_7
    flr "Congratulations! You earned a GOLD STAR!"
    call add_gold_star from _call_add_gold_star_2
    play voice2 mc_thinking_hmm5 noloop
    if fl_goldstars >= 1:
        mct "Another one? What did I get this one for?"
    elif True:
        mct "A gold star? What did I get this for?"

    play sound sfx_door_open2
    $ d15s02_goldstar = True

    stop music fadeout 3.0
    jump d15s03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
