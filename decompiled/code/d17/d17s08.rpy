image d17s08-a1 = Movie(play = "images/Day-17/s08/anim/d17s08-a1-4x-60fps.webm"    , start_image = "d17s08-29mc-sy-bj1_c3_00_i")
image d17s08-a1-f = Movie(play = "images/Day-17/s08/anim/d17s08-a1-2x-50fps.webm"    , start_image = "d17s08-29mc-sy-bj1_c3_00_i")
image d17s08-a1-2 = Movie(play = "images/Day-17/s08/anim/d17s08-a1-2-4x-60fps.webm"  , start_image = "d17s08-30-a1 mc-sy-bj-anim-1-00_i")
image d17s08-a1-2-f = Movie(play = "images/Day-17/s08/anim/d17s08-a1-2-2x-50fps.webm"  , start_image = "d17s08-30-a1 mc-sy-bj-anim-1-00_i")
image d17s08-a2 = Movie(play = "images/Day-17/s08/anim/d17s08-a2-4x-60fps.webm"    , start_image = "d17s08-30-a2 mc-sy-bj-anim-2-00_i")
image d17s08-a2-f = Movie(play = "images/Day-17/s08/anim/d17s08-a2-2x-50fps.webm"    , start_image = "d17s08-30-a2 mc-sy-bj-anim-2-00_i")
image d17s08-a3 = Movie(play = "images/Day-17/s08/anim/d17s08-a3-4x-60fps.webm"    , start_image = "d17s08-30-a3 mc-sy-bj2-anim3-00_i")
image d17s08-a3-f = Movie(play = "images/Day-17/s08/anim/d17s08-a3-2x-50fps.webm"    , start_image = "d17s08-30-a3 mc-sy-bj2-anim3-00_i")
image d17s08-a10 = Movie(play = "images/Day-17/s08/anim/d17s08-28-a10-4x-60fps.webm", start_image = "d17s08-28-a10 mc-sy-handjob-anim-10-00_i")
image d17s08-a10-f = Movie(play = "images/Day-17/s08/anim/d17s08-28-a10-2x-50fps.webm", start_image = "d17s08-28-a10 mc-sy-handjob-anim-10-00_i")
image d17s08-a11 = Movie(play = "images/Day-17/s08/anim/d17s08-28-a11-4x-60fps.webm", start_image = "d17s08-28-a11 mc-sy-handjob-anim-11-00_i")
image d17s08-a11-f = Movie(play = "images/Day-17/s08/anim/d17s08-28-a11-2x-50fps.webm", start_image = "d17s08-28-a11 mc-sy-handjob-anim-11-00_i")
image d17s08-a12 = Movie(play = "images/Day-17/s08/anim/d17s08-28-a12-4x-60fps.webm", start_image = "d17s08-28-a12 mc-sy-handjob-anim-12-00_i")
image d17s08-a12-f = Movie(play = "images/Day-17/s08/anim/d17s08-28-a12-2x-50fps.webm", start_image = "d17s08-28-a12 mc-sy-handjob-anim-12-00_i")

image d17s08_blowjob_cum:
    "d17s08-30-2 mc-sy-cum1"
    pause (0.15)
    "d17s08-30-2 mc-sy-cum2" with hpunch
    pause (0.15)
    "d17s08-30-2 mc-sy-cum3" with hpunch
    pause (0.15)
    "d17s08-30-2 mc-sy-cum4" with hpunch
    pause (0.15)
    "d17s08-30-2 mc-sy-cum2"
    pause (0.15)
    "d17s08-30-2 mc-sy-cum3"
    pause (0.15)
    "d17s08-30-2 mc-sy-cum4"
    pause (0.15)
    "d17s08-30-2 mc-sy-cum2"
    pause (0.15)
    "d17s08-30-2 mc-sy-cum3"
    pause (0.15)
    "d17s08-30-2 mc-sy-cum4"
    pause (0.15)
    "d17s08-30-2 mc-sy-cum5"
    pause (0.15)
    "d17s08-30-2 mc-sy-cum2"
    pause (0.15)
    "d17s08-30-2 mc-sy-cum1_c3" with Dissolve (0.4)
    pause (0.25)

