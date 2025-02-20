image d19s07-a1 = Movie(play = "images/Day-19/s07/anim/d19s07-a30-1-2x-50fps.webm", start_image = "d19s07-a30-1 mc-mk-sex-01")
image d19s07-a1-f = Movie(play = "images/Day-19/s07/anim/d19s07-a30-1-2x-60fps.webm", start_image = "d19s07-a30-1 mc-mk-sex-01")
image d19s07-a2 = Movie(play = "images/Day-19/s07/anim/d19s07-a30-2-2x-50fps.webm", start_image = "d19s07-a30-2 mc-mk-sex-01")
image d19s07-a2-f = Movie(play = "images/Day-19/s07/anim/d19s07-a30-2-2x-60fps.webm", start_image = "d19s07-a30-2 mc-mk-sex-01")
image d19s07-a3 = Movie(play = "images/Day-19/s07/anim/d19s07-a30-3-2x-50fps.webm", start_image = "d19s07-a30-3 mc-mk-sex-01")
image d19s07-a3-f = Movie(play = "images/Day-19/s07/anim/d19s07-a30-3-2x-60fps.webm", start_image = "d19s07-a30-3 mc-mk-sex-01")

image d19s07-a4 = Movie(play = "images/Day-19/s07/anim/d19s07-a31-1-2x-50fps.webm", start_image = "d19s07-a31-1 mc-mk-sex-01")
image d19s07-a4-f = Movie(play = "images/Day-19/s07/anim/d19s07-a31-1-2x-60fps.webm", start_image = "d19s07-a31-1 mc-mk-sex-01")
image d19s07-a5 = Movie(play = "images/Day-19/s07/anim/d19s07-a31-2-2x-50fps.webm", start_image = "d19s07-a31-2 mc-mk-sex-01")
image d19s07-a5-f = Movie(play = "images/Day-19/s07/anim/d19s07-a31-2-2x-60fps.webm", start_image = "d19s07-a31-2 mc-mk-sex-01")
image d19s07-a6 = Movie(play = "images/Day-19/s07/anim/d19s07-a31-3-2x-50fps.webm", start_image = "d19s07-a31-3 mc-mk-sex-01")
image d19s07-a6-f = Movie(play = "images/Day-19/s07/anim/d19s07-a31-3-2x-60fps.webm", start_image = "d19s07-a31-3 mc-mk-sex-01")

image d19s07-a7 = Movie(play = "images/Day-19/s07/anim/d19s07-a32-1-2x-50fps.webm", start_image = "d19s07-a32-1 mc-mk-sex-01_i")
image d19s07-a7-f = Movie(play = "images/Day-19/s07/anim/d19s07-a32-1-2x-60fps.webm", start_image = "d19s07-a32-1 mc-mk-sex-01_i")
image d19s07-a8 = Movie(play = "images/Day-19/s07/anim/d19s07-a32-2-2x-50fps.webm", start_image = "d19s07-a32-2 mc-mk-sex-01_i")
image d19s07-a8-f = Movie(play = "images/Day-19/s07/anim/d19s07-a32-2-2x-60fps.webm", start_image = "d19s07-a32-2 mc-mk-sex-01_i")
image d19s07-a9 = Movie(play = "images/Day-19/s07/anim/d19s07-a32-3-2x-50fps.webm", start_image = "d19s07-a32-3 mc-mk-sex-01_i")
image d19s07-a9-f = Movie(play = "images/Day-19/s07/anim/d19s07-a32-3-2x-60fps.webm", start_image = "d19s07-a32-3 mc-mk-sex-01_i")

image d19s07-a10 = Movie(play = "images/Day-19/s07/anim/d19s07-a34-1-2x-50fps.webm", start_image = "d19s07-a34-1 mc-mk-sex-01_i")
image d19s07-a10-f = Movie(play = "images/Day-19/s07/anim/d19s07-a34-1-2x-60fps.webm", start_image = "d19s07-a34-1 mc-mk-sex-01_i")
image d19s07-a11 = Movie(play = "images/Day-19/s07/anim/d19s07-a34-2-2x-50fps.webm", start_image = "d19s07-a34-2 mc-mk-sex-01_i")
image d19s07-a11-f = Movie(play = "images/Day-19/s07/anim/d19s07-a34-2-2x-60fps.webm", start_image = "d19s07-a34-2 mc-mk-sex-01_i")
image d19s07-a12 = Movie(play = "images/Day-19/s07/anim/d19s07-a34-3-2x-50fps.webm", start_image = "d19s07-a34-3 mc-mk-sex-01_i")
image d19s07-a12-f = Movie(play = "images/Day-19/s07/anim/d19s07-a34-3-2x-60fps.webm", start_image = "d19s07-a34-3 mc-mk-sex-01_i")

label d19s07:

    $ d19s07_take_virginity = False
    $ d19s07_fuck_only = False
    $ d19s07_need = False
    $ d19s07_problem = False
    $ d19s07_friend = False
    $ d19s07_mk_nordin = False

    if date_mk is False:
        jump d19s08

    scene black
    show screen scene_transistion(_("30 minutes later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene d19s07-01 mc-mk-cafe-entry1_c1
    with Fade(0.5, 0.5, 0.9)
    pause
    queue music thinking_music_3
    $ renpy.music.set_volume(0.7, 3.5, "music")
    play sound sfx_double_door1
    scene d19s07-01 mc-mk-cafe-entry1_c2 with dissolve
    pause
    scene d19s07-01 mc-mk-cafe-entry1_c3 with dissolve
    pause
    play sound sfx_door_closed2
    scene d19s07-02 mc-mk-cafe-stand-talk1_c1 with dissolve
    play voice2 d2s9_mchey noloop volume 1.4
    mc "Hey Maria. I heard you work here after meals."
    scene d19s07-02 mc-mk-cafe-stand-talk1_c2 with dissolve
    play voice3 maria_what noloop
    mk "I didn't expect to see you again."
    mct "Honestly, I've thought that I'd never see her again... several times now."
    scene d19s07-03 mc-mk-cafe-stand-talk2_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.5
    mc "What can I say? I'm here."
    scene d19s07-03 mc-mk-cafe-stand-talk2_c2 with dissolve
    pause
    scene d19s07-04 mc-mk-cafe-sit1_c1 with dissolve
    play voice3 min_disappointed_ehh3 noloop
    if d15s05_leave is True:
        mk "You just left me there. Sucking cock. In that toilet."
    elif d15s05_rescue is True:
        mk "You just left me there. With that Counselor. Seeking mental help."
    elif date_mk_tr is False:
        mk "You've left me alone. For over a week."
    else:
        mk "You just left me there. Naked. In that toilet."
    scene d19s07-05 mc-mk-cafe-sit2_c2 with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "I did.{w} Do you hate me?"
    scene d19s07-05 mc-mk-cafe-sit2_c1 with dissolve
    play voice3 min_no_happy noloop
    mk "Quite the opposite.{w} If I weren't a lesbian, I'd marry you."
    scene d19s07-04 mc-mk-cafe-sit1_c2 with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "Wha-?"
    scene d19s07-04 mc-mk-cafe-sit1_c1 with dissolve
    play voice3 min_arrogant_hm noloop
    if d15s05_rescue is True:
        mk "It was exactly what I needed."
    elif d15s05_leave is True:
        mk "I was being sarcastic, duh."
    else:
        mk "Sorry, I was just trying to sound friendly."
    scene d19s07-07 mc-mk-cafe-sit4_c2 with dissolve
    play voice2 d2s9_confused noloop volume 1.4
    mc "Uh, okay."
    scene d19s07-07 mc-mk-cafe-sit4_c1 with dissolve
    play voice3 min_arrogant_huh2 noloop
    mk "Pleasantries aside, what did you want me for?"
    scene d19s07-07 mc-mk-cafe-sit4_c2 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "No nonsense, huh?"
    scene d19s07-07 mc-mk-cafe-sit4_c1 with dissolve
    play voice3 min_disappointed_ehh1 noloop
    mk "Just tell me what it is already."
    menu:
        "Convince Maria to Seduce Professor Nordin"(hint="d19s07m01c01") if date_mk_tr is True:

            $ d19s07_fuck_only = False

            scene d19s07-06 mc-mk-cafe-sit3_c2 with dissolve
            play voice2 d1s5b_ehhh noloop volume 1.4
            mc "Fine.{w} I need you to seduce and fuck Professor Nordin."
            scene d19s07-10 mc-mk-cafe-sit7_c1 with dissolve
            play voice3 amrose_disgust_eww noloop
            mk "Ew.{w} Seriously?"
            scene d19s07-09 mc-mk-cafe-sit6_c2 with dissolve
            play voice2 mc_thinking_mmm3 noloop
            mc "It's for my final exam."
            scene d19s07-09 mc-mk-cafe-sit6_c1 with dissolve
            play voice3 min_old_hmm noloop
            mk "I see.{w}.. still, \"Ew.\""
            scene d19s07-10 mc-mk-cafe-sit7_c2 with dissolve
            play voice2 mc_yes_yeah6 noloop
            mc "Agreed, but it's necessary. Can you do it?"
            scene d19s07-10 mc-mk-cafe-sit7_c1 with dissolve
            play voice3 min_happy_mmm noloop
            if d15s05_mk_virgin_pussy is True and d15s05_vaginal is False:
                $ d19s07_take_virginity = True
                mk "You want him to fuck my virgin pussy?"
            elif d15s05_leave is True:
                mk "You want him to fuck my well-used cunt?"
            else:
                mk "I assume you want it to be vaginal sex?"
            scene d19s07-06 mc-mk-cafe-sit3_c2 with dissolve
            play voice2 mc_yes_yeah7 noloop
            mc "I guess so.{w} Is that a problem?"

            if d15s05_rescue is True:
                jump d19s07_problem

            scene d19s07-06 mc-mk-cafe-sit3_c1 with dissolve
            play voice3 min_no_nah noloop
            mk "If that's what you want, I'll do it."
            play voice2 mc_surprised_huh5 noloop
            mc "Seriously?"
            mk "Do you want me to put up a fight? I'll do this for you."
            scene d19s07-05 mc-mk-cafe-sit2_c2 with dissolve
            play voice2 mc_thinking_mmm4 noloop
            mc "I don't want you to... I just expected..."
            scene d19s07-05 mc-mk-cafe-sit2_c1 with dissolve
            play voice3 min_disappointed_mph noloop
            mk "Get over it.{w} What do you want me to do?"

            jump d19s07_roleplay

        "Just a Booty Call"(hint="d19s07m01c02") if d15s05_rescue is False:

            $ d19s07_fuck_only = True

            scene d19s07-04 mc-mk-cafe-sit1_c2 with dissolve
            play voice2 mc_thinking_emm1 noloop
            mc "Actually, I was just hoping you'd be D.T.F."
            scene d19s07-09 mc-mk-cafe-sit6_c1 with dissolve
            play voice3 maria_aah noloop
            mk "Me? Down to fuck you?"
            scene d19s07-06 mc-mk-cafe-sit3_c2 with dissolve
            play voice2 mc_yes_yeah1 noloop
            if date_mk_tr is True:
                mc "I wasn't planning on sharing you with anyone else... this time."
            else:
                mc "I'm not going to share you with anyone else."
            scene d19s07-06 mc-mk-cafe-sit3_c1 with dissolve
            play voice3 min_old_hmm noloop
            mk "What about AmRose?"
            scene d19s07-08 mc-mk-cafe-sit5_c2 with dissolve
            play voice2 mc_no_uhuh1 noloop
            mc "Not this time. Just me."
            scene d19s07-09 mc-mk-cafe-sit6_c1 with dissolve
            play voice3 min_happy_mmm noloop
            mk "Hmm.{w} Okay."
            scene d19s07-10 mc-mk-cafe-sit7_c2 with dissolve
            play voice2 d1s2_hmm noloop volume 1.4
            mc "Just like that?"
            scene d19s07-10 mc-mk-cafe-sit7_c1 with dissolve
            play voice3 min_disappointed_mph noloop
            mk "Did you want me to put up more of a fight?"
            play voice2 d3s11b_mcheh noloop
            mc "I might enjoy that."

            jump d19s07_sex

label d19s07_problem:

    $ d19s07_problem = True

    scene d19s07-06 mc-mk-cafe-sit3_c1 with dissolve
    play voice3 min_disappointed_mph noloop
    mk "That's a problem."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh?"
    mk "Why don't you do it?"
    scene d19s07-07 mc-mk-cafe-sit4_c2 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "I'm pretty sure I'm not his type, but I've seen the way he looks at you."
    scene d19s07-08 mc-mk-cafe-sit5_c1 with dissolve
    play voice3 min_happy_relief noloop
    mk "Look, you and I have fucked, and I gotta admit that was kinda fun, but it was also repulsive."
    play voice2 mc_arrogant_heh2 noloop
    mc "Repulsive?"
    mk "You might have forgotten, but I'm a lesbian. Guys don't do it for me."
    scene d19s07-04 mc-mk-cafe-sit1_c2 with dissolve
    play voice2 mc_disappointed_off1 noloop
    if d15s05_rescue is True or d15s05_leave is True or d15s05_suck is True:
        mc "Really? So I just imagined you sucking and fucking every guy you could in that toilet stall?"
    else:
        mc "I didn't forget, but I guess..."
    scene d19s07-04 mc-mk-cafe-sit1_c1 with dissolve
    play voice3 maria_what noloop
    mk "What?"
    scene d19s07-05 mc-mk-cafe-sit2_c2 with dissolve
    play voice2 mc_disappointed_ehh2 noloop
    mc "I mean, I figured you enjoyed it. That maybe you were bisexual or something."
    scene d19s07-09 mc-mk-cafe-sit6_c1 with dissolve
    play voice3 min_thinking_hmm1 noloop
    mk "Look, maybe I've got some identity issues ever since that night we fucked in that dream."
    mk "Maybe all the stress of college broke my brain a bit."
    mk "Maybe there are some other issues I need to work through that I don't want to tell you about."
    mk "I'm going to be working on that. Maybe I'll be back for the autumn semester. Maybe I'll drop out or try to finish my senior year sometime later."
    scene d19s07-09 mc-mk-cafe-sit6_c2 with dissolve
    play voice2 mc_surprised_wow1 noloop
    mc "Wow. Seriously?{w} I had no idea."
    scene d19s07-10 mc-mk-cafe-sit7_c1 with dissolve
    play voice3 dahlia_yes_yeah4 noloop
    mk "Yeah, well.{w} I guess I just have to ask... how important is this to you?"
    play voice2 mc_thinking_hmm5 noloop
    mc "What do you want?"
    mk "I'd like to think that we are friends."
    scene d19s07-10 mc-mk-cafe-sit7_c2 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay."
    scene d19s07-25 mc-mk-problem1_c1 with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    mk "If you're my friend, there isn't anything I wouldn't do for you. Even this."
    play voice2 d1s1_mmm noloop
    mct "But if I were really her friend, I wouldn't ask her to do this."
    mk "So, I guess I need to know. Are we friends? And if so, do you need me to do this?"
    scene d19s07-25 mc-mk-problem1_c2 with dissolve
    menu:
        "Maria is my friend. I can't ask this of her."(hint="d19s07m02c01"):
            $ d19s07_mk_friend = True
            $ d19s07_need = False
        "Maria is my friend, but this is really important."(hint="d19s07m02c02"):

            $ d19s07_mk_friend = True
            $ d19s07_need = True
        "We aren't friends. Let her go."(hint="d19s07m02c03"):

            $ d19s07_mk_friend = False
            $ d19s07_need = False
        "We aren't friends, but I need this."(hint="d19s07m02c04"):

            $ d19s07_mk_friend = False
            $ d19s07_need = True

    if d19s07_mk_friend is True:
        play voice2 d1s5_mcthinks noloop volume 1.5
        mc "I'd like to think we're friends."
        scene d19s07-26-1 mk-problem2_c1 with dissolve
        play voice3 min_thinking_oh noloop
        mk "Really?"
        play voice2 mc_disappointed_ehh3 noloop
        mc "I mean, I don't know you very well, and I don't understand what is going on with you these days..."
        mc "But, you're interesting to be around and I've honestly come to like it when you're around."
        scene d19s07-26-4 mk-problem5_c1 with dissolve
        play voice3 min_thinking_mhh noloop
        mk "Not because of the sex?"
        play voice2 mc_thinking_hmm4 noloop
        mc "Well, not JUST because of the sex."
        scene d19s07-26-3 mk-problem4_c1 with dissolve
        play voice3 min_old_laugh noloop
        mk "*laughs* Fair enough."
    else:
        play voice2 d1s5_mcthinks noloop volume 1.5
        mc "Honestly?{w} I'm not going to lie. We aren't friends."
        scene d19s07-27-8 mk-problem8_c1 with dissolve
        play voice3 min_thinking_mhh noloop
        mk "Understood."
        play voice2 mc_disappointed_ehh3 noloop
        mc "I don't really know or understand you. You seem kinda unhinged."
        scene d19s07-27-11 mk-problem11_c1 with dissolve
        play voice3 dahlia_yes_yeah3 noloop
        mk "I am, yeah.{w} Well, at least I have been."
        play voice2 mc_thinking_hmm1 noloop
        mc "I'm not saying we can't ever be friends. I'd like to get to know you better."
        scene d19s07-27-7 mk-problem7_c1 with dissolve
        play voice3 min_thinking_oh noloop
        mk "Likewise.{w} Although, maybe without the sex."
        play voice2 d4s4_mclaugh noloop
        mc "*laughs* Fair enough."

    if d19s07_need is True:
        scene d19s07-11 mc-mk-cafe-stand1_c2 with dissolve
        play voice2 mc_thinking_hmm3 noloop
        mc "That said, this is really important to me."
        if study_points >= 6:
            mc "I can probably get Nordin's vote without this, but I want to be certain."
        else:
            mc "I probably won't get Nordin's vote without you doing this."
        scene d19s07-15 mc-mk-cafe-seduction2_c2 with dissolve
        mc "If you say \"No\" I can respect that.{w} I will respect that."
        mc "But if you could do this for me...{w} well, it would be really important to me."
        scene d19s07-11 mc-mk-cafe-stand1_c1 with dissolve
        play voice3 min_disappointed_ehh2 noloop
        mk "Okay, I'll do it."
        scene d19s07-13 mc-mk-cafe-stand3_c2 with dissolve
        play voice2 mc_yes_yeah8 noloop
        mc "Really?"
        scene d19s07-15 mc-mk-cafe-seduction2_c1 with dissolve
        play voice3 min_yes_ugu noloop
        mk "It might be good for me to do this. Get something out of my system."
        play voice2 mc_arrogant_huh3 noloop
        mc "If you're certain."
        mk "I am.{w} What do you want me to do?"

        jump d19s07_roleplay
    else:

        scene d19s07-11 mc-mk-cafe-stand1_c2 with dissolve
        play voice2 mc_arrogant_nah1 noloop
        mc "Having said that, I've reconsidered.{w} I can't ask this of you."
        scene d19s07-20 mc-mk-cafe-negative1_c1 with dissolve
        play voice3 min_disappointed_ehh2 noloop
        mk "It's a relief to hear you say that, but I should tell you..."
        mk "You're very charismatic - for a guy. I'm sure you can convince me if you change your mind."
        scene d19s07-21 mc-mk-cafe-negative2_c2 with dissolve
        play voice2 mc_no_nah2 noloop
        if study_points >= 6:
            mc "I can probably get Nordin's vote without this, but either way it was wrong of me to suggest it."
        else:
            mc "I won't change my mind. It was wrong of me to even ask you."
        mc "I didn't realize what you were going through, but I definitely don't want to exploit you or anyone."
        scene d19s07-22 mc-mk-cafe-talk1_c1 with dissolve
        play voice3 min_arrogant_huh1 noloop
        mk "Huh. Charismatic and moral.{w} You're a good man, [mcname] Young."
        scene d19s07-22 mc-mk-cafe-talk1_c2 with dissolve
        mct "I'm not. I'm really really not.{w} But I'm trying to be."
        scene d19s07-23 mc-mk-cafe-talk2_c2 with dissolve
        play voice2 mc_yes_aga2 noloop
        mc "Thank you.{w}.. and good luck. I hope to see you again in the autumn semester."
        scene d19s07-23 mc-mk-cafe-talk2_c1 with dissolve
        play voice3 min_yes_ugu noloop
        mk "Ditto.{w} Good luck and I hope to see you again."

        stop music fadeout 3.5
        jump d19s08

label replay_d19s07:
label d19s07_roleplay:

    $ d19s07_mk_nordin = True

    if _in_replay:
        play music thinking_music_3
        $ renpy.music.set_volume(0.7, 1.5, "music")
    scene d19s07-15 mc-mk-cafe-seduction2_c2 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "I thought we could do a little roleplay."
    scene d19s07-16 mc-mk-cafe-seduction3_c1 with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    mk "Let me guess - you play Professor Nordin?"
    scene d19s07-16 mc-mk-cafe-seduction3_c2 with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "Exactly. And you play as yourself.{w} You show me how you're going to seduce him."
    scene d19s07-17 mc-mk-cafe-seduction4_c1 with dissolve
    play voice3 maria_argh noloop
    mk "And then I fuck you, right?"
    scene d19s07-17 mc-mk-cafe-seduction4_c2 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Well, you will fuck him... so in this roleplay... yeah."
    if d19s07_take_virginity is True:
        scene d19s07-15 mc-mk-cafe-seduction2_c2 with dissolve
        mc "Would you prefer that you lose your virginity to the old man?"
        scene d19s07-15 mc-mk-cafe-seduction2_c1 with dissolve
        play voice3 dahlia_arrogant_pff noloop
        mk "Honestly?{w} As far as I'm concerned you took my virginity on the roof of that building."
        play voice2 mc_thinking_mmm5 noloop
        mc "That was just a dream... or something."
        mk "It was real enough for me."
        scene d19s07-14 mc-mk-cafe-seduction1_c2 with dissolve
        play voice2 mc_thinking_mmm1 noloop
        mc "Well, now you'll get to compare it to the real thing."
        play voice3 min_yes_simple noloop
        mk "I suppose that's true."
    else:
        mc "Is that going to be a problem?"
        scene d19s07-18 mc-mk-cafe-seduction5_c1 with dissolve
        play voice3 dahlia_no_uhuh noloop
        mk "Sure, why not."
    scene d19s07-12 mc-mk-cafe-stand2_c2 with dissolve
    play voice2 mc_yes_okay3 noloop
    mc "Okay.{w} Pretend that I'm Professor Nordin and you're you."
    mc "There's no classes tomorrow, but maybe we can get him to the classroom for some reason?"
    scene d19s07-14 mc-mk-cafe-seduction1_c1 with dissolve
    play voice3 min_thinking_hmm3 noloop
    mk "He'll be in his office tomorrow. He's always there for students who need help."
    scene d19s07-14 mc-mk-cafe-seduction1_c2 with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "Okay, so let's do that instead.{w} I guess you need his help."
    scene d19s07-15 mc-mk-cafe-seduction2_c1 with dissolve
    play voice3 maria_meeh noloop
    mk "It is more like I'm helping you, but yeah, I get what you're saying."
    scene d19s07-15 mc-mk-cafe-seduction2_c2 with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "You walk into the room, closing it behind you, and approach his desk."
    scene d19s07-16 mc-mk-cafe-seduction3_c1 with dissolve
    play voice3 min_thinking_emm noloop
    mk "Professor Nordin, may I have a moment of your time?"
    scene d19s07-16 mc-mk-cafe-seduction3_c2 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Ah, Miss Kovalevich. Did you find your pencil?"
    scene d19s07-17 mc-mk-cafe-seduction4_c1 with dissolve
    play voice3 min_surprised_oh noloop
    mk "That is actually what I wanted to - discuss - with you."
    scene d19s07-17 mc-mk-cafe-seduction4_c2 with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Oh? What do you mean?"
    scene d19s07-18 mc-mk-cafe-seduction5_c1 with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    mk "I wanted to talk to you about Mister Young's pencil."
    scene d19s07-18 mc-mk-cafe-seduction5_c2 with dissolve
    play voice2 d2s12_emmm noloop volume 1.4
    mc "Do you really want to be that obvious from the beginning? You could leave my name out of it."
    scene d19s07-15 mc-mk-cafe-seduction2_c1 with dissolve
    play voice3 min_old_hmm noloop
    mk "If that's what you want."
    scene d19s07-18 mc-mk-cafe-seduction5_c1 with dissolve
    mk "Professor, I was hoping to talk to you about my lost pencil."
    scene d19s07-17 mc-mk-cafe-seduction4_c2 with dissolve
    play voice2 mc_no_nope1 noloop

    $ Lovense.stop()

    mc "I'm afraid I can't help you with that. You could check the Lost & Found."
    play sound sfx_cloth_rustling4 volume 1.4
    $ Lovense.vibrate(8)
    scene d19s07-19 mc-mk-cafe-crotch_c1 with hpunch
    play voice3 dahlia_happy_hmm2 noloop
    mk "I think I know exactly where it is."
    scene d19s07-19 mc-mk-cafe-crotch_c2 with dissolve
    play voice2 mc_scared_huuuh3 noloop
    mc "Miss Kovalevich! I must object!!!"
    scene d19s07-20 mc-mk-cafe-negative1_c1 with dissolve
    $ Lovense.vibrate(1)
    play voice3 min_surprised_what noloop
    mk "What? Why?"
    scene d19s07-20 mc-mk-cafe-negative1_c2 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Let him make the first move - physically. Your job is to seduce him into making a move."
    play voice3 min_thinking_oh noloop
    mk "Oh, it's like Hancock."
    play voice2 mc_surprised_huh6 noloop
    mc "Huh?"
    scene d19s07-21 mc-mk-cafe-negative2_c1 with dissolve
    play voice3 dahlia_no_simple noloop
    mk "No, not Hancock. That other film he was in. Where the guy is supposed to get 90%% of the way to the kiss, but let her come that last 10%%... or not."
    play voice2 mc_thinking_hmm4 noloop
    mc "Sorta. Except you're a girl."
    mk "Still, I should get to 90%% and let him put out the last 10%%."
    scene d19s07-21 mc-mk-cafe-negative2_c2 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah, I guess.{w} Exactly... I think."
    scene d19s07-22 mc-mk-cafe-talk1_c1 with dissolve
    play voice3 min_thinking_hmm1 noloop
    mk "What happens if I end up like the secretary in the Maltese Falcon?"
    scene d19s07-22 mc-mk-cafe-talk1_c2 with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "You mean if you do everything right down to licking his cigarette and he doesn't stick his dick in you?"
    scene d19s07-23 mc-mk-cafe-talk2_c1 with dissolve
    play voice3 min_yes_aga noloop
    mk "Exactly. What happens if he ignores my advances?"
    scene d19s07-23 mc-mk-cafe-talk2_c2 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Then I guess you have two choices."
    scene d19s07-25 mc-mk-problem1_c1 with dissolve
    play voice3 min_surprised_huh1 noloop
    mk "Either rape him or walk away?"
    scene d19s07-25 mc-mk-problem1_c2 with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "Not exactly what I had in mind, but..."
    scene d19s07-26-1 mk-problem2_c1 with dissolve
    play voice3 min_happy_relief noloop
    mk "What exactly do you need me to do?"
    scene d19s07-25 mc-mk-problem1_c2 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay, so I'm going to be outside the room-"
    scene d19s07-27-12 mk-problem12_c1 with dissolve
    play voice3 min_surprised_huh2 noloop
    mk "With the door closed, how will you know what's going on?"
    play voice2 mc_thinking_hmm5 noloop
    mc "Easy. You'll leave it open a crack so I can watch."
    scene d19s07-27-13 mk-problem13_c1 with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    mk "Okay."
    scene d19s07-25 mc-mk-problem1_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "So, the moment he penetrates you, I'll see it. I'll walk in - catching him in the act."
    if is_antagonist_mode is True:
        mk "And then you leverage that to get his vote on your Final Exam?"
    else:
        mk "And then you let him know that I'm a present and a bribe from you to him."
    scene d19s07-25 mc-mk-problem1_c2 with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "Exactly."
    scene d19s07-23 mc-mk-cafe-talk2_c1 with dissolve
    play voice3 min_disappointed_ehh3 noloop
    mk "So, all you really need is his dick inside me.{w} Oral, anal, vaginal... it doesn't make a difference, right?"
    scene d19s07-23 mc-mk-cafe-talk2_c2 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Vaginal or Anal would be preferred.{w} Oral might be..."
    if is_antagonist_mode is True:
        mc "Well, he might not feel as compromised."
    else:
        mc "Well, he might not feel as thankful for the gift."
    scene d19s07-20 mc-mk-cafe-negative1_c1 with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    mk "Easy enough.{w} Leave it to me."
    scene d19s07-20 mc-mk-cafe-negative1_c2 with dissolve
    play voice2 d1s2_hmm noloop volume 1.6
    mc "You're sure?"
    scene d19s07-18 mc-mk-cafe-seduction5_c1 with dissolve
    play voice3 dahlia_sex_closedmoan1 noloop
    mk "Fuck me and find out."
    scene d19s07-18 mc-mk-cafe-seduction5_c2 with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "What?"
    play sound sfx_cloth_rustling2
    $ Lovense.vibrate(4)
    scene d19s07-19 mc-mk-cafe-crotch_c1 with dissolve
    play voice3 dahlia_sex_closedmoan2 noloop
    mk "Fuck me.{w} I'll do what you want tomorrow, but first you gotta pump my cunthole full of your semen right here, right now."
    scene d19s07-19 mc-mk-cafe-crotch_c2 with dissolve
    play voice2 d2s9_confused noloop volume 1.4
    mc "I forget - I've been with so many people lately...{w} Are you on birth control?"
    scene d19s07-19 mc-mk-cafe-crotch_c1 with dissolve
    play voice3 maria_argh noloop volume 1.4
    mk "Doesn't matter.{w} Are you gonna pump me full of your seed or not?"
    play voice2 mc_arrogant_hm3 noloop
    mc "I guess I really don't have a choice."

    jump d19s07_sex

label d19s07_sex:

    $ Lovense.stop()
    scene d19s07-28 mc-mk-undress1_c1 with fade
    $ Lovense.vibrate(2)
    play sound sfx_skirt_off2
    play voice3 maria_aah noloop
    mk "Bring it on, sex machine!"
    play voice2 mc_yes_yeah7 noloop
    mc "Alright! How do you want it?!"
    scene d19s07-28 mc-mk-undress1_c2 with dissolve
    play voice3 min_disappointed_ehh1 noloop
    mk "I have three conditions. The last is that you MUST creampie my pussy."
    play voice2 mc_yes_sure1 noloop
    mc "Sounds good so far."
    play sound sfx_cloth_rustling5
    scene d19s07-28-2 mc-mk-undress2_c1 with dissolve
    play voice3 min_thinking_hmm2 noloop
    mk "The second is that you have to help me recreate a scene."
    scene d19s07-28-2 mc-mk-undress2_c2 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Okay...{w} Wait, what?"
    scene d19s07-28-2 mc-mk-undress2_c1 with dissolve
    play voice3 min_thinking_emm noloop
    mk "Do you remember how we were atop that roof when you deflowered me?"
    mk "When your penis was the first to penetrate my virgin vagina?"
    scene d19s07-28-2 mc-mk-undress2_c3 with dissolve
    play voice2 d9s2_yeah noloop volume 2.5
    mc "Technically, I guess. It wasn't real and your hymen-"
    play sound sfx_underpants_off1 volume 1.6
    scene d19s07-29-4 mc-mk-forplay4_c2 with dissolve
    play voice3 min_yes_simple noloop
    mk "Yes, yes, I broke my hymen with a hairbrush long before I met you, but you were the first and the only penis that has ever been inside me."
    if date_mk_tr is True and d15s05_rescue is False:
        play voice2 mc_hey_hey2 noloop
        mc "We both know that isn't true."
        mk "The only penis that ever mattered."
        mc "So, you want to recreate that event."
    scene d19s07-29 mc-mk-forplay_c1 with dissolve
    $ Lovense.vibrate(5)
    play voice3 dahlia_sex_closedmoan3 noloop
    mk "Wait just a second. I'm flying through the air towards you."
    scene d19s07-29 mc-mk-forplay_c3 with dissolve
    mk "And then - here I am - spread out before you."
    scene d19s07-29 mc-mk-forplay_c2 with dissolve
    play voice3 min_old_moan1 noloop volume 1.6
    mk "Waiting for your cock."
    play voice2 d1s1_mmm noloop
    mct "That's my cue."
    $ renpy.music.set_volume(1.0, 1.5, "music")
    $ Lovense.vibrate(7)
    scene d19s07-a30-1 mc-mk-sex-01 with hpunch
    play voice3 maria_yes noloop
    mk "FUCK YES!!!{w} Just like the first time."
    play voice2 d7s4_mcbreathing
    play voice3 min_old_moans
    $ Lovense.pattern("6;10", 1700)
    scene d19s07-a1
    pause
    scene d19s07-a2 with dissolve
    mct "Like a virgin. Hey! Touched for the very first time."
    pause
    scene d19s07-a3 with dissolve
    mk "TAKE ME LIKE THERE'S NO TOMORROW."
    pause
    $ Lovense.pattern("6;10", 900)
    scene d19s07-a1-f with dissolve
    mct "Ok, let me tell ya what \"Like a Virgin\" is about."
    pause
    scene d19s07-a2-f with dissolve
    mct "It's all about this cooze who's a regular fuck machine."
    pause
    scene d19s07-a3-f with dissolve
    mct "I'm talking, morning, day,night, afternoon..."
    pause
    stop voice2 fadeout 1.0
    play sound sfx_bed_slide3 volume 0.5
    $ Lovense.stop()
    $ Lovense.vibrate(5)
    scene d19s07-a31-1 mc-mk-sex-01 with fade
    play voice3 min_disappointed_off noloop
    mk "Where are you?{w} What are you thinking about?"
    play voice2 d7s4_mcbreathing
    play voice3 min_old_breathing
    queue voice3 min_old_moans
    $ Lovense.pattern("6;10", 1700)
    scene d19s07-a4
    pause
    scene d19s07-a5 with dissolve
    mct "Dick, dick, dick, dick, dick, dick, dick, dick, dick."
    mc "I'm right here on the roof with you."
    pause
    scene d19s07-a6 with dissolve
    mk "Good. Now I want you to put your hands on my shoulders."
    mc "Okay..."
    pause
    $ Lovense.pattern("6;10", 900)
    scene d19s07-a4-f with dissolve
    mk "Now push me."
    mc "What?!"
    pause
    scene d19s07-a5-f with dissolve
    mk "Push me off the roof.{w} DO IT!!!"
    pause
    scene d19s07-a6-f with dissolve
    mc "Okay."
    play voice3 maria_laughing noloop
    queue voice3 min_old_moans
    mk "Hahahahahahahahaha!!!"
    pause
    stop voice3 fadeout 1.0
    $ Lovense.stop()
    $ Lovense.vibrate(5)
    scene d19s07-a32-1 mc-mk-sex-01_i with fade
    play voice2 d1s5_mchappy noloop
    mc "Was that your second condition?"
    play voice2 d7s4_mcbreathing
    play voice3 min_old_moans
    $ Lovense.pattern("6;10", 1700)
    scene d19s07-a7
    pause
    scene d19s07-a8 with dissolve
    mk "I can't hear you. I'm falling indefinitely."
    pause
    scene d19s07-a9 with dissolve
    mc "Your first condition was that I help you recreate the scene."
    mk "Yes! Thank you."
    pause
    $ Lovense.pattern("6;10", 900)
    scene d19s07-a7-f with dissolve
    mc "Your last condition was that I creampie your pussy."
    mct "Which is getting harder to do as you act like a crazy cunt."
    pause
    scene d19s07-a8-f with dissolve
    mk "YES!!! I still want that."
    mc "So, what's your second condition?"
    if persistent.is_special is True:
        mk "I want you to rape the shit out of me!!!"
    else:
        mk "I want you to fuck the shit out of me!!!"
    mc "What?!"
    pause
    scene d19s07-a9-f with dissolve
    mk "Do me! As roughly as possible!!"
    mk "Choke me! Pound me!! Throw me on the floor and have your way with me!!!"
    mk "Think of every rough sex porn you've ever seen and do it all to me!!!!!"
    pause
    stop voice3 fadeout 1.0
    stop voice2 fadeout 1.0
    $ Lovense.stop()
    $ Lovense.vibrate(7)
    scene d19s07-a34-1 mc-mk-sex-01_i with fade
    play voice3 maria_yes noloop
    mk "YESSS!!!!!"
    play voice2 mc_scared_oh2 noloop
    mc "Well, you asked for it..."
    play voice2 d7s4_mcbreathing
    play voice3 min_old_longmoan1
    $ Lovense.pattern("8;12", 1700)
    scene d19s07-a10
    pause
    scene d19s07-a11 with dissolve
    pause
    scene d19s07-a12 with dissolve
    pause
    $ Lovense.pattern("8;12", 900)
    scene d19s07-a10-f with dissolve
    pause
    scene d19s07-a11-f with dissolve
    pause
    scene d19s07-a12-f with dissolve
    pause

    if d19s07_mk_nordin is True:
        jump d19s07_ending
    else:
        stop voice3 fadeout 3.0
        stop voice2 fadeout 3.0
        stop music fadeout 3.5

        $ Lovense.stop()

        $ renpy.end_replay()
        jump d19s08

label d19s07_ending:

    play voice3 min_old_orgasm1 noloop
    $ Lovense.stop()
    $ Lovense.vibrate(17)
    scene d19s07-37 mc-mk-end1-cum_c1 with vpunch
    play voice2 d9s5_auch2 noloop
    mk "OH FUCK YESSS YOU BASTARD!!!"
    $ renpy.music.set_volume(0.6, 4.5, "music")
    queue voice2 mc_surprised_what3 noloop
    $ Lovense.vibrate(1)
    mc "Wait, what?!"
    queue voice3 maria_laughing noloop
    mk "PUMP ME FULL OF YOUR SEED!!! I HOPE I GET PREGNANT WITH YOUR BASTARD CHILD!!!"

    $ Lovense.stop()

    scene d19s07-38 mc-mk-end2_c1 with dissolve
    play voice2 mc_pain_ou1 noloop
    mct "Is she insane?"
    scene d19s07-38 mc-mk-end2_c2 with dissolve
    play voice3 min_angry_breath noloop
    mk "*panting* I'm just kidding.{w} I'm on birth control now."
    scene d19s07-38 mc-mk-end2_c3 with dissolve
    play voice2 mc_pain_rrrr noloop
    mc "Fucking hell. You scared the shit out of me."
    scene d19s07-39 mk-end-ceiling1_c2 with dissolve
    play voice3 min_happy_mmm noloop
    mk "Really?{w} I might be into that."
    $ renpy.end_replay()
    $ unlock_gallery_slot("scene", "d19s07")
    if d19s07_problem is False:
        play voice2 mc_hey_hey3 noloop
        mc "You are more than a little crazy, aren't you?"
        scene d19s07-39-2 mk-end-ceiling2_c2 with dissolve
        play voice3 dahlia_disappointed_ehh2 noloop
        mk "I am.{w} I really need to do something about it."
        play voice2 mc_thinking_mmm3 noloop
        mc "Is there some medication or counseling...?"
        scene d19s07-39-3 mk-end-ceiling3_c2 with dissolve
        play voice3 min_no_nah noloop
        mk "Don't worry. I've got plans for the summer."
        play voice2 mc_disappointed_off1 noloop
        mc "I'm afraid to hear what they might be."
        if persistent.is_special is True:
            scene d19s07-39-4 mk-end-ceiling4_c2 with dissolve
            play voice3 dahlia_disappointed_hmm1 noloop
            mk "I've got a month paid & scheduled at a detox center."
            play voice2 mc_arrogant_huh3 noloop
            mc "You're on drugs or something?"
            scene d19s07-40 mk-end-face1_c2 with dissolve
            play voice3 min_surprised_oh noloop
            mk "I thought that was obvious."
            scene d19s07-40-2 mk-end-face2_c2 with dissolve
            mk "I've only been getting through college this year with a lot of help from Amphetamines."
            play voice2 mc_angry_huh2 noloop
            mc "Damn. I didn't realize."
        scene d19s07-40-3 mk-end-face3_c2 with dissolve
        play voice3 dahlia_disappointed_hmm2 noloop
        mk "Like I said, don't worry about it."
    scene d19s07-39-4 mk-end-ceiling4_c2 with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    mk "I think I'm going to clean up a bit before I leave. There's a big industrial sink in the back."
    play voice2 mc_yes_yeah5 noloop
    mc "I think I could use a shower myself."
    scene d19s07-39-2 mk-end-ceiling2_c2 with dissolve
    play voice3 min_surprised_ehh2 noloop
    mk "Maybe we can share..."
    play voice2 mc_arrogant_hm1 noloop
    mc "Weren't you a lesbian?"
    scene d19s07-40 mk-end-face1_c2 with dissolve
    play voice3 maria_aah noloop
    mk "Wait. You mean you aren't really a woman?!"
    play voice2 mc_surprised_what1 noloop
    mc "What?!"
    scene d19s07-39-2 mk-end-ceiling2_c2 with dissolve
    play voice3 dahlia_happy_laugh4 noloop
    mk "I'm just fucking with you."
    play voice2 mc_angry_hm1 noloop
    mc "I'm so confused."

    stop music fadeout 3.5
    jump d19s08
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