label d17s08:

    $ d17s08_points = 0

    scene black
    show screen scene_transistion(_("Later that evening"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound sfx_door_open3
    scene d17s08-1-1 mc-lc-talk1-1_c3
    with Fade(0.5, 0.5, 0.9)
    $ renpy.music.set_volume(0.45, 2.5, "music")
    play music love_gospel_intro fadein 2.0
    play voice3 lydia_lydiahey noloop
    lc "I'm glad you could come over tonight. {w}I like sleeping with my boyfriend, even if I'm not {i}sleeping{/i} with my boyfriend."
    scene d17s08-1-2 mc-lc-talk1-2_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "I enjoy it too."
    scene d17s08-1-2 mc-lc-talk1-2_c3 with dissolve
    play voice3 lydia_hmmmm noloop
    lc "I hope that doesn't upset you too much. We'll get there, I'm just not sure-"
    scene d17s08-1-1 mc-lc-talk1-1_c1 with dissolve
    play voice2 mc_no_nono1 noloop
    if love_lc is True:
        mc "Don't worry about it. I love you, and I enjoy every moment we're together."
    elif True:
        mc "Don't worry about it. I enjoy every moment we're together. We don't have to rush things."
    scene d17s08-1-2 mc-lc-talk1-2_c3 with dissolve
    play voice3 lydia_thinking noloop
    lc "Can I ask you a weird question?"
    scene d17s08-1-2 mc-lc-talk1-2_c1 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Of course."
    scene d17s08-1-1 mc-lc-talk1-1_c3 with dissolve
    play voice3 lydia_haha noloop
    lc "So, I was looking it up, and apparently I'm what they call a \"voyeur\". I like watching other people having sex."
    play voice2 mc_yes_sure1 noloop
    mc "Sure, I know what a voyeur is."
    play voice3 dahlia_thinking_hmm4 noloop
    lc "Do you think that's what I am?"
    scene d17s08-1-2 mc-lc-talk1-2_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "If it walks like a duck and quacks like a duck, yeah. I'd say you're a voyeur."
    scene d17s08-1-2 mc-lc-talk1-2_c3 with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    lc "Okay, so the other side of voyeur is an exhibitionist. Do you think of yourself as an exhibitionist?"
    scene d17s08-1-1 mc-lc-talk1-1_c1 with dissolve
    play voice2 d2s9_confused noloop volume 1.6
    mc "I mean, I like it when you're watching me fuck other people, but I wouldn't call myself an exhibitionist."
    scene d17s08-1-1 mc-lc-talk1-1_c3 with dissolve
    play voice3 lydia_moan1 noloop
    lc "But you were with all those people on Sunday - especially mud wrestling in front of that audience."
    scene d17s08-1 mc-lc-talk1_c2 with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "True. I don't have a problem with other people watching, but I was always focused on my partner."
    scene d17s08-1 mc-lc-talk1_c1 with dissolve
    play voice3 dahlia_thinking_mmm2 noloop
    lc "Hmm. {w}So, what if I ran into some real exhibitionists on campus?"
    scene d17s08-1 mc-lc-talk1_c3 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, well. I mean, I suppose I've been in that situation."
    scene d17s08-1-3 mc-lc-talk1-3_c1 with dissolve
    play voice3 lydia_aga noloop
    lc "Of course you have. I should've known."
    if date_pw is True:
        if date_mh is True:
            scene d17s08-1-3 mc-lc-talk1-3_c3 with dissolve
            play voice2 mc_thinking_hmm2 noloop
            mc "I'm not going to say who I was with, because they might not want people to know."
            scene d17s08-2 mc-lc-talk2_c1 with dissolve
            play voice3 lydia_morningoh noloop
            lc "Oh?"
            scene d17s08-2 mc-lc-talk2_c3 with dissolve
            play voice2 mc_thinking_mmm4 noloop
            mc "You'll understand in a minute. So, I was at the beach with someone a week or two ago."
            mc "We were swimming - naked - having fun. Got out of the water, had a bit more fun on the sand."
            mc "We thought we were all alone until someone else walked by."
            scene d17s08-4 mc-lc-talk4_c1 with dissolve
            play voice3 lydia_huh2 noloop
            lc "O.M.G. Did you freak out?"
            scene d17s08-4 mc-lc-talk4_c3 with dissolve
            play voice2 mc_no_no2 noloop
            mc "I didn't, but the woman I was with got completely terrified."
            mc "She started thinking about her life, her career, her reputation, and all of that."
            scene d17s08-5 mc-lc-talk5_c1 with dissolve
            play voice3 lydia_oops noloop
            lc "Oh, wow."
            scene d17s08-5 mc-lc-talk5_c3 with dissolve
            play voice2 mc_happy_a1 noloop
            mc "It was no big deal, really. The person who walked by is a friend of mine and wouldn't say anything to anyone."
            mc "Still, for the person I was with - the situation went from relaxed and freeing to scary in an instant."
        elif True:
            scene d17s08-1-3 mc-lc-talk1-3_c3 with dissolve
            play voice2 mc_thinking_hmm2 noloop
            mc "So, a couple of the girls{w} - sorry - women that I've been with have enjoyed taking risks like that in public."
            mc "One of them loves to be seen. She intentionally flashes people and would run around bareass naked everywhere if she could."
            scene d17s08-2 mc-lc-talk2_c1 with dissolve
            play voice3 dahlia_thinking_hmm1 noloop
            lc "Is that Polly?"
            scene d17s08-2 mc-lc-talk2_c3 with dissolve
            play voice2 mc_yes_yeah7 noloop
            mc "Yeah, how did you know?"
            scene d17s08-4 mc-lc-talk4_c1 with dissolve
            play voice3 lydia_laugh noloop
            lc "She was here on Sunday."
            scene d17s08-4 mc-lc-talk4_c3 with dissolve
            play voice2 mc_disappointed_ah1 noloop
            mc "Oh, right. {w}Polly's girlfriend, on the other hand, isn't as comfortable with being seen in public."
            scene d17s08-5 mc-lc-talk5_c1 with dissolve
            play voice3 lydia_huh2 noloop
            lc "I didn't know she had a girlfriend. {w}Anyone I know?"
            scene d17s08-5 mc-lc-talk5_c3 with dissolve
            play voice2 mc_yes_yes1 noloop
            mc "Yes, but I'm not sure if they're public with their relationship yet."
            scene d17s08-6 mc-lc-talk6_c1 with dissolve
            play voice3 dahlia_thinking_hmm3 noloop
            lc "Mysterious."
            scene d17s08-6 mc-lc-talk6_c3 with dissolve
            play voice2 mc_yes_aga2 noloop
            mc "Anyway, her girlfriend is pretty cool with doing risky things, but I'm almost certain she would freak the fuck out if we got caught."

    elif cage_ntr is True:
        scene d17s08-1-3 mc-lc-talk1-3_c3 with dissolve
        play voice2 mc_thinking_hmm2 noloop
        mc "I can't speak for everyone, but I can tell you what I did."
        scene d17s08-2 mc-lc-talk2_c1 with dissolve
        play voice3 dahlia_thinking_hmm1 noloop
        lc "Please do."
        scene d17s08-2 mc-lc-talk2_c3 with dissolve
        play voice2 mc_thinking_mmm4 noloop
        mc "So, the first day I got back from being sick - shortly after I found out about Fetish Locator..."
        mc "I was sitting there during class when Min ate Antony's cum right there in the front row."
        scene d17s08-4 mc-lc-talk4_c1 with dissolve
        play voice3 dahlia_surprised_what noloop
        lc "She did what?!"
        scene d17s08-4 mc-lc-talk4_c3 with dissolve
        play voice2 mc_yes_aga1 noloop
        mc "She jerked him off under the desk, and then licked his cum off her hand."
        scene d17s08-5 mc-lc-talk5_c1 with dissolve
        play voice3 lydia_ah noloop
        lc "During class?!"
        scene d17s08-5 mc-lc-talk5_c3 with dissolve
        play voice2 mc_yes_yes1 noloop
        mc "Yep. I'm pretty certain I was the only person that noticed at the time."
        scene d17s08-6 mc-lc-talk6_c1 with dissolve
        play voice3 lydia_huh2 noloop
        lc "How is that possible?"
        scene d17s08-6 mc-lc-talk6_c3 with dissolve
        play voice2 mc_arrogant_huh1 noloop
        mc "I was just sitting in the right place at the right time, I guess."
        scene d17s08-2 mc-lc-talk2_c1 with dissolve
        play voice3 dahlia_happy_hmm1 noloop
        lc "Did they notice you watching?"
        scene d17s08-2 mc-lc-talk2_c3 with dissolve
        play voice2 mc_no_nope2 noloop
        mc "Nope. Class just went on like nothing had happened."
        scene d17s08-4 mc-lc-talk4_c1 with dissolve
        play voice3 lydia_oops noloop
        lc "Did you ever say anything to them about that?"
        scene d17s08-4 mc-lc-talk4_c3 with dissolve
        play voice2 mc_no_uhuh1 noloop
        mc "It didn't come up."
        scene d17s08-5 mc-lc-talk5_c1 with dissolve
        play voice3 dahlia_happy_hmm2 noloop
        lc "Not even after we all saw them together at Min's Party?"
        scene d17s08-1-3 mc-lc-talk1-3_c3 with dissolve
        play voice2 mc_thinking_emm1 noloop
        mc "That was kinda different. They knew they had an audience there."
    elif True:
        scene d17s08-1-3 mc-lc-talk1-3_c3 with dissolve
        play voice2 mc_thinking_hmm2 noloop
        mc "I can't speak for everyone, but I can tell you what I did."
        scene d17s08-2 mc-lc-talk2_c1 with dissolve
        play voice3 dahlia_thinking_hmm1 noloop
        lc "Please do."
        scene d17s08-2 mc-lc-talk2_c3 with dissolve
        play voice2 mc_thinking_mmm4 noloop
        mc "I was in the locker room getting dressed after my shower and heard some noises coming from the other side of the lockers."
        mc "It turned out to be a couple of people fucking."
        scene d17s08-4 mc-lc-talk4_c1 with dissolve
        play voice3 lydia_huh2 noloop
        lc "Oh, wow. Did they notice you?"
        scene d17s08-4 mc-lc-talk4_c3 with dissolve
        play voice2 mc_no_nope2 noloop
        mc "Nope. I just went about my business and then left the locker room without interrupting them."
        scene d17s08-5 mc-lc-talk5_c1 with dissolve
        play voice3 dahlia_surprised_wow noloop
        lc "Wow. I'm not sure I could do that. {w}I'd have to either run away or stay & watch."
        scene d17s08-5 mc-lc-talk5_c3 with dissolve
        play voice2 mc_yes_aga2 noloop
        mc "Anyway, I realized I had forgotten something - I think it was my phone - so I went back for it."
        scene d17s08-6 mc-lc-talk6_c1 with dissolve
        play voice3 dahlia_happy_hmm1 noloop
        lc "Did you-?"
        scene d17s08-6 mc-lc-talk6_c3 with dissolve
        play voice2 mc_no_no2 noloop
        mc "No, but a friend of mine was standing there and jerking off watching them."
        scene d17s08-2 mc-lc-talk2_c1 with dissolve
        play voice3 dahlia_happy_hmm2 noloop
        lc "Did that bother them at all?"
        scene d17s08-6 mc-lc-talk6_c3 with dissolve
        play voice2 mc_no_uhuh1 noloop
        mc "Not at all. I found out later that was his kink. He liked watching that girl having sex with other people and she enjoyed having him watch."
        scene d17s08-4 mc-lc-talk4_c1 with dissolve
        play voice3 lydia_laugh noloop
        lc "So, it sounds like I shouldn't watch people - even if they are in public - unless I'm sure they're okay with me being there."
        scene d17s08-4 mc-lc-talk4_c3 with dissolve
        play voice2 d9s2_yeah noloop volume 1.8
        mc "Sounds about right."
        scene d17s08-5 mc-lc-talk5_c1 with dissolve
        play voice3 dahlia_thinking_hmm3 noloop
        lc "But then, why would they do something like that in the first place?"
        scene d17s08-6 mc-lc-talk6_c3 with dissolve
        play voice2 mc_thinking_hmm5 noloop
        mc "Oh, hmm.{w}.. well, I think the thrill for most exhibitionists is the chance of getting caught."
        mc "I don't think they actually want to be caught. They just want that risk they might be."

    scene d17s08-7 lc-sex-talk1_c1 with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    lc "Could I watch discreetly while I'm pretending to do something else?"
    scene d17s08-6 mc-lc-talk6_c3 with dissolve
    play voice2 mc_happy_hah1 noloop
    mc "You sound like this isn't just a fantasy."
    scene d17s08-12 lc-sex-talk6_c1 with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    lc "Maybe I have a neighbor that doesn't always close their curtains."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh?"
    scene d17s08-18 mc-lc-leave1_c1 with dissolve
    play voice3 lydia_hmmmm noloop
    lc "Anyway, I'm going to get a shower before we go to bed. I'll be back."
    scene d17s08-18-2 mc-lc-leave2_c2 with dissolve
    play voice2 mc_yes_okay3 noloop
    mc "Okay."
    play sound sfx_door_closed2

label replay_d17s08:

    if _in_replay:
        play music love_gospel
    queue music love_gospel
    scene d17s08-19_mc-empty_c1 with dissolve
    pause
    play sound sfx_door_open3
    scene d17s08-20 mc-sy-entry1_c1 with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "Stacy?"
    play sound sfx_door_creak2 volume 2.0
    scene d17s08-20-2 mc-sy-entry1-2_c1 with dissolve
    play voice3 fshhh noloop
    sy "I'm creeping."
    play voice2 d2s12_emmm noloop
    mc "What are you doing here?"
    scene d17s08-21 mc-sy-entry2_c1 with dissolve
    play voice3 stacy_mmm2 noloop
    sy "I need to get the data off your {i}USB device{/i}."
    scene d17s08-21 mc-sy-entry2_c2 with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "But, I mean, how are you here?"
    scene d17s08-22 mc-sy-entry3_c1 with dissolve
    play voice3 stacy_laugh4 noloop
    sy "I let myself in."
    scene d17s08-21 mc-sy-entry2_c2 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "I'm certain the door was locked."
    scene d17s08-22 mc-sy-entry3_c1 with dissolve
    play voice3 polly_aga noloop
    sy "And it will be locked again after I leave."
    scene d17s08-21 mc-sy-entry2_c2 with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What?"
    play voice3 stacy_angryhuh noloop
    sy "Just give me the device."
    scene d17s08-22 mc-sy-entry3_c2 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Uh, sure."
    scene d17s08-23 mc-sy-entry4_c1 with dissolve
    play voice3 stacy_hmm noloop
    sy "How long does your girlfriend take in the shower?"
    scene d17s08-23 mc-sy-entry4_c2 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "I mean, she's a girl, so..."
    scene d17s08-23 mc-sy-entry4_c1 with dissolve
    play voice3 stacy_huh2 noloop
    sy "Hmm. I don't take very long in the shower."
    scene d17s08-23 mc-sy-entry4_c2 with dissolve
    play voice2 mc_yes_yeah6 noloop
    mc "Yeah, but she's..."
    mc "Probably 30 minutes to an hour?"
    scene d17s08-24 mc-sy-entry5_c1 with dissolve
    play voice3 stacy_oh2 noloop
    sy "That should be plenty of time for the data transfer."
    scene d17s08-24 mc-sy-entry5_c2 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Oh, okay."
    if date_sy is True:
        $ d17s08_points = 6
        scene d17s08-25 mc-sy-kneel1_c1 with dissolve
        play voice3 stacy_mmm1 noloop
        sy "Actually... that should also be plenty of time for a little fun."
        scene d17s08-25 mc-sy-kneel1_c2 with dissolve
        play voice2 mc_yes_yeah8 noloop
        if persistent.is_special is True:
            mc "I mean, we could just wait for Lydia to get back if you want-"
        elif True:
            mc "Yeah, probably don't want Lydia to know about us just yet."
        scene d17s08-25 mc-sy-kneel1_c3 with dissolve
        play voice3 fshhh noloop
        sy "Shhh. {w}We're being sneaky."
        scene d17s08-25 mc-sy-kneel1_c2 with dissolve
        play voice2 mc_disappointed_off2 noloop
        mc "Oh, okay."


        $ Lovense.stop()

        scene d17s08-28 mc-sy-handjob_c1 with dissolve
        $ Lovense.vibrate(1)
        play voice3 stacy_moan4 noloop
        sy "This looks delicious."
        scene d17s08-28 mc-sy-handjob_c2 with dissolve
        play voice2 mc_arrogant_hm1 noloop
        mc "I'll take your word for it."
        scene d17s08-28 mc-sy-handjob_c3 with dissolve
        play voice3 dahlia_disappointed_ehh2 noloop
        sy "Let me show you."
        $ Lovense.vibrate(4)
        play voice3 stacy_sucks1
        scene d17s08-a1 with dissolve
        play voice2 d7s4_mcbreathing fadein 8.0
        pause
        play voice3 aaleyah_sucking_deep
        $ Lovense.vibrate(6)
        scene d17s08-a1-2 with dissolve
        pause
        scene d17s08-a2 with dissolve
        pause
        scene d17s08-a3 with dissolve
        pause
        play voice3 stacy_sucks1
        $ Lovense.vibrate(5)
        scene d17s08-a1-f with dissolve
        pause
        play voice3 aaleyah_sucking_deep
        $ Lovense.vibrate(8)
        scene d17s08-a1-2-f with dissolve
        pause
        scene d17s08-a2-f with dissolve
        pause
        scene d17s08-a3-f with dissolve
        pause
        $ renpy.music.set_volume(1.0, 0.0, "sound2")
        play sound2 sfx_handjob_cream1 volume 0.5
        scene d17s08-a11 with dissolve
        $ Lovense.vibrate(6)
        play voice3 stacy_moan1 noloop
        sy "How was that?"
        scene d17s08-a12 with dissolve
        mc "Your mouth is amazing."
        scene d17s08-a10 with dissolve
        play voice3 stacy_oh noloop
        sy "Just my mouth?"
        scene d17s08-a12 with dissolve
        if persistent.is_special is True:
            mc "You are absolutely amazing, sis."
        elif True:
            mc "You are absolutely amazing."
        play sound2 sfx_handjob_cream1
        scene d17s08-a11-f with dissolve
        play voice3 stacy_yes2 noloop
        sy "Damn right."
        mc "You're a fucking goddess."
        sy "You said it."
        scene d17s08-a12-f with dissolve
        mc "Just a little bit more..."
        play voice3 stacy_suckmoan3 noloop
        sy "Only if you promise to come down my throat."
        scene d17s08-a10-f with dissolve
        mc "You want me to fuck your face?"
        play voice3 stacy_moan6 noloop
        sy "No. I want you to cum in my mouth so intensely that it shoots down my throat."
        mc "Oh, fuck yes."
        stop sound2 fadeout 1.0
        play voice3 mc_sex_sucking_slow2
        $ Lovense.vibrate(10)
        scene d17s08-30 mc-sy-bj2_c1 with dissolve
        mc "What a fucking goddess you are..."
        scene d17s08-30 mc-sy-bj2_c2 with dissolve
        $ Lovense.vibrate(12)
        play voice2 mc_pain_ou1 noloop
        mc "Oh..."
        mc "OH-"
        $ Lovense.vibrate(14)
        scene d17s08-30 mc-sy-bj2_c3 with dissolve
        pause
        play voice2 d1s5_orgasm2 noloop
        play sound ["<silence 0.5>", mc_cum_sound1]
        play voice3 stacy_moans1 noloop
        scene d17s08_blowjob_cum with Dissolve (0.4)
        stop voice3 fadeout 1.0
        queue voice3 ["<silence 0.7>", gulp] noloop
        $ Lovense.vibrate(17)
        mc "OH FUCK YESSS"
        $ renpy.music.set_volume(0.3, 3.5, "music")
        scene d17s08-31 mc-sy-leave-talk1_c1 with fade


        $ Lovense.stop()

        play voice2 mc_scared_oh1 noloop
        mc "That's-"
        mc "That's fucking terrific."
        mc "How did you get so good at that?"
        scene d17s08-31 mc-sy-leave-talk1_c3 with dissolve
        play voice3 stacy_angry noloop
        sy "Research."
        scene d17s08-31 mc-sy-leave-talk1_c2 with dissolve
        play voice2 d1s2_hmm noloop volume 1.8
        mc "Research?"
        scene d17s08-32 mc-sy-leave-talk2_c3 with dissolve
        play voice3 polly_laughter noloop
        sy "I had six months to go through your porn box."
        scene d17s08-32 mc-sy-leave-talk2_c2 with dissolve
        play voice2 mc_disappointed_off1 noloop
        mc "Oh yeah."
        scene d17s08-31 mc-sy-leave-talk1_c3 with dissolve
        play voice3 stacy_hmm noloop
        sy "I know exactly what you want and how to give it to you."
        scene d17s08-32 mc-sy-leave-talk2_c2 with dissolve
        play voice2 mc_scared_huuuh1 noloop
        mc "You are incredible."
        call buzz from _call_buzz_22
        scene d17s08-23 mc-sy-entry4_c1 with dissolve
        call add_points (d17s08_points) from _call_add_points_11
        play voice3 stacy_oh2 noloop
        sy "Oh, look at that, we have got [d17s08_points] points for..."
    elif True:
        scene d17s08-33 mc-sy-leave-talk3_c1 with dissolve
        play voice3 stacy_mmm1 noloop
        sy "So, how's things?"
        scene d17s08-33 mc-sy-leave-talk3_c2 with dissolve
        play voice2 mc_arrogant_hm1 noloop
        mc "Um... good?"
        scene d17s08-24 mc-sy-entry5_c1 with dissolve
        play voice3 stacy_angry noloop
        sy "You own clothes, don't you?"
        scene d17s08-24 mc-sy-entry5_c2 with dissolve
        play voice2 d1s5b_ehhh noloop volume 1.6
        mc "It was just my girlfriend & I.{w}.. I was getting ready to sleep."
        scene d17s08-33 mc-sy-leave-talk3_c1 with dissolve
        play voice3 stacy_uhuh noloop
        sy "I'm not complaining. I'm just saying, after Sunday..."
        scene d17s08-33 mc-sy-leave-talk3_c2 with dissolve
        play voice2 mc_yes_yeah5 noloop
        mc "You and AmRose stole my clothes on Sunday."
        scene d17s08-33 mc-sy-leave-talk3_c1 with dissolve
        play voice3 stacy_huh noloop
        sy "Are you even allowed to wear clothing in this house?"
        scene d17s08-32 mc-sy-leave-talk2_c2 with dissolve
        play voice2 mc_yes_yes3 noloop
        mc "Yes. I am allowed to wear clothing."
        if cage_ntr is True:
            mc "*mumbles* probably"
        scene d17s08-32 mc-sy-leave-talk2_c3 with dissolve
        play voice3 polly_laughter noloop
        sy "Alright. I'll give you the benefit of the doubt."
        scene d17s08-32 mc-sy-leave-talk2_c2 with dissolve
        play voice2 d1s5_mchappy noloop volume 1.7
        mc "So, when did you modify your phone to download data on-?"
        scene d17s08-31 mc-sy-leave-talk1_c3 with dissolve
        play voice3 stacy_oh noloop
        sy "Finding Mira? Oh, earlier today."
        play voice2 d1s2_hmm noloop volume 1.7
        mc "Mira?"
        play voice3 stacy_mmm2 noloop
        sy "That shiba inu we're trying to find. You know the one I'm talking about."
        scene d17s08-31 mc-sy-leave-talk1_c1 with dissolve
        if is_antagonist_mode is False:
            mct "Oh, right. Fetish Locator might be listening."
        elif True:
            mct "Oh, right. Retention might be listening."
        play voice2 mc_yes_yeah7 noloop
        mc "Right, that lost... dog. I didn't realize it had a name."
        scene d17s08-32 mc-sy-leave-talk2_c3 with dissolve
        play voice3 stacy_upset1 noloop
        sy "Don't worry. We'll find it."
        scene d17s08-32 mc-sy-leave-talk2_c2 with dissolve
        play voice2 mc_thinking_hmm3 noloop
        mc "So, is there any progress on finding... Mira?"
        scene d17s08-31 mc-sy-leave-talk1_c3 with dissolve
        play voice3 stacy_hmm noloop
        sy "Well, the data transfer goes both ways. There's an update to the search software."
        play voice2 d2s9_mchey noloop
        mc "That sounds nice."
        scene d17s08-31 mc-sy-leave-talk1_c1 with dissolve
        play voice3 polly_aga noloop
        sy "Hopefully we'll find Mira tomorrow."
    play sound4 sfx_barefoot_steps1 volume 1.5
    scene d17s08-34 mc-sy-hear_c1 with dissolve
    play voice2 mc_scared_huh3 noloop
    if persistent.is_special is True:
        mc "Uh, sis. My girlfriend's coming this way."
    elif True:
        mc "Uh, Stacy. Lydia's coming this way."
    stop sound4 fadeout 1.0
    scene d17s08-35 mc-lc-enter1_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Hey sexy lady."
    play voice3 lydia_lydiahey noloop
    lc "Hey yourself, naked man."
    scene d17s08-35 mc-lc-enter1_c2 with dissolve
    if date_sy is True:
        play voice3 lydia_morningoh noloop
        lc "Oh good, you jerked off while I was in the shower."
        scene d17s08-36 mc-lc-enter2_c1 with dissolve
        lc "Not that I didn't want to be here when you came, but I'm tired."
    elif cage_ntr is True:
        play voice3 lydia_moan1 noloop
        lc "Damn, you're so fucking sexy."
        scene d17s08-36 mc-lc-enter2_c1 with dissolve
        lc "If I wasn't so fucking tired I would throw you on the bed and have my way with you."
    elif True:
        play voice3 lydia_lydwow noloop
        lc "Wow. You are so incredibly sexy right now."
        scene d17s08-36 mc-lc-enter2_c1 with dissolve
        lc "If I wasn't so tired I would do such horrible things with you."
    $ renpy.music.set_volume(0.25, 6.5, "music")
    scene d17s08-36 mc-lc-enter2_c3 with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "Too much time studying for finals?"
    scene d17s08-36 mc-lc-enter2_c2 with dissolve
    play voice3 lydia_oof noloop
    lc "You have no idea how much my throat hurts from singing practice."
    play sound sfx_door_creak4
    with hpunch
    play voice3 dahlia_surprised_ah2 noloop
    lc "Did you hear-?"
    play voice3 dahlia_sex_closedmoan1 noloop
    play voice2 d1s5_orgasm noloop
    play sound maria_kiss1
    scene d17s08-37 mc-lc-kiss_c1 with vpunch
    pause
    $ renpy.end_replay()
    if date_sy is True:
        $ unlock_gallery_slot("scene", "d17s08")
    play sound maria_kiss2
    play voice2 mc_thinking_mmm1 noloop
    play voice3 dahlia_sex_closedmoan2 noloop
    scene d17s08-37 mc-lc-kiss_c2 with dissolve
    pause
    scene d17s08-37 mc-lc-kiss_c3 with dissolve
    pause
    scene d17s08-38 mc-lc-getting-ready1_c1 with dissolve
    play voice3 lydia_oops noloop
    lc "What was that for?"
    play voice2 mc_yes_yeah1 noloop
    mc "I was just overwhelmed with the desire to kiss you."
    scene d17s08-38 mc-lc-getting-ready1_c2 with dissolve
    play voice3 lydia_haha noloop
    lc "I like that."
    scene d17s08-38 mc-lc-getting-ready1_c3 with dissolve
    play voice2 d2s9_confused noloop volume 1.6
    mc "So, you were telling me about your neighbor?"
    scene d17s08-39 mc-lc-getting-ready2_c1 with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    lc "Oh, you remembered that."
    play voice2 d1s5_mcthinks noloop volume 1.8
    mc "Was I supposed to forget about it?"
    scene d17s08-39 mc-lc-getting-ready2_c2 with dissolve
    play voice3 lydia_hmmmm noloop
    lc "If you don't mind... I'll tell you about it some other time."
    play voice2 mc_arrogant_hm3 noloop
    mc "I dunno..."
    play voice3 dahlia_thinking_hmm2 noloop
    lc "Yeah?"
    scene d17s08-39 mc-lc-getting-ready2_c3 with dissolve
    play voice2 d3s11b_mcheh noloop
    mc "It seems like you've been cheating on me by watching other people..."
    scene d17s08-39 mc-lc-getting-ready2_c1 with dissolve
    play voice3 dahlia_arrogant_ha noloop
    lc "Ha! It's not like that-"
    scene d17s08-38 mc-lc-getting-ready1_c3 with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "I might have to punish you for not telling me about it."
    scene d17s08-39 mc-lc-getting-ready2_c2 with dissolve
    play voice3 lydia_ah noloop
    lc "Okay, okay! {w}I promise to make it up to you in the morning."
    play voice2 mc_yes_ugu1 noloop
    mc "I hope so."
    $ renpy.music.set_volume(0.1, 3.5, "music")
    play sound sfx_cloth_rustling3
    scene d17s08-40 mc-lc-getting-bes1_c1 with fade
    play voice3 dahlia_thinking_mmm2 noloop
    lc "Good night, my lovely."
    if love_lc is True:
        play voice2 mc_yes_aga2 noloop
        mc "Rest well, my love."
    elif cage_ntr is True and date_sy is True:
        play voice2 mc_disappointed_ah1 noloop
        mc "*mumbles* These women are going to be the end of me."
        play voice3 dahlia_surprised_what noloop
        lc "What?!"
        play voice2 d1s2_hmm noloop volume 1.7
        mc "Huh?"
        play voice3 lydia_thinking noloop
        lc "What did you say?"
        play voice2 mc_thinking_mmm4 noloop
        mc "Rest well, beautiful."
        play voice3 lydia_morningoh noloop
        lc "Oh. {w}Thank you."
    elif True:
        play voice2 mc_yes_aga2 noloop
        mc "Rest well, beautiful."
    scene d17s08-41 mc-lc-getting-bed2_c1 with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    lc "Oh, remind me in the morning..."
    play voice2 d7s6_moan1 noloop
    mc "What's that?"
    play voice3 lydia_laugh noloop
    lc "I want you to help me create my Fetish Locator account."
    scene d17s08-42 mc-lc-getting-bed3_c1 with dissolve
    play voice2 mc_pain_mff3 noloop
    mct "Oh, crap."
    stop music fadeout 4.0

    jump d18s01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
